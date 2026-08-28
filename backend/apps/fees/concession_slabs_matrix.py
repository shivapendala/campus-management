"""
EduCore Framework - Fee Concession Slabs & Category Matrix

Defines structural configurations of state scholarships and institutional waivers.
"""

from typing import Dict, Any

class ConcessionSlabsMatrix:
    def __init__(self, regulation_year: str):
        self.regulation_year = regulation_year
        self.slabs: Dict[str, Dict[str, Any]] = {
            "GOVT_SPONSORED_SC_ST": {"waiver_pct": 100.0, "needs_income_cert": False, "minimum_cgpa": 0.0},
            "MERIT_CUM_MEANS_GEN": {"waiver_pct": 50.0, "needs_income_cert": True, "minimum_cgpa": 7.5},
            "MINORITY_COMMUNITY_SCH": {"waiver_pct": 25.0, "needs_income_cert": True, "minimum_cgpa": 6.5},
            "INSTITUTION_SPORTS_QUOTA": {"waiver_pct": 75.0, "needs_income_cert": False, "minimum_cgpa": 5.0}
        }

    def verify_candidate_eligibility(self, slab_key: str, student_cgpa: float, has_income_cert: bool) -> bool:
        slab = self.slabs.get(slab_key)
        if not slab:
            return False
            
        if slab["needs_income_cert"] and not has_income_cert:
            return False
            
        return student_cgpa >= slab["minimum_cgpa"]
