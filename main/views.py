from django.shortcuts import render, redirect, HttpResponse
from django.views.generic import ListView, DetailView
from .models import *
from users.models import Profile
import datetime, json
from .forms import ReviewForm, DishImageForm
from django.contrib.auth.decorators import login_required
from django.db import transaction
from findbestservery import main


class ServeryDetail(DetailView):
    model = Servery
    context_object_name = 'servery'
    template_name = 'servery_detail.html'


class ServeryList(ListView):
    model = Servery
    context_object_name = 'serveries'
    template_name = 'servery_list.html'


class DishAppearanceDetail(DetailView):
    model = DishAppearance
    context_object_name = 'dish_appearance'
    template_name = 'dish_appearance_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['review_form'] = ReviewForm
        context['image_form'] = DishImageForm
        return context


class MealDetail(DetailView):
    model = Meal
    context_object_name = 'meal'
    template_name = 'meal_detail.html'


class Leaderboard(ListView):
    model = Profile
    paginate_by = 5
    context_object_name = 'profiles'
    template_name = 'leaderboard.html'

    def get_queryset(self):
        sorted_profiles = sorted(Profile.objects.all(), key=lambda x: x.review_count, reverse=True)
        for index, profile in enumerate(sorted_profiles):
            profile.rank = index + 1
        return sorted_profiles


class DishAppearanceLeaderboard(ListView):
    model = DishAppearance
    paginate_by = 5
    context_object_name = 'dish_appearances'
    template_name = 'dish_appearance_leaderboard.html'

    def get_queryset(self):
        sorted_dishes = sorted(DishAppearance.objects.all(), key=lambda x: (x.average_stars), reverse=True)
        for index, dish in enumerate(sorted_dishes):
            dish.rank = index + 1
        return sorted_dishes


class WeeklyMenu(ListView):
    model = Meal
    context_object_name = 'meals'
    template_name = 'weekly_menu.html'


class UserDetail(DetailView):
    model = User
    context_object_name = 'user_to_view'
    template_name = 'user_detail.html'


@login_required()
@transaction.atomic
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            if Review.objects.filter(user=request.user, dish_appearance=DishAppearance.objects.get(
                    pk=request.GET.get('dish', ''))).count() > 0:
                r = Review.objects.get(user=request.user, dish_appearance=DishAppearance.objects.get(
                    pk=request.GET.get('dish', '')))
                r.stars = form.cleaned_data.get('stars')
                if len(form.cleaned_data.get('review_text')) > 0:
                    r.review_text = form.cleaned_data.get('review_text')
                r.save()
            else:
                Review.objects.create(user=request.user, stars=form.cleaned_data.get('stars'),
                                      review_text=form.cleaned_data.get('review_text'),
                                      dish_appearance=DishAppearance.objects.get(pk=request.GET.get('dish', '')))
            return redirect('dish_appearance_detail', request.GET.get('dish', ''))
    else:
        form = ReviewForm(request.user)
    return render(request, 'dish_appearance_detail.html', {'form': form})


@login_required()
def edit_dish(request):
    if request.method == "POST":
        form = DishImageForm(request.POST)
        if form.is_valid():
            d = Dish.objects.get(pk=request.GET.get('dish', ''))
            d.image = form.cleaned_data.get('image')
            d.save()
        return redirect('dish_appearance_detail', DishAppearance.objects.filter(dish=d).last().uuid)
    else:
        form = DishImageForm()

    return render(request, "edit_dish.html", {"form": form})


def get_user_data(request):
    max_value = -100
    correct_key = ''
    for key, value in main(
            request.GET.get('location',
                            'ChIJf8hcvX7AQIYRH9dtCL4HGXw')).items():  # uses Baker College if location is not in request parameters
        if value > max_value:
            max_value = value
            correct_key = key
    print(correct_key)
    current_dishes = Servery.objects.get(name=correct_key).current_dishes
    return HttpResponse(
        json.dumps(
            {
                'current_dishes': [{'dish': dish.dish.name, 'stars': dish.average_stars, 'reviews': dish.review_count}
                                   for dish in current_dishes],
                'servery': correct_key,
            }
        ),
        content_type="application/json")
