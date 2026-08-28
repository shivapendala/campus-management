from django.contrib import admin
from .models import Event, EventRegistration


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'event_type', 'venue', 'start_time', 'end_time', 'capacity', 'is_public')
    list_filter = ('event_type', 'is_public', 'start_time')
    search_fields = ('title', 'venue', 'description')


@admin.register(EventRegistration)
class EventRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'event', 'registered_at', 'attendance_status')
    list_filter = ('attendance_status', 'registered_at', 'event__event_type')
    search_fields = ('user__username', 'event__title')
