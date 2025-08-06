from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from app.utils.admin import AuditFieldsAdminMixin

from .models import Availability, Professional


class AvailabilityInline(admin.TabularInline):
    """
    Displays a professional's availability times in a tabular format.
    """

    model = Availability
    extra = 3
    fields = ('weekday', 'start_time', 'end_time')


@admin.register(Professional)
class ProfessionalAdmin(AuditFieldsAdminMixin, admin.ModelAdmin):
    list_display = ('name', 'list_services', 'created_at', 'updated_at')
    list_filter = ('services',)
    search_fields = ('name',)
    fieldsets = [
        (None, {
            'fields': ('name', 'services',)
        }),
    ]
    inlines = [AvailabilityInline,]

    def list_services(self, obj):
        """
        Helper method to display a professional's services in the list.
        """
        return ', '.join([service.name for service in obj.service.all()])
    
    list_services.short_description = 'Services'
