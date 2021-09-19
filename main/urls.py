from django.urls import path
from . import views

urlpatterns = [
    path('s/<slug:slug>/', views.ServeryDetail.as_view(), name='servery_detail'),
    path('', views.ServeryList.as_view(), name='servery_list'),
    path('leaderboard/', views.Leaderboard.as_view(), name='leaderboard'),
    path('dish_leaderboard/', views.DishAppearanceLeaderboard.as_view(), name='dish_appearance_leaderboard'),
    path('d/<str:pk>', views.DishAppearanceDetail.as_view(), name='dish_appearance_detail'),
    path('m/<str:pk>', views.MealDetail.as_view(), name='meal_detail'),
    path('review/', views.review, name='review'),
    path('edit_dish/', views.edit_dish, name='edit_dish'),
    path('weekly_menu/', views.WeeklyMenu.as_view(), name='weekly_menu'),
    path('get_user_data/', views.get_user_data, name='get_user_data'),
    path('u/<int:pk>/<str:username>', views.UserDetail.as_view(), name='user_detail')
]