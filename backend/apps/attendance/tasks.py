from decimal import Decimal
from typing import List, Dict, Any
from django.utils import timezone
from django.core.exceptions import ValidationError
from apps.attendance.models import AttendanceRecord, AttendanceStatus
from apps.students.models import Student
from apps.notifications.models import Notification, NotificationType


def validate_attendance_date_not_in_future(att_date):
    """
    Ensures attendance cannot be recorded for future calendar dates.
    """
    if att_date > timezone.now().date():
        raise ValidationError("Attendance session date cannot be scheduled in the future.")


def task_audit_and_dispatch_attendance_shortage_notices():
    """
    Background automated task: Scans student attendance across all courses and dispatches warning notices to students under 75%.
    """
    students = Student.objects.all()
    dispatched_count = 0

    for student in students:
        records = AttendanceRecord.objects.filter(student=student)
        total = records.count()
        if total >= 10:
            attended = records.filter(status__in=[AttendanceStatus.PRESENT, AttendanceStatus.LATE]).count()
            pct = (attended / total) * 100.0
            if pct < 75.0:
                Notification.objects.create(
                    recipient=student.user,
                    title="⚠️ Urgent: Attendance Shortage Warning Alert",
                    message=f"Your overall course attendance is currently at {pct:.1f}%, which is below the mandatory 75% threshold. Please meet your HOD.",
                    notification_type=NotificationType.WARNING,
                )
                dispatched_count += 1

    return dispatched_count
