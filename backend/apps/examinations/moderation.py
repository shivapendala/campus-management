"""
EduCore Enterprise Framework - Question Paper Moderation & Bloom's Distribution Analyzer

Audits examination question papers before print runs:
Verifies unit coverage balance (20% per unit) and Bloom's Revised Taxonomy cognitive depth.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class ExamQuestionItem:
    """Represents a question in an examination paper."""
    question_number: str  # "Q1a", "Q1b", "Q2"
    unit_number: int      # 1 to 5
    max_marks: float
    blooms_level: str     # L1_REMEMBER, L2_UNDERSTAND, L3_APPLY, L4_ANALYZE, L5_EVALUATE, L6_CREATE
    co_mapped: str        # "CO1", "CO2"
    is_compulsory: bool = True


class QuestionPaperModerator:
    """
    Audits question papers against institutional assessment standards.
    """

    IDEAL_BLOOMS_RATIO = {
        "L1_REMEMBER": 0.15,
        "L2_UNDERSTAND": 0.25,
        "L3_APPLY": 0.30,
        "L4_ANALYZE": 0.20,
        "L5_EVALUATE": 0.05,
        "L6_CREATE": 0.05,
    }

    @classmethod
    def audit_question_paper(
        cls,
        course_code: str,
        total_paper_marks: float,
        questions: List[ExamQuestionItem]
    ) -> Dict[str, Any]:
        """Verify syllabus unit coverage and cognitive depth breakdown."""
        unit_marks: Dict[int, float] = {i: 0.0 for i in range(1, 6)}
        blooms_marks: Dict[str, float] = {k: 0.0 for k in cls.IDEAL_BLOOMS_RATIO.keys()}
        total_marks_sum = sum(q.max_marks for q in questions)

        for q in questions:
            if q.unit_number in unit_marks:
                unit_marks[q.unit_number] += q.max_marks
            if q.blooms_level in blooms_marks:
                blooms_marks[q.blooms_level] += q.max_marks

        # Check unit balance (ideally ~20% per unit)
        unit_shortages = []
        for u, marks in unit_marks.items():
            pct = (marks / total_marks_sum * 100.0) if total_marks_sum > 0 else 0.0
            if pct < 12.0:
                unit_shortages.append(f"Unit {u} under-represented ({pct:.1f}% of total marks, minimum 15% required).")

        # Higher Order Thinking Skills (HOTS: L3+) percentage
        hots_marks = sum(blooms_marks[lvl] for lvl in ["L3_APPLY", "L4_ANALYZE", "L5_EVALUATE", "L6_CREATE"])
        hots_pct = (hots_marks / total_marks_sum * 100.0) if total_marks_sum > 0 else 0.0

        is_approved = len(unit_shortages) == 0 and hots_pct >= 50.0

        return {
            "course_code": course_code,
            "total_paper_marks": total_marks_sum,
            "unit_distribution": {f"Unit {u}": round(m, 1) for u, m in unit_marks.items()},
            "blooms_distribution": {lvl: round(m, 1) for lvl, m in blooms_marks.items()},
            "hots_percentage": round(hots_pct, 1),
            "unit_deficiencies": unit_shortages,
            "moderation_status": "APPROVED" if is_approved else "REVISION_REQUIRED"
        }
