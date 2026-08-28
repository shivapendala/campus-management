"""
EduCore Framework - Library Circulation Rules Matrix

Defines borrowing limits, loan periods, and overdue fine multipliers.
"""

from typing import Dict, Any

class CirculationRulesMatrix:
    def __init__(self):
        # Maximum allowed books and loan periods by membership type
        self.membership_limits: Dict[str, Dict[str, Any]] = {
            "STUDENT": {"max_books": 4, "loan_days": 14, "fine_per_day": 5.0},
            "FACULTY": {"max_books": 10, "loan_days": 30, "fine_per_day": 0.0},
            "RESEARCH_SCHOLAR": {"max_books": 6, "loan_days": 21, "fine_per_day": 2.0}
        }

    def check_borrowing_eligibility(self, current_borrowed_count: int, membership_type: str) -> bool:
        rules = self.membership_limits.get(membership_type)
        if not rules:
            return False
        return current_borrowed_count < rules["max_books"]

    def calculate_overdue_fine(self, days_overdue: int, membership_type: str) -> float:
        if days_overdue <= 0:
            return 0.0
            
        rules = self.membership_limits.get(membership_type)
        if not rules:
            return 0.0
            
        base_fine = rules["fine_per_day"]
        
        # Apply progressive multipliers for severe delays
        if days_overdue > 30:
            return days_overdue * base_fine * 2.0
        elif days_overdue > 14:
            return days_overdue * base_fine * 1.5
        return days_overdue * base_fine
