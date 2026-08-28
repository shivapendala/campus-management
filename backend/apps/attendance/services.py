from datetime import date
from decimal import Decimal
from typing import Dict, List, Any
from django.db.models import Count, Q
from .models import AttendanceRecord, AttendanceStatus
from apps.students.models import Student
from apps.courses.models import Course


class AttendanceAnalyticsService:
    """
    Enterprise Attendance Analytics Service.
    Implements attendance percentage formulas, monthly heatmaps, and condonation shortage audit registers.
    """

    @classmethod
    def calculate_student_course_attendance(cls, student_id: int, course_id: int) -> Dict[str, Any]:
        """
        Calculates exact attendance metrics using standard formula:
        Attendance % = (Present Classes / Total Classes) * 100
        """
        records = AttendanceRecord.objects.filter(student_id=student_id, course_id=course_id)
        total_classes = records.count()
        if total_classes == 0:
            return {
                'total_classes': 0,
                'present_classes': 0,
                'absent_classes': 0,
                'late_classes': 0,
                'leave_classes': 0,
                'attendance_percentage': 100.0,
                'shortage_alert': False,
            }

        present_classes = records.filter(status__in=[AttendanceStatus.PRESENT, AttendanceStatus.LATE]).count()
        absent_classes = records.filter(status=AttendanceStatus.ABSENT).count()
        late_classes = records.filter(status=AttendanceStatus.LATE).count()
        leave_classes = records.filter(status=AttendanceStatus.LEAVE).count()

        percentage = round((present_classes / total_classes) * 100.0, 2)
        shortage_alert = percentage < 75.0

        return {
            'total_classes': total_classes,
            'present_classes': present_classes,
            'absent_classes': absent_classes,
            'late_classes': late_classes,
            'leave_classes': leave_classes,
            'attendance_percentage': percentage,
            'shortage_alert': shortage_alert,
        }

    @classmethod
    def get_section_condonation_shortage_roster(cls, department_id: int, semester: int, threshold: float = 75.0) -> List[Dict[str, Any]]:
        """
        Retrieves all students whose attendance falls below the condonation threshold (< 75%).
        """
        students = Student.objects.filter(department_id=department_id, year=((semester + 1) // 2))
        shortage_list = []
        for s in students:
            records = AttendanceRecord.objects.filter(student=s)
            total = records.count()
            if total > 0:
                present = records.filter(status__in=[AttendanceStatus.PRESENT, AttendanceStatus.LATE]).count()
                pct = round((present / total) * 100.0, 1)
                if pct < threshold:
                    shortage_list.append({
                        'student_id': s.student_id,
                        'student_name': s.name,
                        'total_classes': total,
                        'attended_classes': present,
                        'percentage': pct,
                        'shortage_gap': round(threshold - pct, 1),
                    })
        return shortage_list
