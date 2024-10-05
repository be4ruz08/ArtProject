from django.contrib import admin
from .models import Category, ArtWork


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ArtWork)
class ArtWorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'category', 'created_at')
    search_fields = ('title', 'description', 'artist__name', 'category__name')
    list_filter = ('created_at', 'category')
