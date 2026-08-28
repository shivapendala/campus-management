from rest_framework import serializers
from .models import Exam, ExamResult
from apps.courses.serializers import CourseSerializer
from apps.students.serializers import StudentSerializer
from apps.courses.models import Course
from apps.students.models import Student


class ExamResultSerializer(serializers.ModelSerializer):
    student_detail = StudentSerializer(source='student', read_only=True)
    student = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), required=False)
    student_id = serializers.PrimaryKeyRelatedField(queryset=Student.objects.all(), source='student', write_only=True, required=False)
    is_passed = serializers.BooleanField(read_only=True)

    class Meta:
        model = ExamResult
        fields = [
            'id', 'exam', 'student', 'student_id', 'student_detail',
            'marks_obtained', 'grade', 'remarks', 'is_passed', 'recorded_at'
        ]
        read_only_fields = ['id', 'recorded_at']


class ExamSerializer(serializers.ModelSerializer):
    course_detail = CourseSerializer(source='course', read_only=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), required=False)
    course_id = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all(), source='course', write_only=True, required=False)
    results = ExamResultSerializer(many=True, read_only=True)
    total_candidates = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = [
            'id', 'name', 'course', 'course_id', 'course_detail',
            'exam_type', 'date', 'start_time', 'end_time',
            'max_marks', 'passing_marks', 'venue', 'total_candidates', 'results', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def get_total_candidates(self, obj):
        return obj.results.count()
