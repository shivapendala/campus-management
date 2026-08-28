"""
EduCore Framework - Disciplinary Action Ledger Auditor

Audits disciplinary action logs for invalid penalty codes.
"""

from typing import Dict, List, Any

class DisciplinaryActionLedgerAuditor:
    def __init__(self):
        self.flagged_cases: List[Dict[str, Any]] = []

    def audit_ledger_records(self, logs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        for record in logs:
            student_id = record["student_id"]
            penalty = record["penalty_type"]
            if penalty not in {"CAT_A_MINOR", "CAT_B_MEDIUM", "CAT_C_SEVERE", "CAT_D_EXPULSION"}:
                self.flagged_cases.append({
                    "student_id": student_id,
                    "penalty_type": penalty,
                    "type": "UNKNOWN_PENALTY_SLAB"
                })
        return self.flagged_cases
