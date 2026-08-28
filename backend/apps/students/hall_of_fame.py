"""
EduCore Enterprise Framework - Student Hall of Fame & Academic Distinction Roster

Maintains institutional rolls of honor:
- University Gold Medalists
- Semester Department Toppers
- Hackathon & Innovation Champions
- Sports Excellence Roll
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class AcademicDistinctionRecord:
    """Represents a student accolade or award entry."""
    award_id: str
    student_id: int
    student_roll: str
    student_name: str
    department: str
    award_title: str  # GOLD_MEDAL, DEPARTMENT_TOPPER, HACKATHON_WINNER, BEST_OUTGOING_STUDENT
    academic_year: str
    cgpa_at_time: float
    citation_text: str


class StudentHallOfFameManager:
    """
    Manages distinction records and alumni awards.
    """

    @classmethod
    def get_department_toppers(cls, student_records: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Identify highest CGPA holder per department."""
        dept_groups: Dict[str, List[Dict[str, Any]]] = {}
        for s in student_records:
            dept = s.get("department", "CSE")
            if dept not in dept_groups:
                dept_groups[dept] = []
            dept_groups[dept].append(s)

        toppers = []
        for dept, students in dept_groups.items():
            sorted_s = sorted(students, key=lambda x: float(x.get("cgpa", 0.0)), reverse=True)
            if sorted_s:
                top = sorted_s[0]
                toppers.append({
                    "department": dept,
                    "roll_number": top.get("roll_number"),
                    "name": top.get("name"),
                    "cgpa": top.get("cgpa"),
                    "award": f"Department Rank 1 - {dept} Gold Medalist"
                })

        return toppers
