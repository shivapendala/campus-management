"""
EduCore Framework - Statutory Refund Ledger Reporter

Generates summaries of processed fee refunds.
"""

from typing import Dict, List, Any

class StatutoryRefundLedgerReporter:
    def __init__(self, academic_year: str):
        self.academic_year = academic_year

    def generate_refund_summary(self, refund_records: List[Dict[str, Any]]) -> Dict[str, Any]:
        total_refunded = sum(r["amount"] for r in refund_records)
        return {
            "academic_year": self.academic_year,
            "total_refunds_count": len(refund_records),
            "total_refunded_amount": total_refunded
        }
