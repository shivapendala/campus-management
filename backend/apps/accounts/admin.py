from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'phone', 'status', 'is_staff')
    list_filter = ('role', 'status', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Campus Details', {
            'fields': ('role', 'phone', 'status', 'department_name', 'bio', 'address', 'avatar')
        }),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Campus Details', {
            'fields': ('role', 'phone', 'status', 'department_name', 'email')
        }),
    )
    search_fields = ('username', 'first_name', 'last_name', 'email', 'phone')
