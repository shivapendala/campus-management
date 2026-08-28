from django.contrib import admin
from .models import Faculty


@admin.register(Faculty)
class FacultyAdmin(admin.ModelAdmin):
    list_display = ('faculty_id', 'name', 'email', 'phone', 'department', 'designation', 'status', 'joining_date')
    list_filter = ('department', 'designation', 'status')
    search_fields = ('faculty_id', 'name', 'email', 'phone')
