from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import *
import datetime


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


class MealDetail(DetailView):
    model = Meal
    context_object_name = 'meal'
    template_name = 'meal_detail.html'


class CurrentMealList(ListView):
    model = Meal
    context_object_name = 'meals'
    template_name = 'current_meal_list.html'

    # def get_queryset(self):
    #     return super().get_queryset().filter(meal_start_time__gte=datetime.datetime.now().time(),
    #                                          meal_end_time__lte=datetime.datetime.now().time())
