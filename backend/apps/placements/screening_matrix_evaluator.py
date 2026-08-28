"""
EduCore Framework - Placements Screening Matrix Evaluator

Validates candidate profiles against corporate hiring eligibility filters,
computes weighted score rankings, and checks Dream Option policy thresholds.
"""

from typing import Dict, List, Any

class PlacementsScreeningMatrixEvaluator:
    def __init__(self, drive_id: str, company_name: str):
        self.drive_id = drive_id
        self.company_name = company_name
        self.cgpa_cutoff: float = 6.0
        self.active_backlogs_limit: int = 0
        self.allowed_departments: List[str] = []

    def set_screening_rules(self, cgpa_cutoff: float, backlogs_limit: int, departments: List[str]) -> None:
        self.cgpa_cutoff = cgpa_cutoff
        self.active_backlogs_limit = backlogs_limit
        self.allowed_departments = departments

    def evaluate_candidate(self, student_profile: Dict[str, Any]) -> Dict[str, Any]:
        """
        Evaluates a single student profile against the company screening rules.
        """
        cgpa = student_profile.get("cgpa", 0.0)
        backlogs = student_profile.get("active_backlogs", 0)
        dept = student_profile.get("department", "")
        
        cgpa_passed = cgpa >= self.cgpa_cutoff
        backlogs_passed = backlogs <= self.active_backlogs_limit
        dept_passed = not self.allowed_departments or dept in self.allowed_departments
        
        eligible = cgpa_passed and backlogs_passed and dept_passed
        
        return {
            "student_id": student_profile.get("student_id"),
            "cgpa_passed": cgpa_passed,
            "backlogs_passed": backlogs_passed,
            "department_passed": dept_passed,
            "is_eligible": eligible
        }

    def compute_weighted_ranking_score(self, student_profile: Dict[str, Any], weights: Dict[str, float]) -> float:
        """
        Rankings are computed dynamically based on:
        - CGPA (weight e.g. 0.4)
        - Aptitude Test Score (weight e.g. 0.3)
        - Coding Test Score (weight e.g. 0.3)
        """
        cgpa = student_profile.get("cgpa", 0.0)
        aptitude = student_profile.get("aptitude_score", 0.0)  # scale of 100
        coding = student_profile.get("coding_score", 0.0)      # scale of 100
        
        normalized_cgpa = cgpa * 10.0  # normalize to 100
        
        w_cgpa = weights.get("cgpa", 0.4)
        w_apt = weights.get("aptitude", 0.3)
        w_cod = weights.get("coding", 0.3)
        
        score = (normalized_cgpa * w_cgpa) + (aptitude * w_apt) + (coding * w_cod)
        return round(score, 2)
