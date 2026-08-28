from rest_framework import serializers
from .models import FeeCategory, FeeStructure, FeePayment
from apps.departments.serializers import DepartmentSerializer
from apps.students.serializers import StudentSerializer
from apps.departments.models import Department
from apps.students.models import Student


class FeeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = FeeCategory
        fields = ['id', 'name', 'description']


class FeeStructureSerializer(serializers.ModelSerializer):
    department_detail = DepartmentSerializer(source='department', read_only=True)
    category_detail = FeeCategorySerializer(source='category', read_only=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), required=False)
    category = serializers.PrimaryKeyRelatedField(queryset=FeeCategory.objects.all(), required=False)
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), source='department', write_only=True, required=False)
    category_id = serializers.PrimaryKeyRelatedField(queryset=FeeCategory.objects.all(), source='category', write_only=True, required=False)

    class Meta:
        model = FeeStructure
        fields = [
            'id', 'title', 'category', 'category_id', 'category_detail',
            'department', 'department_id', 'department_detail',
            'semester', 'academic_year', 'amount', 'due_date', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']


class FeePaymentSerializer(serializers.ModelSerializer):
    student_detail = StudentSerializer(source='student', read_only=True)
    fee_structure_detail = FeeStructureSerializer(source='fee_structure', read_only=True)
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), required=False)
    fee_structure = serializers.PrimaryKeyRelatedField(queryset=FeeStructure.objects.all(), required=False)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True, required=False)
    fee_structure_id = serializers.PrimaryKeyRelatedField(queryset=FeeStructure.objects.all(), source='fee_structure', write_only=True, required=False)

    class Meta:
        model = FeePayment
        fields = [
            'id', 'invoice_number', 'student', 'student_id', 'student_detail',
            'fee_structure', 'fee_structure_id', 'fee_structure_detail',
            'amount_paid', 'payment_method', 'transaction_id', 'status',
            'payment_date', 'remarks'
        ]
        read_only_fields = ['id', 'invoice_number', 'payment_date']
