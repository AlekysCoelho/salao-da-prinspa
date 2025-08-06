from django.contrib import admin

from app.utils.admin import AuditFieldsAdminMixin

from .models import Appointment


@admin.register(Appointment)
class AppointmentAdmin(AuditFieldsAdminMixin, admin.ModelAdmin):
    list_display = (
        'client__name',
        'professional__name',
        'service__name',
        'scheduled_at',
        'status',
        'created_at',
        'updated_at'
    )
    list_filter = (
        'status',
        'professional',
        'service',
        'scheduled_at'
    )
    search_fields = (
        'client__name',
        'professional__name',
        'service__name'
    )
    fieldsets = [
        (None, {
            'fields': ('client', 'professional', 'service', 'scheduled_at', 'status')
        }),
    ]
