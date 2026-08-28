import pytest
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from apps.accounts.models import UserRole
from apps.departments.models import Department
from apps.students.models import Student
from apps.faculty.models import Faculty
from apps.courses.models import Course, Enrollment

User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def admin_user(db):
    user = User.objects.create_superuser(
        username='admin_test',
        email='admin@test.edu',
        password='password123',
        role=UserRole.ADMIN
    )
    return user


@pytest.fixture
def student_user(db):
    user = User.objects.create_user(
        username='student_test',
        email='student@test.edu',
        password='password123',
        role=UserRole.STUDENT,
        first_name='Test',
        last_name='Student'
    )
    return user


@pytest.fixture
def auth_client(api_client, admin_user):
    api_client.force_authenticate(user=admin_user)
    return api_client


@pytest.fixture
def sample_department(db):
    return Department.objects.create(
        code='CS',
        name='Computer Science',
        established_year=2000,
        description='Computer Science Dept'
    )
