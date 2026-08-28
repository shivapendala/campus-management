from django.contrib import admin
from .models import Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'head_of_department', 'building_block', 'established_year', 'created_at')
    search_fields = ('code', 'name', 'head_of_department')
    list_filter = ('established_year', 'building_block')
