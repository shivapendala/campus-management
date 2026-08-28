import pytest
from django.urls import reverse
from rest_framework import status
from apps.faculty.models import Faculty


@pytest.mark.django_db
class TestFacultyCompleteFlow:
    def test_faculty_directory_lifecycle(self, auth_client, admin_user, sample_department):
        faculty = Faculty.objects.create(
            user=admin_user,
            name='Dr. Alan Turing',
            email='turing@campus.edu',
            department=sample_department,
            faculty_id='FAC-CSE-099',
            designation='Professor',
            specialization='Theoretical Computer Science',
        )
        assert faculty.faculty_id == 'FAC-CSE-099'

        url = reverse('faculty-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK

        detail_url = reverse('faculty-detail', kwargs={'pk': faculty.pk})
        detail_res = auth_client.get(detail_url)
        assert detail_res.status_code == status.HTTP_200_OK
        assert detail_res.data['name'] == 'Dr. Alan Turing'
