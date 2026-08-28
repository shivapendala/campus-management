from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from apps.campus.models import Department, Course

User = get_user_model()


class CampusTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser(
            username='campus_admin',
            email='admin@campus.edu',
            password='adminpassword123'
        )
        self.client.force_authenticate(user=self.admin)
        self.dept = Department.objects.create(
            name='Computer Science',
            code='CS',
            established_year=1995
        )

    def test_create_and_list_departments(self):
        response = self.client.get('/api/campus/departments/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_course(self):
        response = self.client.post('/api/campus/courses/', {
            'code': 'CS-101',
            'title': 'Data Structures',
            'department': self.dept.id,
            'credits': 4,
            'capacity': 50
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 1)
