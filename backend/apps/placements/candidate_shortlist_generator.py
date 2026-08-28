"""
EduCore Framework - Placement Candidate Shortlist Generator

Gathers candidates matching corporate requirements, runs cutoffs,
and exports structured details lists.
"""

from typing import Dict, List, Any

class CandidateShortlistGenerator:
    def __init__(self, target_company: str, cgpa_cutoff: float):
        self.target_company = target_company
        self.cgpa_cutoff = cgpa_cutoff
        self.backlog_limit = 0
        self.restricted_departments: List[str] = []

    def configure_filter_params(self, backlog_limit: int, departments: List[str]) -> None:
        self.backlog_limit = backlog_limit
        self.restricted_departments = departments

    def filter_eligible_pool(self, student_pool: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        shortlisted: List[Dict[str, Any]] = []
        for student in student_pool:
            cgpa = student.get("cgpa", 0.0)
            backlogs = student.get("active_backlogs", 0)
            dept = student.get("department", "")
            
            if cgpa < self.cgpa_cutoff:
                continue
            if backlogs > self.backlog_limit:
                continue
            if self.restricted_departments and dept not in self.restricted_departments:
                continue
                
            shortlisted.append({
                "student_id": student.get("student_id"),
                "name": student.get("name"),
                "cgpa": cgpa,
                "department": dept,
                "email": student.get("email")
            })
            
        return shortlisted
