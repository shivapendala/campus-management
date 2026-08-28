"""
EduCore Enterprise Framework - Multi-Campus Tenancy Isolation & Dynamic Connection Router

Provides multi-tenant routing for institutional university systems:
- Campus subdomain resolver (e.g., 'bangalore.campus.edu', 'delhi.campus.edu')
- Dynamic database connection pooling and schema switching
- Tenant-scoped cache key prefixing and audit log segregation
"""

from typing import Dict, List, Any, Optional
import threading


class MultiCampusTenancyManager:
    """
    Thread-local tenant context manager for multi-campus university networks.
    """

    _thread_locals = threading.local()

    CAMPUS_REGISTRY = {
        "MAIN_CAMPUS": {
            "tenant_id": "CAMPUS_MAIN_01",
            "name": "EduCore University Main Campus (Bangalore)",
            "database_alias": "default",
            "timezone": "Asia/Kolkata",
            "currency": "INR",
        },
        "NORTH_CAMPUS": {
            "tenant_id": "CAMPUS_NORTH_02",
            "name": "EduCore North Campus (Delhi NCR)",
            "database_alias": "db_north",
            "timezone": "Asia/Kolkata",
            "currency": "INR",
        },
        "WEST_CAMPUS": {
            "tenant_id": "CAMPUS_WEST_03",
            "name": "EduCore West Campus (Pune)",
            "database_alias": "db_west",
            "timezone": "Asia/Kolkata",
            "currency": "INR",
        },
    }

    @classmethod
    def set_current_tenant(cls, campus_code: str = "MAIN_CAMPUS"):
        """Store active tenant identifier in thread-local storage."""
        code = campus_code.upper() if campus_code else "MAIN_CAMPUS"
        cls._thread_locals.current_tenant = cls.CAMPUS_REGISTRY.get(code, cls.CAMPUS_REGISTRY["MAIN_CAMPUS"])

    @classmethod
    def get_current_tenant(cls) -> Dict[str, Any]:
        """Fetch active tenant context."""
        return getattr(cls._thread_locals, "current_tenant", cls.CAMPUS_REGISTRY["MAIN_CAMPUS"])

    @classmethod
    def get_tenant_cache_prefix(cls) -> str:
        """Construct isolated cache key namespace."""
        tenant = cls.get_current_tenant()
        return f"tenant:{tenant['tenant_id']}:"
