from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.forms import ModelForm
from django import forms
from .models import *

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(required=True, label="Account name")
    first_name = forms.CharField(required=True, label="First name")
    last_name = forms.CharField(required=True, label="Last name")
    email = forms.CharField(required=True, label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput,
                required=True)
    password2 = forms.CharField(label="Confirm password",
                widget=forms.PasswordInput, required=True)

class GroupCreationForm(ModelForm):
    name = forms.Charfield(required=True, label="Group name")
