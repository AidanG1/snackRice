from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class SettingsForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ["phone_number", 'walking_factor', 'food_factor']
