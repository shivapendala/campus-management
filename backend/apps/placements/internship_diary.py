"""
EduCore Enterprise Framework - Summer Internship Weekly Work Diary & Mentor Appraisal

Manages mandatory 8-week engineering summer internships:
- Weekly progress log entries submitted by student
- Industry external mentor feedback and evaluation (1 to 5 rating)
- Faculty internal mentor review and credit award (3 credits)
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class WeeklyInternshipLog:
    """Represents one week of industrial training."""
    week_number: int  # 1 to 8
    key_tasks_completed: str
    skills_acquired: List[str]
    hours_worked: int = 40
    industry_mentor_rating: int = 5  # 1 to 5
    mentor_remarks: str = "Excellent performance on backend microservices."


class InternshipDiaryManager:
    """
    Computes total internship hours and final viva qualification.
    """

    @classmethod
    def evaluate_internship_completion(cls, logs: List[WeeklyInternshipLog]) -> Dict[str, Any]:
        """Aggregate weekly entries and compute average mentor rating."""
        total_weeks = len(logs)
        total_hours = sum(l.hours_worked for l in logs)
        avg_rating = sum(l.industry_mentor_rating for l in logs) / total_weeks if total_weeks > 0 else 0.0

        is_complete = total_weeks >= 8 and total_hours >= 320 and avg_rating >= 3.0

        return {
            "completed_weeks": total_weeks,
            "total_hours_logged": total_hours,
            "average_mentor_rating": round(avg_rating, 2),
            "is_internship_certified": is_complete,
            "credits_awarded": 3 if is_complete else 0,
            "status": "QUALIFIED_FOR_FINAL_VIVA" if is_complete else "INCOMPLETE_HOURS"
        }
