"""
EduCore Framework - Library Circulation Rules Auditor

Audits book loan periods and alerts overdue accounts.
"""

from typing import Dict, List, Any

class CirculationRulesAuditor:
    def __init__(self, academic_year: str):
        self.academic_year = academic_year
        self.overdue_violations: List[Dict[str, Any]] = []

    def audit_active_loans(self, active_loans: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        for loan in active_loans:
            s_id = loan["student_id"]
            days = loan["days_borrowed"]
            allowed = loan["allowed_days"]
            
            if days > allowed:
                self.overdue_violations.append({
                    "student_id": s_id,
                    "accession_number": loan["accession_number"],
                    "days_overdue": days - allowed,
                    "type": "LOAN_PERIOD_EXCEEDED"
                })
        return self.overdue_violations
