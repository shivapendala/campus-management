import pytest
from django.urls import reverse
from rest_framework import status
from apps.accounts.models import User
from apps.departments.models import Department
from apps.students.models import Student


@pytest.mark.django_db
class TestStudentsCompleteFlow:
    def test_student_lifecycle(self, auth_client, admin_user, sample_department):
        student = Student.objects.create(
            user=admin_user,
            student_id='STU-TEST-001',
            name='Test Student Flow',
            email='test_student_flow@campus.edu',
            department=sample_department,
            year=2,
            section='A',
        )
        assert student.id is not None
        assert student.student_id == 'STU-TEST-001'

        url = reverse('student-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK

        detail_url = reverse('student-detail', kwargs={'pk': student.pk})
        detail_res = auth_client.get(detail_url)
        assert detail_res.status_code == status.HTTP_200_OK
        assert detail_res.data['name'] == 'Test Student Flow'
