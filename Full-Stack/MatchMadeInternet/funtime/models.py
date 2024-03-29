from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profilePic = models.FileField(upload_to='profilePics/')
    