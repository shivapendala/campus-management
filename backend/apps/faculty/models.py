from django.db import models
from django.conf import settings
from apps.departments.models import Department


class FacultyStatus(models.TextChoices):
    ACTIVE = 'ACTIVE', 'Active'
    ON_LEAVE = 'ON_LEAVE', 'On Leave'
    RETIRED = 'RETIRED', 'Retired'
    RESIGNED = 'RESIGNED', 'Resigned'


class Faculty(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='faculty_profile'
    )
    faculty_id = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, default='')
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='faculty_members'
    )
    designation = models.CharField(
        max_length=100,
        default='Assistant Professor',
        help_text='e.g. Professor, Associate Professor, Assistant Professor, HOD, Dean'
    )
    qualification = models.CharField(max_length=150, blank=True, default='Ph.D.')
    specialization = models.CharField(max_length=200, blank=True, default='')
    office_room = models.CharField(max_length=50, blank=True, default='')
    joining_date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=FacultyStatus.choices,
        default=FacultyStatus.ACTIVE
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculty Members'

    def __str__(self):
        return f"{self.faculty_id} - {self.name} ({self.designation})"

    def save(self, *args, **kwargs):
        if self.user and not self.name:
            self.name = self.user.get_full_name() or self.user.username
        if self.user and not self.email:
            self.email = self.user.email
        super().save(*args, **kwargs)
