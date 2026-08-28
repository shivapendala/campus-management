"""
EduCore Framework - Library Circulation Rules Ledger Verifier

Reconciles active borrowing counts with system rules limits.
"""

from typing import Dict, List, Any

class CirculationRulesLedgerVerifier:
    def __init__(self):
        self.limit_violations: List[Dict[str, Any]] = []

    def verify_borrowings(self, student_borrowed_counts: Dict[str, int], rules: Dict[str, Dict[str, Any]]) -> List[Dict[str, Any]]:
        for student_id, count in student_borrowed_counts.items():
            membership = "STUDENT"  # Default membership type lookup
            m_rules = rules.get(membership, {"max_books": 4})
            max_limit = m_rules["max_books"]
            
            if count > max_limit:
                self.limit_violations.append({
                    "student_id": student_id,
                    "borrowed_count": count,
                    "max_limit": max_limit,
                    "type": "BORROW_LIMIT_EXCEEDED"
                })
        return self.limit_violations
