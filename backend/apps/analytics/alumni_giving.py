"""
EduCore Enterprise Framework - Alumni Giving & Endowment Fund Analytics

Tracks alumni philanthropy, endowment corpus returns, and designated gifts:
- Chair Professorships
- Merit Scholarship Endowments
- Advanced Research Laboratory Naming Rights
"""

from typing import Dict, List, Any, Optional
import datetime
from dataclasses import dataclass, field


@dataclass
class EndowmentGift:
    """Represents an alumni financial contribution to institutional corpus."""
    gift_id: str
    alumni_name: str
    graduation_year: int
    amount_inr: float
    gift_purpose: str  # SCHOLARSHIP_CORPUS, CHAIR_PROFESSORSHIP, LAB_INFRASTRUCTURE, UNRESTRICTED
    donation_date: str
    tax_receipt_80g_number: str


class AlumniGivingAnalyticsEngine:
    """
    Computes cohort retention in alumni giving and total corpus yield.
    """

    @classmethod
    def aggregate_endowment_fund(cls, gifts: List[EndowmentGift]) -> Dict[str, Any]:
        """Aggregate total endowment balance and purpose breakdown."""
        total_corpus = sum(g.amount_inr for g in gifts)
        by_purpose: Dict[str, float] = {}

        for g in gifts:
            by_purpose[g.gift_purpose] = by_purpose.get(g.gift_purpose, 0.0) + g.amount_inr

        # Estimated 7.5% annual interest yield for scholarship disbursements
        annual_yield = total_corpus * 0.075

        return {
            "total_endowment_corpus_inr": round(total_corpus, 2),
            "annual_operating_yield_inr": round(annual_yield, 2),
            "total_unique_donors": len(set(g.alumni_name for g in gifts)),
            "purpose_breakdown": {k: round(v, 2) for k, v in by_purpose.items()},
            "beneficiary_scholarships_supported": int(annual_yield // 50000)  # Rs. 50k per scholar
        }
