"""
EduCore Enterprise Framework - UGC Statutory 5-Tier Admission Cancellation Fee Refund Engine

Implements UGC Notification (October 2018 / 2023 Guidelines) on Fee Refunds:
1. 15 days or more before formally notified last date of admission: 100% Refund (Max Rs. 1,000 deduction)
2. Less than 15 days before last date: 90% Refund
3. 15 days or less after last date: 80% Refund
4. 30 days or less, but more than 15 days after last date: 50% Refund
5. More than 30 days after last date: 0% Refund
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime


class StatutoryFeeRefundEngine:
    """
    Computes UGC statutory fee refunds upon admission withdrawal.
    """

    MAX_ADMINISTRATIVE_DEDUCTION_INR = 1000.0

    @classmethod
    def calculate_statutory_refund(
        cls,
        total_fees_paid_inr: float,
        formal_last_date_of_admission_iso: str,
        withdrawal_application_date_iso: str
    ) -> Dict[str, Any]:
        """
        Calculate refundable amount according to UGC 5-tier policy.
        """
        last_dt = datetime.date.fromisoformat(formal_last_date_of_admission_iso)
        withdraw_dt = datetime.date.fromisoformat(withdrawal_application_date_iso)

        days_diff = (last_dt - withdraw_dt).days  # Positive if before, negative if after

        if days_diff >= 15:
            # Tier 1: 100% minus max Rs. 1,000
            refund_pct = 100.0
            deduction = min(cls.MAX_ADMINISTRATIVE_DEDUCTION_INR, total_fees_paid_inr * 0.05)
            tier_desc = "Tier 1: 15+ days before last date (100% refund less Rs. 1,000 processing fee)"
        elif 0 <= days_diff < 15:
            # Tier 2: 90%
            refund_pct = 90.0
            deduction = total_fees_paid_inr * 0.10
            tier_desc = "Tier 2: < 15 days before last date (90% refund)"
        elif -15 <= days_diff < 0:
            # Tier 3: 80%
            refund_pct = 80.0
            deduction = total_fees_paid_inr * 0.20
            tier_desc = "Tier 3: <= 15 days after last date (80% refund)"
        elif -30 <= days_diff < -15:
            # Tier 4: 50%
            refund_pct = 50.0
            deduction = total_fees_paid_inr * 0.50
            tier_desc = "Tier 4: 16-30 days after last date (50% refund)"
        else:
            # Tier 5: 0%
            refund_pct = 0.0
            deduction = total_fees_paid_inr
            tier_desc = "Tier 5: > 30 days after last date (No refund)"

        refundable_amount = max(0.0, total_fees_paid_inr - deduction)

        return {
            "total_fees_paid": total_fees_paid_inr,
            "days_relative_to_deadline": days_diff,
            "ugc_refund_tier": tier_desc,
            "refund_percentage": refund_pct,
            "retained_deduction_amount": round(deduction, 2),
            "approved_refund_amount": round(refundable_amount, 2),
            "status": "REFUND_SANCTIONED" if refundable_amount > 0 else "NO_REFUND_ENTITLED"
        }
