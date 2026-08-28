"""
EduCore Framework - Disciplinary Action Auditor

Audits disciplinary action records for active suspension offsets accuracy.
"""

from datetime import datetime
from typing import Dict, List, Any

class DisciplinaryActionAuditor:
    def __init__(self):
        self.anomalous_suspensions: List[Dict[str, Any]] = []

    def audit_active_suspensions(self, active_suspensions: Dict[str, datetime]) -> List[Dict[str, Any]]:
        now = datetime.now()
        for s_id, end_date in active_suspensions.items():
            days_remaining = (end_date - now).days
            if days_remaining > 365:
                self.anomalous_suspensions.append({
                    "student_id": s_id,
                    "suspension_end_date": end_date,
                    "days_remaining": days_remaining,
                    "type": "EXCESSIVE_SUSPENSION_PERIOD"
                })
        return self.anomalous_suspensions
