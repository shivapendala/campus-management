"""
EduCore Enterprise Framework - Student Course-End Evaluation & Faculty Feedback Analyzer

Aggregates anonymous semester course feedback (10 parameters on 1 to 5 Likert scale):
- Subject Knowledge & Clarity
- Punctuality & Regularity
- Coverage of 5-Unit Syllabus
- Encouragement of Doubts & Questions
- Fairness in Internal Evaluation
"""

from typing import Dict, List, Any, Optional
import statistics
from dataclasses import dataclass, field


@dataclass
class FacultyFeedbackParameter:
    """Represents an evaluation metric in the student feedback questionnaire."""
    param_code: str
    param_title: str
    average_score: float  # 1.0 to 5.0
    attainment_pct: float


class StudentFacultyFeedbackAnalyzer:
    """
    Computes overall teacher evaluation score and identifies pedagogical strengths.
    """

    PARAMETERS = [
        ("P1_KNOWLEDGE", "Command over the subject and conceptual clarity"),
        ("P2_PUNCTUALITY", "Punctuality and regularity in conducting scheduled classes"),
        ("P3_SYLLABUS", "Pacing and thorough completion of all 5 syllabus units"),
        ("P4_INTERACTION", "Encouragement of student discussions and problem-solving"),
        ("P5_EVALUATION", "Fairness, transparency, and timely return of internal marks"),
        ("P6_RESOURCES", "Provision of quality course materials and reference books"),
        ("P7_TECH_USE", "Effective use of modern ICT tools and practical demos"),
    ]

    @classmethod
    def analyze_feedback_batch(
        cls,
        faculty_id: int,
        course_code: str,
        feedback_responses: List[Dict[str, float]]  # [{"P1_KNOWLEDGE": 4.5, "P2_PUNCTUALITY": 4.8, ...}, ...]
    ) -> Dict[str, Any]:
        """Compute composite feedback score and parameter-by-parameter breakdown."""
        if not feedback_responses:
            return {"total_responses": 0, "overall_rating_5": 0.0, "rating_band": "NO_DATA"}

        total_respondents = len(feedback_responses)
        param_summaries: List[FacultyFeedbackParameter] = []
        overall_scores_list = []

        for p_code, p_title in cls.PARAMETERS:
            scores_for_p = [resp[p_code] for resp in feedback_responses if p_code in resp]
            if scores_for_p:
                avg_p = statistics.mean(scores_for_p)
                attainment = (avg_p / 5.0) * 100.0
                param_summaries.append(FacultyFeedbackParameter(
                    param_code=p_code,
                    param_title=p_title,
                    average_score=round(avg_p, 2),
                    attainment_pct=round(attainment, 1)
                ))
                overall_scores_list.extend(scores_for_p)

        composite_rating = statistics.mean(overall_scores_list) if overall_scores_list else 0.0

        if composite_rating >= 4.5:
            band = "EXCELLENT (FACULTY ROLE MODEL)"
        elif composite_rating >= 3.8:
            band = "VERY GOOD"
        elif composite_rating >= 3.0:
            band = "SATISFACTORY"
        else:
            band = "COUNSELING & FDP RECOMMENDED"

        return {
            "faculty_id": faculty_id,
            "course_code": course_code,
            "total_student_respondents": total_respondents,
            "overall_feedback_rating_out_of_5": round(composite_rating, 2),
            "attainment_percentage": round((composite_rating / 5.0) * 100.0, 1),
            "performance_band": band,
            "parameter_breakdown": [
                {
                    "code": p.param_code,
                    "title": p.param_title,
                    "score": p.average_score,
                    "attainment_pct": p.attainment_pct
                }
                for p in param_summaries
            ]
        }
