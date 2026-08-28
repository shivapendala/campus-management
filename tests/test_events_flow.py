import pytest
from datetime import timedelta
from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from apps.events.models import Event, EventRegistration


@pytest.mark.django_db
class TestEventsCompleteFlow:
    def test_event_creation_and_pass_registration(self, auth_client, admin_user):
        event = Event.objects.create(
            title='Annual International Hackathon 2026',
            event_type='HACKATHON',
            venue='Innovation Arena',
            start_time=timezone.now() + timedelta(days=10),
            end_time=timezone.now() + timedelta(days=12),
            capacity=250,
        )
        assert event.capacity == 250

        reg = EventRegistration.objects.create(
            event=event,
            user=admin_user,
        )
        assert reg.id is not None

        url = reverse('event-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK
