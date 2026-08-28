"""
EduCore Enterprise Framework - Grievance Committee Routing & Whistleblower Protection

Routes filed complaints to specialized institutional statutory committees:
- Internal Complaints Committee (ICC for Prevention of Sexual Harassment)
- Anti-Ragging Cell
- SC/ST / Equal Opportunity Cell
- Academic Grievance Cell
- Hostel & Mess Affairs Committee
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class CommitteeRoutingTarget:
    """Represents the assigned statutory resolution committee."""
    committee_code: str
    committee_name: str
    chairperson_email: str
    member_count: int
    is_confidential: bool = False
    requires_anonymous_masking: bool = False


class GrievanceRoutingMatrix:
    """
    Directs complaints based on sensitive categories to correct grievance cells.
    """

    COMMITTEES = {
        "ANTI_RAGGING": CommitteeRoutingTarget(
            committee_code="ARC",
            committee_name="Institutional Anti-Ragging Committee",
            chairperson_email="anti-ragging@educore.campus.edu",
            member_count=7,
            is_confidential=True,
            requires_anonymous_masking=True
        ),
        "GENDER_HARASSMENT": CommitteeRoutingTarget(
            committee_code="ICC",
            committee_name="Internal Complaints Committee (POSH Cell)",
            chairperson_email="icc-posh@educore.campus.edu",
            member_count=5,
            is_confidential=True,
            requires_anonymous_masking=True
        ),
        "EQUAL_OPPORTUNITY": CommitteeRoutingTarget(
            committee_code="EOC",
            committee_name="SC/ST & Equal Opportunity Grievance Cell",
            chairperson_email="equal-opportunity@educore.campus.edu",
            member_count=5,
            is_confidential=True
        ),
        "ACADEMIC": CommitteeRoutingTarget(
            committee_code="AGC",
            committee_name="Academic Grievance Redressal Committee",
            chairperson_email="dean-academics@educore.campus.edu",
            member_count=6
        ),
        "HOSTEL_MESS": CommitteeRoutingTarget(
            committee_code="HMC",
            committee_name="Hostel & Mess Administration Committee",
            chairperson_email="chief-warden@educore.campus.edu",
            member_count=4
        ),
        "INFRASTRUCTURE": CommitteeRoutingTarget(
            committee_code="EMC",
            committee_name="Estate & Infrastructure Maintenance Committee",
            chairperson_email="estate-officer@educore.campus.edu",
            member_count=3
        ),
    }

    @classmethod
    def resolve_routing(cls, category: str, is_whistleblower_requested: bool = False) -> CommitteeRoutingTarget:
        """Resolve destination statutory committee for a grievance."""
        cat_key = category.upper()
        target = cls.COMMITTEES.get(cat_key, cls.COMMITTEES["INFRASTRUCTURE"])

        if is_whistleblower_requested:
            # Enforce anonymity
            return CommitteeRoutingTarget(
                committee_code=target.committee_code,
                committee_name=target.committee_name,
                chairperson_email=target.chairperson_email,
                member_count=target.member_count,
                is_confidential=True,
                requires_anonymous_masking=True
            )

        return target
