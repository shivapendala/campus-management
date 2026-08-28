"""
EduCore Framework - Disciplinary Action Ledger

Logs disciplinary orders and fines collections history.
"""

from datetime import datetime
from typing import Dict, List, Any

class DisciplinaryActionLedger:
    def __init__(self):
        self.action_logs: List[Dict[str, Any]] = []

    def record_disciplinary_action(self, student_id: str, penalty_type: str, details: str) -> None:
        self.action_logs.append({
            "student_id": student_id,
            "penalty_type": penalty_type,
            "details": details,
            "recorded_at": datetime.now()
        })
