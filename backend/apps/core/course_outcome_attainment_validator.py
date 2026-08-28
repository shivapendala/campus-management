"""
EduCore Framework - Course Outcome Attainment Validator

Validates exam mark sheets against direct attainment matrices,
detecting anomalous marks entries, outliers, and verifying total calculations.
"""

from typing import Dict, List, Any

class CourseOutcomeAttainmentValidator:
    def __init__(self, course_code: str, academic_term: str):
        self.course_code = course_code
        self.academic_term = academic_term
        self.validation_errors: List[str] = []

    def validate_marks_entry_bounds(self, marks_ledger: List[Dict[str, Any]], max_marks: float) -> bool:
        """
        Validates that all student scores fall within 0.0 and the maximum marks allotted.
        """
        is_valid = True
        for record in marks_ledger:
            student_id = record.get("student_id")
            score = record.get("score")
            
            if score is None:
                self.validation_errors.append(f"Missing score for student '{student_id}'.")
                is_valid = False
                continue
                
            if not (0.0 <= score <= max_marks):
                self.validation_errors.append(
                    f"Out of bounds: Student '{student_id}' score ({score}) exceeds maximum marks ({max_marks}) or is negative."
                )
                is_valid = False
                
        return is_valid

    def check_attainment_outliers(self, marks_ledger: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Identifies student marks that are statistical outliers (Z-Score > 2.5 or Z-Score < -2.5).
        """
        scores = [r["score"] for r in marks_ledger if r.get("score") is not None]
        if not scores:
            return []
            
        n = len(scores)
        mean = sum(scores) / n
        
        variance = sum((x - mean) ** 2 for x in scores) / n
        std_dev = (variance ** 0.5) if variance > 0 else 0.0
        
        outliers: List[Dict[str, Any]] = []
        if std_dev == 0:
            return outliers
            
        for record in marks_ledger:
            score = record.get("score")
            if score is not None:
                z_score = (score - mean) / std_dev
                if abs(z_score) > 2.5:
                    outliers.append({
                        "student_id": record["student_id"],
                        "score": score,
                        "z_score": round(z_score, 2)
                    })
                    
        return outliers

    def verify_direct_attainment_sums(self, co_attainment_rates: Dict[str, float]) -> bool:
        """
        Verifies that no course outcome attainment percentage exceeds 100% or falls below 0%.
        """
        is_valid = True
        for co, rate in co_attainment_rates.items():
            if not (0.0 <= rate <= 100.0):
                self.validation_errors.append(
                    f"Invalid attainment percentage: Outcome '{co}' has attainment rate of {rate}%."
                )
                is_valid = False
        return is_valid
