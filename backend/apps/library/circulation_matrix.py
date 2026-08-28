"""
EduCore Enterprise Framework - Library Circulation Policy & Borrowing Matrix

Defines role-based borrowing quotas and loan durations:
- Undergraduate Students: 3 Books (14 Days loan period, 2 Renewals max)
- Postgraduate Students: 5 Books (21 Days loan period, 2 Renewals max)
- PhD Research Scholars: 8 Books (30 Days loan period, 3 Renewals max)
- Faculty Members: 10 Books (90 Days / Full Semester loan period, 4 Renewals max)
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass


@dataclass
class CirculationPolicyRule:
    """Represents borrowing rules for a patron category."""
    patron_role: str
    max_concurrent_books: int
    loan_duration_days: int
    max_renewals_allowed: int
    can_borrow_reference_books: bool = False


class LibraryCirculationMatrix:
    """
    Evaluates circulation entitlement rules.
    """

    POLICIES = {
        "STUDENT": CirculationPolicyRule("STUDENT", max_concurrent_books=3, loan_duration_days=14, max_renewals_allowed=2),
        "PG_STUDENT": CirculationPolicyRule("PG_STUDENT", max_concurrent_books=5, loan_duration_days=21, max_renewals_allowed=2),
        "RESEARCH_SCHOLAR": CirculationPolicyRule("RESEARCH_SCHOLAR", max_concurrent_books=8, loan_duration_days=30, max_renewals_allowed=3),
        "FACULTY": CirculationPolicyRule("FACULTY", max_concurrent_books=10, loan_duration_days=90, max_renewals_allowed=4, can_borrow_reference_books=True),
        "HOD": CirculationPolicyRule("HOD", max_concurrent_books=10, loan_duration_days=90, max_renewals_allowed=4, can_borrow_reference_books=True),
        "ADMIN": CirculationPolicyRule("ADMIN", max_concurrent_books=15, loan_duration_days=180, max_renewals_allowed=5, can_borrow_reference_books=True),
    }

    @classmethod
    def evaluate_checkout_eligibility(
        cls,
        patron_role: str,
        current_borrowed_count: int,
        outstanding_fine_dues: float,
        is_reference_book: bool = False
    ) -> Tuple[bool, str]:
        """
        Check if patron can check out an additional book.
        Returns: (is_eligible, reason)
        """
        policy = cls.POLICIES.get(patron_role.upper(), cls.POLICIES["STUDENT"])

        if outstanding_fine_dues > 50.0:
            return False, f"Checkout blocked: Outstanding library fine of Rs. {outstanding_fine_dues:.2f} (Clear dues first)."

        if current_borrowed_count >= policy.max_concurrent_books:
            return False, f"Borrowing quota reached: Maximum {policy.max_concurrent_books} books allowed concurrently for {patron_role}."

        if is_reference_book and not policy.can_borrow_reference_books:
            return False, "Reference section books are restricted to in-library reading only for students."

        return True, "Eligible for checkout."
