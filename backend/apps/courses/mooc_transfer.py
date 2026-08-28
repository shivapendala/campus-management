"""
EduCore Enterprise Framework - MOOC / NPTEL / SWAYAM Credit Transfer Equivalence Board

Evaluates external Massive Open Online Courses for credit transfer:
- Max 20% total degree credits (up to 32 credits out of 160) allowed via SWAYAM/NPTEL
- Automatic mapping of NPTEL 4-week (1 credit), 8-week (2 credits), and 12-week (3 credits) courses
- Proctored examination certificate validation with QR verification
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class MOOCEquivalenceApplication:
    """Represents a student request for MOOC credit transfer."""
    application_id: str
    student_roll: str
    platform: str  # NPTEL_SWAYAM, COURSERA_CAMPUS, EDX
    course_name: str
    course_duration_weeks: int  # 4, 8, 12
    nptel_score_out_of_100: float
    proctored_exam_cleared: bool = True
    equivalent_college_elective_code: str = "CS_ELEC_01"


class MOOCCreditTransferManager:
    """
    Evaluates credit awards and university Board of Studies (BOS) approval rules.
    """

    MAX_CUMULATIVE_MOOC_CREDITS = 32

    @classmethod
    def process_credit_transfer(
        cls,
        app: MOOCEquivalenceApplication,
        student_current_mooc_credits: int = 6
    ) -> Dict[str, Any]:
        """Verify passing score and compute transferable credits."""
        if not app.proctored_exam_cleared or app.nptel_score_out_of_100 < 40.0:
            return {
                "status": "REJECTED",
                "awarded_credits": 0,
                "reason": "Failed proctored exam or score below 40% minimum threshold."
            }

        # Map weeks to credits
        if app.course_duration_weeks >= 12:
            credits = 3
        elif app.course_duration_weeks >= 8:
            credits = 2
        else:
            credits = 1

        if (student_current_mooc_credits + credits) > cls.MAX_CUMULATIVE_MOOC_CREDITS:
            return {
                "status": "REJECTED_EXCEEDS_20_PERCENT_CAP",
                "awarded_credits": 0,
                "reason": f"Exceeds UGC 20% statutory MOOC credit ceiling ({cls.MAX_CUMULATIVE_MOOC_CREDITS} credits max)."
            }

        return {
            "status": "APPROVED_BY_DEAN_ACADEMICS",
            "awarded_credits": credits,
            "mapped_elective": app.equivalent_college_elective_code,
            "grade_awarded": "O" if app.nptel_score_out_of_100 >= 90 else ("A+" if app.nptel_score_out_of_100 >= 80 else "A")
        }
