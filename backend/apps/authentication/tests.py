from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status

User = get_user_model()


class AuthenticationTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='django_testuser',
            email='test@campus.edu',
            password='testpassword123',
            role='STUDENT'
        )

    def test_obtain_jwt_token(self):
        response = self.client.post('/api/auth/token/', {
            'username': 'django_testuser',
            'password': 'testpassword123'
        }, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)
        self.assertEqual(response.data['user']['username'], 'django_testuser')

    def test_protected_profile_access(self):
        # Without token
        response = self.client.get('/api/auth/profile/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

        # With token
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/auth/profile/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['username'], 'django_testuser')
