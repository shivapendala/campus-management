"""
EduCore Enterprise Framework - Industrial Consultancy & Testing Revenue Manager

Tracks industrial consultancy contracts, client billings, and revenue distribution:
- 60% to Principal Investigator / Faculty Team
- 40% to Institutional Infrastructure & Development Fund
"""

from typing import Dict, List, Any, Optional
import datetime
from dataclasses import dataclass, field


@dataclass
class IndustrialConsultancyProject:
    """Represents an industrial testing or software consultancy assignment."""
    project_id: str
    title: str
    client_organization: str
    faculty_lead_id: int
    contract_value: float
    received_value: float
    start_date: str
    status: str  # ACTIVE, COMPLETED, DELIVERED


class IndustrialConsultancyManager:
    """
    Computes revenue share splits according to university consultancy rules.
    """

    FACULTY_SHARE_PCT = 60.0
    INSTITUTION_SHARE_PCT = 40.0

    @classmethod
    def compute_revenue_split(cls, project: IndustrialConsultancyProject) -> Dict[str, Any]:
        """Compute institutional and investigator revenue distributions."""
        fac_share = (project.received_value * cls.FACULTY_SHARE_PCT / 100.0)
        inst_share = (project.received_value * cls.INSTITUTION_SHARE_PCT / 100.0)

        return {
            "project_id": project.project_id,
            "title": project.title,
            "client": project.client_organization,
            "total_received": project.received_value,
            "faculty_investigator_share": round(fac_share, 2),
            "institutional_development_share": round(inst_share, 2),
            "status": project.status
        }
