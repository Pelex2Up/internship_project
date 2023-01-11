from django.urls import path
from . import views

app_name = 'cafe_core_app'

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<meal_category>', views.meal_category, name='meal_category'),
    path('<int:meal_id>/meal', views.meal_preview, name='meal'),
    path('meal_statistics/', views.top_meals, name='click_statistics'),
    path('<int:meal_id>/meal_stat', views.meal_click_stat, name='meal_click_stat'),
    path('<str:meal_type>/top_users/', views.top_users, name='top_users')
]