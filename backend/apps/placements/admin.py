from django.contrib import admin
from .models import Company, PlacementDrive, JobApplication


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'contact_person', 'contact_email', 'contact_phone')
    search_fields = ('name', 'industry', 'contact_person')


@admin.register(PlacementDrive)
class PlacementDriveAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'job_role', 'package_lpa', 'eligibility_gpa', 'drive_date', 'status')
    list_filter = ('status', 'drive_date', 'company')
    search_fields = ('title', 'job_role', 'company__name')


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('student', 'drive', 'status', 'applied_at')
    list_filter = ('status', 'applied_at', 'drive__company')
    search_fields = ('student__student_id', 'student__user__username', 'drive__title')
