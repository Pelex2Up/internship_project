from rest_framework import serializers
from .models import Meal, UserClick, MealClick


class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class UserClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClick
        fields = '__all__'


class MealClickSerializer(serializers.ModelSerializer):
    class Meta:
        model = MealClick
        fields = '__all__'
