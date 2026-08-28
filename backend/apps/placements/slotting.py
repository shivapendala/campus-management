"""
EduCore Enterprise Framework - Placement Season Day-0/Day-1 Slotting Engine

Prioritizes company recruitment calendar slots based on CTC package tiers,
alumni conversion history, and global Fortune 500 employer prestige scores.
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
from dataclasses import dataclass, field


@dataclass
class CompanyDriveSlot:
    """Represents a scheduled corporate drive slot."""
    company_name: str
    ctc_lpa: float
    offered_roles_count: int
    tier: str  # SUPER_DREAM (Day 0), DREAM (Day 1), CORE (Day 2), MASS (Day 3)
    priority_score: float
    scheduled_date: str
    interview_rooms_allocated: int = 4


class PlacementDriveSlottingEngine:
    """
    Computes company slot priorities for campus placement season.
    """

    @classmethod
    def calculate_priority_score(
        cls,
        ctc_lpa: float,
        past_hires_count: int,
        is_fortune_500: bool = False,
        is_tier_1_product: bool = False
    ) -> Tuple[float, str]:
        """
        Compute score out of 100 and determine Day slotting tier.
        """
        ctc_score = min(50.0, (ctc_lpa / 40.0) * 50.0)  # Up to 50 pts for 40 LPA
        history_score = min(20.0, past_hires_count * 2.0)
        prestige_score = (15.0 if is_tier_1_product else 0.0) + (15.0 if is_fortune_500 else 0.0)

        total_score = round(ctc_score + history_score + prestige_score, 1)

        if ctc_lpa >= 18.0 or total_score >= 80.0:
            tier = "SUPER_DREAM (Day 0)"
        elif ctc_lpa >= 10.0 or total_score >= 60.0:
            tier = "DREAM (Day 1)"
        elif ctc_lpa >= 6.0 or total_score >= 40.0:
            tier = "CORE_REGULAR (Day 2)"
        else:
            tier = "MASS_RECRUITER (Day 3)"

        return total_score, tier
