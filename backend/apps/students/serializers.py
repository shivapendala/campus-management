from rest_framework import serializers
from .models import Student
from apps.accounts.serializers import UserSerializer
from apps.departments.serializers import DepartmentSerializer
from apps.departments.models import Department


class StudentSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source='user', read_only=True)
    department_detail = DepartmentSerializer(source='department', read_only=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), required=False, allow_null=True)
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
            'id', 'student_id', 'name', 'email', 'phone',
            'department', 'department_id', 'department_detail',
            'year', 'section', 'semester', 'admission_date', 'status',
            'gpa', 'date_of_birth', 'gender', 'guardian_name', 'guardian_phone',
            'user', 'user_detail'
        ]
        read_only_fields = ['id', 'admission_date']
