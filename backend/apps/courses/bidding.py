"""
EduCore Enterprise Framework - Elective Course Bidding & Allocation Engine

Allocates seats in high-demand Professional and Open Elective courses
using multi-preference priority queues, CGPA merit ranking, and quota constraints.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class ElectiveCourseOffering:
    """Represents an elective course offered in a semester."""
    course_code: str
    course_name: str
    total_seat_capacity: int
    offering_department: str
    allocated_students: List[int] = field(default_factory=list)


@dataclass
class StudentElectivePreference:
    """Represents a student's ordered elective preferences."""
    student_id: int
    roll_number: str
    cgpa: float
    preferences: List[str]  # Ordered list of course codes: ["CS701", "CS702", "CS703"]


class ElectiveAllocationEngine:
    """
    Executes Gale-Shapley style merit-ordered stable allocation of elective seats.
    """

    @classmethod
    def allocate_electives(
        cls,
        offerings: Dict[str, ElectiveCourseOffering],
        student_preferences: List[StudentElectivePreference]
    ) -> Dict[str, Any]:
        """
        Allocate students to elective courses ranked strictly by descending CGPA merit.
        """
        # Sort students descending by CGPA
        sorted_students = sorted(student_preferences, key=lambda s: s.cgpa, reverse=True)

        allocations: Dict[int, str] = {}  # student_id -> allocated_course_code
        unallocated_students: List[int] = []

        for student in sorted_students:
            allocated = False
            for preferred_course in student.preferences:
                course = offerings.get(preferred_course)
                if course and len(course.allocated_students) < course.total_seat_capacity:
                    course.allocated_students.append(student.student_id)
                    allocations[student.student_id] = preferred_course
                    allocated = True
                    break

            if not allocated:
                unallocated_students.append(student.student_id)

        course_utilization = {
            code: {
                "name": off.course_name,
                "capacity": off.total_seat_capacity,
                "enrolled": len(off.allocated_students),
                "occupancy_rate_pct": round((len(off.allocated_students) / off.total_seat_capacity * 100.0), 2)
            }
            for code, off in offerings.items()
        }

        return {
            "total_students_processed": len(student_preferences),
            "successfully_allocated_count": len(allocations),
            "unallocated_count": len(unallocated_students),
            "allocations_map": allocations,
            "course_occupancy": course_utilization,
            "allocation_rate_pct": round((len(allocations) / len(student_preferences) * 100.0), 2) if student_preferences else 0.0
        }
