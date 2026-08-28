"""
EduCore Framework - NEP Outcome Attainment Ledger Auditor

Audits outcome ledger score entries.
"""

from typing import Dict, List, Any

class NEPOutcomeAttainmentLedgerAuditor:
    def __init__(self):
        self.validation_errors: List[str] = []

    def audit_ledger_entries(self, logs: List[Dict[str, Any]]) -> List[str]:
        for entry in logs:
            po = entry["po_code"]
            score = entry["attainment_score"]
            if not (0.0 <= score <= 100.0):
                self.validation_errors.append(f"Invalid range: Outcome '{po}' score {score}% is out of bounds.")
        return self.validation_errors
