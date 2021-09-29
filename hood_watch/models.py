from django.db import models
from django.contrib.auth.models import User
from django.db.models import ImageField
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime as dt


class Neighbourhood(models.Model):
    
    name = models.CharField(max_length=20)
    location = models.CharField(max_length=20, null=True)
    hood_photo = models.ImageField(upload_to='images/hoods/', null=True)
    police_contact = models.IntegerField(blank=True, null=True)
    health_contact = models.IntegerField(blank=True, null=True)

    # def save(self):
    #     self.save()

    @classmethod
    def get_hoods(cls):
        hoods = Neighbourhood.objects.all()
        return hoods

    def __str__(self):
        return f'{self.name}'


class Profile(models.Model):
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True)
    
    profile_pic = models.ImageField(upload_to='images/profiles/', blank=True, default = 0, null=True)
    
    email = models.EmailField(blank=True, default="email", null=True)
    contact = models.IntegerField(blank=True, default=0, null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.SET_NULL, null=True, related_name='neighbour', blank=True)


    def __str__(self):
        return f'{self.user.username}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Post(models.Model):

    title = models.CharField(max_length = 20, null=True)
    post_image = models.ImageField(upload_to='images/posts', blank=True, default = 0, null=True)
    content = models.TextField(max_length = 500, blank=True, null=True)
    date = models.DateTimeField(auto_now=True, blank=True, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='author', null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='post', null=True)

    # def save(self):
    #     self.save()

    @classmethod
    def get_posts(cls):
        posts = Post.objects.all()
        return posts

    def __str__(self):
        return f'{self.title}'


class Business(models.Model):
    name = models.CharField(max_length=100, null=True)
    business_pic = models.ImageField(upload_to='images/business/',null=True, blank=True, default = 0)
    description = models.TextField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner', null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True, related_name='business')

    def __str__(self):
        return f'{self.name}'

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(name__icontains=name).all()