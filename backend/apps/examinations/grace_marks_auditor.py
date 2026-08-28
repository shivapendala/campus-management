"""
EduCore Framework - Grace Marks Auditor

Audits grace marks allocations to prevent violations of standard thresholds.
"""

from typing import Dict, List, Any

class GraceMarksAuditor:
    def __init__(self, academic_term: str):
        self.academic_term = academic_term
        self.violations: List[Dict[str, Any]] = []

    def audit_grace_allocations(self, grace_records: List[Dict[str, Any]], max_allowed_grace: float = 5.0) -> List[Dict[str, Any]]:
        for record in grace_records:
            student_id = record["student_id"]
            course = record["course_code"]
            grace = record["grace_applied"]
            
            if grace > max_allowed_grace:
                self.violations.append({
                    "student_id": student_id,
                    "course_code": course,
                    "grace_applied": grace,
                    "type": "GRACE_MARKS_EXCEEDED",
                    "description": f"Grace marks allocated ({grace}) exceeds maximum standard ceiling of {max_allowed_grace}."
                })
        return self.violations
