from decimal import Decimal
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.departments.models import Department


class StudentStatus(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    SUSPENDED = 'SUSPENDED', 'Suspended'
    GRADUATED = 'GRADUATED', 'Graduated'
    ALUMNI = 'ALUMNI', 'Alumni'


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )
    student_id = models.CharField(max_length=25, unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students'
    )
    semester = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    gpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=Decimal('3.50'),
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('4.00'))]
    )
    admission_date = models.DateField(auto_now_add=True)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, default='')
    blood_group = models.CharField(max_length=10, blank=True, default='')
    
    guardian_name = models.CharField(max_length=120, blank=True, default='')
    guardian_phone = models.CharField(max_length=20, blank=True, default='')
    guardian_email = models.EmailField(blank=True, default='')
    emergency_contact = models.CharField(max_length=20, blank=True, default='')
    
    status = models.CharField(
        max_length=20,
        choices=StudentStatus.choices,
        default=StudentStatus.ACTIVE
    )

    class Meta:
        ordering = ['student_id']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        full_name = self.user.get_full_name() or self.user.username
        return f"{self.student_id} - {full_name}"
