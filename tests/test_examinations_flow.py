import pytest
from datetime import date
from decimal import Decimal
from django.urls import reverse
from rest_framework import status
from apps.examinations.models import Exam, ExamResult, ExamType
from apps.courses.models import Course
from apps.students.models import Student


@pytest.mark.django_db
class TestExaminationsCompleteFlow:
    def test_exam_scheduling_and_marks_entry(self, auth_client, admin_user, sample_department):
        course = Course.objects.create(
            department=sample_department, code='CSE-302', title='Computer Networks', credits=4
        )
        student = Student.objects.create(
            user=admin_user, student_id='STU-EXAM-001', name='Exam Candidate', email='exam_stu@campus.edu', department=sample_department, year=2, section='A'
        )

        exam = Exam.objects.create(
            name='Fall 2026 Mid-Terms - Computer Networks',
            course=course,
            exam_type=ExamType.MIDTERM,
            date=date.today(),
            max_internal_marks=Decimal('30.00'),
            max_external_marks=Decimal('70.00'),
            max_marks=Decimal('100.00'),
        )
        assert exam.max_marks == Decimal('100.00')

        result = ExamResult.objects.create(
            exam=exam,
            student=student,
            internal_marks=Decimal('28.50'),
            external_marks=Decimal('66.50'),
            marks_obtained=Decimal('95.00'),
            grade='A+',
            grade_point=Decimal('10.0'),
            is_verified_by_hod=True,
        )
        assert result.grade == 'A+'

        url = reverse('exam-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK
