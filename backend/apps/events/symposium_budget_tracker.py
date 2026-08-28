"""
EduCore Enterprise Framework - Symposium Budget & Revenue Tracker

Manages finances for student events:
- Track allocations (Tuition Fund, Sponsorships, Ticket Sales)
- Verify and record vendor expenses
- Flag budget overruns dynamically
"""

from typing import Dict, List, Any, Tuple


class SymposiumBudgetTracker:
    """
    Enforces budgetary discipline on university technical fests.
    """

    @classmethod
    def process_financial_summary(
        cls,
        allocated_budget: float,
        sponsorship_corpus: float,
        ticket_sales_revenue: float,
        expenses_ledger: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Summarize financial health of the event.
        """
        total_funds = allocated_budget + sponsorship_corpus + ticket_sales_revenue
        total_expenses = sum(float(exp.get("amount", 0)) for exp in expenses_ledger)

        net_balance = total_funds - total_expenses
        budget_overflow = total_expenses > total_funds

        # Alert if vendor is over 25% of total budget
        alerts = []
        for exp in expenses_ledger:
            pct = (float(exp.get("amount", 0)) / total_funds * 100.0) if total_funds > 0 else 0.0
            if pct > 25.0:
                alerts.append(f"High Expense Alert: Vendor '{exp.get('vendor')}' consumes {round(pct, 1)}% of total fund.")

        return {
            "total_funding_corpus": round(total_funds, 2),
            "total_expenses_incurred": round(total_expenses, 2),
            "net_surplus_or_deficit": round(net_balance, 2),
            "is_budget_overrun": budget_overflow,
            "financial_alerts": alerts,
            "status": "DEFICIT_WARNING" if budget_overflow else "FINANCIALLY_SECURE"
        }
