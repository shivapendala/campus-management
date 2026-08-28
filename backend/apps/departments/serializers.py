from rest_framework import serializers
from .models import Department


class DepartmentSerializer(serializers.ModelSerializer):
    students_count = serializers.SerializerMethodField()
    faculty_count = serializers.SerializerMethodField()
    courses_count = serializers.SerializerMethodField()

    class Meta:
        model = Department
        fields = [
            'id', 'name', 'code', 'description', 'established_year',
            'head_of_department', 'building_block', 'contact_email', 'contact_phone',
            'students_count', 'faculty_count', 'courses_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_students_count(self, obj):
        return getattr(obj, 'students', []).count() if hasattr(obj, 'students') else 0

    def get_faculty_count(self, obj):
        return getattr(obj, 'faculty_members', []).count() if hasattr(obj, 'faculty_members') else 0

    def get_courses_count(self, obj):
        return getattr(obj, 'courses', []).count() if hasattr(obj, 'courses') else 0
