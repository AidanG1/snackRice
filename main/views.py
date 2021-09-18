from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
import datetime
from .forms import ReviewForm
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
        return context


class MealDetail(DetailView):
    model = Meal
    context_object_name = 'meal'
    template_name = 'meal_detail.html'

    # def get_queryset(self):
    #     return super().get_queryset().filter(meal_start_time__gte=datetime.datetime.now().time(),
    #                                          meal_end_time__lte=datetime.datetime.now().time())


class Leaderboard(ListView):
    model = User
    context_object_name = 'users'
    template_name = 'leaderboard.html'


@login_required()
@transaction.atomic
def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(user=request.user, stars=form.cleaned_data.get('stars'),
                                  review_text=form.cleaned_data.get('review_text'),
                                  dish_appearance=DishAppearance.objects.get(pk=request.GET.get('dish', '')))
            return redirect('dish_appearance_detail', request.GET.get('dish', ''))
    else:
        form = ReviewForm(request.user)
    return render(request, 'dish_appearance_detail.html', {'form': form})
