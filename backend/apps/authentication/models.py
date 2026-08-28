from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UserRole(models.TextChoices):
    ADMIN = 'ADMIN', _('Administrator')
    FACULTY = 'FACULTY', _('Faculty / Professor')
    STUDENT = 'STUDENT', _('Student')
    STAFF = 'STAFF', _('Campus Staff')


class User(AbstractUser):
    """
    Custom User model with role-based access control for Campus Management.
    """
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(
        max_length=20,
        choices=UserRole.choices,
        default=UserRole.STUDENT,
        help_text=_('Designates role of the user within the campus management system.')
    )
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True, default='')
    department_name = models.CharField(max_length=100, blank=True, default='')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = ['email']

    class Meta:
        ordering = ['-date_joined']
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"

    @property
    def is_admin_role(self):
        return self.role == UserRole.ADMIN or self.is_superuser

    @property
    def is_faculty_role(self):
        return self.role == UserRole.FACULTY

    @property
    def is_student_role(self):
        return self.role == UserRole.STUDENT
