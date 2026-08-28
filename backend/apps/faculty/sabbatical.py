"""
EduCore Enterprise Framework - Faculty Sabbatical Leave & Postdoctoral Fellowship Engine

Manages academic sabbaticals, Fulbright fellowships, and international research leaves:
Enforces statutory return-of-service bond contracts (minimum 2 years post-sabbatical service).
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class SabbaticalLeaveRecord:
    """Represents an approved academic research sabbatical leave."""
    leave_id: str
    faculty_id: int
    host_institution: str  # MIT, Stanford, NUS, Oxford, IISc Bangalore
    host_country: str
    start_date: str
    end_date: str
    duration_months: int
    research_objective: str
    bond_amount_inr: float = 1000000.0  # Rs. 10 Lakhs indemnity bond
    bond_service_obligation_years: int = 2
    is_board_approved: bool = True


class SabbaticalLeaveManager:
    """
    Evaluates faculty sabbatical eligibility (requires minimum 6 years continuous service).
    """

    @classmethod
    def evaluate_sabbatical_eligibility(cls, continuous_years_service: float) -> Dict[str, Any]:
        """Verify service tenure for sabbatical."""
        is_eligible = continuous_years_service >= 6.0
        return {
            "continuous_years_service": continuous_years_service,
            "statutory_service_requirement_years": 6.0,
            "is_eligible": is_eligible,
            "max_sabbatical_duration_months": 12 if is_eligible else 0
        }
