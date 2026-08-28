import pytest
from datetime import date
from django.urls import reverse
from rest_framework import status
from apps.attendance.models import AttendanceSession, AttendanceRecord, AttendanceStatus
from apps.courses.models import Course
from apps.students.models import Student


@pytest.mark.django_db
class TestAttendanceCompleteFlow:
    def test_attendance_recording_and_reports(self, auth_client, admin_user, sample_department):
        course = Course.objects.create(
            department=sample_department, code='CSE-301', title='Operating Systems', credits=4
        )
        student = Student.objects.create(
            user=admin_user, student_id='STU-ATT-001', name='Attendance Student', email='att_stu@campus.edu', department=sample_department, year=2, section='A'
        )

        session = AttendanceSession.objects.create(
            course=course, date=date.today(), topic_covered='Virtual Memory & Paging'
        )

        record = AttendanceRecord.objects.create(
            session=session, student=student, status=AttendanceStatus.PRESENT
        )
        assert record.status == AttendanceStatus.PRESENT

        url = reverse('attendance-record-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK
