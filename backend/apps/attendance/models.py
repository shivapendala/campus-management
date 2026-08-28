from django.db import models
from apps.courses.models import Course
from apps.faculty.models import Faculty
from apps.students.models import Student


class SessionType(models.TextChoices):
    LECTURE = 'LECTURE', 'Lecture'
    LAB = 'LAB', 'Practical / Lab'
    TUTORIAL = 'TUTORIAL', 'Tutorial'
    WORKSHOP = 'WORKSHOP', 'Workshop'


class AttendanceStatus(models.TextChoices):
    PRESENT = 'PRESENT', 'Present'
    ABSENT = 'ABSENT', 'Absent'
    LATE = 'LATE', 'Late'
    EXCUSED = 'EXCUSED', 'Excused'


class AttendanceSession(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendance_sessions')
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name='conducted_sessions')
    date = models.DateField()
    session_type = models.CharField(max_length=20, choices=SessionType.choices, default=SessionType.LECTURE)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    topic_covered = models.CharField(max_length=255, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-created_at']
        verbose_name = 'Attendance Session'
        verbose_name_plural = 'Attendance Sessions'

    def __str__(self):
        return f"{self.course.code} - {self.date} ({self.get_session_type_display()})"


class AttendanceRecord(models.Model):
    session = models.ForeignKey(AttendanceSession, on_delete=models.CASCADE, related_name='records')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendance_records')
    status = models.CharField(max_length=20, choices=AttendanceStatus.choices, default=AttendanceStatus.PRESENT)
    remarks = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        unique_together = ('session', 'student')
        ordering = ['student__student_id']
        verbose_name = 'Attendance Record'
        verbose_name_plural = 'Attendance Records'

    def __str__(self):
        return f"{self.student.student_id} - {self.session.course.code} ({self.status})"
