"""
EduCore Enterprise Framework - Corporate Event Sponsorship Deliverables Tracker

Manages event sponsorship tiers:
- Title Sponsor (Rs. 5,00,000+: Keynote address, prime stage backdrop, 10 delegate passes)
- Platinum Sponsor (Rs. 2,50,000: Exhibit booth, logo on brochure, 5 delegate passes)
- Gold Sponsor (Rs. 1,00,000: Banner display, 2 delegate passes)
- Silver Sponsor (Rs. 50,000: Logo on website, certificate acknowledgement)
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class EventSponsorshipContract:
    """Represents an active corporate sponsorship agreement."""
    contract_id: str
    event_id: str
    sponsor_company: str
    tier: str  # TITLE, PLATINUM, GOLD, SILVER
    pledged_amount: float
    received_amount: float
    booth_allocated: Optional[str] = None
    passes_issued_count: int = 0
    is_fulfilled: bool = False


class EventSponsorshipManager:
    """
    Computes sponsorship deliverables fulfillment status.
    """

    @classmethod
    def get_tier_deliverables(cls, tier: str) -> Dict[str, Any]:
        """Fetch contractual deliverables for sponsorship tier."""
        tier_upper = tier.upper()
        if tier_upper == "TITLE":
            return {"max_passes": 10, "booth_size": "PREMIUM_ISLAND_30SQM", "keynote_slot_minutes": 20, "logo_placement": "PRIME_BANNER"}
        elif tier_upper == "PLATINUM":
            return {"max_passes": 5, "booth_size": "CORNER_BOOTH_18SQM", "keynote_slot_minutes": 10, "logo_placement": "MAIN_BACKDROP"}
        elif tier_upper == "GOLD":
            return {"max_passes": 2, "booth_size": "STANDARD_BOOTH_9SQM", "keynote_slot_minutes": 0, "logo_placement": "WEBSITE_AND_BROCHURE"}
        else:
            return {"max_passes": 1, "booth_size": "NONE", "keynote_slot_minutes": 0, "logo_placement": "WEBSITE_FOOTER"}
