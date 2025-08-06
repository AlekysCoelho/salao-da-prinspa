from django.contrib import admin


class AuditFieldsAdminMixin(admin.ModelAdmin):
    """
    Mixin to add audit fields (created_at, updated_at) in Admin classes
    """

    readonly_fields = ('created_at', 'updated_at')

    def get_fieldsets(self, request, obj=None):
        """
        Override the fieldsets method to add audit fields.
        """

        fieldsets = super().get_fieldsets(request, obj)
        audit_fieldset = ('Registration dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        })
        return list(fieldsets) + [audit_fieldset]