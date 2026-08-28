from rest_framework import viewsets, permissions, filters
from .models import Company, PlacementDrive, JobApplication
from .serializers import CompanySerializer, PlacementDriveSerializer, JobApplicationSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'industry', 'contact_person']
    ordering_fields = ['name', 'created_at']


class PlacementDriveViewSet(viewsets.ModelViewSet):
    queryset = PlacementDrive.objects.select_related('company').prefetch_related('applications').all()
    serializer_class = PlacementDriveSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'job_role', 'company__name', 'location']
    ordering_fields = ['package_lpa', 'drive_date', 'status']


class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.select_related('drive__company', 'student__user').all()
    serializer_class = JobApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['student__student_id', 'student__user__username', 'drive__company__name', 'drive__job_role']
    ordering_fields = ['applied_at', 'status']
