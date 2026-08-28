from rest_framework import viewsets, permissions, filters
from .models import FeeCategory, FeeStructure, FeePayment
from .serializers import FeeCategorySerializer, FeeStructureSerializer, FeePaymentSerializer


class FeeCategoryViewSet(viewsets.ModelViewSet):
    queryset = FeeCategory.objects.all()
    serializer_class = FeeCategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description']


class FeeStructureViewSet(viewsets.ModelViewSet):
    queryset = FeeStructure.objects.select_related('category', 'department').all()
    serializer_class = FeeStructureSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'department__name', 'academic_year']
    ordering_fields = ['amount', 'due_date', 'semester']


class FeePaymentViewSet(viewsets.ModelViewSet):
    queryset = FeePayment.objects.select_related('student__user', 'fee_structure__category').all()
    serializer_class = FeePaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['invoice_number', 'student__student_id', 'student__user__username', 'transaction_id']
    ordering_fields = ['amount_paid', 'payment_date', 'status']
