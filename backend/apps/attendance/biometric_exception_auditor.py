"""
EduCore Framework - Biometric Attendance Exception Auditor

Audits attendance exception requests and flags unapproved absences.
"""

from typing import Dict, List, Any

class BiometricExceptionAuditor:
    def __init__(self, academic_term: str):
        self.academic_term = academic_term
        self.exceptions_anomalies: List[Dict[str, Any]] = []

    def audit_exceptions(self, exceptions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        for exc in exceptions:
            e_id = exc["exception_id"]
            status = exc["status"]
            if status == "PENDING_VERIFICATION":
                self.exceptions_anomalies.append({
                    "exception_id": e_id,
                    "type": "PENDING_APPROVAL",
                    "description": "Leave exception request is pending proctor approval."
                })
        return self.exceptions_anomalies
