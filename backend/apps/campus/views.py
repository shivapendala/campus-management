from rest_framework import viewsets, permissions, filters
from .models import Department, FacultyMember, Student, Course, Enrollment
from .serializers import (
    DepartmentSerializer,
    FacultyMemberSerializer,
    StudentSerializer,
    CourseSerializer,
    EnrollmentSerializer
)


class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'code', 'description']
    ordering_fields = ['name', 'code', 'established_year']


class FacultyMemberViewSet(viewsets.ModelViewSet):
    queryset = FacultyMember.objects.select_related('user', 'department').all()
    serializer_class = FacultyMemberSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'specialization', 'office_room']
    ordering_fields = ['joining_date', 'designation']


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related('user', 'department').all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['student_id', 'user__username', 'user__first_name', 'user__last_name', 'department__name']
    ordering_fields = ['student_id', 'gpa', 'semester', 'enrollment_date']


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related('department', 'instructor__user').prefetch_related('enrollments').all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['code', 'title', 'department__name']
    ordering_fields = ['code', 'title', 'credits', 'capacity']


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.select_related('student__user', 'course').all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['student__student_id', 'student__user__username', 'course__code', 'course__title']
    ordering_fields = ['enrolled_at', 'grade', 'attendance_percentage']
