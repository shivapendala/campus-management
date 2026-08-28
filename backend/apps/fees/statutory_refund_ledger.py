"""
EduCore Framework - Statutory Refund Ledger

Logs tuition fee refund transactions for board audit trail records.
"""

from datetime import datetime
from typing import Dict, List, Any

class StatutoryRefundLedger:
    def __init__(self, academic_year: str):
        self.academic_year = academic_year
        self.refund_records: List[Dict[str, Any]] = []

    def record_refund(self, student_id: str, refund_amount: float, payment_ref: str) -> Dict[str, Any]:
        record = {
            "refund_id": f"RFD-{len(self.refund_records) + 1:04d}",
            "student_id": student_id,
            "amount": refund_amount,
            "payment_reference": payment_ref,
            "status": "PROCESSED",
            "timestamp": datetime.now()
        }
        self.refund_records.append(record)
        return record
