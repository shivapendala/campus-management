from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'department_name', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Campus Profile Information', {
            'fields': ('role', 'phone_number', 'department_name', 'bio', 'avatar')
        }),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Campus Profile Information', {
            'fields': ('role', 'phone_number', 'department_name', 'bio', 'email')
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email', 'department_name')
