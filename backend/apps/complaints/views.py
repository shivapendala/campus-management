from rest_framework import viewsets, permissions, filters
from .models import Complaint
from .serializers import ComplaintSerializer


class ComplaintViewSet(viewsets.ModelViewSet):
    queryset = Complaint.objects.select_related('submitted_by', 'assigned_to').all()
    serializer_class = ComplaintSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['ticket_id', 'title', 'description', 'submitted_by__username']
    ordering_fields = ['created_at', 'priority', 'status']

    def perform_create(self, serializer):
        serializer.save(submitted_by=self.request.user)
