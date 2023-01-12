from django.urls import path, include
from rest_framework import routers
from .api import MealViewSet, MealClickViewSet, UserClickViewSet
from . import views

app_name = 'cafe_core_app'

router = routers.DefaultRouter()
router.register('api/meal', MealViewSet, 'api_meal-list')
router.register('api/meal_click', MealClickViewSet, 'api_meal_click-list')
router.register('api/user_click', UserClickViewSet, 'api_user-click-list')

urlpatterns = [
    path('', views.menu, name='menu'),
    path('<meal_category>', views.meal_category, name='meal_category'),
    path('<int:meal_id>/meal', views.meal_preview, name='meal'),
    path('meal_statistics/', views.top_meals, name='click_statistics'),
    path('<int:meal_id>/meal_stat', views.meal_click_stat, name='meal_click_stat'),
    path('<str:meal_type>/top_users/', views.top_users, name='top_users'),
    path('', include(router.urls))
]