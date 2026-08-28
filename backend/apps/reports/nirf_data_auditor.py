"""
EduCore Framework - NIRF Data Auditor

Audits compiled NIRF metrics to verify calculations integrity.
"""

from typing import Dict, List, Any

class NIRFDataAuditor:
    def __init__(self, target_year: str):
        self.target_year = target_year
        self.validation_warnings: List[str] = []

    def audit_graduation_metrics(self, graduation_outcomes: Dict[str, Any]) -> List[str]:
        for cat, data in graduation_outcomes.items():
            pct = data["graduation_percentage"]
            if pct < 50.0:
                self.validation_warnings.append(
                    f"Low graduation rate warning: Category '{cat}' graduation rate is below 50% ({pct}%)."
                )
        return self.validation_warnings
