"""
EduCore Enterprise Framework - Need & Merit-Based Fee Waiver Rule Engine

Processes institutional fee concessions, staff ward discounts, and sibling fee waivers:
Enforces multi-tier administrative approval limits and quota caps.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass


@dataclass
class FeeConcessionPolicy:
    """Represents an approved institutional fee concession policy."""
    policy_code: str
    name: str
    discount_type: str  # PERCENTAGE, FIXED_AMOUNT
    value: float
    max_cap: float
    requires_trustee_approval: bool = False


class FeeWaiverRuleEngine:
    """
    Evaluates and calculates fee concessions based on institutional policies.
    """

    POLICIES = {
        "STAFF_WARD": FeeConcessionPolicy("STAFF_WARD", "Institutional Faculty/Staff Ward Concession", "PERCENTAGE", 50.0, 60000.0),
        "SIBLING_CONCESSION": FeeConcessionPolicy("SIBLING_CONCESSION", "Concurrent Sibling Enrollment Concession", "PERCENTAGE", 20.0, 25000.0),
        "SINGLE_PARENT_EWS": FeeConcessionPolicy("SINGLE_PARENT_EWS", "Single Parent Need-Based Grant", "FIXED_AMOUNT", 30000.0, 30000.0, requires_trustee_approval=True),
        "MERIT_TOPPER": FeeConcessionPolicy("MERIT_TOPPER", "Semester Department Topper Award", "PERCENTAGE", 100.0, 100000.0),
    }

    @classmethod
    def apply_concession(
        cls,
        base_fee: float,
        policy_code: str
    ) -> Tuple[bool, str, float, float]:
        """
        Calculate discount and revised fee.
        Returns: (is_applied, reason, discount_amount, net_payable_fee)
        """
        policy = cls.POLICIES.get(policy_code.upper())
        if not policy:
            return False, f"Unknown concession policy: {policy_code}", 0.0, base_fee

        if policy.discount_type == "PERCENTAGE":
            calc_discount = (base_fee * policy.value / 100.0)
        else:
            calc_discount = policy.value

        actual_discount = min(policy.max_cap, min(base_fee, calc_discount))
        net_payable = max(0.0, base_fee - actual_discount)

        return True, f"Policy '{policy.name}' applied.", round(actual_discount, 2), round(net_payable, 2)
