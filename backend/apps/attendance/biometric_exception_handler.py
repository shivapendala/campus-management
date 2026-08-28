"""
EduCore Framework - Biometric Attendance Exception Handler

Logs student leave permissions, medical certificate clearances,
and proctor attendance overrides to reconcile missing card swipes.
"""

from datetime import datetime
from typing import Dict, List, Any

class BiometricExceptionStatus:
    def __init__(self):
        self.exception_registry: List[Dict[str, Any]] = []

    def record_medical_leave(self, student_id: str, start_date: datetime, end_date: datetime, medical_cert_ref: str) -> Dict[str, Any]:
        exception = {
            "exception_id": f"EXC-MED-{len(self.exception_registry) + 1:04d}",
            "student_id": student_id,
            "category": "MEDICAL_LEAVE",
            "start_date": start_date,
            "end_date": end_date,
            "reference_document": medical_cert_ref,
            "status": "PENDING_VERIFICATION"
        }
        self.exception_registry.append(exception)
        return exception

    def approve_exception(self, exception_id: str, verifier_id: str) -> bool:
        for exc in self.exception_registry:
            if exc["exception_id"] == exception_id:
                exc["status"] = "APPROVED"
                exc["verified_by"] = verifier_id
                exc["verification_time"] = datetime.now()
                return True
        return False

    def check_active_exemption(self, student_id: str, check_date: datetime) -> bool:
        """
        Returns true if the student has an approved attendance exemption for the given date.
        """
        for exc in self.exception_registry:
            if exc["student_id"] == student_id and exc["status"] == "APPROVED":
                if exc["start_date"] <= check_date <= exc["end_date"]:
                    return True
        return False
