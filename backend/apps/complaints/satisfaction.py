"""
EduCore Enterprise Framework - Post-Resolution Satisfaction Scorer & Grievance KPI Metrics

Computes Grievance Redressal Index (GRI), Net Promoter Score (NPS),
average resolution turnaround time (TAT), and student resolution satisfaction ratings.
"""

from typing import Dict, List, Any, Optional
import statistics


class GrievanceSatisfactionAnalytics:
    """
    Computes grievance resolution speed and student satisfaction indices.
    """

    @classmethod
    def compute_resolution_metrics(
        cls,
        resolved_cases: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Compute mean turnaround time (in hours) and satisfaction score (1.0 to 5.0).
        """
        if not resolved_cases:
            return {
                "total_resolved": 0, "avg_turnaround_hours": 0.0,
                "avg_satisfaction_score": 0.0, "satisfaction_rate_pct": 0.0
            }

        turnaround_times = [float(c.get("tat_hours", 24.0)) for c in resolved_cases]
        ratings = [float(c.get("satisfaction_rating", 4.0)) for c in resolved_cases if c.get("satisfaction_rating")]

        avg_tat = statistics.mean(turnaround_times) if turnaround_times else 0.0
        avg_rating = statistics.mean(ratings) if ratings else 0.0

        satisfied_count = sum(1 for r in ratings if r >= 4.0)
        satisfaction_pct = (satisfied_count / len(ratings) * 100.0) if ratings else 0.0

        return {
            "total_resolved_cases": len(resolved_cases),
            "avg_turnaround_hours": round(avg_tat, 1),
            "avg_satisfaction_score": round(avg_rating, 2),
            "satisfaction_rate_pct": round(satisfaction_pct, 1),
            "redressal_efficiency_rating": "EXCELLENT" if avg_tat <= 48 and avg_rating >= 4.0 else "GOOD"
        }
