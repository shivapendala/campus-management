"""
EduCore Enterprise Framework - Examination Hall Seating Arrangement Generator

Generates automated examination hall desk allocations with branch interweaving
to ensure no two students from the same department/subject sit adjacent to each other.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class ExamHallDesk:
    """Represents an individual desk in an examination room."""
    hall_name: str
    row_number: int
    column_number: int
    desk_code: str  # e.g., "LH101-R1-C1"
    assigned_student_roll: Optional[str] = None
    assigned_student_name: Optional[str] = None
    department_code: Optional[str] = None
    subject_code: Optional[str] = None


class ExamSeatingArrangementEngine:
    """
    Interleaves students from multiple departments in a checkerboard pattern.
    """

    @classmethod
    def generate_interleaved_seating(
        cls,
        hall_name: str,
        rows: int,
        columns: int,
        student_rosters_by_dept: Dict[str, List[Dict[str, str]]]  # { "CSE": [...], "ECE": [...] }
    ) -> List[ExamHallDesk]:
        """
        Allocate students to a grid of desks alternating departments across adjacent columns.
        """
        desks: List[ExamHallDesk] = []
        dept_keys = list(student_rosters_by_dept.keys())
        if not dept_keys:
            return []

        # Pointers for each department roster
        dept_indices = {d: 0 for d in dept_keys}

        for r in range(1, rows + 1):
            for c in range(1, columns + 1):
                desk_code = f"{hall_name}-R{r}-C{c}"

                # Alternate department based on (row + column) mod count
                dept_target = dept_keys[(r + c) % len(dept_keys)]
                idx = dept_indices[dept_target]
                roster = student_rosters_by_dept[dept_target]

                if idx < len(roster):
                    student = roster[idx]
                    dept_indices[dept_target] += 1
                    desks.append(ExamHallDesk(
                        hall_name=hall_name,
                        row_number=r,
                        column_number=c,
                        desk_code=desk_code,
                        assigned_student_roll=student.get("roll_number"),
                        assigned_student_name=student.get("name"),
                        department_code=dept_target,
                        subject_code=student.get("subject_code")
                    ))
                else:
                    # Empty desk if roster exhausted
                    desks.append(ExamHallDesk(
                        hall_name=hall_name,
                        row_number=r,
                        column_number=c,
                        desk_code=desk_code
                    ))

        return desks
