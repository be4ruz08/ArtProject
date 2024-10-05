from django.contrib import admin
from .models import Artist


@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date', 'death_date')
    search_fields = ('name', 'biography')
    list_filter = ('birth_date', 'death_date')