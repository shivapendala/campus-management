import pytest
from django.urls import reverse
from rest_framework import status
from apps.courses.models import Course


@pytest.mark.django_db
class TestCoursesCompleteFlow:
    def test_course_catalog_lifecycle(self, auth_client, sample_department):
        course = Course.objects.create(
            department=sample_department,
            code='CSE-101',
            title='Data Structures & Algorithms',
            credits=4,
            description='Core data structures and algorithms course.',
        )
        assert course.code == 'CSE-101'

        url = reverse('course-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK

        detail_url = reverse('course-detail', kwargs={'pk': course.pk})
        detail_res = auth_client.get(detail_url)
        assert detail_res.status_code == status.HTTP_200_OK
        assert detail_res.data['code'] == 'CSE-101'
