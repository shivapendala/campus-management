"""
EduCore Framework - Grace Marks Ledger Reconciler

Reconciles allocated grace marks with grade ledger averages.
"""

from typing import Dict, List, Any

class GraceMarksLedgerReconciler:
    def __init__(self, academic_term: str):
        self.academic_term = academic_term
        self.anomalies: List[Dict[str, Any]] = []

    def reconcile_ledgers(self, grace_records: List[Dict[str, Any]], marks_ledger: Dict[str, float]) -> List[Dict[str, Any]]:
        for record in grace_records:
            s_id = record["student_id"]
            course = record["course_code"]
            grace = record["grace_applied"]
            
            raw_score = marks_ledger.get(f"{s_id}_{course}", 0.0)
            if raw_score >= 40.0:
                self.anomalies.append({
                    "student_id": s_id,
                    "course_code": course,
                    "type": "SUPERFLUOUS_GRACE_ALLOCATION",
                    "description": f"Student secured passing score ({raw_score}) but was allocated {grace} grace marks."
                })
        return self.anomalies
