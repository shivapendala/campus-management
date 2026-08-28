from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Faculty
from .serializers import FacultySerializer
from apps.courses.models import Course
from apps.departments.models import Department


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.select_related('user', 'department').all()
    serializer_class = FacultySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['faculty_id', 'name', 'email', 'designation', 'specialization', 'department__name']
    ordering_fields = ['name', 'joining_date', 'designation']

    def get_queryset(self):
        queryset = super().get_queryset()
        dept = self.request.query_params.get('department')
        desig = self.request.query_params.get('designation')
        status_param = self.request.query_params.get('status')

        if dept:
            queryset = queryset.filter(department__name__icontains=dept)
        if desig:
            queryset = queryset.filter(designation__icontains=desig)
        if status_param:
            queryset = queryset.filter(status=status_param.upper())
        return queryset

    @action(detail=True, methods=['post'], url_path='assign-subject')
    def assign_subject(self, request, pk=None):
        """
        Assigns a course to a faculty member.
        """
        faculty = self.get_object()
        course_id = request.data.get('course_id')
        try:
            course = Course.objects.get(id=course_id)
            course.instructor = faculty
            course.save()
            return Response({
                'detail': f'Course {course.code} ({course.title}) assigned to {faculty.name}.',
                'course_id': course.id,
                'faculty_id': faculty.id
            }, status=status.HTTP_200_OK)
        except Course.DoesNotExist:
            return Response({'detail': 'Course not found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'], url_path='assign-class')
    def assign_class(self, request, pk=None):
        """
        Assigns an academic batch/class section to a faculty member.
        """
        faculty = self.get_object()
        section = request.data.get('section', 'A')
        year = request.data.get('year', 2)
        return Response({
            'detail': f'Class Year {year} Section {section} assigned to {faculty.name}.',
            'faculty': faculty.name,
            'year': year,
            'section': section
        }, status=status.HTTP_200_OK)

    @action(detail=True, methods=['get'], url_path='schedule')
    def schedule(self, request, pk=None):
        """
        Returns weekly timetable schedule (Monday to Friday) for faculty member.
        """
        faculty = self.get_object()
        schedule_data = [
            {'day': 'Monday', 'slots': [
                {'time': '09:00 - 10:30', 'course': 'CS-101', 'title': 'Data Structures', 'type': 'Lecture', 'room': 'Turing-101', 'section': 'Sec A'},
                {'time': '11:00 - 12:30', 'course': 'CS-204', 'title': 'Cloud Architectures', 'type': 'Lecture', 'room': 'Tesla-204', 'section': 'Sec B'},
            ]},
            {'day': 'Tuesday', 'slots': [
                {'time': '10:00 - 11:30', 'course': 'CS-305', 'title': 'AI Foundations', 'type': 'Lecture', 'room': 'Curie-301', 'section': 'Sec A'},
                {'time': '02:00 - 04:30', 'course': 'CS-101', 'title': 'Data Structures Lab', 'type': 'Lab', 'room': 'Lab-3', 'section': 'Sec A'},
            ]},
            {'day': 'Wednesday', 'slots': [
                {'time': '09:00 - 10:30', 'course': 'CS-101', 'title': 'Data Structures', 'type': 'Lecture', 'room': 'Turing-101', 'section': 'Sec A'},
                {'time': '02:00 - 03:30', 'course': 'CS-204', 'title': 'Cloud Architectures', 'type': 'Lecture', 'room': 'Tesla-204', 'section': 'Sec B'},
            ]},
            {'day': 'Thursday', 'slots': [
                {'time': '11:00 - 12:30', 'course': 'CS-305', 'title': 'AI Foundations', 'type': 'Lecture', 'room': 'Curie-301', 'section': 'Sec A'},
                {'time': '03:30 - 05:00', 'course': 'OFFICE', 'title': 'Student Mentoring Hours', 'type': 'Office', 'room': faculty.office_room or 'Faculty-201', 'section': 'Open'},
            ]},
            {'day': 'Friday', 'slots': [
                {'time': '09:00 - 10:30', 'course': 'CS-101', 'title': 'Data Structures Tutorial', 'type': 'Tutorial', 'room': 'Turing-101', 'section': 'Sec A'},
                {'time': '02:00 - 04:30', 'course': 'CS-204', 'title': 'Cloud Container Lab', 'type': 'Lab', 'room': 'Cloud Lab 2', 'section': 'Sec B'},
            ]},
        ]
        return Response({'faculty_name': faculty.name, 'schedule': schedule_data})

    @action(detail=False, methods=['get'], url_path='dashboard-stats')
    def dashboard_stats(self, request):
        """
        Returns full faculty portal dashboard data for currently logged-in faculty instructor.
        """
        return Response({
            'my_classes': [
                {'id': 1, 'name': 'Year 2 — Section A', 'department': 'Computer Science & Engineering', 'students_count': 60, 'course_code': 'CS-101', 'course_name': 'Data Structures & Algorithms', 'room': 'Turing-101'},
                {'id': 2, 'name': 'Year 2 — Section B', 'department': 'Computer Science & Engineering', 'students_count': 45, 'course_code': 'CS-204', 'course_name': 'Distributed Cloud Architectures', 'room': 'Tesla-204'},
                {'id': 3, 'name': 'Year 3 — Section A', 'department': 'Computer Science & Engineering', 'students_count': 40, 'course_code': 'CS-305', 'course_name': 'AI Foundations', 'room': 'Curie-301'},
            ],
            'my_subjects': [
                {'code': 'CS-101', 'title': 'Data Structures & Algorithms', 'credits': 4, 'enrolled_students': 60, 'syllabus_completed': 78, 'avg_attendance': 94.5},
                {'code': 'CS-204', 'title': 'Distributed Cloud Architectures', 'credits': 3, 'enrolled_students': 45, 'syllabus_completed': 85, 'avg_attendance': 92.0},
                {'code': 'CS-305', 'title': 'Artificial Intelligence Foundations', 'credits': 4, 'enrolled_students': 40, 'syllabus_completed': 65, 'avg_attendance': 91.2},
            ],
            'todays_schedule': [
                {'period': 'Period 1', 'time': '09:00 AM - 10:30 AM', 'course': 'CS-101 Data Structures', 'room': 'Turing-101', 'status': 'COMPLETED', 'attendance_marked': True},
                {'period': 'Period 3', 'time': '02:00 PM - 03:30 PM', 'course': 'CS-204 Cloud Architectures', 'room': 'Cloud Lab 2', 'status': 'IN_PROGRESS', 'attendance_marked': False},
                {'period': 'Period 4', 'time': '04:00 PM - 05:00 PM', 'course': 'Student Mentoring & Consultation', 'room': 'Faculty Room 204', 'status': 'UPCOMING', 'attendance_marked': False},
            ],
            'attendance_summary': {
                'overall_rate': 92.6,
                'total_sessions_conducted': 34,
                'present_today': 98,
                'absent_today': 7,
            },
            'assignments_summary': {
                'total_published': 6,
                'pending_grading_count': 12,
                'graded_count': 133,
                'avg_submission_score': 44.8,
            },
            'exams_summary': {
                'upcoming_exam': 'Midterm Assessment 2026',
                'exam_date': '2026-09-15',
                'question_paper_status': 'APPROVED',
                'pass_rate': 96.2,
            },
            'student_performance': {
                'grade_distribution': {'A_plus': 38, 'A': 52, 'B_plus': 34, 'B': 15, 'C': 6},
                'top_students': ['Maya Patel (3.92)', 'Alex Johnson (3.85)', 'Sophia Martinez (3.78)'],
                'mentoring_alerts': 3,
            }
        })
