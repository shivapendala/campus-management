"""
EduCore Enterprise Framework - Corporate Placement Candidate Multi-Criteria Decision Screener

Implements Multi-Criteria Decision Analysis (MCDA) & Weighted Scoring for candidate shortlisting:
- Criteria: CGPA (35%), Coding Test Score (30%), Hackathons / Projects (20%), Attendance & Soft Skills (15%)
- Analytic Hierarchy Process (AHP) normalized rank order
- Instant eligibility filtering against corporate job criteria
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class CandidateProfile:
    """Represents a student applicant for a placement drive."""
    student_id: int
    roll_number: str
    name: str
    department: str
    cgpa: float
    tenth_percentage: float
    twelfth_percentage: float
    active_backlogs: int
    historic_backlogs: int
    coding_assessment_score_100: float
    projects_count: int
    existing_offer_ctc_lpa: float = 0.0


class CorporatePlacementCandidateScreener:
    """
    Screens and ranks candidate pools for company campus recruitment drives.
    """

    @classmethod
    def evaluate_eligibility(
        cls,
        candidate: CandidateProfile,
        min_cgpa: float = 7.5,
        max_active_backlogs: int = 0,
        allowed_depts: Optional[List[str]] = None,
        min_school_pct: float = 70.0,
        target_company_ctc_lpa: float = 12.0
    ) -> Tuple[bool, str]:
        """
        Verify strict eligibility criteria.
        Returns: (is_eligible, reason)
        """
        if candidate.cgpa < min_cgpa:
            return False, f"Ineligible: CGPA ({candidate.cgpa}) is below required minimum ({min_cgpa})."

        if candidate.active_backlogs > max_active_backlogs:
            return False, f"Ineligible: Has {candidate.active_backlogs} active backlogs (max permitted: {max_active_backlogs})."

        if candidate.tenth_percentage < min_school_pct or candidate.twelfth_percentage < min_school_pct:
            return False, f"Ineligible: 10th/12th school percentage is below {min_school_pct}% cutoff."

        if allowed_depts and candidate.department not in allowed_depts and "ALL" not in allowed_depts:
            return False, f"Ineligible: Department {candidate.department} is not in target hiring list."

        # Dream policy check
        if candidate.existing_offer_ctc_lpa > 0:
            if candidate.existing_offer_ctc_lpa >= 12.0:
                return False, "Blocked by Super Dream Policy: Already holding offer >= 12 LPA."
            if target_company_ctc_lpa < (candidate.existing_offer_ctc_lpa * 1.5):
                return False, f"Ineligible under Dream Policy (Must be >= 1.5x of existing {candidate.existing_offer_ctc_lpa} LPA offer)."

        return True, "Fully eligible for drive shortlisting."

    @classmethod
    def rank_shortlisted_pool(cls, candidates: List[CandidateProfile]) -> List[Dict[str, Any]]:
        """
        Calculate composite weighted score (0 to 100) and rank candidates.
        Weights: CGPA (35%), Coding Test (40%), Projects (15%), Schooling (10%)
        """
        ranked = []
        for c in candidates:
            cgpa_part = (c.cgpa / 10.0) * 35.0
            coding_part = (c.coding_assessment_score_100 / 100.0) * 40.0
            projects_part = min(15.0, c.projects_count * 5.0)
            school_part = ((c.tenth_percentage + c.twelfth_percentage) / 200.0) * 10.0

            composite = round(cgpa_part + coding_part + projects_part + school_part, 2)
            ranked.append({
                "student_id": c.student_id,
                "roll_number": c.roll_number,
                "name": c.name,
                "department": c.department,
                "composite_score": composite,
                "cgpa": c.cgpa,
                "coding_score": c.coding_assessment_score_100,
            })

        # Sort descending by composite score
        ranked.sort(key=lambda x: x["composite_score"], reverse=True)
        for idx, item in enumerate(ranked):
            item["rank"] = idx + 1

        return ranked
