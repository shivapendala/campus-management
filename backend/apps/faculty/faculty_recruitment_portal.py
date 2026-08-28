"""
EduCore Enterprise Framework - Career Advancement Scheme (CAS) Faculty Recruitment & Promotion Engine

Computes statutory UGC CAS score eligibility for Assistant to Associate, and Associate to Professor:
- Minimum Teaching Years Requirement (4 to 5 years per grade band)
- Minimum Research Publications in Scopus/UGC Care List (min 3 to 10 indexed papers)
- Research Guidance (minimum 1 awarded Ph.D. scholar for Professor band)
- Selection Committee Expert Scoring Matrix (out of 100 marks)
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class FacultyCASApplication:
    """Represents a faculty application for CAS career promotion."""
    application_id: str
    faculty_id: int
    current_designation: str  # ASSISTANT_PROF_STAGE_1, ASSISTANT_PROF_STAGE_2, ASSOCIATE_PROFESSOR
    target_designation: str  # ASSOCIATE_PROFESSOR, PROFESSOR, SENIOR_PROFESSOR
    years_in_current_cadre: float
    scopus_publications_count: int
    phd_scholars_graduated_count: int
    sponsored_projects_value_inr: float
    cumulative_api_score: float
    fdp_days_attended: int


class FacultyCASPromotionEngine:
    """
    Evaluates promotional readiness against statutory UGC 2018 regulations.
    """

    @classmethod
    def evaluate_promotion_eligibility(cls, app: FacultyCASApplication) -> Dict[str, Any]:
        """Verify statutory criteria for promotional interview call."""
        if "PROFESSOR" in app.target_designation:
            req_years = 3.0
            req_pubs = 10
            req_phd = 1
            req_api = 110.0
        else:  # To Associate Professor
            req_years = 4.0
            req_pubs = 5
            req_phd = 0
            req_api = 75.0

        years_ok = app.years_in_current_cadre >= req_years
        pubs_ok = app.scopus_publications_count >= req_pubs
        phd_ok = app.phd_scholars_graduated_count >= req_phd
        api_ok = app.cumulative_api_score >= req_api

        is_eligible = years_ok and pubs_ok and phd_ok and api_ok

        return {
            "application_id": app.application_id,
            "target_cadre": app.target_designation,
            "is_shortlisted_for_interview": is_eligible,
            "verifications": {
                "service_tenure": {"met": years_ok, "actual": app.years_in_current_cadre, "required": req_years},
                "scopus_publications": {"met": pubs_ok, "actual": app.scopus_publications_count, "required": req_pubs},
                "phd_guidance": {"met": phd_ok, "actual": app.phd_scholars_graduated_count, "required": req_phd},
                "api_score": {"met": api_ok, "actual": app.cumulative_api_score, "required": req_api}
            }
        }
