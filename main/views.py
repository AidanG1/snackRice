from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
from users.models import Profile
import datetime
from .forms import ReviewForm, DishImageForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import transaction


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

    # def get_queryset(self):
    #     return super().get_queryset().filter(meal_start_time__gte=datetime.datetime.now().time(),
    #                                          meal_end_time__lte=datetime.datetime.now().time())


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
        sorted_dishes = sorted(DishAppearance.objects.all(), key=lambda x: x.average_stars, reverse=True)
        for index, dish in enumerate(sorted_dishes):
            dish.rank = index + 1
        return sorted_dishes


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
