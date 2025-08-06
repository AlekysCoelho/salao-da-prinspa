from django.contrib import admin

from .models import Service


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ('name', 'active', 'duration',)
    list_filter = ('name', 'active',)
    search_fields = ('name',)