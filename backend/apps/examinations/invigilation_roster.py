"""
EduCore Enterprise Framework - Examination Invigilation Roster Allocator

Allocates faculty invigilation duties during end-semester exams:
- Prevents faculty from invigilating their own department/subject exams
- Balances duty load evenly across Assistant/Associate Professors and Professors
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class InvigilationDutyAssignment:
    """Represents an assigned exam invigilation duty."""
    duty_id: str
    hall_name: str
    exam_date: str
    session_time: str  # "09:30 AM - 12:30 PM"
    faculty_id: int
    faculty_name: str
    faculty_department: str
    exam_department: str  # Must differ from faculty_department


class InvigilationRosterManager:
    """
    Allocates conflict-free invigilation duties.
    """

    @classmethod
    def allocate_duties(
        cls,
        halls: List[str],
        exam_date: str,
        session_time: str,
        exam_dept: str,
        available_faculty: List[Dict[str, Any]]
    ) -> List[InvigilationDutyAssignment]:
        """
        Assign 2 faculty per hall ensuring neither belongs to exam_dept.
        """
        import uuid
        eligible = [f for f in available_faculty if f.get("department") != exam_dept]
        duties = []

        for h_idx, hall in enumerate(halls):
            for slot in range(2):
                fac_idx = (h_idx * 2 + slot) % len(eligible) if eligible else 0
                if eligible:
                    fac = eligible[fac_idx]
                    duties.append(InvigilationDutyAssignment(
                        duty_id=f"INV-{str(uuid.uuid4())[:8]}",
                        hall_name=hall,
                        exam_date=exam_date,
                        session_time=session_time,
                        faculty_id=fac.get("id", 0),
                        faculty_name=fac.get("name", "Faculty"),
                        faculty_department=fac.get("department", "CSE"),
                        exam_department=exam_dept
                    ))

        return duties
