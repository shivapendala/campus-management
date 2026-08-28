"""
EduCore Framework - Library Circulation Rules Ledger

Maintains circulation guidelines configurations and histories.
"""

from typing import Dict, List, Any

class CirculationRulesLedger:
    def __init__(self):
        self.rules_registry: List[Dict[str, Any]] = []

    def register_rule(self, membership_type: str, max_books: int, loan_days: int) -> None:
        self.rules_registry.append({
            "membership_type": membership_type,
            "max_books": max_books,
            "loan_days": loan_days
        })
