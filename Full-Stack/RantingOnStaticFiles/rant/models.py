from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.auth.forms import *
from django import forms
# Create your models here.

class Entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,)
    title = models.CharField(max_length=100, default='')
    desc = models.CharField(max_length=500, blank=True)
    image1 = models.ImageField()
    image2 = models.ImageField(blank=True)
    image3 = models.ImageField(blank=True)
    image4 = models.ImageField(blank=True)
    image5 = models.ImageField(blank=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ppic = models.ImageField()


'''
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': PasswordInput
        }
'''

class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ['title','desc','image1','image2','image3','image4','image5']
        labels = {
            'desc': "Description",
        }

class ProfileCreationForm1(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']

class ProfileCreationForm2(ModelForm):
    class Meta:
        model = Profile
        fields = ['ppic']
        labels = {
            'ppic': "Profile Picture"
        }