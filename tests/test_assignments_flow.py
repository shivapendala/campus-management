import pytest
from datetime import timedelta
from decimal import Decimal
from django.utils import timezone
from django.urls import reverse
from rest_framework import status
from apps.assignments.models import Assignment, AssignmentSubmission, SubmissionStatus
from apps.courses.models import Course
from apps.students.models import Student


@pytest.mark.django_db
class TestAssignmentsCompleteFlow:
    def test_assignment_lifecycle(self, auth_client, admin_user, sample_department):
        course = Course.objects.create(
            department=sample_department, code='CSE-401', title='Machine Learning', credits=4
        )
        student = Student.objects.create(
            user=admin_user, student_id='STU-ASSIGN-001', name='Assignment Student', email='assign_stu@campus.edu', department=sample_department, year=3, section='A'
        )

        assignment = Assignment.objects.create(
            course=course,
            title='Lab 1: Convolutional Neural Network on CT scans',
            description='Build and evaluate a CNN classifier.',
            max_score=Decimal('50.00'),
            deadline=timezone.now() + timedelta(days=7),
        )
        assert assignment.max_score == Decimal('50.00')

        submission = AssignmentSubmission.objects.create(
            assignment=assignment,
            student=student,
            submission_text='Implemented CNN with 98% accuracy.',
            score=Decimal('48.50'),
            feedback='Outstanding results and clean documentation.',
            status=SubmissionStatus.GRADED,
        )
        assert submission.status == SubmissionStatus.GRADED

        url = reverse('assignment-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK
