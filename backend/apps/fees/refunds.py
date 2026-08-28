"""
EduCore Enterprise Framework - Statutory Fee Refund State Machine (UGC Mandate)

Implements University Grants Commission (UGC) fee refund brackets upon student withdrawal:
- 100% refund: Formal notice received 15 days or more before formally notified last date of admission
- 90% refund: Less than 15 days before last date of admission
- 80% refund: 15 days or less after formally notified last date of admission
- 50% refund: 30 days or less, but more than 15 days after last date of admission
- 0% refund: More than 30 days after last date of admission
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
from apps.core.workflow import GenericWorkflowStateMachine, WorkflowTransition


class UGCFeeRefundEngine:
    """
    Computes statutory refund percentage brackets and orchestrates refund approval workflow.
    """

    STATES = {"REQUESTED", "VERIFIED_BY_ACCOUNTS", "DEAN_APPROVED", "DISBURSED", "REJECTED"}

    @classmethod
    def calculate_ugc_refund_amount(
        cls,
        total_fee_paid: float,
        admission_cutoff_date_iso: str,
        withdrawal_date_iso: Optional[str] = None
    ) -> Tuple[float, float, str]:
        """
        Calculate refund percentage according to statutory UGC guidelines.
        Returns: (refund_percentage, refund_amount, statutory_slab_name)
        """
        cutoff_dt = datetime.date.fromisoformat(admission_cutoff_date_iso)
        withdrawn_dt = datetime.date.fromisoformat(withdrawal_date_iso) if withdrawal_date_iso else datetime.date.today()

        days_diff = (cutoff_dt - withdrawn_dt).days

        if days_diff >= 15:
            pct = 100.0
            slab = "Slab 1: 15+ days prior to last admission date (100% Refund, Max Rs. 1000 processing fee)"
            amount = max(0.0, total_fee_paid - 1000.0)
        elif days_diff >= 0:
            pct = 90.0
            slab = "Slab 2: Less than 15 days prior to last admission date (90% Refund)"
            amount = total_fee_paid * 0.90
        elif days_diff >= -15:
            pct = 80.0
            slab = "Slab 3: 15 days or less after last admission date (80% Refund)"
            amount = total_fee_paid * 0.80
        elif days_diff >= -30:
            pct = 50.0
            slab = "Slab 4: 16 to 30 days after last admission date (50% Refund)"
            amount = total_fee_paid * 0.50
        else:
            pct = 0.0
            slab = "Slab 5: More than 30 days after last admission date (0% Refund)"
            amount = 0.0

        return pct, round(amount, 2), slab

    @classmethod
    def build_workflow(cls) -> GenericWorkflowStateMachine:
        """Create state machine for institutional fee refund lifecycle."""
        transitions = {
            "verify_accounts": WorkflowTransition(
                name="verify_accounts",
                from_states={"REQUESTED"},
                to_state="VERIFIED_BY_ACCOUNTS",
                allowed_roles={"ACCOUNTANT", "ADMIN"},
                description="Bursar confirms fee payment receipt and bank account details"
            ),
            "approve_dean": WorkflowTransition(
                name="approve_dean",
                from_states={"VERIFIED_BY_ACCOUNTS"},
                to_state="DEAN_APPROVED",
                allowed_roles={"ADMIN"},
                description="Dean of Academic Affairs sanctions refund voucher"
            ),
            "disburse_funds": WorkflowTransition(
                name="disburse_funds",
                from_states={"DEAN_APPROVED"},
                to_state="DISBURSED",
                allowed_roles={"ACCOUNTANT", "ADMIN"},
                description="Direct NEFT/RTGS fund transfer initiated to student bank account"
            ),
            "reject_refund": WorkflowTransition(
                name="reject_refund",
                from_states={"REQUESTED", "VERIFIED_BY_ACCOUNTS"},
                to_state="REJECTED",
                allowed_roles={"ADMIN", "ACCOUNTANT"},
                description="Reject refund request due to false documentation"
            ),
        }

        return GenericWorkflowStateMachine(
            name="FeeRefundWorkflow",
            initial_state="REQUESTED",
            valid_states=cls.STATES,
            transitions=transitions
        )
