import datetime

from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render
from qsstats import QuerySetStats

from .models import Meal, MealClick, UserClick
from django.utils import timezone


def menu(request):
    meals_categories = list(filter(lambda el: 'NO_TYPE' not in el[0], Meal.MealType.choices))
    return render(request, 'cafe_core_app/menu.html', {'meals_categories': meals_categories})


def meal_category(request, meal_category):
    meal_by_category = Meal.objects.filter(meal_type=meal_category)
    if request.user.is_authenticated:
        user = User.objects.get(id=request.user.id)
        user.userclick_set.create(click_date=timezone.now(), category=meal_category)
    return render(request, 'cafe_core_app/meals.html', {'meals': meal_by_category, 'meal_category': meal_category})


def meal_preview(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    meal.mealclick_set.create(click_date=timezone.now())
    return render(request, 'cafe_core_app/meal.html', {'meal': meal})


def top_meals(request):
    meal = Meal.objects.all()
    total_clicks = {}

    for meal_object in meal:
        clicks = MealClick.objects.filter(meal_id=meal_object.id).count()
        meal_name = meal_object.name
        total_clicks.update({meal_name: clicks})

    top3_meals = sorted(total_clicks, key=total_clicks.get)[::-1]
    top_clicks = sorted(total_clicks.values())[::-1]

    context = {
        'top3_meal': top3_meals[:3],
        'top3_click': top_clicks[:3]
    }

    return render(request, 'cafe_core_app/meal_statistics.html', context)


def meal_click_stat(request, meal_id):
    meal = Meal.objects.get(id=meal_id)
    meal_click = MealClick.objects.filter(meal_id=meal_id)

    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date.today()

    qsstats = QuerySetStats(meal_click, date_field='click_date', aggregate=Count('meal_id'))
    value_line = qsstats.time_series(start_date, end_date, interval='days')

    total_count = 0

    for i in value_line:
        total_count += i[1]

    context = {
        'meal': meal,
        'value_line': value_line,
        'total_count': total_count,
    }
    return render(request, 'cafe_core_app/meal_click_stat.html', context)


def top_users(request, meal_type):
    users = User.objects.all()
    result = []
    for user in users:
        clicks = UserClick.objects.filter(user_id=user.id, category=meal_type).count()
        result.append([clicks, user.username])

    result = sorted(result, reverse=True)[:10]
    context = {
        'top_users': result,
        'meal_type': meal_type
    }
    return render(request, 'cafe_core_app/top_users.html', context)
