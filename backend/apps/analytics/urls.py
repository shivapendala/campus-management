from django.urls import path
from .views import (
    DashboardOverviewView,
    DepartmentDistributionView,
    EnrollmentTrendsView,
    GradeDistributionView
)

urlpatterns = [
    path('overview/', DashboardOverviewView.as_view(), name='analytics_overview'),
    path('department-distribution/', DepartmentDistributionView.as_view(), name='analytics_dept_distribution'),
    path('enrollment-trends/', EnrollmentTrendsView.as_view(), name='analytics_enrollment_trends'),
    path('grade-distribution/', GradeDistributionView.as_view(), name='analytics_grade_distribution'),
]
