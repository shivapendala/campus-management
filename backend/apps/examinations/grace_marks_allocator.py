"""
EduCore Framework - Grace Marks Allocator

Applies university grace marks policies to border cases,
allowing students close to passing thresholds to clear courses.
"""

from typing import Dict, List, Any

class GraceMarksAllocator:
    def __init__(self, pass_threshold: float = 40.0, max_grace_marks_total: float = 5.0):
        self.pass_threshold = pass_threshold
        self.max_grace_marks_total = max_grace_marks_total
        self.allocated_grace_records: List[Dict[str, Any]] = []

    def evaluate_and_allocate_grace(self, student_id: str, course_code: str, raw_score: float) -> Dict[str, Any]:
        """
        Determines if student is eligible for grace marks.
        Only applies if raw_score is below pass_threshold and within max_grace_marks_total limit.
        """
        deficit = self.pass_threshold - raw_score
        eligible = 0.0 < deficit <= self.max_grace_marks_total
        
        grace_applied = 0.0
        final_score = raw_score
        status = "FAIL"
        
        if eligible:
            grace_applied = deficit
            final_score = self.pass_threshold
            status = "PASS_WITH_GRACE"
            
            self.allocated_grace_records.append({
                "student_id": student_id,
                "course_code": course_code,
                "raw_score": raw_score,
                "grace_applied": grace_applied
            })
            
        return {
            "student_id": student_id,
            "course_code": course_code,
            "raw_score": raw_score,
            "grace_applied": grace_applied,
            "final_score": final_score,
            "status": status
        }
