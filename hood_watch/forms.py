from .models import *
from django.db.models import ImageField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, IntegerField, EmailField, CharField, Form, ImageField


class ProfileForm(forms.Form):
    class Meta:
        model = Profile
        exclude = ('user', 'neighbourhood')


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ('user', 'neighbourhood')


class PostForm(forms.ModelForm):    
    class Meta:
        model = Post
        exclude = ('user', 'hood')