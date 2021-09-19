from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class SettingsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)
        self.fields['walking_factor'].widget.attrs = {'min': 1, 'max': 10}
        self.fields['food_factor'].widget.attrs = {'min': 1, 'max': 10}

    class Meta:
        model = Profile
        fields = ["phone_number", 'walking_factor', 'food_factor', 'receive_notification_time','eggs', 'fish', 'gluten', 'milk', 'peanuts',
                  'shellfish', 'soy', 'tree_nuts', 'vegan', 'vegetarian']
