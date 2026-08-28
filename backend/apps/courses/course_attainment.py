"""
EduCore Enterprise Framework - Continuous Internal Assessment (CIA) Attainment Engine

Blends internal continuous evaluation (Mid-Terms, Quizzes, Lab Assignments)
with end-semester external exam marks to produce definitive Course Outcome (CO) attainment files.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class StudentAssessmentScore:
    """Individual student marks across assessment components."""
    student_roll: str
    mid_term_1_marks: float  # Max 30
    mid_term_2_marks: float  # Max 30
    assignment_marks: float  # Max 10
    end_semester_marks: float  # Max 60


class CIAAttainmentCalculator:
    """
    Computes total CIA score (40% weight) and End-Sem score (60% weight).
    """

    @classmethod
    def compute_student_total(cls, score: StudentAssessmentScore) -> Tuple[float, str, bool]:
        """
        Calculate total composite score out of 100:
        Best of 2 Mid-Terms (20) + Assignment/Quiz (10) + End-Sem Exam (60)
        Returns: (total_marks_100, grade_letter, is_passed)
        """
        best_mid = max(score.mid_term_1_marks, score.mid_term_2_marks)
        mid_weighted = (best_mid / 30.0) * 20.0
        quiz_weighted = min(10.0, score.assignment_marks)
        internal_total = mid_weighted + quiz_weighted  # Max 30

        end_sem_weighted = min(70.0, score.end_semester_marks)  # Max 70

        grand_total = round(internal_total + end_sem_weighted, 1)

        # Passing rule: min 35% in End-Sem and min 40% in Grand Total
        is_passed = (end_sem_weighted >= 24.5) and (grand_total >= 40.0)

        if grand_total >= 90.0:
            grade = "O"
        elif grand_total >= 80.0:
            grade = "A+"
        elif grand_total >= 70.0:
            grade = "A"
        elif grand_total >= 60.0:
            grade = "B+"
        elif grand_total >= 50.0:
            grade = "B"
        elif grand_total >= 40.0:
            grade = "C"
        else:
            grade = "F"

        return grand_total, grade, is_passed
