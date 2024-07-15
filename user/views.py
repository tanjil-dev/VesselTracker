from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
from django.contrib.auth import authenticate, login as auth_login, logout
from VesselAPIs.models import *
from user.forms import *

class Home(View):
    template = 'home.html'
    data = None
    def get(self, request):
        self.data = Voyage.objects.all().order_by('-id')
        context = {
            'data1': self.data,
        }
        return render(request, template_name=self.template, context=context)
    def post(self, request):
        self.data = Voyage.objects.filter(vessel__name__contains=request.POST['search']).order_by('-id')
        context = {
            'data1': self.data,
        }
        return render(request, template_name=self.template, context=context)

class VesselView(View):
    template = 'home.html'
    data = None
    def get(self, request):
        self.data = Vessel.objects.all().order_by('-id')
        context = {
            'data2': self.data,
        }
        return render(request, template_name=self.template, context=context)
    def post(self, request):
        self.data = Vessel.objects.filter(name__contains=request.POST['search'])
        context = {
            'data2': self.data,
        }
        return render(request, template_name=self.template, context=context)

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
        messages.success(request, 'You are logged out!')
        return redirect('login')

@login_required(login_url='login')
def profile(request):
    user_form = UserUpdateForm()
    profile_form = ProfileUpdateForm()
    context = {
        'form1': user_form,
        'form2': profile_form
    }
    return render(request, template_name='profile.html', context=context)