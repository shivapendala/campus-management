"""
EduCore Enterprise Framework - Library Overdue Fine & Lost Book Penalty Calculator

Computes tiered overdue fines excluding institutional holidays and Sundays:
- Standard Fine: Rs. 2/day for first 7 days overdue
- Escalated Fine: Rs. 5/day for days 8 to 21
- Severe Fine: Rs. 10/day for days 22+
- Lost Book Penalty: 2.0x book replacement cost + Rs. 100 processing fee
"""

import datetime
from typing import Dict, List, Any, Optional, Tuple, Set


class LibraryFineCalculator:
    """
    Computes working day library overdue fines and replacement penalties.
    """

    @classmethod
    def calculate_overdue_fine(
        cls,
        due_date_iso: str,
        return_date_iso: Optional[str] = None,
        institutional_holidays: Optional[Set[str]] = None
    ) -> Tuple[float, int, List[Dict[str, Any]]]:
        """
        Calculate overdue fine excluding Sundays and institutional holidays.
        Returns: (total_fine, billable_overdue_days, calculation_breakdown)
        """
        due_dt = datetime.date.fromisoformat(due_date_iso)
        ret_dt = datetime.date.fromisoformat(return_date_iso) if return_date_iso else datetime.date.today()
        holidays = institutional_holidays or set()

        if ret_dt <= due_dt:
            return 0.0, 0, []

        billable_days = 0
        curr_dt = due_dt + datetime.timedelta(days=1)

        while curr_dt <= ret_dt:
            # Exclude Sunday (weekday == 6) and holidays
            if curr_dt.weekday() != 6 and curr_dt.isoformat() not in holidays:
                billable_days += 1
            curr_dt += datetime.timedelta(days=1)

        # Tiered calculation
        total_fine = 0.0
        breakdown = []

        if billable_days <= 0:
            return 0.0, 0, []

        # Tier 1: Days 1-7 (Rs. 2/day)
        t1_days = min(7, billable_days)
        t1_fine = t1_days * 2.0
        total_fine += t1_fine
        breakdown.append({"tier": "Tier 1 (Days 1-7)", "days": t1_days, "rate": 2.0, "subtotal": t1_fine})

        # Tier 2: Days 8-21 (Rs. 5/day)
        if billable_days > 7:
            t2_days = min(14, billable_days - 7)
            t2_fine = t2_days * 5.0
            total_fine += t2_fine
            breakdown.append({"tier": "Tier 2 (Days 8-21)", "days": t2_days, "rate": 5.0, "subtotal": t2_fine})

        # Tier 3: Days 22+ (Rs. 10/day)
        if billable_days > 21:
            t3_days = billable_days - 21
            t3_fine = t3_days * 10.0
            total_fine += t3_fine
            breakdown.append({"tier": "Tier 3 (Days 22+)", "days": t3_days, "rate": 10.0, "subtotal": t3_fine})

        return round(total_fine, 2), billable_days, breakdown

    @classmethod
    def calculate_lost_book_replacement_cost(cls, original_book_price: float) -> Tuple[float, Dict[str, Any]]:
        """Compute lost book replacement bill: 2x MRP + Rs. 100 processing surcharge."""
        multiplier_charge = original_book_price * 2.0
        processing_fee = 100.0
        total = multiplier_charge + processing_fee

        return round(total, 2), {
            "original_book_mrp": original_book_price,
            "penalty_multiplier": "2.0x MRP",
            "replacement_cost": multiplier_charge,
            "administrative_fee": processing_fee,
            "total_payable": total
        }
