from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, IntegerField, EmailField, CharField, Form, ImageField


class ProfileForm(forms.Form):
    profile_pic = forms.ImageField(required = False, label = 'Image Field') 
    email = forms.EmailField(required = False, label='Email')
    contact = forms.IntegerField(required = False, label='Contact')


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','hood']


class PostForm(forms.ModelForm):    
    class Meta:
        model = Post
        exclude = ['user']