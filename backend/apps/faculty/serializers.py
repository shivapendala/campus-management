from rest_framework import serializers
from .models import Faculty
from apps.accounts.serializers import UserSerializer
from apps.departments.serializers import DepartmentSerializer
from apps.departments.models import Department


class FacultySerializer(serializers.ModelSerializer):
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
        model = Faculty
        fields = [
            'id', 'user', 'faculty_id', 'department', 'department_id', 'department_detail',
            'designation', 'qualification', 'specialization', 'office_room',
            'office_hours', 'joining_date', 'is_active'
        ]
