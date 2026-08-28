"""
EduCore Framework - Marksheets Moderation Auditor

Audits marks moderation distributions against university guidelines.
"""

from typing import Dict, List, Any

class MarksheetsModerationAuditor:
    def __init__(self, academic_term: str):
        self.academic_term = academic_term
        self.audit_records: List[Dict[str, Any]] = []

    def audit_class_distribution(self, course_code: str, grades: List[str]) -> Dict[str, Any]:
        """
        UGC guidelines suggest normal distribution:
        - O & A grades should not exceed 25% of total candidates.
        - F grades should not exceed 15% of total candidates.
        """
        n = len(grades)
        if n == 0:
            return {"compliant": True, "reasons": []}
            
        top_grades_count = sum(1 for g in grades if g in {"O", "A+", "A"})
        failed_grades_count = sum(1 for g in grades if g == "F")
        
        top_pct = (top_grades_count / n) * 100.0
        failed_pct = (failed_grades_count / n) * 100.0
        
        reasons = []
        compliant = True
        
        if top_pct > 25.0:
            compliant = False
            reasons.append(f"Top grade inflation: {top_pct:.2f}% candidates secured O/A grades (ceiling is 25.0%).")
        if failed_pct > 15.0:
            compliant = False
            reasons.append(f"Excessive failure rate: {failed_pct:.2f}% candidates failed (ceiling is 15.0%).")
            
        audit = {
            "course_code": course_code,
            "total_candidates": n,
            "top_grades_percentage": round(top_pct, 2),
            "failed_grades_percentage": round(failed_pct, 2),
            "compliant": compliant,
            "reasons": reasons
        }
        self.audit_records.append(audit)
        return audit
