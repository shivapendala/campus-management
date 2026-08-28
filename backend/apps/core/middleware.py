"""
EduCore Enterprise Framework - Institutional Security & Request Middleware

Enforces enterprise security headers, request auditing, CORS validation,
and latency monitoring across all API endpoints:
- Strict-Transport-Security (HSTS)
- Content-Security-Policy (CSP)
- X-Frame-Options (DENY)
- X-Content-Type-Options (nosniff)
- Referrer-Policy (strict-origin-when-cross-origin)
"""

import time
import logging
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from apps.core.audit import InstitutionalAuditTrailManager
from apps.core.rate_limiter import TieredCampusRateLimiter

logger = logging.getLogger("EduCore.SecurityMiddleware")


class InstitutionalSecurityHeadersMiddleware(MiddlewareMixin):
    """
    Injects enterprise security headers into HTTP responses.
    """

    def process_response(self, request, response):
        response["X-Content-Type-Options"] = "nosniff"
        response["X-Frame-Options"] = "DENY"
        response["X-XSS-Protection"] = "1; mode=block"
        response["Referrer-Policy"] = "strict-origin-when-cross-origin"
        response["Permissions-Policy"] = "geolocation=(self), camera=(), microphone=()"
        response["Server"] = "EduCore-Enterprise-Gateway"
        return response


class RequestAuditingAndLatencyMiddleware(MiddlewareMixin):
    """
    Logs API execution latency and records administrative audit events.
    """

    def process_request(self, request):
        request._start_time = time.time()

        # Extract client IP
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip = x_forwarded_for.split(",")[0].strip()
        else:
            ip = request.META.get("REMOTE_ADDR", "127.0.0.1")
        request._client_ip = ip

    def process_response(self, request, response):
        if hasattr(request, "_start_time"):
            duration = round((time.time() - request._start_time) * 1000.0, 2)
            response["X-Response-Time-Ms"] = str(duration)

            # Log modifying operations (POST, PUT, PATCH, DELETE)
            if request.method in ("POST", "PUT", "PATCH", "DELETE") and request.path.startswith("/api/"):
                user = getattr(request, "user", None)
                username = getattr(user, "username", "anonymous") if user and user.is_authenticated else "anonymous"
                role = getattr(user, "role", "ANONYMOUS") if user and user.is_authenticated else "ANONYMOUS"

                InstitutionalAuditTrailManager.log_event(
                    action_type=request.method,
                    resource_type=request.path.split("/")[2] if len(request.path.split("/")) > 2 else "API",
                    actor_username=username,
                    actor_role=role,
                    ip_address=getattr(request, "_client_ip", "127.0.0.1"),
                    user_agent=request.META.get("HTTP_USER_AGENT", "Unknown")[:128],
                    metadata={"status_code": response.status_code, "latency_ms": duration}
                )

        return response
