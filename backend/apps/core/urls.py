"""
EduCore Enterprise Framework - Core Security URL Routing
"""

from django.urls import path
from apps.core.views import (
    SystemHealthAPIView,
    SecurityAuditTrailAPIView,
    RolePermissionsMatrixAPIView,
    PasswordValidationAPIView
)

urlpatterns = [
    path("health/", SystemHealthAPIView.as_view(), name="system-health"),
    path("audit-logs/", SecurityAuditTrailAPIView.as_view(), name="audit-logs"),
    path("permissions/", RolePermissionsMatrixAPIView.as_view(), name="role-permissions"),
    path("validate-password/", PasswordValidationAPIView.as_view(), name="validate-password"),
]
