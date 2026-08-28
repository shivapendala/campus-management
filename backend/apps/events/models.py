from django.db import models
from django.conf import settings


class EventType(models.TextChoices):
    SEMINAR = 'SEMINAR', 'Academic Seminar'
    WORKSHOP = 'WORKSHOP', 'Technical Workshop'
    CULTURAL = 'CULTURAL', 'Cultural Fest'
    SPORTS = 'SPORTS', 'Sports Tournament'
    CONFERENCE = 'CONFERENCE', 'Conference / Symposium'
    HACKATHON = 'HACKATHON', 'Hackathon / Codefest'


class Event(models.Model):
    title = models.CharField(max_length=200)
    organizer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='organized_events')
    event_type = models.CharField(max_length=30, choices=EventType.choices, default=EventType.WORKSHOP)
    venue = models.CharField(max_length=150, default='Main Campus Auditorium')
    description = models.TextField(blank=True, default='')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    capacity = models.PositiveIntegerField(default=100)
    banner_image_url = models.URLField(blank=True, null=True)
    is_public = models.BooleanField(default=True)
    registration_deadline = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-start_time']
        verbose_name = 'Event'
        verbose_name_plural = 'Events'

    def __str__(self):
        return f"{self.title} ({self.get_event_type_display()})"

    @property
    def registered_count(self):
        return self.registrations.count()


class AttendanceStatus(models.TextChoices):
    REGISTERED = 'REGISTERED', 'Registered'
    ATTENDED = 'ATTENDED', 'Attended'
    CANCELLED = 'CANCELLED', 'Cancelled'
    NO_SHOW = 'NO_SHOW', 'No Show'


class EventRegistration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='registrations')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='event_registrations')
    registered_at = models.DateTimeField(auto_now_add=True)
    attendance_status = models.CharField(max_length=20, choices=AttendanceStatus.choices, default=AttendanceStatus.REGISTERED)
    certificate_url = models.URLField(blank=True, null=True)

    class Meta:
        unique_together = ('event', 'user')
        ordering = ['-registered_at']
        verbose_name = 'Event Registration'
        verbose_name_plural = 'Event Registrations'

    def __str__(self):
        return f"{self.user.username} registered for {self.event.title}"
