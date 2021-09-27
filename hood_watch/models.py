from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

import datetime as dt
import numpy as np

class User(models.Model):

    name = models.CharField(max_length =20, default="bio")
    hood = models.CharField(max_length=20, null=True, default="hood")
    
    profile_pic = models.ImageField(upload_to='images/profiles/', blank=True, default = 0)
    email = models.EmailField(blank=True, default="email")
    contact = models.IntegerField(blank=True, default=0)

    def save(self):
        self.save()

    def __str__(self):
        return self