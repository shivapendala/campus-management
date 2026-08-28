"""
EduCore Enterprise Framework - Faculty Workload Balancing & Credit Hour Optimizer

Enforces statutory AICTE/UGC teaching workload norms:
- Professor: 14 teaching hours/week
- Associate Professor: 14 teaching hours/week
- Assistant Professor: 16 teaching hours/week
Computes lab-to-theory conversion factors (1 Lab hour = 0.5 or 0.75 lecture credits).
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class CourseTeachingAssignment:
    """Represents a scheduled course assigned to a faculty member."""
    course_code: str
    course_name: str
    course_type: str  # THEORY, LAB, TUTORIAL, PROJECT_GUIDANCE
    lecture_hours_per_week: int
    lab_hours_per_week: int
    tutorial_hours_per_week: int
    batch_count: int = 1


@dataclass
class FacultyWorkloadAudit:
    """Complete workload compliance assessment for a faculty member."""
    faculty_id: int
    faculty_code: str
    faculty_name: str
    designation: str  # PROFESSOR, ASSOCIATE_PROFESSOR, ASSISTANT_PROFESSOR, ADJUNCT
    department: str
    target_hours: int
    actual_theory_hours: int
    actual_lab_hours: int
    actual_tutorial_hours: int
    total_effective_hours: float
    workload_status: str  # OPTIMAL, UNDERLOADED, OVERLOADED
    variance_hours: float
    assignments: List[CourseTeachingAssignment] = field(default_factory=list)


class FacultyWorkloadOptimizer:
    """
    Computes effective teaching load and flags underloaded/overloaded faculty members.
    """

    STATUTORY_NORMS = {
        "PROFESSOR": 14,
        "ASSOCIATE_PROFESSOR": 14,
        "ASSISTANT_PROFESSOR": 16,
        "LECTURER": 18,
        "ADJUNCT": 8,
        "GUEST_FACULTY": 6,
    }

    # Weight multipliers: 1 Theory hr = 1.0, 1 Lab hr = 0.75, 1 Tutorial = 1.0
    THEORY_WEIGHT = 1.0
    LAB_WEIGHT = 0.75
    TUTORIAL_WEIGHT = 1.0

    @classmethod
    def audit_faculty_workload(
        cls,
        faculty_id: int,
        faculty_code: str,
        faculty_name: str,
        designation: str,
        department: str,
        assigned_courses: List[CourseTeachingAssignment]
    ) -> FacultyWorkloadAudit:
        """Calculate total weekly workload and evaluate statutory variance."""
        norm_key = designation.upper().replace(" ", "_")
        target_hours = cls.STATUTORY_NORMS.get(norm_key, 16)

        total_theory = 0
        total_lab = 0
        total_tut = 0

        for assign in assigned_courses:
            total_theory += (assign.lecture_hours_per_week * assign.batch_count)
            total_lab += (assign.lab_hours_per_week * assign.batch_count)
            total_tut += (assign.tutorial_hours_per_week * assign.batch_count)

        effective_hours = (
            (total_theory * cls.THEORY_WEIGHT) +
            (total_lab * cls.LAB_WEIGHT) +
            (total_tut * cls.TUTORIAL_WEIGHT)
        )
        effective_hours = round(effective_hours, 2)
        variance = round(effective_hours - target_hours, 2)

        if abs(variance) <= 1.5:
            status = "OPTIMAL"
        elif variance > 1.5:
            status = "OVERLOADED"
        else:
            status = "UNDERLOADED"

        return FacultyWorkloadAudit(
            faculty_id=faculty_id,
            faculty_code=faculty_code,
            faculty_name=faculty_name,
            designation=designation,
            department=department,
            target_hours=target_hours,
            actual_theory_hours=total_theory,
            actual_lab_hours=total_lab,
            actual_tutorial_hours=total_tut,
            total_effective_hours=effective_hours,
            workload_status=status,
            variance_hours=variance,
            assignments=assigned_courses
        )

    @classmethod
    def department_workload_balance_summary(cls, faculty_audits: List[FacultyWorkloadAudit]) -> Dict[str, Any]:
        """Aggregate department workload distribution and balance metrics."""
        if not faculty_audits:
            return {"total_faculty": 0, "avg_effective_hours": 0.0, "status_breakdown": {}}

        total = len(faculty_audits)
        avg_hours = sum(f.total_effective_hours for f in faculty_audits) / total
        status_counts = {"OPTIMAL": 0, "UNDERLOADED": 0, "OVERLOADED": 0}

        for f in faculty_audits:
            status_counts[f.workload_status] = status_counts.get(f.workload_status, 0) + 1

        return {
            "total_faculty": total,
            "avg_effective_hours_per_faculty": round(avg_hours, 2),
            "status_breakdown": status_counts,
            "optimal_balance_percentage": round((status_counts["OPTIMAL"] / total * 100.0), 2)
        }
