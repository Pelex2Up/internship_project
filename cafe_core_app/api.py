from rest_framework import viewsets, permissions
from .models import Meal, MealClick, UserClick
from .serializers import MealSerializer, MealClickSerializer, UserClickSerializer


class MealViewSet(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = MealSerializer


class MealClickViewSet(viewsets.ModelViewSet):
    queryset = MealClick.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = MealClickSerializer


class UserClickViewSet(viewsets.ModelViewSet):
    queryset = UserClick.objects.all()
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserClickSerializer
