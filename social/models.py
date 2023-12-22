from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.OneToOneField(Token, on_delete=models.CASCADE)


class Blog(models.Model):
    blog_name = models.CharField(max_length=100, blank=False)
    blog_description = models.TextField(max_length=800, blank=False)
    blog_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.blog_name


class Game(models.Model):
    game_name = models.CharField(max_length=100, blank=False)
    game_description = models.TextField(max_length=800, blank=False)
    video_link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.game_name
