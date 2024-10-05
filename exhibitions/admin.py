from django.contrib import admin
from .models import Exhibition


@admin.register(Exhibition)
class ExhibitionAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'location')
    search_fields = ('title', 'description', 'location')
    list_filter = ('start_date', 'end_date')