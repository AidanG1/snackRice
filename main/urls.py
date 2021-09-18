from django.urls import path
from . import views

urlpatterns = [
    path('s/<slug:slug>/', views.ServeryDetail.as_view(), name='servery_detail'),
    path('', views.ServeryList.as_view(), name='servery_list'),
    path('meals/', views.CurrentMealList.as_view(), name='curren_meal_list'),
    path('d/<str:pk>', views.DishAppearanceDetail.as_view(), name='dish_appearance_detail'),
    path('m/<str:pk>', views.MealDetail.as_view(), name='meal_detail'),
]