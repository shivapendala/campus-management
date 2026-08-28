import uuid
from django.db import models
from django.conf import settings


class ComplaintCategory(models.TextChoices):
    ACADEMIC = 'ACADEMIC', 'Academic & Examinations'
    HOSTEL = 'HOSTEL', 'Hostel & Accommodation'
    FINANCE = 'FINANCE', 'Fee & Finance'
    INFRASTRUCTURE = 'INFRASTRUCTURE', 'Campus Infrastructure & Wi-Fi'
    HARASSMENT = 'HARASSMENT', 'Harassment / Discipline'
    CANTEEN = 'CANTEEN', 'Canteen & Food Quality'
    OTHER = 'OTHER', 'Other General Concerns'


class ComplaintPriority(models.TextChoices):
    LOW = 'LOW', 'Low'
    MEDIUM = 'MEDIUM', 'Medium'
    HIGH = 'HIGH', 'High'
    URGENT = 'URGENT', 'Urgent'


class ComplaintStatus(models.TextChoices):
    OPEN = 'OPEN', 'Open'
    UNDER_REVIEW = 'UNDER_REVIEW', 'Under Review'
    RESOLVED = 'RESOLVED', 'Resolved'
    REJECTED = 'REJECTED', 'Rejected'


class Complaint(models.Model):
    ticket_id = models.CharField(max_length=50, unique=True, default=uuid.uuid4)
    submitted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='filed_complaints')
    category = models.CharField(max_length=30, choices=ComplaintCategory.choices, default=ComplaintCategory.ACADEMIC)
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=20, choices=ComplaintPriority.choices, default=ComplaintPriority.MEDIUM)
    status = models.CharField(max_length=20, choices=ComplaintStatus.choices, default=ComplaintStatus.OPEN)
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='assigned_complaints'
    )
    resolution_notes = models.TextField(blank=True, default='')
    resolved_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Complaint'
        verbose_name_plural = 'Complaints'

    def __str__(self):
        return f"Ticket #{self.ticket_id[:8]} - {self.title} ({self.status})"
