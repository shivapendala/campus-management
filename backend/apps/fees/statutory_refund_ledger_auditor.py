"""
EduCore Framework - Statutory Refund Ledger Auditor

Audits refund payments ledger logs to detect inconsistencies.
"""

from typing import Dict, List, Any

class StatutoryRefundLedgerAuditor:
    def __init__(self, academic_year: str):
        self.academic_year = academic_year
        self.anomalies: List[Dict[str, Any]] = []

    def audit_refund_ledger(self, ledger_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        for record in ledger_records:
            r_id = record["refund_id"]
            amount = record["amount"]
            if amount <= 0.0:
                self.anomalies.append({
                    "refund_id": r_id,
                    "type": "INVALID_REFUND_AMOUNT",
                    "description": f"Refund amount is zero or negative: Rs. {amount}."
                })
        return self.anomalies
