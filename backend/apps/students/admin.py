from django.contrib import admin
from .models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'user', 'department', 'semester', 'gpa', 'status', 'admission_date')
    list_filter = ('department', 'semester', 'status')
    search_fields = ('student_id', 'user__username', 'user__first_name', 'user__last_name', 'guardian_name')
