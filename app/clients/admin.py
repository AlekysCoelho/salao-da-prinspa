from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client
    list_display = ('name', 'phone', 'email',)
    list_filter = ('name', 'email',)
    search_fields = ('name',)