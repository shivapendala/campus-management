"""
EduCore Enterprise Framework - Institutional Alumni Network & Career Tracking Engine

Manages graduated student network, alumni endowments, mentorship programs,
distinguished alumni awards, and global chapter registries.
"""

from typing import Dict, List, Any, Optional
import datetime
from dataclasses import dataclass, field


@dataclass
class AlumniProfile:
    """Represents a registered institutional alumnus."""
    alumnus_id: int
    roll_number: str
    full_name: str
    graduation_year: int
    department: str
    current_company: str
    current_designation: str
    industry_domain: str  # SOFTWARE, HARDWARE, FINTECH, AUTOMOTIVE, ACADEMIA, ENTREPRENEURSHIP
    work_city: str
    work_country: str
    linkedin_url: Optional[str] = None
    is_mentor_volunteer: bool = False
    total_endowment_contributions: float = 0.0


class AlumniNetworkManager:
    """
    Manages alumni engagement, geographic chapter distributions, and endowment metrics.
    """

    @classmethod
    def compute_alumni_metrics(cls, profiles: List[AlumniProfile]) -> Dict[str, Any]:
        """Aggregate global employment distributions and endowment totals."""
        if not profiles:
            return {"total_alumni": 0, "mentors_count": 0, "total_endowments": 0.0}

        total = len(profiles)
        mentors = sum(1 for a in profiles if a.is_mentor_volunteer)
        total_endowments = sum(a.total_endowment_contributions for a in profiles)

        domain_counts: Dict[str, int] = {}
        for a in profiles:
            domain_counts[a.industry_domain] = domain_counts.get(a.industry_domain, 0) + 1

        country_counts: Dict[str, int] = {}
        for a in profiles:
            country_counts[a.work_country] = country_counts.get(a.work_country, 0) + 1

        return {
            "total_alumni_registered": total,
            "active_student_mentors": mentors,
            "total_endowment_contributions": round(total_endowments, 2),
            "top_industry_domains": domain_counts,
            "global_countries_presence": country_counts,
            "mentor_engagement_rate_pct": round((mentors / total * 100.0), 2) if total > 0 else 0.0
        }
