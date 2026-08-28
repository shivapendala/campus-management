"""
EduCore Framework - NIRF Data Ledger Auditor

Audits compiled statistics records.
"""

from typing import Dict, List, Any

class NIRFDataLedgerAuditor:
    def __init__(self, target_year: str):
        self.target_year = target_year
        self.warnings: List[str] = []

    def audit_ledger_entries(self, entries: List[Dict[str, Any]]) -> List[str]:
        for entry in entries:
            cat = entry["category"]
            pct = entry["graduation_percentage"]
            if pct > 100.0 or pct < 0.0:
                self.warnings.append(f"Invalid range: Category '{cat}' has value of {pct}%.")
        return self.warnings
