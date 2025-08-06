from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from rolepermissions.roles import assign_role

from .forms import UsersChangeForm, UsersCreationForm

User = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = UsersCreationForm
    form = UsersChangeForm
    model = User

    list_display = ("username", "email", "is_staff", "is_active")
    list_filter = ("is_staff", "is_active")

    fieldsets = (
        (None, {"fields": ("username", "email", "password", "bio")}),
        ("Permissões", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    # Corrigindo o add_fieldsets para usar os campos 'password1' e 'password2'
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("username", "email", "bio", "password1", "password2", "role"),
        }),
    )
    search_fields = ("username", "email")
    ordering = ("username",)

    def save_model(self, request, obj, form, change):
        # Movemos esta lógica para o save do formulário para manter a consistência
        if not change and 'role' in form.cleaned_data:
            assign_role(obj, form.cleaned_data['role'])
        super().save_model(request, obj, form, change)


admin.site.register(User, CustomUserAdmin)