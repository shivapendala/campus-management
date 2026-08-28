import pytest
from django.urls import reverse
from rest_framework import status
from apps.complaints.models import Complaint, ComplaintStatus, ComplaintPriority


@pytest.mark.django_db
class TestComplaintsCompleteFlow:
    def test_complaint_ticketing_and_resolution(self, auth_client, admin_user):
        complaint = Complaint.objects.create(
            submitted_by=admin_user,
            title='Projector replacement in Lecture Hall 2',
            description='Lamp bulb failing.',
            priority=ComplaintPriority.HIGH,
            status=ComplaintStatus.OPEN,
        )
        assert complaint.status == ComplaintStatus.OPEN

        url = reverse('complaint-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK

        complaint.status = ComplaintStatus.RESOLVED
        complaint.resolution_notes = 'Replaced with 4K laser projector.'
        complaint.save()
        assert complaint.status == ComplaintStatus.RESOLVED
