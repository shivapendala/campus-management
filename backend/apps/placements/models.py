from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from apps.students.models import Student


class Company(models.Model):
    name = models.CharField(max_length=150, unique=True)
    website = models.URLField(blank=True, null=True)
    industry = models.CharField(max_length=100, default='Information Technology')
    contact_person = models.CharField(max_length=100, blank=True, default='')
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name


class DriveStatus(models.TextChoices):
    UPCOMING = 'UPCOMING', 'Upcoming'
    ONGOING = 'ONGOING', 'Ongoing'
    COMPLETED = 'COMPLETED', 'Completed'
    CANCELLED = 'CANCELLED', 'Cancelled'


class PlacementDrive(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='drives')
    title = models.CharField(max_length=200)
    job_role = models.CharField(max_length=150)
    job_description = models.TextField(blank=True, default='')
    package_lpa = models.DecimalField(max_digits=6, decimal_places=2, help_text='Package in LPA (Lakhs Per Annum)')
    eligibility_gpa = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal('3.00'))
    drive_date = models.DateField()
    application_deadline = models.DateTimeField()
    location = models.CharField(max_length=150, default='Campus Placement Auditorium')
    status = models.CharField(max_length=20, choices=DriveStatus.choices, default=DriveStatus.UPCOMING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-drive_date']
        verbose_name = 'Placement Drive'
        verbose_name_plural = 'Placement Drives'

    def __str__(self):
        return f"{self.company.name} - {self.job_role} ({self.package_lpa} LPA)"


class ApplicationStatus(models.TextChoices):
    APPLIED = 'APPLIED', 'Applied'
    SHORTLISTED = 'SHORTLISTED', 'Shortlisted'
    INTERVIEW_SCHEDULED = 'INTERVIEW_SCHEDULED', 'Interview Scheduled'
    OFFERED = 'OFFERED', 'Offer Received'
    REJECTED = 'REJECTED', 'Rejected'
    ACCEPTED = 'ACCEPTED', 'Offer Accepted'


class JobApplication(models.Model):
    drive = models.ForeignKey(PlacementDrive, on_delete=models.CASCADE, related_name='applications')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='job_applications')
    resume_url = models.URLField(blank=True, null=True)
    status = models.CharField(max_length=30, choices=ApplicationStatus.choices, default=ApplicationStatus.APPLIED)
    applied_at = models.DateTimeField(auto_now_add=True)
    offer_letter_url = models.URLField(blank=True, null=True)
    remarks = models.TextField(blank=True, default='')

    class Meta:
        unique_together = ('drive', 'student')
        ordering = ['-applied_at']
        verbose_name = 'Job Application'
        verbose_name_plural = 'Job Applications'

    def __str__(self):
        return f"{self.student.student_id} for {self.drive.company.name} ({self.status})"
