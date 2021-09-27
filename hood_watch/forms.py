from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, IntegerField, EmailField, CharField, Form, ImageField


class ProfileForm(forms.Form):

    name = forms.CharField(max_length =20, label='Username')
    hood = forms.CharField(max_length=20, label='Hood')

    profile_pic = forms.ImageField(required = False, label = 'Image Field') 
    email = forms.EmailField(required = False, label='Email')
    contact = forms.IntegerField(required = False, label='Contact')