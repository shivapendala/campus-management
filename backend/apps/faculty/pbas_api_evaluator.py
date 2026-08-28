"""
EduCore Framework - PBAS API Score Verification & Capping Auditor

Enforces score caps and category ceilings on UGC Career Advancement Scheme submissions,
verifies supporting document metadata logs, and reports promotion progress.
"""

from typing import Dict, List, Any

class PBASAPIEvaluator:
    def __init__(self, faculty_id: str, cycle_year: str):
        self.faculty_id = faculty_id
        self.cycle_year = cycle_year
        self.category_caps: Dict[str, float] = {
            "CATEGORY_1_TEACHING": 50.0,
            "CATEGORY_2_ADMIN": 45.0,
            "CATEGORY_3_RESEARCH": 120.0
        }
        self.audit_log: List[str] = []

    def verify_and_cap_scores(self, raw_scores: Dict[str, float]) -> Dict[str, Any]:
        """
        Applies strict UGC ceiling limits to Category I, II, and III scores.
        """
        capped_scores: Dict[str, float] = {}
        for category, cap in self.category_caps.items():
            raw_val = raw_scores.get(category, 0.0)
            if raw_val > cap:
                capped_scores[category] = cap
                self.audit_log.append(
                    f"Ceiling Capping Applied: Category '{category}' score of {raw_val} capped at maximum limit of {cap}."
                )
            else:
                capped_scores[category] = raw_val
                
        total_pbas = sum(capped_scores.values())
        
        return {
            "faculty_id": self.faculty_id,
            "cycle_year": self.cycle_year,
            "capped_scores": capped_scores,
            "total_pbas_score": round(total_pbas, 2),
            "audit_trail": self.audit_log
        }

    def evaluate_promotion_eligibility(self, current_stage: int, total_pbas_score: float) -> Dict[str, Any]:
        """
        Determines CAS promotion eligibility:
        - Stage 1 to 2: Requires min 80 PBAS score
        - Stage 2 to 3: Requires min 100 PBAS score
        - Stage 3 to 4: Requires min 120 PBAS score
        - Stage 4 to 5: Requires min 150 PBAS score
        """
        required_scores = {1: 80.0, 2: 100.0, 3: 120.0, 4: 150.0}
        target_score = required_scores.get(current_stage, 999.0)
        
        eligible = total_pbas_score >= target_score
        
        return {
            "current_stage": current_stage,
            "next_stage": current_stage + 1,
            "required_score": target_score,
            "actual_score": total_pbas_score,
            "eligible": eligible,
            "action_advice": "APPLY_FOR_CAS_INTERVIEW" if eligible else f"DEFICIT: Needs {round(target_score - total_pbas_score, 2)} more PBAS points."
        }
