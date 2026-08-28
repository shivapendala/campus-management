"""
EduCore Enterprise Framework - Faculty Research & Publications Ledger

Tracks Scopus/SCI/UGC-CARE indexed journal publications, citations,
patents filed/granted, h-index calculation, and conference proceedings.
"""

from typing import Dict, List, Any, Optional
import datetime
from dataclasses import dataclass, field


@dataclass
class PublicationRecord:
    """Represents an academic research publication or patent."""
    pub_id: str
    title: str
    authors: List[str]
    faculty_id: int
    pub_type: str  # JOURNAL, CONFERENCE, PATENT, BOOK_CHAPTER, MONOGRAPH
    journal_name: str
    indexing: str  # SCOPUS, SCI, ESCI, UGC_CARE, IEEE, ACM, OTHER
    impact_factor: float
    citation_count: int
    publication_date: str
    doi_or_issn: str
    is_peer_reviewed: bool = True


class FacultyResearchLedger:
    """
    Computes research metrics: h-index, i10-index, total citations, and journal impact weights.
    """

    @classmethod
    def calculate_h_index(cls, citation_counts: List[int]) -> int:
        """
        Compute the h-index of a researcher:
        A scientist has index h if h of their N papers have at least h citations each.
        """
        if not citation_counts:
            return 0
        sorted_citations = sorted(citation_counts, reverse=True)
        h = 0
        for i, c in enumerate(sorted_citations):
            if c >= (i + 1):
                h = i + 1
            else:
                break
        return h

    @classmethod
    def calculate_i10_index(cls, citation_counts: List[int]) -> int:
        """Compute i10-index: Number of publications with at least 10 citations."""
        return sum(1 for c in citation_counts if c >= 10)

    @classmethod
    def summarize_faculty_research_profile(
        cls,
        faculty_id: int,
        publications: List[PublicationRecord]
    ) -> Dict[str, Any]:
        """Generate comprehensive research profile summary."""
        total_pubs = len(publications)
        citations = [p.citation_count for p in publications]
        total_citations = sum(citations)
        h_idx = cls.calculate_h_index(citations)
        i10_idx = cls.calculate_i10_index(citations)

        scopus_sci_count = sum(1 for p in publications if p.indexing in ("SCOPUS", "SCI", "IEEE", "ACM"))
        patents_count = sum(1 for p in publications if p.pub_type == "PATENT")
        avg_impact = (sum(p.impact_factor for p in publications) / total_pubs) if total_pubs > 0 else 0.0

        return {
            "faculty_id": faculty_id,
            "total_publications": total_pubs,
            "total_citations": total_citations,
            "h_index": h_idx,
            "i10_index": i10_idx,
            "scopus_sci_indexed_count": scopus_sci_count,
            "patents_count": patents_count,
            "average_impact_factor": round(avg_impact, 2),
            "research_rank": "DISTINGUISHED" if h_idx >= 15 else ("ESTABLISHED" if h_idx >= 7 else "EMERGING")
        }
