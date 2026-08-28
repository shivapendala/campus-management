"""
EduCore Framework - Grace Marks Ledger Reporter

Generates summaries of grace marks records.
"""

from typing import Dict, List, Any

class GraceMarksLedgerReporter:
    def __init__(self, academic_term: str):
        self.academic_term = academic_term

    def generate_grace_summary(self, grace_records: List[Dict[str, Any]]) -> Dict[str, Any]:
        total_grace_applied = sum(r["grace_applied"] for r in grace_records)
        return {
            "academic_term": self.academic_term,
            "total_beneficiaries": len(grace_records),
            "total_grace_marks_allocated": total_grace_applied
        }
