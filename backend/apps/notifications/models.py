from django.db import models
from django.conf import settings


class NotificationType(models.TextChoices):
    INFO = 'INFO', 'Information'
    WARNING = 'WARNING', 'Warning Alert'
    SUCCESS = 'SUCCESS', 'Success'
    ACADEMIC = 'ACADEMIC', 'Academic Notification'
    FEE_REMINDER = 'FEE_REMINDER', 'Fee Reminder'
    EXAM_ALERT = 'EXAM_ALERT', 'Exam Alert'


class Notification(models.Model):
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=200)
    message = models.TextField()
    notification_type = models.CharField(max_length=30, choices=NotificationType.choices, default=NotificationType.INFO)
    is_read = models.BooleanField(default=False)
    link_url = models.CharField(max_length=255, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Notification'
        verbose_name_plural = 'Notifications'

    def __str__(self):
        return f"To {self.recipient.username}: {self.title} ({'Read' if self.is_read else 'Unread'})"
