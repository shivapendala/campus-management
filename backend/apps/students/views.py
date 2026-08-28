from rest_framework import viewsets, permissions, filters
from .models import Student
from .serializers import StudentSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.select_related('user', 'department').all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'student_id', 'user__username', 'user__first_name', 'user__last_name',
        'user__email', 'department__name', 'guardian_name'
    ]
    ordering_fields = ['student_id', 'gpa', 'semester', 'admission_date']
