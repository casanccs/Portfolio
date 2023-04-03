from django.shortcuts import render
from .forms import *
from django.core.files.storage import default_storage
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import *

@login_required(login_url='/accounts/login/')
def index(request):
    if request.method == "POST": #User submits a file
        form = EntryForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            newEntry = Entry(user=request.user, title=data['title'], desc=data['desc']
                             , image1=request.FILES['image1'])
            try:
                newEntry.image2 = request.FILES['image2']
                try:
                    newEntry.image3 = request.FILES['image3']
                    try:
                        newEntry.image4 = request.FILES['image4']
                        try:
                            newEntry.image5 = request.FILES['image5']
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
            newEntry.save()
            return HttpResponseRedirect(reverse('index'))
        else:
            context = {
                'profile': Profile.objects.get(user=request.user),
                'form': form
            }

            return render(request, 'index.html', context)

    #photos = get_all_photoObjects_from_folder()

    context = {
        'entries': Entry.objects.all(),
        'profile': Profile.objects.get(user=request.user),
        'form': EntryForm()
    }

    return render(request, 'index.html', context)


'''
@login_required(login_url='/login/')
def LogoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def LoginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            #process data
            return HttpResponseRedirect(reverse('index'))
    else:
        form = LoginForm()
        context = {
            'form': form,
        }
    return render(request, 'login.html', context)
'''

'''
def ProfileCreateView(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(data['username'], data['email'], data['password'])
            user.first_name = data['first_name']
            user.last_name = data['last_name']
            user.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return HttpResponseRedirect(reverse('createProfile'))
    else:
        form = UserForm()
        context = {
            'form': form,
        }
    return render(request, 'createProfile.html', context)
'''

def ProfileCreateView(request):
    if request.method == 'POST':
        form1 = ProfileCreationForm1(request.POST)
        form2 = ProfileCreationForm2(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            data = form1.cleaned_data
            user = User.objects.create_user(data['username'], data['email'], data['password1'])
            user.save()
            profile = Profile(user=user, ppic=request.FILES['ppic'])
            profile.save()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            context = {
                'form1': form1,
                'form2': form2,
            }
            return render(request, 'createProfile.html', context)
    else:
        form1 = ProfileCreationForm1()
        form2 = ProfileCreationForm2()
        context = {
            'form1': form1,
            'form2': form2,
        }
    return render(request, 'createProfile.html', context)