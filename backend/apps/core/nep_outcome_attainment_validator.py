"""
EduCore Framework - NEP Outcome Attainment Validator

Validates credit alignments and calculates deviations in program outcome attainments.
"""

from typing import Dict, List, Any

class NEPOutcomeAttainmentValidator:
    def __init__(self, target_attainment_pct: float = 60.0):
        self.target_attainment_pct = target_attainment_pct
        self.attainment_deviations: Dict[str, float] = {}

    def audit_attainment_matrix(self, attainment_scores: Dict[str, float]) -> Dict[str, Any]:
        """
        Validates the program outcome (PO) attainment percentages against the institutional target.
        """
        failed_pos: List[str] = []
        for po, score in attainment_scores.items():
            deviation = score - self.target_attainment_pct
            self.attainment_deviations[po] = round(deviation, 2)
            if score < self.target_attainment_pct:
                failed_pos.append(po)
                
        compliant = len(failed_pos) == 0
        
        return {
            "target_threshold_percentage": self.target_attainment_pct,
            "compliant": compliant,
            "failed_outcomes": failed_pos,
            "deviations_log": self.attainment_deviations
        }
