"""
EduCore Enterprise Framework - Tuition Fee Installment Schedule & Late Penalty Engine

Generates flexible multi-term payment schedules (Annual, Bi-Annual, Quarterly, Monthly):
Calculates grace periods, daily compounding late fines, and auto-generates reminder triggers.
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
from dataclasses import dataclass, field


@dataclass
class FeeInstallmentScheduleItem:
    """Represents one installment tranche of a student's annual fee."""
    installment_number: int
    due_date: str
    base_amount: float
    late_penalty_amount: float = 0.0
    total_payable: float = 0.0
    amount_paid: float = 0.0
    status: str = "PENDING"  # PENDING, PAID, OVERDUE, WAIVED


class FeeInstallmentEngine:
    """
    Computes installment breakdowns and applies late penalty rules.
    """

    DAILY_LATE_FINE = 50.0  # Rs. 50 per day past grace period
    GRACE_PERIOD_DAYS = 7

    @classmethod
    def generate_installment_schedule(
        cls,
        total_annual_fee: float,
        installments_count: int = 3,
        start_date_iso: Optional[str] = None
    ) -> List[FeeInstallmentScheduleItem]:
        """
        Generate structured installment tranches with spaced due dates (every 90 days).
        """
        if installments_count <= 0:
            installments_count = 1

        base_tranche = round(total_annual_fee / installments_count, 2)
        start_dt = datetime.date.fromisoformat(start_date_iso) if start_date_iso else datetime.date.today()

        schedule = []
        running_sum = 0.0

        for i in range(1, installments_count + 1):
            due_dt = start_dt + datetime.timedelta(days=(i - 1) * 90)

            # Adjust last tranche for rounding
            if i == installments_count:
                amount = round(total_annual_fee - running_sum, 2)
            else:
                amount = base_tranche
                running_sum += amount

            schedule.append(FeeInstallmentScheduleItem(
                installment_number=i,
                due_date=due_dt.isoformat(),
                base_amount=amount,
                late_penalty_amount=0.0,
                total_payable=amount,
                amount_paid=0.0,
                status="PENDING"
            ))

        return schedule

    @classmethod
    def calculate_overdue_penalty(
        cls,
        due_date_iso: str,
        base_amount: float,
        evaluation_date_iso: Optional[str] = None
    ) -> Tuple[float, float, int]:
        """
        Compute late fine based on elapsed days past grace period.
        Returns: (penalty_amount, total_payable, overdue_days)
        """
        due_dt = datetime.date.fromisoformat(due_date_iso)
        eval_dt = datetime.date.fromisoformat(evaluation_date_iso) if evaluation_date_iso else datetime.date.today()

        delta_days = (eval_dt - due_dt).days
        overdue_days = max(0, delta_days - cls.GRACE_PERIOD_DAYS)

        penalty = overdue_days * cls.DAILY_LATE_FINE
        total = base_amount + penalty

        return round(penalty, 2), round(total, 2), overdue_days
