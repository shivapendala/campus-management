from rest_framework import serializers
from .models import Department, FacultyMember, Student, Course, Enrollment
from apps.authentication.serializers import UserSerializer


class DepartmentSerializer(serializers.ModelSerializer):
    courses_count = serializers.IntegerField(source='courses.count', read_only=True)
    students_count = serializers.IntegerField(source='students.count', read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'code', 'description', 'established_year', 'courses_count', 'students_count', 'created_at']


class FacultyMemberSerializer(serializers.ModelSerializer):
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
        model = FacultyMember
        fields = [
            'id', 'user', 'department', 'department_id', 'department_detail',
            'designation', 'office_room', 'specialization', 'joining_date'
        ]


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
            'id', 'student_id', 'user', 'department', 'department_id',
            'department_detail', 'semester', 'gpa', 'enrollment_date'
        ]


class CourseSerializer(serializers.ModelSerializer):
    department_detail = DepartmentSerializer(source='department', read_only=True)
    instructor_detail = FacultyMemberSerializer(source='instructor', read_only=True)
    enrolled_count = serializers.IntegerField(source='current_enrolled_count', read_only=True)

    class Meta:
        model = Course
        fields = [
            'id', 'code', 'title', 'description', 'department', 'department_detail',
            'instructor', 'instructor_detail', 'credits', 'capacity', 'enrolled_count',
            'semester_offered', 'created_at'
        ]


class EnrollmentSerializer(serializers.ModelSerializer):
    student_detail = StudentSerializer(source='student', read_only=True)
    course_detail = CourseSerializer(source='course', read_only=True)

    class Meta:
        model = Enrollment
        fields = [
            'id', 'student', 'student_detail', 'course', 'course_detail',
            'enrolled_at', 'grade', 'attendance_percentage'
        ]
