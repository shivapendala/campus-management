"""
EduCore Enterprise Framework - Student Merit & Need-Based Scholarship Engine

Calculates student eligibility for institutional scholarships, government fee waivers,
merit rank rewards, and manages disbursement disbursement ledgers.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class ScholarshipScheme:
    """Represents an institutional or government scholarship scheme."""
    scheme_code: str
    name: str
    sponsor: str  # INSTITUTIONAL, GOVERNMENT, ALUMNI_ENDOWMENT, CORPORATE
    min_cgpa: float
    max_family_income: float
    min_attendance_pct: float
    waiver_amount: float
    waiver_percentage: float
    max_recipients: int
    is_active: bool = True


class StudentScholarshipEngine:
    """
    Evaluates scholarship eligibility rules and computes tuition discount amounts.
    """

    AVAILABLE_SCHEMES: List[ScholarshipScheme] = [
        ScholarshipScheme(
            scheme_code="MERIT_CHANCELLOR",
            name="Chancellor's Merit Gold Award",
            sponsor="INSTITUTIONAL",
            min_cgpa=9.2,
            max_family_income=10000000.0,
            min_attendance_pct=85.0,
            waiver_amount=50000.0,
            waiver_percentage=50.0,
            max_recipients=50
        ),
        ScholarshipScheme(
            scheme_code="NEED_COMMUNITY",
            name="EWS Community Financial Grant",
            sponsor="GOVERNMENT",
            min_cgpa=6.5,
            max_family_income=250000.0,
            min_attendance_pct=75.0,
            waiver_amount=35000.0,
            waiver_percentage=40.0,
            max_recipients=150
        ),
        ScholarshipScheme(
            scheme_code="WOMEN_IN_STEM",
            name="Women in Engineering Leadership Endowment",
            sponsor="ALUMNI_ENDOWMENT",
            min_cgpa=8.0,
            max_family_income=800000.0,
            min_attendance_pct=80.0,
            waiver_amount=40000.0,
            waiver_percentage=40.0,
            max_recipients=100
        ),
        ScholarshipScheme(
            scheme_code="SPORTS_EXCELLENCE",
            name="National Sports Champion Fee Concession",
            sponsor="INSTITUTIONAL",
            min_cgpa=6.0,
            max_family_income=10000000.0,
            min_attendance_pct=65.0,
            waiver_amount=60000.0,
            waiver_percentage=60.0,
            max_recipients=20
        ),
    ]

    @classmethod
    def evaluate_eligible_schemes(
        cls,
        student_id: int,
        cgpa: float,
        family_income: float,
        attendance_pct: float,
        tuition_fee: float,
        gender: str = "OTHER",
        is_sports_national: bool = False
    ) -> List[Dict[str, Any]]:
        """Determine all qualifying scholarship schemes for a student."""
        eligible_schemes = []

        for scheme in cls.AVAILABLE_SCHEMES:
            if not scheme.is_active:
                continue

            if scheme.scheme_code == "WOMEN_IN_STEM" and gender.upper() != "FEMALE":
                continue

            if scheme.scheme_code == "SPORTS_EXCELLENCE" and not is_sports_national:
                continue

            if cgpa < scheme.min_cgpa:
                continue

            if family_income > scheme.max_family_income:
                continue

            if attendance_pct < scheme.min_attendance_pct:
                continue

            # Calculate concession amount
            pct_amount = (tuition_fee * scheme.waiver_percentage / 100.0)
            actual_discount = min(scheme.waiver_amount, pct_amount)

            eligible_schemes.append({
                "scheme_code": scheme.scheme_code,
                "name": scheme.name,
                "sponsor": scheme.sponsor,
                "waiver_percentage": scheme.waiver_percentage,
                "approved_waiver_amount": round(actual_discount, 2),
                "net_payable_fee": round(max(0.0, tuition_fee - actual_discount), 2),
                "qualification_reason": f"Satisfies CGPA >={scheme.min_cgpa} and Income <={scheme.max_family_income:,.0f}"
            })

        return eligible_schemes
