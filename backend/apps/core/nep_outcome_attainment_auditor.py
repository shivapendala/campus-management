"""
EduCore Framework - NEP Outcome Attainment Auditor

Audits program outcome deviation records.
"""

from typing import Dict, List, Any

class NEPOutcomeAttainmentAuditor:
    def __init__(self):
        self.critical_deficits: List[str] = []

    def audit_deviations(self, deviations: Dict[str, float], threshold: float = -10.0) -> List[str]:
        for po, dev in deviations.items():
            if dev < threshold:
                self.critical_deficits.append(
                    f"Critical Attainment Deficit: Program Outcome '{po}' has deviation score of {dev}% (Threshold: {threshold}%)."
                )
        return self.critical_deficits
