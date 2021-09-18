from django.contrib import admin
from .models import *


class ServeryDisplay(admin.ModelAdmin):
    list_display = ['uuid', 'slug', 'name']


class DishAppearanceDisplay(admin.ModelAdmin):
    list_display = ['uuid', 'dish', 'meal']


class DishDisplay(admin.ModelAdmin):
    list_display = ['uuid', 'name', 'vegan']


class MealDisplay(admin.ModelAdmin):
    list_display = ['uuid', 'servery', 'meal_type', 'meal_date', 'meal_start_time', 'meal_end_time']


class ReviewDisplay(admin.ModelAdmin):
    list_display = ['uuid', 'dish_appearance', 'user', 'stars', 'review_datetime']


admin.site.register(Servery, ServeryDisplay)
admin.site.register(Dish, DishDisplay)
admin.site.register(DishAppearance, DishAppearanceDisplay)
admin.site.register(Meal, MealDisplay)
admin.site.register(Review, ReviewDisplay)
