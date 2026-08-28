"""
EduCore Enterprise Framework - Departmental Budget Allocation & Fiscal Ledger

Manages annual departmental budgets across recurring (OPEX) and non-recurring (CAPEX) heads:
Lab equipment procurement, student consumable kits, faculty development grants, and conferences.
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
from dataclasses import dataclass, field


@dataclass
class BudgetHeadAllocation:
    """Represents a specific line item in the departmental budget."""
    head_code: str  # LAB_EQUIPMENT, CONSUMABLES, FDP_TRAVEL, STUDENT_ACTIVITIES, LIBRARY
    head_name: str
    is_capex: bool
    allocated_amount: float
    utilized_amount: float
    committed_amount: float  # Purchase orders issued but not yet invoiced


class DepartmentBudgetManager:
    """
    Computes budget variances, burn rates, and evaluates procurement approvals.
    """

    @classmethod
    def evaluate_procurement_requisition(
        cls,
        requested_amount: float,
        head_allocation: BudgetHeadAllocation
    ) -> Tuple[bool, str, Dict[str, Any]]:
        """
        Check if requested expenditure is within remaining uncommitted budget allocation.
        """
        available_funds = head_allocation.allocated_amount - (head_allocation.utilized_amount + head_allocation.committed_amount)

        if requested_amount <= available_funds:
            new_committed = head_allocation.committed_amount + requested_amount
            burn_rate_pct = ((head_allocation.utilized_amount + new_committed) / head_allocation.allocated_amount * 100.0)
            return True, "Requisition approved within sanctioned allocation.", {
                "head_code": head_allocation.head_code,
                "sanctioned_amount": head_allocation.allocated_amount,
                "previous_available": available_funds,
                "requested_amount": requested_amount,
                "remaining_after_commitment": round(available_funds - requested_amount, 2),
                "forecasted_burn_rate_pct": round(burn_rate_pct, 2)
            }
        else:
            deficit = requested_amount - available_funds
            return False, f"Insufficient funds: Exceeds remaining allocation by Rs. {deficit:,.2f}.", {
                "head_code": head_allocation.head_code,
                "available_funds": available_funds,
                "requested_amount": requested_amount,
                "budget_deficit": deficit
            }

    @classmethod
    def department_fiscal_summary(
        cls,
        department_code: str,
        fiscal_year: str,
        allocations: List[BudgetHeadAllocation]
    ) -> Dict[str, Any]:
        """Aggregate total department budget allocation, utilization, and variance."""
        total_allocated = sum(a.allocated_amount for a in allocations)
        total_utilized = sum(a.utilized_amount for a in allocations)
        total_committed = sum(a.committed_amount for a in allocations)
        total_spent_and_committed = total_utilized + total_committed
        unspent_balance = total_allocated - total_spent_and_committed

        overall_burn_rate = (total_spent_and_committed / total_allocated * 100.0) if total_allocated > 0 else 0.0

        capex_allocated = sum(a.allocated_amount for a in allocations if a.is_capex)
        capex_spent = sum(a.utilized_amount for a in allocations if a.is_capex)

        opex_allocated = sum(a.allocated_amount for a in allocations if not a.is_capex)
        opex_spent = sum(a.utilized_amount for a in allocations if not a.is_capex)

        return {
            "department_code": department_code,
            "fiscal_year": fiscal_year,
            "total_allocated": total_allocated,
            "total_utilized": total_utilized,
            "total_committed": total_committed,
            "unspent_balance": round(unspent_balance, 2),
            "burn_rate_pct": round(overall_burn_rate, 2),
            "capex_summary": {
                "allocated": capex_allocated,
                "utilized": capex_spent,
                "utilization_pct": round((capex_spent / capex_allocated * 100.0), 2) if capex_allocated > 0 else 0.0
            },
            "opex_summary": {
                "allocated": opex_allocated,
                "utilized": opex_spent,
                "utilization_pct": round((opex_spent / opex_allocated * 100.0), 2) if opex_allocated > 0 else 0.0
            },
            "heads_breakdown": [
                {
                    "code": a.head_code,
                    "name": a.head_name,
                    "allocated": a.allocated_amount,
                    "utilized": a.utilized_amount,
                    "committed": a.committed_amount,
                    "available": round(a.allocated_amount - (a.utilized_amount + a.committed_amount), 2),
                    "burn_rate_pct": round(((a.utilized_amount + a.committed_amount) / a.allocated_amount * 100.0), 2) if a.allocated_amount > 0 else 0.0
                }
                for a in allocations
            ]
        }
