# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from testapp.forms import UserForm
from testapp.forms import UserProfileInfoforms

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'testapp/index.html')

@login_required
def userlogout(request):
    logout(request)
    return redirect('/')

def register(request):
    registered = False

    if request.method == "POST":
        userform = UserForm(data=request.POST)
        profileform = UserProfileInfoforms(data=request.POST)

        if userform.is_valid() and profileform.is_valid():
            user =userform.save()
            user.set_password(user.password)
            user.save()

            profile = profileform.save(commit= False)
            profile.user = user

            if 'Profile_pic'in request.FILES:
                profile.Profile_pic=request.FILES['Profile_pic']
            profile.save()

            registered=True
        else:
            print(userform.errors,profileform.errors)
    else:
        userform = UserForm()
        profileform = UserProfileInfoforms()

    return render(request,'testapp/register.html',
                          {'userform':userform,
                          'profileform':profileform,
                          'registered':registered})

def userlogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)

        if user:
            if user.is_active:
                login(request,user)
                return redirect('/master/form')
                # return HttpResponseRedirect(reverse('index'))
                # return HttpResponse("succesfully logged in")
                # return render(request,'testapp1/form.html')
            else:
                return HttpResponse("Account Not Active")
        else:
            print("someone tried to login and failed!!")
            print("username:{}and password{}".format(username,password))
            return HttpResponse("invalid login")
    else:
        return render(request,'testapp/login.html',{})
