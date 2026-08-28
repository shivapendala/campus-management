"""
EduCore Enterprise Framework - Double-Blind Peer Review Allocation Engine

Anonymously distributes student project submissions to peers (e.g. 3 reviewers per submission):
Filters outlier marks (Chauvenet's criterion / trimmed mean) and combines peer + faculty scores.
"""

from typing import Dict, List, Any, Optional, Tuple
import statistics


class PeerReviewAllocationEngine:
    """
    Allocates double-blind peer review assignments preventing self-review.
    """

    @classmethod
    def allocate_peer_reviews(
        cls,
        submission_ids: List[int],
        reviews_per_submission: int = 3
    ) -> Dict[int, List[int]]:
        """
        Allocate submissions to student reviewers ensuring no student evaluates their own submission.
        Returns: { reviewer_submission_id: [target_submission_id_1, target_submission_id_2, ...] }
        """
        n = len(submission_ids)
        if n <= reviews_per_submission:
            reviews_per_submission = max(1, n - 1)

        allocations: Dict[int, List[int]] = {sid: [] for sid in submission_ids}

        for i, sid in enumerate(submission_ids):
            for step in range(1, reviews_per_submission + 1):
                target_idx = (i + step) % n
                target_sid = submission_ids[target_idx]
                allocations[sid].append(target_sid)

        return allocations

    @classmethod
    def aggregate_peer_scores(
        cls,
        peer_scores: List[float],
        faculty_score: Optional[float] = None,
        peer_weight: float = 0.30
    ) -> Dict[str, Any]:
        """
        Compute trimmed mean of peer scores and blend with faculty evaluation.
        """
        if not peer_scores:
            final = faculty_score if faculty_score is not None else 0.0
            return {"final_score": round(final, 2), "peer_average": 0.0, "faculty_score": faculty_score}

        # If >= 3 peer scores, drop max and min to eliminate bias/outliers
        if len(peer_scores) >= 3:
            sorted_scores = sorted(peer_scores)
            trimmed = sorted_scores[1:-1]
            peer_avg = statistics.mean(trimmed)
        else:
            peer_avg = statistics.mean(peer_scores)

        if faculty_score is not None:
            composite = (peer_avg * peer_weight) + (faculty_score * (1.0 - peer_weight))
        else:
            composite = peer_avg

        return {
            "final_score": round(composite, 2),
            "peer_average": round(peer_avg, 2),
            "raw_peer_scores": peer_scores,
            "faculty_score": faculty_score,
            "peer_weightage_pct": round(peer_weight * 100.0, 1)
        }
