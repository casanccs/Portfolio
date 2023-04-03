from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=300, null=True,blank=True)
    photos = models.ImageField(blank=True)

    def __str__(self):
        return self.user.username

class Interest(models.Model):
    #An interest can belong to many profiles, and a profile can have many interests
    profile = models.ManyToManyField(Profile)
    interest = models.CharField(max_length=50)


class ChatRoom(models.Model):
    room_name = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.room_name

class Message(models.Model):
    content = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, default=None)
    chat = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, default=None)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.profile.user.username}: {self.content}"