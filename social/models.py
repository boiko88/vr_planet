from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    token = models.OneToOneField(Token, on_delete=models.CASCADE)


class Blog(models.Model):
    blog_name = models.CharField(max_length=100, blank=False)
    blog_description = models.TextField(max_length=100, blank=False)
    blog_image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.blog_name
