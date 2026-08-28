"""
EduCore Framework - Student Academic Progression & Detention Tracker

Audits credit thresholds, verifies prerequisite clearances,
and flags academic probations or detentions.
"""

from typing import Dict, List, Any

class AcademicProgressionTracker:
    def __init__(self, student_id: str, current_semester: int):
        self.student_id = student_id
        self.current_semester = current_semester
        self.credit_records: Dict[str, float] = {}  # course_code -> credits_earned
        self.prerequisite_rules: Dict[str, List[str]] = {}  # course_code -> [prereq_courses]

    def record_earned_credits(self, course_code: str, credits: float) -> None:
        self.credit_records[course_code] = credits

    def set_prerequisite_rule(self, course_code: str, prerequisites: List[str]) -> None:
        self.prerequisite_rules[course_code] = prerequisites

    def verify_prerequisite_clearance(self, course_code: str) -> bool:
        rules = self.prerequisite_rules.get(course_code, [])
        for prereq in rules:
            if prereq not in self.credit_records or self.credit_records[prereq] == 0.0:
                # Student has not cleared prerequisite course
                return False
        return True

    def evaluate_semester_promotion(self, minimum_cumulative_credits: float) -> Dict[str, Any]:
        """
        Audits accumulated credits to determine if student can promote to the next semester.
        """
        total_accumulated = sum(self.credit_records.values())
        promoted = total_accumulated >= minimum_cumulative_credits
        
        status = "PROMOTED"
        if not promoted:
            # Under-credited detention
            status = "ACADEMIC_DETENTION"
            
        return {
            "student_id": self.student_id,
            "accumulated_credits": total_accumulated,
            "required_credits_threshold": minimum_cumulative_credits,
            "promotion_status": status,
            "promoted": promoted
        }
