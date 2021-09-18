from django.shortcuts import render, redirect
from .forms import RegisterForm, SettingsForm
from django.views.generic import ListView
from .models import Profile


# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

        return redirect("login/")
    else:
        form = RegisterForm()

    return render(response, "register.html", {"form": form})


def settings(response):
    if response.method == "POST":
        form = SettingsForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("profile/")
    else:
        form = SettingsForm()

    return render(response, "profile.html", {"form": form})

