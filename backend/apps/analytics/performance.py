"""
EduCore Enterprise Framework - Institutional Academic Performance Engine

Calculates semester-over-semester grade variances, pass percentage heatmaps,
distinction distributions, and academic outlier metrics across cohorts.
"""

from typing import Dict, List, Any, Optional
import math


class InstitutionalPerformanceEngine:
    """
    Computes statistical indicators for academic evaluations:
    Mean, Median, Standard Deviation, Interquartile Range (IQR),
    and Grade Point Attainment distributions.
    """

    @classmethod
    def compute_statistical_summary(cls, scores: List[float]) -> Dict[str, Any]:
        """
        Compute standard descriptive statistics on a distribution of exam marks or GPA values.
        """
        if not scores:
            return {
                "count": 0, "mean": 0.0, "median": 0.0, "std_dev": 0.0,
                "min": 0.0, "max": 0.0, "q1": 0.0, "q3": 0.0, "iqr": 0.0
            }

        sorted_scores = sorted(scores)
        n = len(sorted_scores)
        mean_val = sum(sorted_scores) / n

        # Median
        if n % 2 == 1:
            median_val = sorted_scores[n // 2]
        else:
            median_val = (sorted_scores[n // 2 - 1] + sorted_scores[n // 2]) / 2.0

        # Standard Deviation
        variance = sum((x - mean_val) ** 2 for x in sorted_scores) / n
        std_dev = math.sqrt(variance)

        # Quartiles
        q1 = sorted_scores[int(n * 0.25)]
        q3 = sorted_scores[int(n * 0.75)]
        iqr = q3 - q1

        return {
            "count": n,
            "mean": round(mean_val, 2),
            "median": round(median_val, 2),
            "std_dev": round(std_dev, 2),
            "min": round(sorted_scores[0], 2),
            "max": round(sorted_scores[-1], 2),
            "q1": round(q1, 2),
            "q3": round(q3, 2),
            "iqr": round(iqr, 2)
        }

    @classmethod
    def compute_grade_distribution(cls, scores: List[float]) -> Dict[str, int]:
        """
        Classify scores into standard 10-point scale grade buckets:
        O (90-100), A+ (80-89), A (70-79), B+ (60-69), B (50-59), C (40-49), F (<40)
        """
        distribution = {"O": 0, "A+": 0, "A": 0, "B+": 0, "B": 0, "C": 0, "F": 0}
        for s in scores:
            if s >= 90.0:
                distribution["O"] += 1
            elif s >= 80.0:
                distribution["A+"] += 1
            elif s >= 70.0:
                distribution["A"] += 1
            elif s >= 60.0:
                distribution["B+"] += 1
            elif s >= 50.0:
                distribution["B"] += 1
            elif s >= 40.0:
                distribution["C"] += 1
            else:
                distribution["F"] += 1
        return distribution
