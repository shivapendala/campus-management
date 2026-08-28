"""
EduCore Enterprise Framework - Government & Institutional Scholarship Matrix

Reconciles statutory fee concessions:
- National Scholarship Portal (NSP Post-Matric SC/ST/OBC Scheme)
- Pragati Scholarship for Female Technical Students (AICTE)
- Merit-Cum-Means Institutional Tuition Waiver (50% / 100%)
- Sports Excellence Tuition Concession
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class ScholarshipSchemeRule:
    """Represents a financial aid scholarship policy."""
    scheme_code: str
    scheme_name: str
    funding_source: str  # GOVT_CENTRAL, GOVT_STATE, INSTITUTIONAL_ENDOWMENT
    concession_percentage: float
    max_waiver_cap_inr: float
    min_cgpa_requirement: float
    max_family_income_lpa: float


class ScholarshipMatrixManager:
    """
    Evaluates applicant eligibility against scholarship guidelines.
    """

    SCHEMES = {
        "MERIT_GOLD": ScholarshipSchemeRule("MERIT_GOLD", "Chancellor Gold Merit Award", "INSTITUTIONAL_ENDOWMENT", 50.0, 60000.0, 8.5, 99.0),
        "PRAGATI_AICTE": ScholarshipSchemeRule("PRAGATI_AICTE", "AICTE Pragati Scheme for Girls", "GOVT_CENTRAL", 100.0, 50000.0, 7.0, 8.0),
        "POST_MATRIC_SCST": ScholarshipSchemeRule("POST_MATRIC_SCST", "Post-Matric Welfare Scholarship", "GOVT_STATE", 100.0, 85000.0, 5.0, 2.5),
        "SPORTS_CHAMPION": ScholarshipSchemeRule("SPORTS_CHAMPION", "Varsity Sports Excellence Concession", "INSTITUTIONAL_ENDOWMENT", 75.0, 75000.0, 6.0, 99.0),
    }

    @classmethod
    def evaluate_scholarship(
        cls,
        scheme_code: str,
        student_cgpa: float,
        family_income_lpa: float,
        tuition_fee_inr: float
    ) -> Tuple[bool, float, str]:
        """
        Check qualification and compute approved waiver amount.
        Returns: (is_eligible, waiver_amount_inr, explanation)
        """
        scheme = cls.SCHEMES.get(scheme_code)
        if not scheme:
            return False, 0.0, "Invalid or unrecognized scholarship scheme code."

        if student_cgpa < scheme.min_cgpa_requirement:
            return False, 0.0, f"Ineligible: CGPA ({student_cgpa}) is below scheme threshold ({scheme.min_cgpa_requirement})."

        if family_income_lpa > scheme.max_family_income_lpa:
            return False, 0.0, f"Ineligible: Family annual income ({family_income_lpa} LPA) exceeds ceiling ({scheme.max_family_income_lpa} LPA)."

        waiver_amount = min(scheme.max_waiver_cap_inr, (tuition_fee_inr * scheme.concession_percentage / 100.0))
        return True, round(waiver_amount, 2), f"Approved for Rs. {waiver_amount:,.2f} concession under {scheme.scheme_name}."
