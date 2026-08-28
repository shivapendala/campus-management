"""
EduCore Enterprise Framework - Core Security & System API Views

Provides REST API endpoints for:
- RBAC permission checks
- User audit trail querying
- System health and cache statistics
- Rate limit metrics
"""

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status

from apps.core.security import InstitutionalPermissionMatrix, PasswordSecurityPolicy
from apps.core.audit import InstitutionalAuditTrailManager
from apps.core.caching import InstitutionalCacheManager
from apps.core.rate_limiter import TieredCampusRateLimiter


class SystemHealthAPIView(APIView):
    """Health check endpoint for Docker and monitoring systems."""
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({
            "status": "HEALTHY",
            "service": "EduCore Campus Management Platform",
            "version": "1.0.0",
            "cache_stats": InstitutionalCacheManager.get_stats()
        }, status=status.HTTP_200_OK)


class SecurityAuditTrailAPIView(APIView):
    """Query institutional audit logs with filtering."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if getattr(request.user, "role", "").upper() != "ADMIN":
            return Response({"error": "Admin authorization required for audit logs."}, status=status.HTTP_403_FORBIDDEN)

        resource_type = request.query_params.get("resource_type")
        actor = request.query_params.get("actor")
        action = request.query_params.get("action")
        limit = int(request.query_params.get("limit", 100))

        records = InstitutionalAuditTrailManager.query_logs(
            resource_type=resource_type,
            actor_username=actor,
            action_type=action,
            limit=limit
        )

        serialized = [
            {
                "event_id": r.event_id,
                "timestamp": r.timestamp,
                "actor_username": r.actor_username,
                "actor_role": r.actor_role,
                "action_type": r.action_type,
                "resource_type": r.resource_type,
                "resource_id": r.resource_id,
                "ip_address": r.ip_address,
                "changes": r.changes,
                "severity": r.severity
            }
            for r in records
        ]

        return Response({"count": len(serialized), "records": serialized})


class RolePermissionsMatrixAPIView(APIView):
    """Retrieve granted permissions for a given role or the active user."""
    permission_classes = [IsAuthenticated]

    def get(self, request):
        target_role = request.query_params.get("role", getattr(request.user, "role", "STUDENT"))
        perms = InstitutionalPermissionMatrix.get_role_permissions(target_role)

        return Response({
            "role": target_role.upper(),
            "total_permissions": len(perms),
            "permissions": [
                {
                    "code": p.code,
                    "name": p.name,
                    "category": p.category,
                    "description": p.description,
                    "risk_level": p.risk_level,
                    "requires_mfa": p.requires_mfa
                }
                for p in perms
            ]
        })


class PasswordValidationAPIView(APIView):
    """Validate password strength according to institutional policies."""
    permission_classes = [AllowAny]

    def post(self, request):
        pwd = request.data.get("password", "")
        is_valid, errors, score = PasswordSecurityPolicy.evaluate_strength(pwd)
        return Response({
            "is_valid": is_valid,
            "errors": errors,
            "strength_score": score,
            "rating": "STRONG" if score >= 80 else ("MODERATE" if score >= 50 else "WEAK")
        })
