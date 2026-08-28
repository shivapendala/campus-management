from django.contrib import admin
from .models import Course, Enrollment


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'department', 'instructor', 'credits', 'capacity', 'semester_offered', 'is_elective')
    list_filter = ('department', 'semester_offered', 'is_elective', 'credits')
    search_fields = ('code', 'title', 'department__name')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'status', 'final_grade', 'enrolled_at')
    list_filter = ('status', 'course__department')
    search_fields = ('student__student_id', 'student__user__username', 'course__code', 'course__title')
