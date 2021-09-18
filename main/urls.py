from django.urls import path
from . import views

urlpatterns = [
    path('s/<slug:slug>/', views.ServeryDetail.as_view(), name='servery_detail'),
    path('', views.ServeryList.as_view(), name='servery_list'),
    path('leaderboard/', views.Leaderboard.as_view(), name='leaderboard'),
    path('d/<str:pk>', views.DishAppearanceDetail.as_view(), name='dish_appearance_detail'),
    path('m/<str:pk>', views.MealDetail.as_view(), name='meal_detail'),
    path('review/', views.review, name='review')
]