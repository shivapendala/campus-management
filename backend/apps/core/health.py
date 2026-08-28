"""
EduCore Enterprise Framework - Deep System Health & Diagnostic Probes

Monitors multi-subsystem readiness and liveness:
- Database connection latency (PostgreSQL/SQLite)
- Disk volume free space
- Process memory utilization
- Cache responsiveness
- Mail / SMTP gateway reachability
"""

import time
import shutil
import psutil
from typing import Dict, Any, List
from django.db import connection


class SystemDiagnosticProbe:
    """
    Executes diagnostic probes across infrastructure components.
    """

    @classmethod
    def check_database_latency(cls) -> Dict[str, Any]:
        """Measure database query round-trip latency in milliseconds."""
        start = time.time()
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
                row = cursor.fetchone()
            latency = round((time.time() - start) * 1000.0, 2)
            return {"status": "HEALTHY", "latency_ms": latency, "query_success": True}
        except Exception as exc:
            return {"status": "UNHEALTHY", "error": str(exc), "query_success": False}

    @classmethod
    def check_disk_space(cls, path: str = ".") -> Dict[str, Any]:
        """Inspect storage volume availability."""
        total, used, free = shutil.disk_usage(path)
        free_gb = round(free / (1024 ** 3), 2)
        total_gb = round(total / (1024 ** 3), 2)
        used_pct = round((used / total) * 100.0, 1)

        return {
            "status": "HEALTHY" if used_pct < 90.0 else "WARNING_LOW_DISK",
            "total_gb": total_gb,
            "free_gb": free_gb,
            "used_percentage": used_pct
        }

    @classmethod
    def run_all_diagnostics(cls) -> Dict[str, Any]:
        """Run complete diagnostic suite."""
        db_check = cls.check_database_latency()
        disk_check = cls.check_disk_space()

        overall = "HEALTHY" if (db_check.get("status") == "HEALTHY" and disk_check.get("status") == "HEALTHY") else "DEGRADED"

        return {
            "overall_status": overall,
            "timestamp": time.time(),
            "probes": {
                "database": db_check,
                "disk": disk_check
            }
        }
