from rest_framework import serializers
from .models import Course, Enrollment, TimetableEntry
from apps.departments.serializers import DepartmentSerializer
from apps.faculty.serializers import FacultySerializer
from apps.students.serializers import StudentSerializer
from apps.departments.models import Department
from apps.faculty.models import Faculty
from apps.students.models import Student


class CourseSerializer(serializers.ModelSerializer):
    department_detail = DepartmentSerializer(source='department', read_only=True)
    instructor_detail = FacultySerializer(source='instructor', read_only=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), required=False)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department',
        write_only=True,
        required=False
    )
    instructor = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all(), required=False, allow_null=True)
    instructor_id = serializers.PrimaryKeyRelatedField(
        queryset=Faculty.objects.all(),
        source='instructor',
        write_only=True,
        required=False,
        allow_null=True
    )
    enrolled_count = serializers.IntegerField(source='current_enrolled_count', read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'code', 'title', 'description', 'syllabus',
            'department', 'department_id', 'department_detail',
            'instructor', 'instructor_id', 'instructor_detail',
            'credits', 'capacity', 'enrolled_count', 'semester_offered',
            'is_elective', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class EnrollmentSerializer(serializers.ModelSerializer):
    student_detail = StudentSerializer(source='student', read_only=True)
    course_detail = CourseSerializer(source='course', read_only=True)
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), required=False)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True, required=False)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course', write_only=True, required=False)

    class Meta:
        model = Enrollment
        fields = [
            'id', 'student', 'student_id', 'student_detail',
            'course', 'course_id', 'course_detail',
            'enrolled_at', 'status', 'final_grade'
        ]
        read_only_fields = ['id', 'enrolled_at']


class TimetableEntrySerializer(serializers.ModelSerializer):
    course_detail = CourseSerializer(source='course', read_only=True)
    faculty_detail = FacultySerializer(source='faculty', read_only=True)
    department_detail = DepartmentSerializer(source='department', read_only=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False, allow_null=True)
    faculty = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all(), required=False, allow_null=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), required=False, allow_null=True)

    class Meta:
        model = TimetableEntry
        fields = [
            'id', 'day', 'start_time', 'end_time',
            'course', 'course_detail', 'title',
            'faculty', 'faculty_detail',
            'department', 'department_detail',
            'year', 'section', 'room', 'entry_type',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
