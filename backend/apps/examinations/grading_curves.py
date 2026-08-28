"""
EduCore Enterprise Framework - Relative & Absolute Grading Normalization Curves

Provides dynamic curve adjustment algorithms:
- Absolute Standard 10-Point Scale (Fixed percentage cutoffs)
- Gaussian Relative Grading (Mean +/- Standard Deviation thresholds)
- Percentile-Based Grading (Top 10% = O, Next 20% = A+, etc.)
"""

import math
import statistics
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass


@dataclass
class NormalizedGradeResult:
    """Normalized grade outcome for a student."""
    student_id: int
    roll_number: str
    raw_marks: float
    grade_letter: str
    grade_point: float
    percentile_rank: float


class ExaminationGradingCurveEngine:
    """
    Computes absolute and Gaussian relative grading curves.
    """

    @classmethod
    def apply_absolute_grading(cls, raw_marks: float, max_marks: float = 100.0) -> Tuple[str, float]:
        """Convert raw marks to absolute 10-point letter grade."""
        pct = (raw_marks / max_marks * 100.0) if max_marks > 0 else 0.0

        if pct >= 90.0:
            return "O", 10.0
        elif pct >= 80.0:
            return "A+", 9.0
        elif pct >= 70.0:
            return "A", 8.0
        elif pct >= 60.0:
            return "B+", 7.0
        elif pct >= 50.0:
            return "B", 6.0
        elif pct >= 40.0:
            return "C", 5.0
        else:
            return "F", 0.0

    @classmethod
    def apply_relative_gaussian_curve(
        cls,
        student_scores: List[Dict[str, Any]]  # [{"id": 1, "roll": "...", "marks": 78.5}, ...]
    ) -> List[NormalizedGradeResult]:
        """
        Apply Gaussian relative grading:
        - O  : marks >= Mean + 1.5 * StdDev
        - A+ : Mean + 1.0 * StdDev <= marks < Mean + 1.5 * StdDev
        - A  : Mean + 0.5 * StdDev <= marks < Mean + 1.0 * StdDev
        - B+ : Mean <= marks < Mean + 0.5 * StdDev
        - B  : Mean - 0.5 * StdDev <= marks < Mean
        - C  : Mean - 1.5 * StdDev <= marks < Mean - 0.5 * StdDev
        - F  : marks < Mean - 1.5 * StdDev (or absolute failure marks < 30)
        """
        if not student_scores:
            return []

        marks_list = [s["marks"] for s in student_scores]
        mean_val = statistics.mean(marks_list)
        std_dev = statistics.stdev(marks_list) if len(marks_list) > 1 else 10.0
        if std_dev == 0.0:
            std_dev = 1.0

        sorted_by_marks = sorted(student_scores, key=lambda x: x["marks"])
        total_students = len(student_scores)

        results = []
        for s in student_scores:
            m = s["marks"]
            # Rank percentile
            rank = sum(1 for other in marks_list if other <= m)
            percentile = round((rank / total_students) * 100.0, 1)

            # Minimum passing marks floor check
            if m < 35.0:
                grade, pt = "F", 0.0
            elif m >= (mean_val + 1.5 * std_dev):
                grade, pt = "O", 10.0
            elif m >= (mean_val + 1.0 * std_dev):
                grade, pt = "A+", 9.0
            elif m >= (mean_val + 0.5 * std_dev):
                grade, pt = "A", 8.0
            elif m >= mean_val:
                grade, pt = "B+", 7.0
            elif m >= (mean_val - 0.5 * std_dev):
                grade, pt = "B", 6.0
            elif m >= (mean_val - 1.5 * std_dev):
                grade, pt = "C", 5.0
            else:
                grade, pt = "F", 0.0

            results.append(NormalizedGradeResult(
                student_id=s["id"],
                roll_number=s["roll"],
                raw_marks=m,
                grade_letter=grade,
                grade_point=pt,
                percentile_rank=percentile
            ))

        return results
