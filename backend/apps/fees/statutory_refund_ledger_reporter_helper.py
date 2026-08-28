"""
EduCore Framework - Statutory Refund Ledger Reporter Helper

Formats processed fee refunds summaries.
"""

from typing import Dict, List, Any

class StatutoryRefundLedgerReporterHelper:
    def __init__(self, target_year: str):
        self.target_year = target_year

    def format_refund_summary(self, summary: Dict[str, Any]) -> str:
        return f"Year: {self.target_year} - Total Refunded: Rs. {summary.get('total_refunded_amount')}"
