from django.contrib import admin
from .models import Department, FacultyMember, Student, Course, Enrollment


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'established_year', 'created_at')
    search_fields = ('code', 'name')


@admin.register(FacultyMember)
class FacultyMemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'designation', 'office_room', 'joining_date')
    list_filter = ('department', 'designation')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'specialization')


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'user', 'department', 'semester', 'gpa', 'enrollment_date')
    list_filter = ('department', 'semester')
    search_fields = ('student_id', 'user__username', 'user__first_name', 'user__last_name')


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('code', 'title', 'department', 'instructor', 'credits', 'capacity', 'semester_offered')
    list_filter = ('department', 'semester_offered', 'credits')
    search_fields = ('code', 'title')


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'grade', 'attendance_percentage', 'enrolled_at')
    list_filter = ('grade', 'course__department')
    search_fields = ('student__student_id', 'student__user__username', 'course__code', 'course__title')
