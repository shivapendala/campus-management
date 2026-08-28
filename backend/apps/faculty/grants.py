"""
EduCore Enterprise Framework - Sponsored Research Grants & Consultancy Tracker

Tracks research project funding from DST, SERB, AICTE, ISRO, DRDO, and Corporate R&D:
Grant sanctioning, milestone deliverables, utilization certificates (UC), and overhead splits.
"""

from typing import Dict, List, Any, Optional
import datetime
from dataclasses import dataclass, field


@dataclass
class ResearchGrantProject:
    """Represents a sponsored research or industrial consultancy grant."""
    project_code: str
    title: str
    principal_investigator_id: int
    co_investigators_ids: List[int]
    funding_agency: str  # DST, SERB, AICTE, DRDO, ISRO, CORPORATE
    total_sanctioned_amount: float
    total_received_amount: float
    total_expenditure_amount: float
    start_date: str
    end_date: str
    status: str  # SANCTIONED, ONGOING, COMPLETED, EXTENDED, TERMINATED
    milestones: List[Dict[str, Any]] = field(default_factory=list)


class ResearchGrantManager:
    """
    Computes financial fund utilization rate and institutional overhead shares.
    """

    DEFAULT_INSTITUTIONAL_OVERHEAD_PCT = 15.0  # 15% overhead to university

    @classmethod
    def compute_grant_financials(cls, grant: ResearchGrantProject) -> Dict[str, Any]:
        """Compute expenditure variance and remaining funds for research project."""
        unspent_balance = grant.total_received_amount - grant.total_expenditure_amount
        utilization_rate = (
            (grant.total_expenditure_amount / grant.total_received_amount * 100.0)
            if grant.total_received_amount > 0 else 0.0
        )
        institutional_overhead = (grant.total_sanctioned_amount * cls.DEFAULT_INSTITUTIONAL_OVERHEAD_PCT / 100.0)

        completed_milestones = sum(1 for m in grant.milestones if m.get("is_completed", False))
        total_milestones = len(grant.milestones)
        progress_pct = (completed_milestones / total_milestones * 100.0) if total_milestones > 0 else 0.0

        return {
            "project_code": grant.project_code,
            "title": grant.title,
            "funding_agency": grant.funding_agency,
            "total_sanctioned": grant.total_sanctioned_amount,
            "total_received": grant.total_received_amount,
            "total_spent": grant.total_expenditure_amount,
            "unspent_balance": round(unspent_balance, 2),
            "utilization_rate_pct": round(utilization_rate, 2),
            "institutional_overhead_share": round(institutional_overhead, 2),
            "milestone_progress_pct": round(progress_pct, 2),
            "status": grant.status
        }
