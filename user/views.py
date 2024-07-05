from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout
from user.forms import *

@login_required(login_url='login')
def Home(request):
    template = 'base.html'
    context = {}
    return render(request, template_name=template, context=context)

def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        template = 'login.html'
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect")

        return render(request, template_name=template)


def Signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        template = 'signup.html'
        form = RegistrationForm()
        if request.method == "POST":
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data['username']
                messages.success(request, 'Account registered for '+ user)
                return redirect('home')
        context = {
            'form': form
        }
        return render(request, template_name=template, context=context)

def LogoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('login')
