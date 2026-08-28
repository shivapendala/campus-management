from django.db import models
from django.conf import settings
from apps.departments.models import Department


class Faculty(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='faculty_profile'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='faculty_members'
    )
    faculty_id = models.CharField(max_length=30, unique=True, blank=True, null=True)
    designation = models.CharField(max_length=100, default='Assistant Professor')
    qualification = models.CharField(max_length=150, blank=True, default='Ph.D.')
    specialization = models.CharField(max_length=200, blank=True, default='')
    office_room = models.CharField(max_length=50, blank=True, default='')
    office_hours = models.CharField(max_length=150, blank=True, default='Mon-Fri 2:00 PM - 4:00 PM')
    joining_date = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['user__last_name', 'user__first_name']
        verbose_name = 'Faculty Member'
        verbose_name_plural = 'Faculty Members'

    def __str__(self):
        full_name = self.user.get_full_name() or self.user.username
        return f"Prof. {full_name} ({self.designation})"
