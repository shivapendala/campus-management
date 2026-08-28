from rest_framework import viewsets, permissions, filters
from .models import Faculty
from .serializers import FacultySerializer


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.select_related('user', 'department').all()
    serializer_class = FacultySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'user__username', 'user__first_name', 'user__last_name',
        'user__email', 'faculty_id', 'designation', 'specialization', 'department__name'
    ]
    ordering_fields = ['joining_date', 'designation', 'user__last_name']
