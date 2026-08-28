from django.contrib import admin
from .models import Assignment, AssignmentSubmission


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'faculty', 'max_score', 'deadline', 'is_published')
    list_filter = ('is_published', 'course__department', 'deadline')
    search_fields = ('title', 'course__code', 'course__title')


@admin.register(AssignmentSubmission)
class AssignmentSubmissionAdmin(admin.ModelAdmin):
    list_display = ('student', 'assignment', 'submitted_at', 'score', 'status')
    list_filter = ('status', 'submitted_at')
    search_fields = ('student__student_id', 'student__user__username', 'assignment__title')
