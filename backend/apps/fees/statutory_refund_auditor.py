"""
EduCore Framework - Statutory Fee Refund Auditor

Audits fee refund calculations to identify deviation anomalies.
"""

from typing import Dict, List, Any

class StatutoryRefundAuditor:
    def __init__(self, academic_year: str):
        self.academic_year = academic_year
        self.anomalies: List[Dict[str, Any]] = []

    def audit_refunds(self, refunds_processed: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        for record in refunds_processed:
            s_id = record["student_id"]
            refund_pct = record["applicable_refund_percentage"]
            days_offset = record["cancellation_offset_days"]
            
            # Check compliance rules
            if days_offset >= 15 and refund_pct != 100.0:
                self.anomalies.append({
                    "student_id": s_id,
                    "type": "REFUND_DEFICIT",
                    "description": f"Eligible for 100% refund (offset {days_offset} days), but only allocated {refund_pct}%."
                })
        return self.anomalies
