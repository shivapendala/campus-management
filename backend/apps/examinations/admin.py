from django.contrib import admin
from .models import Exam, ExamResult


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('name', 'course', 'exam_type', 'date', 'max_marks', 'passing_marks', 'venue')
    list_filter = ('exam_type', 'date', 'course__department')
    search_fields = ('name', 'course__code', 'course__title')


@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'exam', 'marks_obtained', 'grade', 'is_passed', 'recorded_at')
    list_filter = ('grade', 'exam__exam_type')
    search_fields = ('student__student_id', 'student__user__username', 'exam__name')
