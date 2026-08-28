"""
EduCore Enterprise Framework - Campus Event Sponsorship & Expenditure Ledger

Tracks event revenues (Sponsorships, Registration Fees, University Grants)
against line-item expenditures (Guest Speaker Honorarium, Stage & Sound, Catering, Merchandise).
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class EventBudgetItem:
    """Represents an income or expense line item for an event."""
    item_code: str
    description: str
    is_income: bool  # True for sponsorship/tickets, False for expense
    budgeted_amount: float
    actual_amount: float


class EventBudgetLedger:
    """
    Computes financial surplus / deficit and ROI for campus festivals and technical symposiums.
    """

    @classmethod
    def compute_event_financials(
        cls,
        event_code: str,
        event_name: str,
        budget_items: List[EventBudgetItem]
    ) -> Dict[str, Any]:
        """Aggregate event income and expenditure."""
        total_income_budgeted = sum(i.budgeted_amount for i in budget_items if i.is_income)
        total_income_actual = sum(i.actual_amount for i in budget_items if i.is_income)

        total_expense_budgeted = sum(i.budgeted_amount for i in budget_items if not i.is_income)
        total_expense_actual = sum(i.actual_amount for i in budget_items if not i.is_income)

        net_profit_or_loss = total_income_actual - total_expense_actual
        variance_expense = total_expense_actual - total_expense_budgeted

        return {
            "event_code": event_code,
            "event_name": event_name,
            "total_revenue_collected": round(total_income_actual, 2),
            "total_expenses_incurred": round(total_expense_actual, 2),
            "net_balance": round(net_profit_or_loss, 2),
            "is_financially_viable": net_profit_or_loss >= 0.0,
            "budget_adherence_pct": round((1.0 - abs(variance_expense) / total_expense_budgeted) * 100.0, 2) if total_expense_budgeted > 0 else 100.0,
            "financial_status": "SURPLUS" if net_profit_or_loss > 0 else ("BREAK_EVEN" if net_profit_or_loss == 0 else "DEFICIT")
        }
