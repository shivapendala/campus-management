import secrets
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UserRole(models.TextChoices):
    ADMIN = 'ADMIN', _('Administrator')
    HOD = 'HOD', _('Head of Department')
    FACULTY = 'FACULTY', _('Faculty / Professor')
    STUDENT = 'STUDENT', _('Student')
    PLACEMENT_OFFICER = 'PLACEMENT_OFFICER', _('Placement Officer')
    ACCOUNTANT = 'ACCOUNTANT', _('Accountant / Finance Officer')
    LIBRARIAN = 'LIBRARIAN', _('Librarian')


class UserStatus(models.TextChoices):
    ACTIVE = 'ACTIVE', _('Active')
    INACTIVE = 'INACTIVE', _('Inactive')
    SUSPENDED = 'SUSPENDED', _('Suspended')
    PENDING = 'PENDING', _('Pending Verification')


class User(AbstractUser):
    """
    Custom User model supporting institutional role-based access.
    """
    email = models.EmailField(_('email address'), unique=True)
    role = models.CharField(
        max_length=30,
        choices=UserRole.choices,
        default=UserRole.STUDENT,
        help_text=_('Designates user institutional role.')
    )
    phone = models.CharField(max_length=20, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        default=UserStatus.ACTIVE
    )
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True, default='')
    address = models.TextField(blank=True, default='')
    department_name = models.CharField(max_length=120, blank=True, default='')
    
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
        return self.role in [UserRole.ADMIN, UserRole.HOD] or self.is_superuser


class PasswordResetToken(models.Model):
    """
    Temporary token for password reset workflow.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='password_reset_tokens')
    token = models.CharField(max_length=64, unique=True, default=secrets.token_urlsafe)
    code = models.CharField(max_length=6, default='123456')
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    is_used = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if not self.expires_at:
            self.expires_at = timezone.now() + timedelta(hours=2)
        if not self.code:
            self.code = f"{secrets.randbelow(900000) + 100000}"
        super().save(*args, **kwargs)

    @property
    def is_valid(self):
        return not self.is_used and timezone.now() < self.expires_at
