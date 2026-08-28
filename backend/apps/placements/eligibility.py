"""
EduCore Enterprise Framework - Corporate Placement Eligibility Rule Engine

Filters student candidate pools against stringent corporate recruitment criteria:
- Minimum 10th / 12th / Diploma / B.Tech CGPA percentages
- Permissible active/historical backlogs (0 vs <= 1)
- Allowed academic departments (CSE, ECE, EEE, MECH, CIVIL)
- One-Student-One-Job Dream / Super Dream policy exclusions
"""

from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, field


@dataclass
class PlacementDriveCriteria:
    """Represents corporate recruitment eligibility requirements."""
    company_name: str
    drive_id: str
    job_role: str
    ctc_lpa: float  # In Lakhs Per Annum (e.g., 12.5 LPA)
    tier_category: str  # REGULAR (< 6 LPA), DREAM (6-12 LPA), SUPER_DREAM (> 12 LPA)
    min_btech_cgpa: float = 6.5
    min_tenth_pct: float = 60.0
    min_twelfth_pct: float = 60.0
    max_active_backlogs: int = 0
    max_history_backlogs: int = 2
    eligible_departments: Set[str] = field(default_factory=lambda: {"CSE", "ECE", "EEE", "MECH", "CIVIL"})
    gender_preference: Optional[str] = None  # None or FEMALE (diversity hiring drives)


class PlacementEligibilityEngine:
    """
    Evaluates candidate qualification for company recruitment drives.
    """

    @classmethod
    def evaluate_candidate(
        cls,
        candidate_profile: Dict[str, Any],
        drive_criteria: PlacementDriveCriteria,
        current_active_offers_max_ctc: float = 0.0
    ) -> Tuple[bool, List[str], List[str]]:
        """
        Evaluate student against criteria and institutional Dream Job policy.
        Returns: (is_eligible, reasons_qualified, reasons_disqualified)
        """
        qualified = []
        disqualified = []

        cgpa = float(candidate_profile.get("cgpa", 0.0))
        tenth = float(candidate_profile.get("tenth_pct", 0.0))
        twelfth = float(candidate_profile.get("twelfth_pct", 0.0))
        active_backlogs = int(candidate_profile.get("active_backlogs", 0))
        history_backlogs = int(candidate_profile.get("history_backlogs", 0))
        dept = str(candidate_profile.get("department", "")).upper()
        gender = str(candidate_profile.get("gender", "")).upper()

        # 1. Department match
        if dept not in drive_criteria.eligible_departments:
            disqualified.append(f"Department {dept} is not eligible for this drive (Eligible: {drive_criteria.eligible_departments}).")
        else:
            qualified.append(f"Department {dept} meets criteria.")

        # 2. CGPA
        if cgpa < drive_criteria.min_btech_cgpa:
            disqualified.append(f"CGPA {cgpa:.2f} is below minimum required {drive_criteria.min_btech_cgpa:.2f}.")
        else:
            qualified.append(f"CGPA {cgpa:.2f} satisfies criteria.")

        # 3. 10th / 12th marks
        if tenth < drive_criteria.min_tenth_pct:
            disqualified.append(f"10th marks ({tenth:.1f}%) below {drive_criteria.min_tenth_pct:.1f}% required.")
        if twelfth < drive_criteria.min_twelfth_pct:
            disqualified.append(f"12th marks ({twelfth:.1f}%) below {drive_criteria.min_twelfth_pct:.1f}% required.")

        # 4. Backlogs
        if active_backlogs > drive_criteria.max_active_backlogs:
            disqualified.append(f"{active_backlogs} active backlog(s) exceeds limit of {drive_criteria.max_active_backlogs}.")
        if history_backlogs > drive_criteria.max_history_backlogs:
            disqualified.append(f"{history_backlogs} historical backlog(s) exceeds limit of {drive_criteria.max_history_backlogs}.")

        # 5. Dream Policy Rule:
        # If student already has an offer, they can only sit for a company offering >= 1.5x higher CTC (Dream)
        if current_active_offers_max_ctc > 0:
            min_ctc_required = current_active_offers_max_ctc * 1.5
            if drive_criteria.ctc_lpa < min_ctc_required:
                disqualified.append(f"Dream policy restriction: Existing offer is {current_active_offers_max_ctc:.1f} LPA; require at least {min_ctc_required:.1f} LPA to apply.")
            else:
                qualified.append(f"Qualifies under Dream Job upgrade policy ({drive_criteria.ctc_lpa:.1f} >= {min_ctc_required:.1f} LPA).")

        # 6. Diversity Hiring Check
        if drive_criteria.gender_preference and gender != drive_criteria.gender_preference.upper():
            disqualified.append(f"Drive restricted to {drive_criteria.gender_preference} candidates.")

        is_eligible = len(disqualified) == 0
        return is_eligible, qualified, disqualified
