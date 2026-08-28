from rest_framework import serializers
from .models import Exam, ExamResult
from apps.courses.serializers import CourseSerializer
from apps.students.serializers import StudentSerializer
from apps.courses.models import Course
from apps.students.models import Student


class ExamSerializer(serializers.ModelSerializer):
    course_detail = CourseSerializer(source='course', read_only=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False)
    course_id = serializers.PrimaryKeyRelatedField(
        queryset=Course.objects.all(),
        source='course',
        write_only=True,
        required=False
    )
    total_students_graded = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = [
            'id', 'name', 'course', 'course_id', 'course_detail',
            'exam_type', 'date', 'start_time', 'end_time', 'semester',
            'max_internal_marks', 'max_external_marks', 'max_marks',
            'passing_marks', 'venue', 'status', 'total_students_graded',
            'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def get_total_students_graded(self, obj):
        return obj.results.count()


class ExamResultSerializer(serializers.ModelSerializer):
    exam_detail = ExamSerializer(source='exam', read_only=True)
    student_detail = StudentSerializer(source='student', read_only=True)
    exam = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all(), required=False)
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), required=False)
    exam_id = serializers.PrimaryKeyRelatedField(queryset=Exam.objects.all(), source='exam', write_only=True, required=False)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True, required=False)
    is_passed = serializers.BooleanField(read_only=True)

    class Meta:
        model = ExamResult
        fields = [
            'id', 'exam', 'exam_id', 'exam_detail',
            'student', 'student_id', 'student_detail',
            'internal_marks', 'external_marks', 'marks_obtained',
            'grade', 'grade_point', 'is_verified_by_hod', 'is_published',
            'remarks', 'is_passed', 'recorded_at'
        ]
        read_only_fields = ['id', 'recorded_at', 'is_passed']
