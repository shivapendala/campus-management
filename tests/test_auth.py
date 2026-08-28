import pytest
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model

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
            'username': 'newuser',
            'email': 'newuser@campus.edu',
            'password': 'strongpassword123',
            'password_confirm': 'strongpassword123',
            'first_name': 'New',
            'last_name': 'User',
            'role': 'STUDENT',
        }
        response = api_client.post(url, payload, format='json')
        assert response.status_code == status.HTTP_201_CREATED
        assert User.objects.filter(username='newuser').exists()

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
        assert response.data['user']['username'] == student_user.username

    def test_jwt_login_invalid_credentials(self, api_client):
        url = reverse('accounts_token')
        payload = {
            'username': 'nonexistent',
            'password': 'wrongpassword',
        }
        response = api_client.post(url, payload, format='json')
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_user_profile_authenticated(self, auth_client, admin_user):
        url = reverse('accounts_profile')
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['username'] == admin_user.username

    def test_user_profile_unauthenticated(self, api_client):
        url = reverse('accounts_profile')
        response = api_client.get(url)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
