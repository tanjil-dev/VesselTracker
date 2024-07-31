from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.views.generic import ListView, TemplateView, View
from django.contrib.auth import authenticate, login as auth_login, logout, update_session_auth_hash
from VesselAPIs.models import *
from user.forms import *


def custom_404(request, exception):
    return render(request, 'user/404.html', {}, status=404)
class HomeView(TemplateView):
    template_name = 'user/home.html'
class VoyageListView(ListView):
    model = Voyage
    template_name = 'user/voyage.html'
    context_object_name = 'data'
    ordering = ['-start_time']

class VesselListView(ListView):
    model = Vessel
    template_name = 'user/vessel.html'
    context_object_name = 'data'
    ordering = ['-created_at']

class ParcelListView(LoginRequiredMixin, ListView):
    model = Parcel
    template_name = 'user/parcel.html'
    context_object_name = 'data'
    ordering = ['-id']
    login_url = 'login'
    def get_queryset(self):
        return Parcel.objects.filter(user=self.request.user).order_by('-id')

class VoyageDetailView(View):
    template = 'user/voyage_detail.html'
    data = None
    def get(self, request, pk):
        self.data = Voyage.objects.get(id=pk)
        context = {
            'data': self.data
        }
        return render(request, template_name=self.template, context=context)

class VesselDetailView(View):
    template = 'user/vessel_detail.html'
    data = None

    def get(self, request, pk):
        self.data = Vessel.objects.get(id=pk)
        context = {
            'data': self.data
        }
        return render(request, template_name=self.template, context=context)

class ParcelDetailView(View):
    template = 'user/parcel_detail.html'
    data = None
    login_url = 'login'
    def get(self, request, pk):
        self.data = Parcel.objects.get(id=pk)
        context = {
            'data': self.data
        }
        return render(request, template_name=self.template, context=context)

def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        template = 'auth/login.html'
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                messages.success(request, 'Your have login successfully!')
                return redirect('home')
            else:
                messages.info(request, "Username or Password is incorrect")

        return render(request, template_name=template)


def Signup(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        template = 'auth/signup.html'
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
        return redirect('home')

@login_required(login_url='login')
def changePassword(request):
    if request.POST:
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your Password Changed Successfully!')
            return redirect('home')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {
        'form': form
    }
    return render(request, template_name="auth/password_change.html", context=context)

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
    return render(request, template_name='user/profile.html', context=context)