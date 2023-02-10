from .models import *
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage


def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    profile = Profile.objects.get(user__exact=request.user)
    context = {
        'profile': profile,
    }
    return render(request, 'store/index.html', context)

def loginView(request):
    if request.POST:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return HttpResponseRedirect(reverse('login'))
        else:
            login(request,user)
            return HttpResponseRedirect(reverse('index'))
    return render(request,'store/login.html', {})

def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def createProfile(request):
    if request.method == 'POST':
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
            first_name=request.POST['firstName'],
            last_name=request.POST['lastName']
        )
        profile = Profile(user=user, address=request.POST['address'], phone=request.POST['phone'], picture=request.FILES['picture'], type=request.POST['type'])
        photoFile = request.FILES['picture']
        fs = FileSystemStorage()
        fs.save(photoFile.name, photoFile)
        user.save()
        profile.save()
        login(request,user)
        return HttpResponseRedirect(reverse('index'))
    
    return render(request, 'store/createProfile.html', {})

