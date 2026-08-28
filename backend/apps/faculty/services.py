from typing import Dict, Any, List
from django.db.models import Count
from .models import Faculty
from apps.courses.models import Course, TimetableEntry


class FacultyWorkloadService:
    """
    Domain service for Faculty Allocation, Teaching Workload Analysis, and Daily Schedules.
    """

    MAX_WEEKLY_TEACHING_HOURS = 18

    @classmethod
    def get_faculty_dossier(cls, faculty_id: int) -> Dict[str, Any]:
        """
        Generates 360° faculty workload summary, assigned courses, and weekly lecture hours.
        """
        faculty = Faculty.objects.select_related('department', 'user').prefetch_related('assigned_courses').get(id=faculty_id)
        assigned_courses = faculty.assigned_courses.all()
        timetable_slots = TimetableEntry.objects.filter(faculty=faculty)

        total_weekly_hours = timetable_slots.count()
        utilization_rate = round((total_weekly_hours / cls.MAX_WEEKLY_TEACHING_HOURS) * 100, 1)

        return {
            'faculty_id': faculty.faculty_id,
            'name': faculty.name,
            'designation': faculty.designation,
            'department': faculty.department.name if faculty.department else 'N/A',
            'department_code': faculty.department.code if faculty.department else 'N/A',
            'assigned_courses_count': assigned_courses.count(),
            'weekly_teaching_hours': total_weekly_hours,
            'max_allowed_hours': cls.MAX_WEEKLY_TEACHING_HOURS,
            'utilization_rate_pct': utilization_rate,
            'assigned_courses': [{'id': c.id, 'code': c.code, 'title': c.title, 'credits': c.credits} for c in assigned_courses],
        }
