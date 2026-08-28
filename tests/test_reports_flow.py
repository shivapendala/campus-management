import pytest
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestReportsCompleteFlow:
    def test_executive_and_multi_dimensional_reports(self, auth_client):
        url = reverse('reports-overview')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK

        fin_url = reverse('reports-finances')
        fin_res = auth_client.get(fin_url)
        assert fin_res.status_code == status.HTTP_200_OK
