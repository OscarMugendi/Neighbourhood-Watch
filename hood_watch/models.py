from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime as dt
import numpy as np


class User(models.Model):
    
    name = models.CharField(max_length =20, default="name")
    
    profile_pic = models.ImageField(upload_to='images/profiles/', blank=True, default = 0)
    
    email = models.EmailField(blank=True, default="email")
    contact = models.IntegerField(blank=True, default=0)

    def save(self):
        self.save()

    def __str__(self):
        return self.name


class Hood(models.Model):

    hood_photo = models.ImageField(upload_to='images/hoods/', default = 0)
    name = models.CharField(max_length=100, null=True, default="name")
    occupants_count = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    police_contact = models.IntegerField(blank=True, default=0)
    health_contact = models.IntegerField(blank=True, default=0)

    def save(self):
        self.save()

    @classmethod
    def get_hoods(cls):
        hoods = Hood.objects.all()
        return hoods

    def __str__(self):
        return self.name


class Post(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length = 20, default="title")
    post_image = models.ImageField(upload_to='images/posts', blank=True, default = 0)
    content = models.TextField(max_length = 500, blank=True, default="content")

    def save(self):
        self.save()

    @classmethod
    def get_posts(cls):
        posts = Post.objects.all()
        return posts

    def __str__(self):
        return self.title


class Business(models.Model):
    business_pic = models.ImageField(upload_to='images/business/',null=True, blank=True, default = 0)
    name = models.CharField(max_length=100, blank=True, null=True, default="name")
    description = models.TextField(max_length=200, blank=True, null=True, default="description")
    email = models.CharField(max_length=100, blank=True, null=True, default="email")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    hood = models.ForeignKey(Hood, on_delete=models.CASCADE, null=True)

    def save(self):
        self.save()

    @classmethod
    def get_businesses(cls):
        businesses = Business.objects.all()
        return businesses

    def __str__(self):
        return self.name