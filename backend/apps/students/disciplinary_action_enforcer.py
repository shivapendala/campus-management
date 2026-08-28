"""
EduCore Framework - Disciplinary Action Enforcer

Verifies compliance checks for active suspensions, outstanding penalty fines,
and blocks exam hall ticket issuance for flagged student profiles.
"""

from datetime import datetime
from typing import Dict, List, Any

class DisciplinaryActionEnforcer:
    def __init__(self):
        self.outstanding_fines: Dict[str, float] = {}  # student_id -> fine_amount
        self.active_suspensions: Dict[str, datetime] = {}  # student_id -> suspension_end_date

    def impose_fine(self, student_id: str, amount: float) -> None:
        self.outstanding_fines[student_id] = self.outstanding_fines.get(student_id, 0.0) + amount

    def clear_fine(self, student_id: str, amount_paid: float) -> float:
        current = self.outstanding_fines.get(student_id, 0.0)
        new_balance = max(0.0, current - amount_paid)
        self.outstanding_fines[student_id] = new_balance
        return new_balance

    def suspend_student(self, student_id: str, end_date: datetime) -> None:
        self.active_suspensions[student_id] = end_date

    def verify_exam_hall_ticket_clearance(self, student_id: str) -> Dict[str, Any]:
        """
        Locks hall ticket if student has outstanding fines or is under active suspension.
        """
        has_fine = self.outstanding_fines.get(student_id, 0.0) > 0.0
        
        suspension_end = self.active_suspensions.get(student_id)
        is_suspended = suspension_end is not None and datetime.now() < suspension_end
        
        cleared = not has_fine and not is_suspended
        
        reason = "CLEARED"
        if not cleared:
            reasons = []
            if has_fine:
                reasons.append(f"Outstanding fine: Rs. {self.outstanding_fines[student_id]}")
            if is_suspended:
                reasons.append(f"Under active suspension until {suspension_end.strftime('%Y-%m-%d')}")
            reason = "LOCKED: " + " & ".join(reasons)
            
        return {
            "student_id": student_id,
            "hall_ticket_status": "ISSUED" if cleared else "LOCKED",
            "reason": reason,
            "can_attend_exams": cleared
        }
