from django.contrib.auth.forms import UserCreationForm
from django import forms
from user.models import *

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['gender', 'image']