"""
EduCore Enterprise Framework - Institutional Internal Seed Research Grants

Manages competitive early-career faculty research grants (Rs. 2,00,000 to Rs. 5,00,000):
- Peer-review evaluation panel scores
- Milestone tranche disbursements
- Outcome deliverables: minimum 1 SCI journal publication + 1 external DST/SERB grant submission
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class SeedGrantProject:
    """Represents an internal institutional seed research grant."""
    grant_id: str
    faculty_lead_id: int
    project_title: str
    sanctioned_amount_inr: float
    disbursed_amount_inr: float
    start_date: str
    completion_deadline: str
    review_score_out_of_100: float
    sci_publication_status: str = "PUBLISHED"  # PENDING, SUBMITTED, PUBLISHED
    external_grant_submitted: bool = True
    status: str = "COMPLETED_SUCCESSFULLY"


class SeedGrantManager:
    """
    Evaluates seed grant return on investment (ROI) and milestone compliance.
    """

    @classmethod
    def audit_grant_outcomes(cls, grant: SeedGrantProject) -> Dict[str, Any]:
        """Check if all mandatory contractual deliverables are fulfilled."""
        is_sci_met = grant.sci_publication_status == "PUBLISHED"
        is_external_met = grant.external_grant_submitted
        all_met = is_sci_met and is_external_met

        return {
            "grant_id": grant.grant_id,
            "title": grant.project_title,
            "sanctioned_inr": grant.sanctioned_amount_inr,
            "deliverables": {
                "sci_publication_published": is_sci_met,
                "external_national_grant_submitted": is_external_met,
            },
            "is_contract_fully_settled": all_met,
            "audit_verdict": "OUTSTANDING_RESEARCH_DELIVERY" if all_met else "DELIVERABLE_PENDING"
        }
