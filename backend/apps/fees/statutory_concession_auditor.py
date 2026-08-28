"""
EduCore Framework - Statutory Fee Concession Auditor

Verifies fee concessions against verification rosters and logs anomalies.
"""

from typing import Dict, List, Any

class StatutoryConcessionAuditor:
    def __init__(self, academic_year: str):
        self.academic_year = academic_year
        self.discrepancies: List[Dict[str, Any]] = []

    def audit_concessions(self, concessions_ledger: List[Dict[str, Any]], verified_income_limits: Dict[str, float]) -> List[Dict[str, Any]]:
        """
        Validates student income declarations against system registers.
        """
        for record in concessions_ledger:
            student_id = record["student_id"]
            declared_income = record["declared_income"]
            actual_income = verified_income_limits.get(student_id)
            
            if actual_income is None:
                self.discrepancies.append({
                    "student_id": student_id,
                    "type": "MISSING_VERIFICATION_RECORD",
                    "description": "No income certificate verified in system database."
                })
            elif declared_income != actual_income:
                self.discrepancies.append({
                    "student_id": student_id,
                    "type": "INCOME_MISMATCH",
                    "description": f"Declared income {declared_income} matches verified certificate {actual_income} incorrectly."
                })
                
        return self.discrepancies
