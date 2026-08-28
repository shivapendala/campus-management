"""
EduCore Framework - Statutory Fee Refund Validator

Calculates permissible refund percentages for admission cancellations
according to UGC statutory guidelines.
"""

from datetime import datetime
from typing import Dict, Any

class StatutoryRefundValidator:
    def __init__(self, academic_start_date: datetime):
        self.academic_start_date = academic_start_date
        # Refund slabs as per UGC guidelines:
        # - >= 15 days before start: 100% refund (minus max 5% processing fee cap 5000)
        # - < 15 days before start: 90% refund
        # - <= 15 days after start: 80% refund
        # - > 15 days and <= 30 days after start: 50% refund
        # - > 30 days after start: 0% refund

    def calculate_refund_amount(self, tuition_paid: float, non_refundable_processing_fee: float, cancellation_date: datetime) -> Dict[str, Any]:
        delta_days = (self.academic_start_date - cancellation_date).days
        
        refund_percentage = 0.0
        processing_fee_deducted = 0.0
        
        if delta_days >= 15:
            refund_percentage = 1.00
            # Processing fee capped at Rs. 5000 as per UGC norms
            processing_fee_deducted = min(non_refundable_processing_fee, 5000.0)
        elif 0 <= delta_days < 15:
            refund_percentage = 0.90
            processing_fee_deducted = 0.0
        elif -15 <= delta_days < 0:
            refund_percentage = 0.80
            processing_fee_deducted = 0.0
        elif -30 <= delta_days < -15:
            refund_percentage = 0.50
            processing_fee_deducted = 0.0
        else:
            refund_percentage = 0.00
            processing_fee_deducted = 0.0
            
        gross_refund = tuition_paid * refund_percentage
        net_refund = max(0.0, gross_refund - processing_fee_deducted)
        
        return {
            "tuition_paid": tuition_paid,
            "cancellation_offset_days": delta_days,
            "applicable_refund_percentage": round(refund_percentage * 100.0, 2),
            "processing_fee_deducted": round(processing_fee_deducted, 2),
            "net_refund_amount": round(net_refund, 2)
        }
