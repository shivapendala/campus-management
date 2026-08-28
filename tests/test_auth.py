import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model
from apps.accounts.models import PasswordResetToken

User = get_user_model()


@pytest.mark.django_db
class TestAuthenticationAPI:
    def test_api_root(self, api_client):
        url = reverse('campus-api-root')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['status'] == 'healthy'
        assert len(response.data['modules']) >= 15

    def test_user_registration(self, api_client):
        url = reverse('accounts_register')
        payload = {
            'username': 'newuser_student',
            'email': 'newuser@campus.edu',
            'password': 'strongpassword123',
            'password_confirm': 'strongpassword123',
            'first_name': 'New',
            'last_name': 'Student',
            'role': 'STUDENT',
            'phone': '+1 555-0199',
            'department_name': 'Computer Science',
        }
        response = api_client.post(url, payload, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(username='newuser_student').exists()

    def test_jwt_login_success(self, api_client, student_user):
        url = reverse('accounts_token')
        payload = {
            'username': student_user.username,
            'password': 'password123',
        }
        response = api_client.post(url, payload, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data
        assert 'user' in response.data
        assert response.data['user']['role'] == student_user.role

    def test_jwt_login_invalid_credentials(self, api_client):
        url = reverse('accounts_token')
        payload = {
            'username': 'nonexistent',
            'password': 'wrongpassword',
        }
        response = api_client.post(url, payload, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_role_verification_endpoint(self, auth_client, admin_user):
        url = reverse('accounts_verify_role')
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['authenticated'] is True
        assert response.data['role'] == admin_user.role
        assert response.data['is_admin'] is True

    def test_forgot_password_and_reset(self, api_client, student_user):
        # 1. Request password reset
        forgot_url = reverse('accounts_forgot_password')
        forgot_res = api_client.post(forgot_url, {'email': student_user.email}, format='json')
        assert forgot_res.status_code == status.HTTP_200_OK
        assert 'reset_token' in forgot_res.data
        token = forgot_res.data['reset_token']

        # 2. Reset password using token
        reset_url = reverse('accounts_reset_password')
        reset_res = api_client.post(reset_url, {
            'token': token,
            'new_password': 'BrandNewPassword123!',
            'confirm_password': 'BrandNewPassword123!',
        }, format='json')
        assert reset_res.status_code == status.HTTP_200_OK

        # 3. Verify login works with new password
        login_url = reverse('accounts_token')
        login_res = api_client.post(login_url, {
            'username': student_user.username,
            'password': 'BrandNewPassword123!',
        }, format='json')
        assert login_res.status_code == status.HTTP_200_OK
