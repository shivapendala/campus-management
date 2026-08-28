from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from apps.courses.models import Course
from apps.students.models import Student


class ExamType(models.TextChoices):
    MIDTERM = 'MIDTERM', 'Midterm Exam'
    FINAL = 'FINAL', 'Final Semester Exam'
    QUIZ = 'QUIZ', 'Quiz / Assessment'
    PRACTICAL = 'PRACTICAL', 'Practical Lab Exam'


class Exam(models.Model):
    name = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
    exam_type = models.CharField(max_length=20, choices=ExamType.choices, default=ExamType.MIDTERM)
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    max_marks = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('100.00'))
    passing_marks = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('40.00'))
    venue = models.CharField(max_length=100, blank=True, default='Main Examination Hall')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', 'start_time']
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'

    def __str__(self):
        return f"{self.name} - {self.course.code} ({self.date})"


class ExamResult(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='exam_results')
    marks_obtained = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    grade = models.CharField(max_length=5, blank=True, default='')
    remarks = models.CharField(max_length=255, blank=True, default='')
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('exam', 'student')
        ordering = ['-marks_obtained']
        verbose_name = 'Exam Result'
        verbose_name_plural = 'Exam Results'

    def __str__(self):
        return f"{self.student.student_id} - {self.exam.name}: {self.marks_obtained}/{self.exam.max_marks}"

    @property
    def is_passed(self):
        return self.marks_obtained >= self.exam.passing_marks
