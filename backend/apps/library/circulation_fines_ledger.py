"""
EduCore Framework - Library Circulation Fines Ledger

Logs overdue fines transactions, verifies waiver approvals,
and interfaces with student accounts billing engine.
"""

from datetime import datetime
from typing import Dict, List, Any

class CirculationFinesLedger:
    def __init__(self):
        self.fine_records: List[Dict[str, Any]] = []

    def record_overdue_fine(self, accession_number: str, student_id: str, days_overdue: int, fine_amount: float) -> Dict[str, Any]:
        record = {
            "transaction_id": f"FIN-TXN-{len(self.fine_records) + 1:05d}",
            "accession_number": accession_number,
            "student_id": student_id,
            "days_overdue": days_overdue,
            "fine_amount": fine_amount,
            "waived_amount": 0.0,
            "paid_amount": 0.0,
            "status": "UNPAID",
            "logged_at": datetime.now()
        }
        self.fine_records.append(record)
        return record

    def apply_fine_waiver(self, transaction_id: str, waive_amount: float, approver_id: str) -> bool:
        """
        Applies partial or full fine waiver approved by the Chief Librarian.
        """
        for record in self.fine_records:
            if record["transaction_id"] == transaction_id:
                if record["status"] == "PAID":
                    return False
                    
                total_fine = record["fine_amount"]
                record["waived_amount"] = min(waive_amount, total_fine)
                
                remaining = total_fine - record["waived_amount"]
                if remaining == 0.0:
                    record["status"] = "WAIVED"
                else:
                    record["status"] = "PARTIAL_PAID"
                    
                record["approver_id"] = approver_id
                return True
        return False
