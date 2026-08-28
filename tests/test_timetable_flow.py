import pytest
from django.urls import reverse
from rest_framework import status
from apps.courses.models import Course, TimetableEntry


@pytest.mark.django_db
class TestTimetableCompleteFlow:
    def test_timetable_and_conflict_detection(self, auth_client, sample_department):
        course = Course.objects.create(
            department=sample_department,
            code='CSE-202',
            title='Database Management Systems',
            credits=4,
        )

        entry = TimetableEntry.objects.create(
            course=course,
            day='Monday',
            start_time='09:00',
            end_time='10:00',
            room='Room Curie-301',
            section='A',
        )
        assert entry.id is not None

        url = reverse('timetable-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK

        conflict_url = reverse('timetable-check-conflicts')
        conflict_res = auth_client.post(conflict_url, {
            'day': 'Monday',
            'start_time': '09:00',
            'end_time': '10:00',
            'room': 'Room Curie-301',
            'section': 'A',
        }, format='json')
        assert conflict_res.status_code == status.HTTP_200_OK
        assert conflict_res.data['has_conflicts'] is True
