"""
EduCore Enterprise Framework - Student Academic Progression & Degree Audit Engine

Calculates semester SGPA, cumulative CGPA, credit accumulation,
backlog resolution verification, honors eligibility, and graduation clearance.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class CourseGradeRecord:
    """Represents an earned course grade and credit points."""
    course_code: str
    course_title: str
    credits: int
    grade_point: float  # 0.0 to 10.0 (O=10, A+=9, A=8, B+=7, B=6, C=5, P=4, F=0)
    grade_letter: str
    is_backlog: bool = False
    attempt_number: int = 1


@dataclass
class SemesterAcademicSummary:
    """Academic achievement summary for an individual semester."""
    semester_number: int
    total_credits_registered: int
    total_credits_earned: int
    sgpa: float
    backlogs_in_semester: int
    courses: List[CourseGradeRecord] = field(default_factory=list)


class AcademicProgressionEngine:
    """
    Computes SGPA, CGPA, and evaluates statutory progression rules:
    - Minimum credits required to promote to next academic year (50% rule)
    - Maximum active backlogs permitted (typically <= 4)
    - Classification of Degree: First Class with Distinction, First Class, Second Class, Pass
    """

    GRADE_SCALE = {
        "O": 10.0,
        "A+": 9.0,
        "A": 8.0,
        "B+": 7.0,
        "B": 6.0,
        "C": 5.0,
        "P": 4.0,
        "F": 0.0,
        "AB": 0.0,
    }

    @classmethod
    def calculate_sgpa(cls, course_grades: List[CourseGradeRecord]) -> Tuple[float, int, int]:
        """
        Calculate Semester Grade Point Average (SGPA):
        SGPA = Sum(Credit * GradePoint) / Sum(Credit)
        Returns: (sgpa, total_registered_credits, total_earned_credits)
        """
        if not course_grades:
            return 0.0, 0, 0

        total_credits = 0
        earned_credits = 0
        total_credit_points = 0.0

        for record in course_grades:
            total_credits += record.credits
            if record.grade_point >= 4.0:  # Passing grade point
                earned_credits += record.credits
            total_credit_points += (record.credits * record.grade_point)

        sgpa = (total_credit_points / total_credits) if total_credits > 0 else 0.0
        return round(sgpa, 2), total_credits, earned_credits

    @classmethod
    def calculate_cgpa(cls, semester_summaries: List[SemesterAcademicSummary]) -> Tuple[float, int, int, int]:
        """
        Calculate Cumulative Grade Point Average (CGPA) across all completed semesters:
        CGPA = Sum(Semester_SGPA * Semester_Credits) / Sum(Semester_Credits)
        Returns: (cgpa, total_credits_registered, total_credits_earned, total_active_backlogs)
        """
        if not semester_summaries:
            return 0.0, 0, 0, 0

        total_registered = 0
        total_earned = 0
        weighted_points = 0.0
        active_backlogs = 0

        for sem in semester_summaries:
            total_registered += sem.total_credits_registered
            total_earned += sem.total_credits_earned
            weighted_points += (sem.sgpa * sem.total_credits_registered)
            active_backlogs += sem.backlogs_in_semester

        cgpa = (weighted_points / total_registered) if total_registered > 0 else 0.0
        return round(cgpa, 2), total_registered, total_earned, active_backlogs

    @classmethod
    def evaluate_year_promotion(
        cls,
        current_year: int,
        total_credits_earned: int,
        total_credits_offered: int,
        active_backlogs: int
    ) -> Tuple[bool, str, List[str]]:
        """
        Evaluate statutory academic promotion criteria for B.Tech / Degree programs:
        - Must secure >= 50% of total credits offered up to current year
        - Active backlogs must not exceed institutional threshold
        """
        conditions_met = []
        violations = []

        credit_attainment_pct = (total_credits_earned / total_credits_offered * 100.0) if total_credits_offered > 0 else 0.0

        # Credit condition (>= 50%)
        if credit_attainment_pct >= 50.0:
            conditions_met.append(f"Credit threshold satisfied ({credit_attainment_pct:.1f}% earned >= 50% required).")
        else:
            violations.append(f"Credit shortage: Only {credit_attainment_pct:.1f}% earned (minimum 50.0% required).")

        # Backlog condition (<= 4 active backlogs)
        if active_backlogs <= 4:
            conditions_met.append(f"Backlog threshold satisfied ({active_backlogs} active <= 4 max).")
        else:
            violations.append(f"Excessive active backlogs ({active_backlogs} active > 4 max allowed).")

        is_promoted = len(violations) == 0
        status_label = f"PROMOTED TO YEAR {current_year + 1}" if is_promoted else "ACADEMICALLY DETAINED"

        return is_promoted, status_label, violations if not is_promoted else conditions_met

    @classmethod
    def classify_degree_division(cls, cgpa: float, had_backlogs_cleared_late: bool = False) -> str:
        """
        Classify graduation award based on final cumulative CGPA:
        - First Class with Distinction: CGPA >= 8.0 (without delayed backlogs)
        - First Class: CGPA >= 6.75
        - Second Class: CGPA >= 5.75
        - Pass Division: CGPA >= 5.0
        - Failed / Incomplete: CGPA < 5.0
        """
        if cgpa >= 8.0 and not had_backlogs_cleared_late:
            return "FIRST CLASS WITH DISTINCTION (HONORS)"
        elif cgpa >= 6.75:
            return "FIRST CLASS"
        elif cgpa >= 5.75:
            return "SECOND CLASS"
        elif cgpa >= 5.0:
            return "PASS DIVISION"
        else:
            return "FAILED / NOT ELIGIBLE FOR DEGREE"
