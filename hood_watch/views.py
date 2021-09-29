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
def profile(request, username):
    return render(request, 'profile.html')


@login_required(login_url='/accounts/login/')
def update_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if form.is_valid():
            form.save()

            return redirect('profile', user.username)
    else:
        form = ProfileForm(instance=request.user.profile)

    return render(request, 'update_profile.html', {'form': form})


# @login_required(login_url='/accounts/login/')
def hoods(request):
    all_hoods = Neighbourhood.objects.all()
    all_hoods = all_hoods[::-1]
    return render(request, 'hoods.html',{"all_hoods": all_hoods})


@login_required(login_url='/accounts/login/')
def hood(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(neighbourhood=hood)
    posts = posts[::-1]

    return render(request, 'hood.html',{"hood": hood, "business": business, "posts": posts})


def new_business(request, hood_id):
    current_user = request.user
    hood_id = Neighbourhood.id
    hood = Neighbourhood

    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():

            business = form.save(commit=False)
            business.user = current_user.profile
            business.hood = hood
            business.save()

            return redirect('hood', hood.id)

    else:
        form = BusinessForm()
        
    return render(request, 'business.html', {"form": form})


@login_required(login_url='/accounts/login/')
def neighbours(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    neighbours = Profile.objects.filter(neighbourhood=hood)
    return render(request, 'neighbours.html', {"neighbours": neighbours})


@login_required(login_url='/accounts/login/')
def new_post(request, hood_id):
    hood = Neighbourhood.objects.get(id=hood_id)
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()

            return redirect('hood', hood.id)
    else:
        form = PostForm()

    return render(request, 'post.html', {'form': form})


@login_required(login_url='/accounts/login/')
def join_hood(request, id):
    neighbourhood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood', hood.id)


@login_required(login_url='/accounts/login/')
def leave_hood(request, id):
    hood = get_object_or_404(Neighbourhood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood', hood.id)


@login_required(login_url='/accounts/login/')
def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Business.objects.filter(name__icontains=name).all()

        print(results)

        message = f'name'

        return render(request, 'search.html', {'results': results, 'message': message})
        
    else:
        message = "Invalid Parameters!"

    return render(request, "search.html")