from datetime import date, timedelta
from decimal import Decimal
import pytest
from django.urls import reverse
from rest_framework import status
from apps.departments.models import Department
from apps.faculty.models import Faculty
from apps.students.models import Student
from apps.courses.models import Course, Enrollment
from apps.attendance.models import AttendanceSession, AttendanceRecord
from apps.examinations.models import Exam, ExamResult
from apps.fees.models import FeeCategory, FeeStructure, FeePayment
from apps.assignments.models import Assignment, AssignmentSubmission
from apps.library.models import Book, BookIssue
from apps.placements.models import Company, PlacementDrive, JobApplication
from apps.complaints.models import Complaint
from apps.events.models import Event, EventRegistration
from apps.notifications.models import Notification


@pytest.mark.django_db
class TestAll15Modules:
    def test_department_endpoints(self, auth_client):
        url = reverse('department-list')
        payload = {'name': 'Civil Engineering', 'code': 'CE', 'established_year': 2005}
        res = auth_client.post(url, payload, format='json')
        assert res.status_code == status.HTTP_201_CREATED
        list_res = auth_client.get(url)
        assert list_res.status_code == status.HTTP_200_OK

    def test_faculty_endpoints(self, auth_client, admin_user, sample_department):
        faculty = Faculty.objects.create(user=admin_user, department=sample_department, faculty_id='FAC-TEST-01', designation='Professor')
        url = reverse('faculty-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK
        assert res.data['count'] >= 1

    def test_students_endpoints(self, auth_client, student_user, sample_department):
        Student.objects.create(user=student_user, department=sample_department, student_id='STU-TEST-01', semester=2, gpa=Decimal('3.80'))
        url = reverse('student-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK
        assert res.data['count'] >= 1

    def test_courses_endpoints(self, auth_client, sample_department):
        url = reverse('course-list')
        payload = {'code': 'CS-301', 'title': 'Algorithms', 'department_id': sample_department.id, 'credits': 4}
        res = auth_client.post(url, payload, format='json')
        assert res.status_code == status.HTTP_201_CREATED

    def test_attendance_endpoints(self, auth_client, sample_department):
        course = Course.objects.create(code='CS-ATT', title='Test Attendance', department=sample_department)
        url = reverse('attendance-session-list')
        payload = {'course_id': course.id, 'date': str(date.today()), 'topic_covered': 'Test Topic'}
        res = auth_client.post(url, payload, format='json')
        assert res.status_code == status.HTTP_201_CREATED

    def test_examinations_endpoints(self, auth_client, sample_department):
        course = Course.objects.create(code='CS-EXM', title='Exam Test', department=sample_department)
        url = reverse('exam-list')
        payload = {'name': 'Midterm 2026', 'course_id': course.id, 'date': str(date.today() + timedelta(days=5)), 'max_marks': '100.00', 'passing_marks': '40.00'}
        res = auth_client.post(url, payload, format='json')
        assert res.status_code == status.HTTP_201_CREATED

    def test_fees_endpoints(self, auth_client, sample_department):
        cat = FeeCategory.objects.create(name='Tuition')
        url = reverse('fee-structure-list')
        payload = {'title': 'Fall Fee', 'category_id': cat.id, 'department_id': sample_department.id, 'semester': 1, 'amount': '2500.00', 'due_date': str(date.today())}
        res = auth_client.post(url, payload, format='json')
        assert res.status_code == status.HTTP_201_CREATED

    def test_assignments_endpoints(self, auth_client, sample_department):
        course = Course.objects.create(code='CS-ASN', title='Assignment Test', department=sample_department)
        url = reverse('assignment-list')
        payload = {'title': 'Homework 1', 'course_id': course.id, 'deadline': '2026-12-31T23:59:59Z', 'max_score': '50.00'}
        res = auth_client.post(url, payload, format='json')
        assert res.status_code == status.HTTP_201_CREATED

    def test_library_endpoints(self, auth_client):
        url = reverse('book-list')
        payload = {'title': 'Clean Code', 'author': 'Robert C. Martin', 'isbn': '978-0132350884', 'total_copies': 5, 'available_copies': 5}
        res = auth_client.post(url, payload, format='json')
        assert res.status_code == status.HTTP_201_CREATED

    def test_placements_endpoints(self, auth_client):
        url = reverse('placement-company-list')
        payload = {'name': 'Microsoft', 'industry': 'Tech', 'website': 'https://microsoft.com'}
        res = auth_client.post(url, payload, format='json')
        assert res.status_code == status.HTTP_201_CREATED

    def test_complaints_endpoints(self, auth_client):
        url = reverse('complaint-list')
        payload = {'title': 'Projector issue', 'description': 'Projector in hall 2 not turning on.', 'category': 'INFRASTRUCTURE', 'priority': 'HIGH'}
        res = auth_client.post(url, payload, format='json')
        assert res.status_code == status.HTTP_201_CREATED

    def test_events_endpoints(self, auth_client):
        url = reverse('event-list')
        payload = {'title': 'Tech Fest 2026', 'start_time': '2026-10-01T09:00:00Z', 'end_time': '2026-10-03T18:00:00Z', 'capacity': 500}
        res = auth_client.post(url, payload, format='json')
        assert res.status_code == status.HTTP_201_CREATED

    def test_notifications_endpoints(self, auth_client, admin_user):
        Notification.objects.create(recipient=admin_user, title='System Update', message='System maintenance scheduled.')
        url = reverse('notification-list')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK
        assert res.data['count'] >= 1

    def test_reports_endpoints(self, auth_client):
        url = reverse('reports-overview')
        res = auth_client.get(url)
        assert res.status_code == status.HTTP_200_OK
        assert 'total_students' in res.data
        assert 'total_fee_collected' in res.data
