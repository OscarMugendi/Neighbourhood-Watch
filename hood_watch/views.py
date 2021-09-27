import os
import json

from decouple import config, Csv
from django.shortcuts import render, redirect, get_object_or_404
from django.conf import settings
from django.templatetags.static import static
from django.http  import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.http  import Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.defaulttags import register
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.mail import EmailMessage
from django.contrib.auth import login, authenticate
from .emails import send_welcome_email

from .models import *
from .forms import *

import datetime as dt

# Create your views here.

def home(request):
    current_user = request.user

    return render(request,"home.html")


@login_required(login_url='/accounts/login/')
def profile(request, id):
    user = request.user
    user_id = user.id
    userf = User.objects.get(pk=user_id)

    if userf:
        print('User found!')
        profile = User.objects.get(id=user.id)

    else:

        print('User not found!')

    return render (request, 'profile.html', {'user':user,})


@login_required(login_url='/accounts/login/')
def update_profile(request,id):
    current_user = request.user 
    title = 'Update Profile'
    profile = Profile.objects.get(id=current_user.id)

    try:

        requested_profile = Profile.objects.get(id = current_user.id)
        if request.method == 'POST':

            form = ProfileForm(request.POST,request.FILES)

            if form.is_valid():
                requested_profile.profile_pic = form.cleaned_data['profile_pic']
                requested_profile.email = form.cleaned_data['email']
                requested_profile.contact = form.cleaned_data['contact']
                requested_profile.user_id= current_user

                requested_profile.save()

                return redirect(profile)
        else:
            
            form = ProfileForm()

    except:
        if request.method == 'POST':

            form = ProfileForm(request.POST,request.FILES)

            if form.is_valid():

                new_profile = Profile(profile_pic = form.cleaned_data['profile_pic'], email = form.cleaned_data['email'], contact = form.cleaned_data['contact'], user = current_user)
                new_profile.save()

                return redirect(profile)

        else:

            form = ProfileForm()

    return render(request,'update_profile.html',{"title":title,"current_user":current_user,"form":form})