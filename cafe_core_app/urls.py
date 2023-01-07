from django.urls import path
from . import views

app_name = 'cafe_core_app'

urlpatterns = [
    path('menu/', views.menu, name='menu'),
    path('', views.menu, name='menu'),
    path('<meal_category>', views.meal_category, name='meal_category'),
    path('<int:meal_id>/meal', views.meal, name='meal'),
    path('meal_statistics', views.meal_statistics, name='click_statistics'),

]