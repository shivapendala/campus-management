from django.urls import path
from .views import (
    OverviewSummaryReportView,
    DepartmentMetricsReportView,
    FinancialSummaryReportView,
    PlacementStatsReportView,
    RecentActivitiesReportView,
)

urlpatterns = [
    path('overview/', OverviewSummaryReportView.as_view(), name='reports-overview'),
    path('departments/', DepartmentMetricsReportView.as_view(), name='reports-departments'),
    path('finances/', FinancialSummaryReportView.as_view(), name='reports-finances'),
    path('placements/', PlacementStatsReportView.as_view(), name='reports-placements'),
    path('activities/', RecentActivitiesReportView.as_view(), name='reports-activities'),
]
