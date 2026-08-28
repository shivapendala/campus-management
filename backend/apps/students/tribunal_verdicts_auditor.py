"""
EduCore Framework - Disciplinary Tribunal Verdicts Auditor

Audits tribunal decision registries to identify pending appeal windows.
"""

from datetime import datetime
from typing import Dict, List, Any

class TribunalVerdictsAuditor:
    def __init__(self):
        self.active_appeals_queue: List[Dict[str, Any]] = []

    def audit_hearings_registry(self, hearings: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        now = datetime.now()
        for case in hearings:
            if case["status"] == "DECIDED":
                deadline = case["appeal_deadline"]
                if deadline and now < deadline:
                    self.active_appeals_queue.append({
                        "case_id": case["case_id"],
                        "student_id": case["student_id"],
                        "appeal_window_open_until": deadline,
                        "action_status": "MONITOR_APPEAL_WINDOW"
                    })
        return self.active_appeals_queue
