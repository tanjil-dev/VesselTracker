from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import ListView, TemplateView
from django.contrib.auth import authenticate, login as auth_login, logout
from VesselAPIs.models import *
from user.forms import *

class HomeView(TemplateView):
    template_name = 'home.html'
class VoyageListView(ListView):
    model = Voyage
    template_name = 'voyage.html'
    context_object_name = 'data'
    ordering = ['-start_time']

class VesselListView(ListView):
    model = Vessel
    template_name = 'vessel.html'
    context_object_name = 'data'
    ordering = ['-created_at']

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
                return redirect('login')
        context = {
            'form': form
        }
        return render(request, template_name=template, context=context)

@login_required(login_url='login')
def LogoutUser(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request, 'You are logged out!')
        return redirect('login')

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated Successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'form1': user_form,
        'form2': profile_form
    }
    return render(request, template_name='profile.html', context=context)