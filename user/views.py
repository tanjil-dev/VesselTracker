from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.views.generic import ListView, TemplateView, View
from django.contrib.auth import authenticate, login as auth_login, logout, update_session_auth_hash
from VesselAPIs.models import *
from user.forms import *

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from .tokens import *

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('home')
def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("auth/template_activate_account.html", {
        'user': user.first_name+" "+user.last_name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user.first_name} {user.last_name}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')

def custom_404(request, exception):
    return render(request, 'user/404.html', {}, status=404)
class HomeView(TemplateView):
    template_name = 'user/home.html'

class Dashboard(TemplateView):
    template_name = 'admin/dashboard.html'
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


def Login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        template = 'auth/login.html'
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)

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
                user = form.save(commit=False)
                user.is_active=False
                user.save()
                email = form.cleaned_data.get('email')
                activateEmail(request, user, email)
                return redirect('home')
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