from django.contrib.auth.models import User
from django.db import models


class Meal(models.Model):
    name = models.CharField('Название блюда', max_length=25, blank=False)
    description = models.TextField('Описание блюда')
    price = models.IntegerField('Цена блюда')
    size = models.IntegerField('Граммовка блюда')

    class MealType(models.TextChoices):
        HOT_MEALS = 'Горячие блюда'
        DRINK = 'Напитки'
        DESSERTS = 'Десерты'
        NO_TYPE = 'NO_TYPE'

    meal_type = models.CharField(
        'Категория блюда',
        max_length=20,
        choices=MealType.choices,
        default=MealType.NO_TYPE,
    )

    def __str__(self):
        return self.name


class MealClick(models.Model):
    meal = models.ForeignKey(Meal, on_delete=models.DO_NOTHING)
    click_date = models.DateTimeField('Дата клика', auto_now_add=True)


class UserClick(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    click_date = models.DateTimeField('Дата клика', auto_now_add=True)
    category = models.CharField('Категория', max_length=50)


class PhotoGallery(models.Model):
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    meal = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='images')
