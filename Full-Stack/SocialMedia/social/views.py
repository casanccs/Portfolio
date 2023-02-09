from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.


def index(request):
    auth = request.user.is_authenticated
    if not auth:
        return HttpResponseRedirect(reverse('login'))
    profile = Profile.objects.get(user__exact=request.user)
    profiles = profile.following.all()
    profiles |= Profile.objects.filter(pk=profile.pk)
    #I want to get entries that belong to CURRENTPROFILE AND PROFILES WHO IS FOLLOWED
    entries = Entry.objects.filter(profile__in=profiles)
    context = {
        'auth': auth,
        'profile': profile,
        'entries': entries
    }
    return render(request, "social/index.html", context)

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def loginView(request):
    try:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('login'))
    except:
        return render(request, 'social/login.html', {})

def createAccountView(request):
    if request.FILES:
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
            first_name=request.POST['firstName'],
            last_name=request.POST['lastName']
        )
        profile = Profile(user=user, bio=request.POST['bio'], picture=request.FILES['picture'])
        photoFile = request.FILES['picture']
        fs = FileSystemStorage()
        fs.save(photoFile.name, photoFile)
        user.save()
        profile.save()
        login(request,user)
        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'social/createAccount.html', {})
    
def editProfileView(request, profile_id):
    profile = Profile.objects.get(id__exact=profile_id)
    context = {
        'profile': profile,
    }
    if request.POST:
        if request.FILES:
            profile.picture=request.FILES['picture']
            photoFile = request.FILES['picture']
            fs = FileSystemStorage()
            fs.save(photoFile.name, photoFile)
        profile.user.username = request.POST['username']
        profile.user.email = request.POST['email']
        profile.user.first_name = request.POST['firstName']
        profile.user.last_name = request.POST['lastName']
        profile.user.save()
        profile.save()
        return HttpResponseRedirect(reverse('index'))
    return render(request, 'social/editProfile.html', context)
    
def createPostView(request):
    if request.FILES:
        print(request.FILES)
        profile = Profile.objects.get(user__exact=request.user)
        post = Entry(profile = profile, text=request.POST['entryText'], picture=request.FILES['picture'])
        post.save()
        photoFile = request.FILES['picture']
        fs = FileSystemStorage()
        fs.save(photoFile.name, photoFile)
        return HttpResponseRedirect(reverse('index'))
    
    return render(request, 'social/createPost.html', {})

def editPostView(request, entry_id):
    profile = Profile.objects.get(user__exact=request.user)
    post = Entry.objects.get(id__exact=entry_id)
    context = {
        'profile': profile,
        'post': post,
    }
    if request.POST:
        if request.FILES:
            post.picture=request.FILES['picture']
            photoFile = request.FILES['picture']
            fs = FileSystemStorage()
            fs.save(photoFile.name, photoFile)
        post.text=request.POST['entryText']
        post.save()
        return HttpResponseRedirect(reverse('index'))
    
    return render(request, 'social/editPost.html', context)

def deletePostView(request, entry_id):
    post = Entry.objects.get(id__exact=entry_id)
    if post.profile.user == request.user:
        if post:
            post.delete()
        return HttpResponseRedirect(reverse('index'))
    else:
        raise Http404

def searchProfileView(request):
    currentProfile = Profile.objects.get(user__exact=request.user)
    if request.POST:
        text = request.POST['searchProfile']
        profiles = Profile.objects.filter(user__username__icontains=text)
    else:
        profiles = Profile.objects.all()
    for profile in profiles:
        if currentProfile.following.filter(user__exact=profile.user).exists():
            profile.followed = True
        else:
            profile.followed = False

    context ={
        'profiles': profiles,
        'currentProfile': currentProfile,
    }
    return render(request, 'social/searchProfile.html', context)

def addFollowView(request, profile_id):
    currentProfile = Profile.objects.get(user__exact=request.user)
    profile = Profile.objects.get(id__exact=profile_id)
    currentProfile.following.add(profile)
    currentProfile.save()
    return HttpResponseRedirect(reverse('searchProfile'))

def removeFollowView(request, profile_id):
    currentProfile = Profile.objects.get(user__exact=request.user)
    profile = Profile.objects.get(id__exact=profile_id)
    currentProfile.following.remove(profile)
    currentProfile.save()
    return HttpResponseRedirect(reverse('searchProfile'))

def accountView(request, profile_id):
    curProfile = Profile.objects.get(user__exact=request.user)
    profile = Profile.objects.get(id__exact=profile_id)
    entries = Entry.objects.filter(profile__exact=profile)
    context = {
        'entries': entries,
        'profile': curProfile,
        'otherProfile': profile,
    }
    return render(request, 'social/accountDetail.html', context)

def messagingView(request, profile_id):
    profile = Profile.objects.get(id__exact=profile_id)
    
    context = {
        'profile': profile,
    }
    return render(request, 'social/messaging.html', context)

def chatView(request, other_id):
    cur = Profile.objects.get(user__exact=request.user)
    other = Profile.objects.get(id__exact=other_id)
    curMessages = Message.objects.filter(author__exact=cur).filter(receiver__exact=other)
    otherMessages = Message.objects.filter(author__exact=other).filter(receiver__exact=cur)
    messages = curMessages | otherMessages
    context = {
        'messages': messages,
    }
    if not cur.messaging.filter(user__exact=other.user).exists():
        cur.messaging.add(other)
        other.messaging.add(cur)

    if request.POST:
        content = request.POST['content']
        message = Message(content=content, author=cur, receiver=other)
        message.save()

    return render(request, 'social/chat.html', context)

def entryDetail(request, entry_id):
    entry = Entry.objects.get(id__exact=entry_id)
    profile = Profile.objects.get(user__exact=request.user)
    if request.POST:
        comment = Comment(profile=profile, text=request.POST['comment'], entry=entry)
        comment.save()
        return HttpResponseRedirect(reverse('entryDetail', kwargs={'entry_id': entry_id}))
    comments = Comment.objects.filter(entry__exact=entry)
    context = {
        'entry': entry,
        'comments': comments,
        'profile': profile,
    }

    return render(request,'social/entryDetail.html', context)


def followingView(request):
    profile = Profile.objects.get(user__exact=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'social/following.html', context)

def followersView(request):
    profile = Profile.objects.get(user__exact=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'social/followers.html', context)

def deleteCommentView(request, comment_id):
    comment = Comment.objects.get(id__exact=comment_id)
    if comment.profile.user == request.user:
        comment.delete()
        return HttpResponseRedirect(reverse('entryDetail', kwargs={'entry_id': comment.entry.id}))
    else:
        raise Http404