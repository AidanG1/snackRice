from django.shortcuts import render, redirect
from .forms import RegisterForm, SettingsForm
from django.views.generic import ListView
from .models import Profile
from django.contrib.auth.decorators import login_required


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


@login_required()
def settings(request):
    rup = request.user.profile
    if request.method == "POST":
        form = SettingsForm(request.POST,
                            initial={
                                'phone_number': rup.phone_number,
                                'default_location': rup.default_location,
                                'walking_factor': rup.walking_factor,
                                'food_factor': rup.food_factor,
                                'receive_notification_time': rup.receive_notification_time,
                                'eggs': rup.eggs,
                                'fish': rup.fish,
                                'gluten': rup.gluten,
                                'milk': rup.milk,
                                'peanuts': rup.peanuts,
                                'shellfish': rup.shellfish,
                                'soy': rup.soy,
                                'tree_nuts': rup.tree_nuts,
                                'vegan': rup.vegan,
                                'vegetarian': rup.vegetarian,
                            })
        if form.is_valid():
            p = request.user.profile
            p.phone_number = form.cleaned_data.get('phone_number')
            p.default_location = form.cleaned_data.get('default_location')
            p.walking_factor = form.cleaned_data.get('walking_factor')
            p.food_factor = form.cleaned_data.get('food_factor')
            p.receive_notification_time = form.cleaned_data.get('receive_notification_time')
            p.eggs = form.cleaned_data.get('eggs')
            p.fish = form.cleaned_data.get('fish')
            p.gluten = form.cleaned_data.get('gluten')
            p.milk = form.cleaned_data.get('milk')
            p.peanuts = form.cleaned_data.get('peanuts')
            p.shellfish = form.cleaned_data.get('shellfish')
            p.soy = form.cleaned_data.get('soy')
            p.tree_nuts = form.cleaned_data.get('tree_nuts')
            p.vegan = form.cleaned_data.get('vegan')
            p.vegetarian = form.cleaned_data.get('vegetarian')
            p.save()
        return redirect("/profile")
    else:
        form = SettingsForm(initial={
            'phone_number': rup.phone_number,
            'default_location': rup.default_location,
            'walking_factor': rup.walking_factor,
            'food_factor': rup.food_factor,
            'receive_notification_time': rup.receive_notification_time,
            'eggs': rup.eggs,
            'fish': rup.fish,
            'gluten': rup.gluten,
            'milk': rup.milk,
            'peanuts': rup.peanuts,
            'shellfish': rup.shellfish,
            'soy': rup.soy,
            'tree_nuts': rup.tree_nuts,
            'vegan': rup.vegan,
            'vegetarian': rup.vegetarian,
        })

    return render(request, "profile.html", {"form": form})
