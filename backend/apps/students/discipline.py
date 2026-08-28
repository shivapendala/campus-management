"""
EduCore Enterprise Framework - Student Disciplinary Action & Conduct Tracker

Tracks disciplinary infractions, Proctorial Board hearings, warning notices,
suspension orders, and conduct demerit point registers.
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
from dataclasses import dataclass, field


@dataclass
class DisciplinaryIncident:
    """Represents a logged disciplinary incident or inquiry."""
    incident_id: str
    student_id: int
    student_roll: str
    incident_date: str
    incident_type: str  # EXAM_MALPRACTICE, HOSTEL_VIOLATION, LAB_DAMAGE, CONDUCT_MISBEHAVIOR, ATTENDANCE_FRAUD
    severity: str        # MINOR, MODERATE, MAJOR, CRITICAL
    description: str
    reported_by_faculty_id: int
    action_taken: str    # VERBAL_WARNING, WRITTEN_WARNING, FINE_LEVIED, SUSPENSION_DAYS, COMMUNITY_SERVICE, EXPULSION
    demerit_points: int = 0
    fine_amount: float = 0.0
    hearing_completed: bool = False
    is_resolved: bool = False


class StudentDisciplineManager:
    """
    Computes conduct score and evaluates eligibility for institutional honors.
    """

    MAX_CONDUCT_SCORE = 100

    @classmethod
    def calculate_student_conduct_score(
        cls,
        incidents: List[DisciplinaryIncident]
    ) -> Tuple[int, str, bool]:
        """
        Calculate net conduct score and determine if student is eligible for campus awards/honors.
        Returns: (conduct_score_out_of_100, conduct_grade, honors_eligible)
        """
        total_demerits = sum(inc.demerit_points for inc in incidents)
        net_score = max(0, cls.MAX_CONDUCT_SCORE - total_demerits)

        has_major_infraction = any(inc.severity in ("MAJOR", "CRITICAL") for inc in incidents)

        if net_score >= 90 and not has_major_infraction:
            grade = "EXEMPLARY CONDUCT"
            honors_eligible = True
        elif net_score >= 75 and not has_major_infraction:
            grade = "GOOD CONDUCT"
            honors_eligible = True
        elif net_score >= 50:
            grade = "PROBATIONARY CONDUCT"
            honors_eligible = False
        else:
            grade = "SEVERE DISCIPLINARY SANCTION"
            honors_eligible = False

        return net_score, grade, honors_eligible
