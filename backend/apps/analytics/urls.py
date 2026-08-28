"""
EduCore Enterprise Framework - Institutional Analytics URL Routing
"""

from django.urls import path
from apps.analytics.views import (
    ExecutiveKPIAnalyticsAPIView,
    StudentAcademicRiskAPIView,
    NAACAccreditationAPIView,
    CampusUtilizationAPIView
)

urlpatterns = [
    path("kpi-overview/", ExecutiveKPIAnalyticsAPIView.as_view(), name="analytics-kpis"),
    path("student-risk/", StudentAcademicRiskAPIView.as_view(), name="analytics-student-risk"),
    path("accreditation-naac/", NAACAccreditationAPIView.as_view(), name="analytics-naac"),
    path("utilization/", CampusUtilizationAPIView.as_view(), name="analytics-utilization"),
]
