from django.contrib import admin
from .models import AttendanceSession, AttendanceRecord


@admin.register(AttendanceSession)
class AttendanceSessionAdmin(admin.ModelAdmin):
    list_display = ('course', 'date', 'session_type', 'faculty', 'start_time', 'end_time')
    list_filter = ('session_type', 'date', 'course__department')
    search_fields = ('course__code', 'course__title', 'topic_covered')


@admin.register(AttendanceRecord)
class AttendanceRecordAdmin(admin.ModelAdmin):
    list_display = ('student', 'session', 'status', 'remarks')
    list_filter = ('status', 'session__date')
    search_fields = ('student__student_id', 'student__user__username', 'session__course__code')
