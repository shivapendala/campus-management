"""
EduCore Framework - Grace Marks Ledger

Records all allocated grace marks transactions for board audits.
"""

from datetime import datetime
from typing import Dict, List, Any

class GraceMarksLedger:
    def __init__(self, academic_term: str):
        self.academic_term = academic_term
        self.allocated_grace_records: List[Dict[str, Any]] = []

    def record_grace(self, student_id: str, course_code: str, grace_applied: float, approver_id: str) -> Dict[str, Any]:
        record = {
            "record_id": f"GRC-{self.academic_term}-{len(self.allocated_grace_records) + 1:04d}",
            "student_id": student_id,
            "course_code": course_code,
            "grace_applied": grace_applied,
            "approver_id": approver_id,
            "timestamp": datetime.now()
        }
        self.allocated_grace_records.append(record)
        return record
