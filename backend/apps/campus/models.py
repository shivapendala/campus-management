from decimal import Decimal
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Department(models.Model):
    name = models.CharField(max_length=120, unique=True)
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=True, default='')
    established_year = models.PositiveIntegerField(default=2000)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.code} - {self.name}"


class FacultyMember(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='faculty_profile'
    )
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='faculty_members'
    )
    designation = models.CharField(max_length=100, default='Assistant Professor')
    office_room = models.CharField(max_length=50, blank=True, default='')
    specialization = models.CharField(max_length=150, blank=True, default='')
    joining_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['user__last_name', 'user__first_name']

    def __str__(self):
        return f"Prof. {self.user.get_full_name() or self.user.username} ({self.designation})"


class Student(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )
    student_id = models.CharField(max_length=20, unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='students'
    )
    semester = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(12)])
    gpa = models.DecimalField(
        max_digits=4,
        decimal_places=2,
        default=3.50,
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('4.00'))]
    )
    enrollment_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ['student_id']

    def __str__(self):
        return f"{self.student_id} - {self.user.get_full_name() or self.user.username}"


class Course(models.Model):
    code = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, default='')
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    instructor = models.ForeignKey(
        FacultyMember,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='taught_courses'
    )
    credits = models.PositiveIntegerField(default=3, validators=[MinValueValidator(1), MaxValueValidator(10)])
    capacity = models.PositiveIntegerField(default=40)
    semester_offered = models.CharField(max_length=20, default='Fall 2026')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return f"{self.code}: {self.title}"

    @property
    def current_enrolled_count(self):
        return self.enrollments.count()


class Enrollment(models.Model):
    class GradeChoices(models.TextChoices):
        A_PLUS = 'A+', 'A+'
        A = 'A', 'A'
        B_PLUS = 'B+', 'B+'
        B = 'B', 'B'
        C = 'C', 'C'
        D = 'D', 'D'
        F = 'F', 'F'
        IN_PROGRESS = 'IP', 'In Progress'

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrolled_at = models.DateTimeField(auto_now_add=True)
    grade = models.CharField(max_length=5, choices=GradeChoices.choices, default=GradeChoices.IN_PROGRESS)
    attendance_percentage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=85.00,
        validators=[MinValueValidator(Decimal('0.00')), MaxValueValidator(Decimal('100.00'))]
    )

    class Meta:
        unique_together = ('student', 'course')
        ordering = ['-enrolled_at']

    def __str__(self):
        return f"{self.student.student_id} in {self.course.code}"
