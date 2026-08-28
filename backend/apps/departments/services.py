from typing import Dict, Any, List
from django.db.models import Count, Avg
from .models import Department
from apps.students.models import Student
from apps.faculty.models import Faculty
from apps.courses.models import Course


class DepartmentPerformanceService:
    """
    Department Academic and Resource Performance Service.
    Aggregates departmental faculty-to-student ratios, course enrollments, and academic health metrics.
    """

    @classmethod
    def get_department_kpi_matrix(cls) -> List[Dict[str, Any]]:
        """
        Generates executive comparative metrics across CSE, ECE, EEE, MECH, and CIVIL.
        """
        departments = Department.objects.prefetch_related('students', 'faculty_members', 'courses').all()
        matrix = []

        for dept in departments:
            student_count = dept.students.count()
            faculty_count = dept.faculty_members.count()
            courses_count = dept.courses.count()

            # Faculty to Student Ratio (e.g. 1:15)
            ratio = round(student_count / max(1, faculty_count), 1)

            matrix.append({
                'id': dept.id,
                'name': dept.name,
                'code': dept.code,
                'student_enrollment': student_count,
                'faculty_strength': faculty_count,
                'courses_offered': courses_count,
                'student_faculty_ratio': f"1:{ratio}",
                'hod_name': dept.hod.get_full_name() if dept.hod else 'Assigned Interim HOD',
            })

        return matrix
