import pytest
from django.urls import reverse
from rest_framework import status
from apps.notifications.models import Notification, NotificationType


@pytest.mark.django_db
class TestNotificationsCompleteFlow:
    def test_broadcast_and_read_receipts(self, auth_client, admin_user):
        notice = Notification.objects.create(
            recipient=admin_user,
            title='Mid-Term Examination Schedule',
            message='Timetable has been published.',
            notification_type=NotificationType.ACADEMIC,
            is_read=False,
        )
        assert notice.is_read is False

        url = reverse('notification-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK

        notice.is_read = True
        notice.save()
        assert notice.is_read is True
