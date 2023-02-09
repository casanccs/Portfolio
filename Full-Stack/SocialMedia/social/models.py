from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#Django-Docs: Extending The Existing User Model
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField('self', blank=True)
    following = models.ManyToManyField('self', blank=True)
    picture = models.ImageField(blank=True) # MUST HAVE PILLOW INSTALLED, also see "Managing Files"
    bio = models.CharField(max_length=100) #Make sure the view says max length
    messaging = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.user.username
# Profiles are NOT created when a user is created, so we must use "django.db.models.signals.post_save" to create or update
    # the related models

class Entry(models.Model):
    picture = models.ImageField(blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    comments = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    dateTime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-dateTime"]

    def __str__(self):
        return f"{self.profile.user.username}'s post"

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.CharField(max_length=500)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE, null=True)
    dateTime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-dateTime"]

    def __str__(self):
        return f"{self.profile.user.username}'s post"
    


class Message(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="Author", null=True)
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="Receiver", null=True)
    content = models.CharField(max_length=500)
    dateTime = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-dateTime"]