from rest_framework import serializers
from .models import Assignment, AssignmentSubmission
from apps.courses.serializers import CourseSerializer
from apps.faculty.serializers import FacultySerializer
from apps.students.serializers import StudentSerializer
from apps.courses.models import Course
from apps.faculty.models import Faculty
from apps.students.models import Student


class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    student_detail = StudentSerializer(source='student', read_only=True)
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), required=False)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True, required=False)

    class Meta:
        model = AssignmentSubmission
        fields = [
            'id', 'assignment', 'student', 'student_id', 'student_detail',
            'submission_text', 'submission_file_url', 'submitted_at',
            'score', 'feedback', 'status'
        ]
        read_only_fields = ['id', 'submitted_at']


class AssignmentSerializer(serializers.ModelSerializer):
    course_detail = CourseSerializer(source='course', read_only=True)
    faculty_detail = FacultySerializer(source='faculty', read_only=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course', write_only=True, required=False)
    faculty = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all(), required=False, allow_null=True)
    faculty_id = serializers.PrimaryKeyRelatedField(queryset=Faculty.objects.all(), source='faculty', write_only=True, required=False, allow_null=True)
    submissions_count = serializers.SerializerMethodField()

    class Meta:
        model = Assignment
        fields = [
            'id', 'title', 'course', 'course_id', 'course_detail',
            'faculty', 'faculty_id', 'faculty_detail',
            'description', 'max_score', 'deadline', 'attachment_url',
            'is_published', 'submissions_count', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']

    def get_submissions_count(self, obj):
        return obj.submissions.count()
