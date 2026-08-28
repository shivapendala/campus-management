"""
EduCore Enterprise Framework - Examination Script Revaluation & Discrepancy Arbiter

Manages end-semester answer script revaluation requests:
Dual-examiner grading discrepancy arbitration (if difference >= 15%, route to Chief Examiner).
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass


@dataclass
class RevaluationArbitrationResult:
    """Outcome of script revaluation review."""
    application_id: str
    student_roll: str
    course_code: str
    original_marks: float
    evaluator_1_marks: float
    evaluator_2_marks: Optional[float]
    final_awarded_marks: float
    grade_changed: bool
    status: str  # FINALIZED, CHIEF_EXAMINER_REVIEW_REQUIRED, NO_CHANGE


class ExaminationRevaluationArbiter:
    """
    Arbitrates multi-evaluator revaluation scores according to university examination manual.
    """

    DISCREPANCY_THRESHOLD_PCT = 15.0  # If marks differ by >= 15% of max marks

    @classmethod
    def arbitrate_revaluation(
        cls,
        application_id: str,
        student_roll: str,
        course_code: str,
        original_marks: float,
        eval_1_marks: float,
        max_marks: float = 100.0,
        eval_2_marks: Optional[float] = None
    ) -> RevaluationArbitrationResult:
        """
        Evaluate marks delta and determine final awarded score:
        - If eval_1 differs from original by < 15%, take average or eval_1 if higher
        - If eval_1 differs by >= 15% and eval_2 provided, arbitrate
        """
        diff_1 = abs(eval_1_marks - original_marks)
        diff_pct = (diff_1 / max_marks) * 100.0

        if diff_pct < cls.DISCREPANCY_THRESHOLD_PCT:
            # Better of original and revaluation
            final_marks = max(original_marks, eval_1_marks)
            grade_changed = final_marks > original_marks
            status = "FINALIZED"
        else:
            if eval_2_marks is None:
                # Requires second independent evaluation
                return RevaluationArbitrationResult(
                    application_id=application_id,
                    student_roll=student_roll,
                    course_code=course_code,
                    original_marks=original_marks,
                    evaluator_1_marks=eval_1_marks,
                    evaluator_2_marks=None,
                    final_awarded_marks=original_marks,
                    grade_changed=False,
                    status="CHIEF_EXAMINER_REVIEW_REQUIRED"
                )
            else:
                # Average of two closest valuations
                candidates = sorted([original_marks, eval_1_marks, eval_2_marks])
                final_marks = round((candidates[1] + candidates[2]) / 2.0, 1)
                grade_changed = final_marks != original_marks
                status = "FINALIZED"

        return RevaluationArbitrationResult(
            application_id=application_id,
            student_roll=student_roll,
            course_code=course_code,
            original_marks=original_marks,
            evaluator_1_marks=eval_1_marks,
            evaluator_2_marks=eval_2_marks,
            final_awarded_marks=final_marks,
            grade_changed=grade_changed,
            status=status
        )
