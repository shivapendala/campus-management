from rest_framework import viewsets, permissions, filters
from .models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.select_related('department', 'instructor__user').prefetch_related('enrollments').all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['code', 'title', 'department__name', 'instructor__user__first_name', 'instructor__user__last_name']
    ordering_fields = ['code', 'title', 'credits', 'capacity', 'semester_offered']


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.select_related('student__user', 'course').all()
    serializer_class = EnrollmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['student__student_id', 'student__user__username', 'course__code', 'course__title']
    ordering_fields = ['enrolled_at', 'status', 'final_grade']
