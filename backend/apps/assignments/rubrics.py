"""
EduCore Enterprise Framework - Multi-Criteria Grading Rubric Evaluator

Evaluates assignment submissions against structured rubric criteria:
- Technical Accuracy (Weight: 40%)
- Code Quality & Documentation (Weight: 25%)
- Algorithm Complexity & Optimization (Weight: 20%)
- Presentation & Formatting (Weight: 15%)
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class RubricCriterionLevel:
    """Represents a performance level within a rubric criterion."""
    level_name: str  # EXEMPLARY, PROFICIENT, DEVELOPING, BEGINNER
    score_percentage: float  # e.g., 100%, 75%, 50%, 25%
    descriptor: str


@dataclass
class RubricCriterion:
    """Represents an evaluation criterion in a rubric."""
    criterion_code: str
    criterion_title: str
    weightage_percentage: float
    max_marks: float
    levels: List[RubricCriterionLevel] = field(default_factory=list)


class AssignmentRubricEvaluator:
    """
    Computes weighted marks across rubric criteria and synthesizes qualitative feedback.
    """

    @classmethod
    def evaluate_submission(
        cls,
        total_assignment_marks: float,
        criteria_scores: Dict[str, float],  # { "TECH_ACCURACY": 38.0, "CODE_QUALITY": 22.5 }
        criteria_definitions: List[RubricCriterion]
    ) -> Dict[str, Any]:
        """Calculate weighted total score and provide section-by-section breakdown."""
        total_earned = 0.0
        max_possible = 0.0
        breakdown = []

        for crit in criteria_definitions:
            awarded = criteria_scores.get(crit.criterion_code, 0.0)
            awarded = min(crit.max_marks, max(0.0, awarded))
            total_earned += awarded
            max_possible += crit.max_marks

            attainment_pct = (awarded / crit.max_marks * 100.0) if crit.max_marks > 0 else 0.0

            if attainment_pct >= 85.0:
                level = "EXEMPLARY"
            elif attainment_pct >= 70.0:
                level = "PROFICIENT"
            elif attainment_pct >= 50.0:
                level = "DEVELOPING"
            else:
                level = "NEEDS_IMPROVEMENT"

            breakdown.append({
                "code": crit.criterion_code,
                "title": crit.criterion_title,
                "max_marks": crit.max_marks,
                "awarded_marks": awarded,
                "attainment_pct": round(attainment_pct, 1),
                "performance_level": level
            })

        final_percentage = (total_earned / max_possible * 100.0) if max_possible > 0 else 0.0

        return {
            "total_awarded_marks": round(total_earned, 2),
            "max_possible_marks": max_possible,
            "overall_percentage": round(final_percentage, 2),
            "criteria_breakdown": breakdown
        }
