from decimal import Decimal
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.departments.models import Department


class StudentStatus(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    INACTIVE = 'INACTIVE', 'Inactive'
    GRADUATED = 'GRADUATED', 'Graduated'
    SUSPENDED = 'SUSPENDED', 'Suspended'


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='student_profile'
    )
    student_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students'
    )
    year = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        help_text='Academic Year (e.g. 1st, 2nd, 3rd, 4th Year)'
    )
    section = models.CharField(max_length=10, default='A')
    semester = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1), MaxValueValidator(12)]
    )
    admission_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=StudentStatus.choices,
        default=StudentStatus.ACTIVE
    )
    gpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=Decimal('3.50'),
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('4.00'))]
    )
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=20, blank=True, default='')
    guardian_name = models.CharField(max_length=120, blank=True, default='')
    guardian_phone = models.CharField(max_length=20, blank=True, default='')

    class Meta:
        ordering = ['student_id']
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def __str__(self):
        return f"{self.student_id} - {self.name}"

    def save(self, *args, **kwargs):
        # Auto-sync name/email with linked user if present
        if self.user and not self.name:
            self.name = self.user.get_full_name() or self.user.username
        if self.user and not self.email:
            self.email = self.user.email
        super().save(*args, **kwargs)
