from rest_framework import serializers
from .models import AttendanceSession, AttendanceRecord
from apps.courses.serializers import CourseSerializer
from apps.faculty.serializers import FacultySerializer
from apps.students.serializers import StudentSerializer
from apps.courses.models import Course
from apps.faculty.models import Faculty
from apps.students.models import Student


class AttendanceRecordSerializer(serializers.ModelSerializer):
    student_detail = StudentSerializer(source='student', read_only=True)
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), required=False)
    student_id = serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(),
        source='student',
        write_only=True,
        required=False
    )

    class Meta:
        model = AttendanceRecord
        fields = [
            'id', 'session', 'student', 'student_id', 'student_detail',
            'status', 'remarks'
        ]


class AttendanceSessionSerializer(serializers.ModelSerializer):
    course_detail = CourseSerializer(source='course', read_only=True)
    faculty_detail = FacultySerializer(source='faculty', read_only=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course', write_only=True, required=False)
    faculty = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all(), required=False, allow_null=True)
    faculty_id = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all(), source='faculty', write_only=True, required=False, allow_null=True)
    records = AttendanceRecordSerializer(many=True, read_only=True)
    total_present = serializers.SerializerMethodField()
    total_absent = serializers.SerializerMethodField()

    class Meta:
        model = AttendanceSession
        fields = [
            'id', 'course', 'course_id', 'course_detail',
            'faculty', 'faculty_id', 'faculty_detail',
            'date', 'session_type', 'start_time', 'end_time',
            'topic_covered', 'records', 'total_present', 'total_absent', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def get_total_present(self, obj):
        return obj.records.filter(status='PRESENT').count()

    def get_total_absent(self, obj):
        return obj.records.filter(status='ABSENT').count()
