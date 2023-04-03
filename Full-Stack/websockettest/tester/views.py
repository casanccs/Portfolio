from django.shortcuts import render
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.core.files.storage import FileSystemStorage

# Create your views here.
def chat(request,room_id):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    profile = Profile.objects.get(user__exact=request.user)
    messages = Message.objects.filter(chat__room_name__exact=room_id)
    context = {
        'profile': profile,
        'messages': messages,
        'room_id': room_id,
    }
    return render(request, "chat.html", context)

def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    context = {

    }
    return render(request, "home.html", context)

def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def LoginView(request):
    if request.method == "POST":
        form = request.POST
        user = authenticate(username=form['username'], password=form['password'])
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'login.html', {})

def CreateAccount(request):
    if request.method == "POST":
        form = request.POST
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
            first_name=request.POST['firstName'],
            last_name=request.POST['lastName']
        )
        profile = Profile(user=user, bio=form['bio'])
        user.save()
        profile.save()
        login(request,user)
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'createAccount.html')