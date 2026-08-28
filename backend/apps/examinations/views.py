from rest_framework import viewsets, permissions, filters
from .models import Exam, ExamResult
from .serializers import ExamSerializer, ExamResultSerializer


class ExamViewSet(viewsets.ModelViewSet):
    queryset = Exam.objects.select_related('course').prefetch_related('results__student__user').all()
    serializer_class = ExamSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'course__code', 'course__title', 'venue']
    ordering_fields = ['date', 'start_time', 'max_marks']


class ExamResultViewSet(viewsets.ModelViewSet):
    queryset = ExamResult.objects.select_related('exam__course', 'student__user').all()
    serializer_class = ExamResultSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['student__student_id', 'student__user__username', 'exam__name', 'grade']
    ordering_fields = ['marks_obtained', 'grade', 'recorded_at']
