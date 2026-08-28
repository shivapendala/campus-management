from decimal import Decimal
from django.db import models
from django.core.validators import MinValueValidator
from apps.courses.models import Course
from apps.faculty.models import Faculty
from apps.students.models import Student


class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    faculty = models.ForeignKey(Faculty, on_delete=models.SET_NULL, null=True, blank=True, related_name='created_assignments')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, default='')
    max_score = models.DecimalField(max_digits=5, decimal_places=2, default=Decimal('100.00'))
    deadline = models.DateTimeField()
    attachment_url = models.URLField(blank=True, null=True)
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-deadline']
        verbose_name = 'Assignment'
        verbose_name_plural = 'Assignments'

    def __str__(self):
        return f"{self.title} ({self.course.code})"


class SubmissionStatus(models.TextChoices):
    SUBMITTED = 'SUBMITTED', 'Submitted'
    GRADED = 'GRADED', 'Graded'
    LATE = 'LATE', 'Late Submission'
    RESUBMITTED = 'RESUBMITTED', 'Resubmitted'


class AssignmentSubmission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='assignment_submissions')
    submission_text = models.TextField(blank=True, default='')
    submission_file_url = models.URLField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)
    score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, validators=[MinValueValidator(Decimal('0.00'))])
    feedback = models.TextField(blank=True, default='')
    status = models.CharField(max_length=20, choices=SubmissionStatus.choices, default=SubmissionStatus.SUBMITTED)

    class Meta:
        unique_together = ('assignment', 'student')
        ordering = ['-submitted_at']
        verbose_name = 'Assignment Submission'
        verbose_name_plural = 'Assignment Submissions'

    def __str__(self):
        return f"{self.student.student_id} - {self.assignment.title}"
