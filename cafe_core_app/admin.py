from django.contrib import admin
from .models import Meal, PhotoGallery


class PhotoGalleryInline(admin.TabularInline):
    fk_name = 'meal'
    model = PhotoGallery


@admin.register(Meal)
class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'meal_type', 'price', 'size', 'id')
    search_fields = ('name', 'meal_type', 'id')
    inlines = [PhotoGalleryInline, ]
