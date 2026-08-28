"""
EduCore Enterprise Framework - Intellectual Property (IPR) & Patent Portfolio Tracker

Manages faculty inventions, Indian Patent Office (IPO) and USPTO filings:
- Application Filing (Provisional / Complete Specification)
- Official Journal Publication
- First Examination Report (FER) response
- Grant Certificate Issuance and Commercial Royalty Licensing
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class PatentRecord:
    """Represents an institutional intellectual property patent asset."""
    patent_id: str
    application_number: str
    title: str
    inventor_faculty_ids: List[int]
    filing_country: str = "INDIA"  # INDIA, US, PCT_INTERNATIONAL
    filing_date: str = "2025-06-15"
    publication_date: Optional[str] = "2025-12-20"
    grant_date: Optional[str] = "2026-07-10"
    status: str = "GRANTED"  # FILED, PUBLISHED, UNDER_EXAMINATION, GRANTED, LICENSED
    commercial_royalty_inr: float = 250000.0


class PatentPortfolioManager:
    """
    Computes NIRF & NAAC Criterion 3 IPR metrics.
    """

    @classmethod
    def summarize_portfolio(cls, patents: List[PatentRecord]) -> Dict[str, Any]:
        """Aggregate total filings, publications, and grants."""
        total = len(patents)
        published = sum(1 for p in patents if p.status in ("PUBLISHED", "UNDER_EXAMINATION", "GRANTED", "LICENSED"))
        granted = sum(1 for p in patents if p.status in ("GRANTED", "LICENSED"))
        total_royalties = sum(p.commercial_royalty_inr for p in patents)

        return {
            "total_patents_filed": total,
            "patents_published": published,
            "patents_granted": granted,
            "total_commercial_royalties_inr": round(total_royalties, 2),
            "ipr_health_index": "HIGH_INNOVATION" if granted >= 5 else "DEVELOPING_IPR"
        }
