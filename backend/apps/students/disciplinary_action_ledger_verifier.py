"""
EduCore Framework - Disciplinary Action Ledger Verifier

Reconciles active actions list with student suspension logs.
"""

from datetime import datetime
from typing import Dict, List, Any

class DisciplinaryActionLedgerVerifier:
    def __init__(self):
        self.discrepancies: List[Dict[str, Any]] = []

    def verify_actions(self, action_logs: List[Dict[str, Any]], active_suspensions: Dict[str, datetime]) -> List[Dict[str, Any]]:
        for record in action_logs:
            s_id = record["student_id"]
            penalty = record["penalty_type"]
            
            if penalty in {"CAT_B_MEDIUM", "CAT_C_SEVERE", "CAT_D_EXPULSION"}:
                susp_end = active_suspensions.get(s_id)
                if not susp_end or datetime.now() > susp_end:
                    self.discrepancies.append({
                        "student_id": s_id,
                        "penalty_type": penalty,
                        "status": "MISSING_ACTIVE_SUSPENSION_RECORD"
                    })
        return self.discrepancies
