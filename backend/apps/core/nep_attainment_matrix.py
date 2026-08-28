"""
EduCore Framework - National Education Policy (NEP) Attainment Matrix Analyzer

Provides calculations for credit frameworks, Multiple Entry and Exit System (MEES) tracking,
academic bank of credits (ABC) alignments, and program outcome projections.
"""

import math
from typing import Dict, List, Any, Optional

class NEPAttainmentMatrix:
    def __init__(self, institution_code: str, academic_year: str):
        self.institution_code = institution_code
        self.academic_year = academic_year
        self.course_registry: Dict[str, Dict[str, Any]] = {}
        self.abc_ledger: Dict[str, List[Dict[str, Any]]] = {}

    def register_course(self, course_code: str, credits: int, category: str, department: str) -> None:
        """
        Registers a course under NEP categories: Multidisciplinary, Ability Enhancement,
        Skill Enhancement, Value Added, Core, or Elective.
        """
        self.course_registry[course_code] = {
            "credits": credits,
            "category": category,
            "department": department,
            "po_mappings": {},
            "co_mappings": {}
        }

    def map_po_weight(self, course_code: str, po_index: int, weight: float) -> bool:
        if course_code not in self.course_registry:
            return False
        if not (0.0 <= weight <= 3.0):
            return False
        self.course_registry[course_code]["po_mappings"][f"PO{po_index}"] = weight
        return True

    def record_abc_credits(self, student_id: str, course_code: str, grade_points: float) -> Dict[str, Any]:
        if course_code not in self.course_registry:
            raise ValueError(f"Course {course_code} not found in NEP registry.")
        
        course = self.course_registry[course_code]
        credits_earned = course["credits"]
        weighted_points = credits_earned * grade_points
        
        entry = {
            "course_code": course_code,
            "credits": credits_earned,
            "grade_points": grade_points,
            "weighted_points": weighted_points,
            "category": course["category"]
        }
        
        if student_id not in self.abc_ledger:
            self.abc_ledger[student_id] = []
        self.abc_ledger[student_id].append(entry)
        return entry

    def calculate_sgpa(self, student_id: str) -> float:
        if student_id not in self.abc_ledger or not self.abc_ledger[student_id]:
            return 0.0
        total_credits = 0.0
        total_weighted_points = 0.0
        for entry in self.abc_ledger[student_id]:
            total_credits += entry["credits"]
            total_weighted_points += entry["weighted_points"]
        return round(total_weighted_points / total_credits, 2) if total_credits > 0 else 0.0

    def evaluate_exit_eligibility(self, student_id: str) -> Dict[str, Any]:
        """
        Evaluates Exit pathways under NEP MEES:
        - 1 Year: Certificate (min 40 credits + 4 credits internship)
        - 2 Years: Diploma (min 80 credits + 4 credits internship)
        - 3 Years: Bachelor's Degree (min 120 credits)
        - 4 Years: Bachelor's with Honours/Research (min 160 credits)
        """
        if student_id not in self.abc_ledger:
            return {"eligible": False, "level": "NONE", "credits": 0}
        
        total_credits = sum(entry["credits"] for entry in self.abc_ledger[student_id])
        
        if total_credits >= 160:
            return {
                "eligible": True,
                "level": "BACHELORS_HONOURS_RESEARCH",
                "credits": total_credits,
                "exit_award": "Bachelor of Technology (Honours/Research)"
            }
        elif total_credits >= 120:
            return {
                "eligible": True,
                "level": "BACHELORS_DEGREE",
                "credits": total_credits,
                "exit_award": "Bachelor of Technology"
            }
        elif total_credits >= 80:
            return {
                "eligible": True,
                "level": "DIPLOMA",
                "credits": total_credits,
                "exit_award": "Undergraduate Diploma in Engineering"
            }
        elif total_credits >= 40:
            return {
                "eligible": True,
                "level": "CERTIFICATE",
                "credits": total_credits,
                "exit_award": "Undergraduate Certificate in Engineering"
            }
        return {
            "eligible": False,
            "level": "NONE",
            "credits": total_credits,
            "exit_award": "No Award (Insufficient Credits)"
        }

    def compute_po_attainment_matrix(self, student_grades: Dict[str, float]) -> Dict[str, float]:
        """
        Calculates student-specific Program Outcome (PO) attainment based on course mappings.
        """
        po_attainment: Dict[str, float] = {}
        po_weights_sum: Dict[str, float] = {}
        
        for course_code, grade in student_grades.items():
            if course_code not in self.course_registry:
                continue
            course = self.course_registry[course_code]
            for po_name, weight in course["po_mappings"].items():
                weighted_contribution = weight * (grade / 10.0)
                po_attainment[po_name] = po_attainment.get(po_name, 0.0) + weighted_contribution
                po_weights_sum[po_name] = po_weights_sum.get(po_name, 0.0) + weight
                
        final_attainment: Dict[str, float] = {}
        for po_name, total_contribution in po_attainment.items():
            max_weight = po_weights_sum[po_name]
            final_attainment[po_name] = round((total_contribution / max_weight) * 100.0, 2) if max_weight > 0 else 0.0
            
        return final_attainment
