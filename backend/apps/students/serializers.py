from rest_framework import serializers
from .models import Student
from apps.accounts.serializers import UserSerializer
from apps.departments.serializers import DepartmentSerializer
from apps.departments.models import Department


class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    department_detail = DepartmentSerializer(source='department', read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department',
        write_only=True,
        required=False,
        allow_null=True
    )

    class Meta:
        model = Student
        fields = [
            'id', 'student_id', 'user', 'department', 'department_id', 'department_detail',
            'semester', 'gpa', 'admission_date', 'date_of_birth', 'gender', 'blood_group',
            'guardian_name', 'guardian_phone', 'guardian_email', 'emergency_contact', 'status'
        ]
