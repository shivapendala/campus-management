import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestAnalyticsAPI:
    def test_overview_endpoint(self, auth_client):
        url = reverse('analytics_overview')
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert 'total_students' in response.data
        assert 'total_faculty' in response.data
        assert 'total_courses' in response.data
        assert 'total_departments' in response.data

    def test_department_distribution_chart_data(self, auth_client):
        url = reverse('analytics_dept_distribution')
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert 'labels' in response.data
        assert 'datasets' in response.data

    def test_enrollment_trends_chart_data(self, auth_client):
        url = reverse('analytics_enrollment_trends')
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert 'labels' in response.data
        assert 'datasets' in response.data

    def test_grade_distribution_chart_data(self, auth_client):
        url = reverse('analytics_grade_distribution')
        response = auth_client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert 'labels' in response.data
        assert 'datasets' in response.data
