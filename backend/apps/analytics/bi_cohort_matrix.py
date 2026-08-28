"""
EduCore Enterprise Framework - Multi-Cohort Longitudinal Analytics & BI Matrices

Performs cohort longitudinal tracking:
- 4-Year Graduation Velocity (Year 1 to Year 4 survival curves)
- Placement Compensation Distribution (Quartiles, Mean, Median, Skewness)
- Departmental Attrition & Retention Heatmaps
"""

import math
from typing import Dict, List, Any, Optional, Tuple


class LongitudinalCohortAnalytics:
    """
    Computes cohort retention curves and compensation statistics.
    """

    @classmethod
    def compute_cohort_survival_curve(
        cls,
        initial_intake: int,
        year1_retained: int,
        year2_retained: int,
        year3_retained: int,
        year4_graduated: int
    ) -> Dict[str, Any]:
        """Calculate cohort retention rates across 4 academic years."""
        y1_pct = (year1_retained / initial_intake * 100.0) if initial_intake > 0 else 0.0
        y2_pct = (year2_retained / initial_intake * 100.0) if initial_intake > 0 else 0.0
        y3_pct = (year3_retained / initial_intake * 100.0) if initial_intake > 0 else 0.0
        y4_pct = (year4_graduated / initial_intake * 100.0) if initial_intake > 0 else 0.0

        return {
            "initial_intake": initial_intake,
            "survival_rates_pct": {
                "year_1_freshman": round(y1_pct, 2),
                "year_2_sophomore": round(y2_pct, 2),
                "year_3_junior": round(y3_pct, 2),
                "year_4_graduation": round(y4_pct, 2)
            },
            "cumulative_attrition_pct": round(100.0 - y4_pct, 2),
            "retention_health": "EXEMPLARY" if y4_pct >= 90.0 else ("STABLE" if y4_pct >= 80.0 else "ATTRITION_ALERT")
        }

    @classmethod
    def compute_salary_distribution_metrics(cls, ctc_offers_lpa: List[float]) -> Dict[str, Any]:
        """Compute mean, median, IQR, and percentiles for campus recruitment salaries."""
        if not ctc_offers_lpa:
            return {"mean": 0.0, "median": 0.0, "p25": 0.0, "p75": 0.0, "p90": 0.0}

        sorted_salaries = sorted(ctc_offers_lpa)
        n = len(sorted_salaries)

        mean_val = sum(sorted_salaries) / n
        median_val = sorted_salaries[n // 2] if n % 2 == 1 else (sorted_salaries[n // 2 - 1] + sorted_salaries[n // 2]) / 2.0
        p25 = sorted_salaries[int(n * 0.25)]
        p75 = sorted_salaries[int(n * 0.75)]
        p90 = sorted_salaries[min(n - 1, int(n * 0.90))]

        # Variance & Std Dev
        variance = sum((s - mean_val) ** 2 for s in sorted_salaries) / n
        std_dev = math.sqrt(variance)

        return {
            "total_offers": n,
            "mean_salary_lpa": round(mean_val, 2),
            "median_salary_lpa": round(median_val, 2),
            "standard_deviation_lpa": round(std_dev, 2),
            "percentile_25_lpa": round(p25, 2),
            "percentile_75_lpa": round(p75, 2),
            "percentile_90_lpa": round(p90, 2),
            "highest_package_lpa": round(max(sorted_salaries), 2),
            "lowest_package_lpa": round(min(sorted_salaries), 2)
        }
