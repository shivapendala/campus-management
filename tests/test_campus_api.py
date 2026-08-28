import pytest
from django.urls import reverse
from rest_framework import status
from apps.campus.models import Department, Student, FacultyMember, Course


@pytest.mark.django_db
class TestCampusAPI:
    def test_department_crud(self, auth_client):
        # Create department
        url = reverse('department-list')
        payload = {
            'code': 'MATH',
            'name': 'Mathematics & Statistics',
            'established_year': 1998,
            'description': 'Pure and applied mathematics.'
        }
        response = auth_client.post(url, payload, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['code'] == 'MATH'

        # List departments
        list_response = auth_client.get(url)
        assert list_response.status_code == status.HTTP_200_OK
        assert len(list_response.data['results']) >= 1

    def test_student_creation_and_listing(self, auth_client, student_user, sample_department):
        url = reverse('student-list')
        payload = {
            'student_id': 'STU-999',
            'department_id': sample_department.id,
            'semester': 3,
            'gpa': '3.75'
        }
        # Create Student profile for existing user
        student = Student.objects.create(
            user=student_user,
            department=sample_department,
            student_id='STU-999',
            semester=3,
            gpa=3.75
        )
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] >= 1

    def test_course_creation_and_listing(self, auth_client, sample_department):
        url = reverse('course-list')
        payload = {
            'code': 'CS-101',
            'title': 'Introduction to Computer Science',
            'department': sample_department.id,
            'credits': 4,
            'capacity': 50,
            'semester_offered': 'Fall 2026'
        }
        response = auth_client.post(url, payload, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['code'] == 'CS-101'
