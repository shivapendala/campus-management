from rest_framework import serializers
from .models import Faculty
from apps.accounts.serializers import UserSerializer
from apps.departments.serializers import DepartmentSerializer
from apps.departments.models import Department


class FacultySerializer(serializers.ModelSerializer):
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
        model = Faculty
        fields = [
            'id', 'faculty_id', 'name', 'email', 'phone',
            'department', 'department_id', 'department_detail',
            'designation', 'qualification', 'specialization',
            'office_room', 'joining_date', 'status', 'user', 'user_detail'
        ]
        read_only_fields = ['id', 'joining_date']
