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


class ExamStatus(models.TextChoices):
    SCHEDULED = 'SCHEDULED', 'Scheduled'
    GRADING = 'GRADING', 'Grading in Progress'
    UNDER_REVIEW = 'UNDER_REVIEW', 'Under HOD Review'
    PUBLISHED = 'PUBLISHED', 'Published / Results Declared'


class Exam(models.Model):
    name = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
    exam_type = models.CharField(max_length=20, choices=ExamType.choices, default=ExamType.MIDTERM)
    date = models.DateField()
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    semester = models.CharField(max_length=30, default='Fall 2026')
    max_internal_marks = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('40.00'))
    max_external_marks = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('60.00'))
    max_marks = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('100.00'))
    passing_marks = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('40.00'))
    venue = models.CharField(max_length=100, blank=True, default='Main Examination Hall')
    status = models.CharField(max_length=25, choices=ExamStatus.choices, default=ExamStatus.SCHEDULED)
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
    internal_marks = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    external_marks = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    marks_obtained = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=Decimal('0.00'),
        validators=[MinValueValidator(Decimal('0.00'))]
    )
    grade = models.CharField(max_length=5, blank=True, default='F')
    grade_point = models.DecimalField(max_digits=4, decimal_places=2, default=Decimal('0.00'))
    is_verified_by_hod = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    remarks = models.CharField(max_length=255, blank=True, default='')
    recorded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('exam', 'student')
        ordering = ['-marks_obtained']
        verbose_name = 'Exam Result'
        verbose_name_plural = 'Exam Results'

    def __str__(self):
        return f"{self.student.student_id} - {self.exam.name}: {self.marks_obtained}/{self.exam.max_marks} ({self.grade})"

    @property
    def is_passed(self):
        return self.marks_obtained >= self.exam.passing_marks
