"""
EduCore Framework - AICTE Data & Compliance Aggregator

Compiles and formats mandatory disclosures, teacher-student ratios (SFR),
and laboratory infrastructure square footage records.
"""

from typing import Dict, List, Any

class AICTEDataAggregator:
    def __init__(self, department: str):
        self.department = department
        self.faculty_count = 0
        self.student_count = 0
        self.total_carpet_area_sqm = 0.0
        self.total_computers_count = 0

    def set_stats(self, faculty: int, students: int, area: float, computers: int) -> None:
        self.faculty_count = faculty
        self.student_count = students
        self.total_carpet_area_sqm = area
        self.total_computers_count = computers

    def calculate_compliance_indicators(self) -> Dict[str, Any]:
        """
        AICTE Recommended norms:
        - Student to Faculty Ratio (SFR) <= 20.0
        - At least 1 computer per 4 students in active semesters (ratio >= 0.25)
        """
        sfr = (self.student_count / self.faculty_count) if self.faculty_count > 0 else 999.0
        computer_ratio = (self.total_computers_count / self.student_count) if self.student_count > 0 else 0.0
        
        sfr_compliant = sfr <= 20.0
        computer_compliant = computer_ratio >= 0.25
        
        return {
            "department": self.department,
            "student_faculty_ratio": round(sfr, 2),
            "sfr_compliant": sfr_compliant,
            "computer_to_student_ratio": round(computer_ratio, 2),
            "computer_ratio_compliant": computer_compliant,
            "carpet_area_registered_sqm": self.total_carpet_area_sqm,
            "fully_compliant": sfr_compliant and computer_compliant
        }
