"""
EduCore Enterprise Framework - Semester Examination Revaluation & Triple Valuation Arbiter

Implements university examination revaluation rules:
- Dual Valuation: Valuer 1 (Internal) and Valuer 2 (External)
- Difference <= 15%: Final mark = Average of Valuer 1 & Valuer 2
- Difference > 15%: Trigger 3rd Independent Valuation (Chief Examiner Arbiter)
- Final mark awarded = Average of closest two evaluation scores
"""

from typing import Dict, List, Any, Optional, Tuple


class ExaminationRevaluationArbiter:
    """
    Arbitrates multi-evaluator marks discrepancies.
    """

    @classmethod
    def resolve_final_mark(
        cls,
        valuer_1_marks: float,
        valuer_2_marks: float,
        valuer_3_marks: Optional[float] = None
    ) -> Dict[str, Any]:
        """Compute final moderated marks for publication."""
        diff_1_2 = abs(valuer_1_marks - valuer_2_marks)

        if diff_1_2 <= 15.0:
            final_mark = (valuer_1_marks + valuer_2_marks) / 2.0
            return {
                "final_marks": round(final_mark, 1),
                "evaluation_mode": "DUAL_VALUATION_CONCORDANCE",
                "discrepancy": diff_1_2,
                "third_valuation_required": False
            }

        # If 3rd valuation provided
        if valuer_3_marks is not None:
            # Compare pairs: (1,2), (1,3), (2,3)
            diffs = [
                (abs(valuer_1_marks - valuer_2_marks), (valuer_1_marks + valuer_2_marks) / 2.0, "VALUER_1_AND_2"),
                (abs(valuer_1_marks - valuer_3_marks), (valuer_1_marks + valuer_3_marks) / 2.0, "VALUER_1_AND_3"),
                (abs(valuer_2_marks - valuer_3_marks), (valuer_2_marks + valuer_3_marks) / 2.0, "VALUER_2_AND_3"),
            ]
            diffs.sort(key=lambda x: x[0])
            closest_avg = diffs[0][1]
            pair_used = diffs[0][2]

            return {
                "final_marks": round(closest_avg, 1),
                "evaluation_mode": f"TRIPLE_VALUATION_CLOSEST_PAIR ({pair_used})",
                "third_valuation_marks": valuer_3_marks,
                "third_valuation_required": True,
                "status": "ARBITRATED_AND_FINALIZED"
            }

        return {
            "final_marks": None,
            "evaluation_mode": "THIRD_VALUATION_PENDING",
            "discrepancy": diff_1_2,
            "third_valuation_required": True,
            "status": "DISPATCHED_TO_CHIEF_EXAMINER"
        }
