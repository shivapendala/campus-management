"""
EduCore Enterprise Framework - Academic Symposium EasyChair-Style Peer Review Manager

Manages conference paper submissions and double-blind peer review:
- Paper tracks and automated reviewer bids
- Double-blind evaluation rubrics (Novelty, Methodology, Results, Clarity)
- Acceptance notification and IEEE Xplore camera-ready submission package
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class ConferencePaperSubmission:
    """Represents a submitted symposium manuscript."""
    paper_id: str
    track_name: str  # AI_ML, EMBEDDED_SYSTEMS, CLOUD_COMPUTING, CYBERSECURITY
    title: str
    author_names: List[str]
    reviewer_scores: List[float]  # Out of 10.0
    camera_ready_submitted: bool = True
    status: str = "ACCEPTED_ORAL_PRESENTATION"  # SUBMITTED, UNDER_REVIEW, ACCEPTED_ORAL_PRESENTATION, ACCEPTED_POSTER, REJECTED


class SymposiumReviewManager:
    """
    Computes average reviewer scores and generates acceptance lists.
    """

    ACCEPTANCE_THRESHOLD = 7.0

    @classmethod
    def evaluate_paper_decision(cls, paper: ConferencePaperSubmission) -> str:
        """Compute final acceptance verdict based on reviewer ratings."""
        if not paper.reviewer_scores:
            return "UNDER_REVIEW"

        avg_score = sum(paper.reviewer_scores) / len(paper.reviewer_scores)

        if avg_score >= cls.ACCEPTANCE_THRESHOLD:
            return "ACCEPTED_ORAL_PRESENTATION"
        elif avg_score >= 5.5:
            return "ACCEPTED_POSTER"
        else:
            return "REJECTED"
