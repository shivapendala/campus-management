from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Enrollment, TimetableEntry
from .serializers import CourseSerializer, EnrollmentSerializer, TimetableEntrySerializer
from apps.faculty.models import Faculty


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related('department', 'instructor').all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['code', 'title', 'department__name', 'instructor__name']
    ordering_fields = ['code', 'semester_offered', 'credits']

    def get_queryset(self):
        queryset = super().get_queryset()
        dept = self.request.query_params.get('department')
        sem = self.request.query_params.get('semester')

        if dept:
            queryset = queryset.filter(department__code__iexact=dept) | queryset.filter(department__name__icontains=dept)
        if sem:
            queryset = queryset.filter(semester_offered=sem)
        return queryset

    @action(detail=True, methods=['post'], url_path='assign-instructor')
    def assign_instructor(self, request, pk=None):
        """
        Assigns or re-assigns an instructor to a course.
        """
        course = self.get_object()
        faculty_id = request.data.get('faculty_id')
        if not faculty_id:
            return Response({'detail': 'faculty_id is required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            faculty = Faculty.objects.get(id=faculty_id)
            course.instructor = faculty
            course.save()
            return Response({
                'detail': f'{faculty.name} successfully assigned as lead instructor for {course.code} ({course.title}).',
                'course_code': course.code,
                'instructor_name': faculty.name,
                'faculty_id': faculty.id,
            }, status=status.HTTP_200_OK)
        except Faculty.DoesNotExist:
            return Response({'detail': 'Faculty member not found.'}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['get'], url_path='syllabus')
    def syllabus(self, request, pk=None):
        """
        Returns structured 5-unit syllabus curriculum, learning objectives, and recommended textbooks.
        """
        course = self.get_object()
        
        # Benchmark syllabus generator for courses
        units = [
            {
                'unit_number': 1,
                'title': f'Introduction to {course.title} & Fundamentals',
                'lecture_hours': 9,
                'topics': ['Core definitions and theoretical framework', 'Asymptotic analysis and mathematical foundations', 'Standard paradigms and architecture'],
            },
            {
                'unit_number': 2,
                'title': 'Core Data Models, Mechanisms & Algorithms',
                'lecture_hours': 10,
                'topics': ['Structural representations and design patterns', 'State transitions and operational mechanics', 'Algorithmic efficiency and constraints'],
            },
            {
                'unit_number': 3,
                'title': 'Advanced System Architectures & Optimization',
                'lecture_hours': 10,
                'topics': ['Concurrency, synchronization, and resource management', 'Performance profiling and bottlenecks', 'Distributed and scalable considerations'],
            },
            {
                'unit_number': 4,
                'title': 'Security, Reliability & Industry Implementation',
                'lecture_hours': 8,
                'topics': ['Robustness, error handling, and fault tolerance', 'Security protocols and validation checks', 'Modern production case studies'],
            },
            {
                'unit_number': 5,
                'title': 'Applied Practical Labs & Capstone Projects',
                'lecture_hours': 8,
                'topics': ['End-to-end laboratory implementation', 'Benchmarking and testing suites', 'Future directions and emerging research'],
            },
        ]

        textbooks = [
            {'title': f'Standard Principles of {course.title}', 'authors': 'Cormen, Leiserson, Rivest, Stein', 'edition': '4th Edition, MIT Press'},
            {'title': f'Applied Modern {course.title} Engineering', 'authors': 'Silberschatz, Galvin, Gagne', 'edition': '10th Edition, Wiley'},
        ]

        return Response({
            'course_code': course.code,
            'title': course.title,
            'credits': course.credits,
            'semester': getattr(course, 'semester_offered', 1),
            'department': course.department.name if course.department else 'General Engineering',
            'instructor': course.instructor.name if course.instructor else 'Not Assigned',
            'units': units,
            'recommended_textbooks': textbooks,
            'prerequisites': 'Foundational Mathematics & Programming',
        })


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.select_related('student', 'course').all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['student__name', 'course__code', 'course__title']


class TimetableEntryViewSet(viewsets.ModelViewSet):
    queryset = TimetableEntry.objects.select_related('course', 'faculty', 'department').all()
    serializer_class = TimetableEntrySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'room', 'section', 'day', 'course__code', 'faculty__name']
    ordering_fields = ['day', 'start_time']

    def get_queryset(self):
        queryset = super().get_queryset()
        day = self.request.query_params.get('day')
        faculty_id = self.request.query_params.get('faculty_id')
        room = self.request.query_params.get('room')
        year = self.request.query_params.get('year')
        section = self.request.query_params.get('section')

        if day:
            queryset = queryset.filter(day=day)
        if faculty_id:
            queryset = queryset.filter(faculty_id=faculty_id)
        if room:
            queryset = queryset.filter(room__iexact=room)
        if year:
            queryset = queryset.filter(year=year)
        if section:
            queryset = queryset.filter(section=section)
        return queryset

    @action(detail=False, methods=['post'], url_path='check-conflicts')
    def check_conflicts(self, request):
        """
        Validates whether a proposed slot has Room, Faculty, or Section conflicts.
        """
        day = request.data.get('day')
        start_time = request.data.get('start_time')
        end_time = request.data.get('end_time')
        room = request.data.get('room')
        faculty_id = request.data.get('faculty_id')
        year = request.data.get('year')
        section = request.data.get('section')
        exclude_id = request.data.get('exclude_id')

        conflicts = []

        # 1. Room collision
        if room and day and start_time:
            room_clash = TimetableEntry.objects.filter(day=day, room__iexact=room, start_time=start_time)
            if exclude_id:
                room_clash = room_clash.exclude(id=exclude_id)
            if room_clash.exists():
                c = room_clash.first()
                conflicts.append({
                    'type': 'ROOM_CONFLICT',
                    'message': f'Room "{room}" is already occupied on {day} at {start_time} by {c.title} ({c.section}).',
                })

        # 2. Faculty double-booking
        if faculty_id and day and start_time:
            fac_clash = TimetableEntry.objects.filter(day=day, faculty_id=faculty_id, start_time=start_time)
            if exclude_id:
                fac_clash = fac_clash.exclude(id=exclude_id)
            if fac_clash.exists():
                c = fac_clash.first()
                conflicts.append({
                    'type': 'FACULTY_CONFLICT',
                    'message': f'Faculty member is already scheduled to teach {c.title} ({c.room}) on {day} at {start_time}.',
                })

        # 3. Section collision
        if year and section and day and start_time:
            sec_clash = TimetableEntry.objects.filter(day=day, year=year, section=section, start_time=start_time)
            if exclude_id:
                sec_clash = sec_clash.exclude(id=exclude_id)
            if sec_clash.exists():
                c = sec_clash.first()
                conflicts.append({
                    'type': 'SECTION_CONFLICT',
                    'message': f'Year {year} Section {section} already has a scheduled slot: {c.title} ({c.room}).',
                })

        has_conflicts = len(conflicts) > 0
        return Response({
            'has_conflicts': has_conflicts,
            'conflicts_count': len(conflicts),
            'conflicts': conflicts,
        }, status=status.HTTP_200_OK)
