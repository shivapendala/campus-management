from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from django.db.models import Count, Avg, Sum
from apps.departments.models import Department
from apps.faculty.models import Faculty
from apps.students.models import Student
from apps.courses.models import Course, Enrollment
from apps.fees.models import FeePayment
from apps.library.models import Book, BookIssue
from apps.placements.models import PlacementDrive, JobApplication
from apps.complaints.models import Complaint
from apps.events.models import Event


class OverviewSummaryReportView(APIView):
    """
    Returns overarching institutional indicators across all 15 modules.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        total_students = Student.objects.count()
        total_faculty = Faculty.objects.count()
        total_departments = Department.objects.count()
        total_courses = Course.objects.count()
        total_books = Book.objects.aggregate(total=Sum('total_copies'))['total'] or 0
        total_fee_collected = FeePayment.objects.filter(status='SUCCESS').aggregate(total=Sum('amount_paid'))['total'] or 0.0
        open_complaints = Complaint.objects.filter(status__in=['OPEN', 'UNDER_REVIEW']).count()
        upcoming_events = Event.objects.count()
        active_placement_drives = PlacementDrive.objects.filter(status__in=['UPCOMING', 'ONGOING']).count()

        avg_gpa = Student.objects.aggregate(avg=Avg('gpa'))['avg'] or 0.0

        return Response({
            'total_students': total_students,
            'total_faculty': total_faculty,
            'total_departments': total_departments,
            'total_courses': total_courses,
            'total_books_in_library': total_books,
            'total_fee_collected': float(total_fee_collected),
            'open_complaints_count': open_complaints,
            'upcoming_events_count': upcoming_events,
            'active_placement_drives': active_placement_drives,
            'average_student_gpa': round(float(avg_gpa), 2),
            'academic_term': 'Fall 2026'
        })


class DepartmentMetricsReportView(APIView):
    """
    Returns student and faculty breakdown per department.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        depts = Department.objects.all()
        data = []
        for d in depts:
            data.append({
                'id': d.id,
                'code': d.code,
                'name': d.name,
                'students_count': d.students.count(),
                'faculty_count': d.faculty_members.count(),
                'courses_count': d.courses.count(),
            })
        return Response(data)


class FinancialSummaryReportView(APIView):
    """
    Returns financial fee collection metrics.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        total_collected = FeePayment.objects.filter(status='SUCCESS').aggregate(total=Sum('amount_paid'))['total'] or 0.0
        pending_payments = FeePayment.objects.filter(status='PENDING').count()
        failed_payments = FeePayment.objects.filter(status='FAILED').count()

        return Response({
            'total_collected': float(total_collected),
            'pending_verifications': pending_payments,
            'failed_transactions': failed_payments,
            'currency': 'USD'
        })


class PlacementStatsReportView(APIView):
    """
    Returns placement drive & job offer statistics.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        total_drives = PlacementDrive.objects.count()
        total_applications = JobApplication.objects.count()
        total_offers = JobApplication.objects.filter(status__in=['OFFERED', 'ACCEPTED']).count()
        avg_package = PlacementDrive.objects.aggregate(avg=Avg('package_lpa'))['avg'] or 0.0

        return Response({
            'total_drives': total_drives,
            'total_applications': total_applications,
            'total_offers_extended': total_offers,
            'average_package_lpa': round(float(avg_package), 2)
        })
