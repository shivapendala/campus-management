from rest_framework import viewsets, permissions, filters
from .models import Event, EventRegistration
from .serializers import EventSerializer, EventRegistrationSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.select_related('organizer').prefetch_related('registrations').all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'venue', 'description', 'event_type']
    ordering_fields = ['start_time', 'created_at', 'capacity']


class EventRegistrationViewSet(viewsets.ModelViewSet):
    queryset = EventRegistration.objects.select_related('event', 'user').all()
    serializer_class = EventRegistrationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['event__title', 'user__username', 'user__first_name', 'user__last_name']
    ordering_fields = ['registered_at', 'attendance_status']
