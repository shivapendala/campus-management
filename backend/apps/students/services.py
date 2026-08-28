import csv
import io
from decimal import Decimal
from typing import List, Dict, Any, Tuple
from django.db import transaction
from django.core.exceptions import ValidationError
from .models import Student, StudentDocument, AcademicHistory
from apps.departments.models import Department
from apps.accounts.models import User


class StudentDossierService:
    """
    Service responsible for Student 360 dossiers, academic records, and batch CSV imports.
    """

    @classmethod
    def generate_next_student_id(cls, department_code: str, year: int) -> str:
        """
        Generates standard institutional student ID: e.g. CSE-2026-042
        """
        total = Student.objects.filter(department__code=department_code).count() + 1
        return f"{department_code}-{year}-{total:03d}"

    @classmethod
    def calculate_cumulative_gpa(cls, student: Student) -> Decimal:
        """
        Calculates cumulative GPA across all historical semesters.
        """
        histories = student.academic_histories.all()
        if not histories.exists():
            return Decimal('0.00')
        total_gpa = sum(h.gpa for h in histories)
        return Decimal(total_gpa / histories.count()).quantize(Decimal('0.01'))

    @classmethod
    @transaction.atomic
    def process_csv_import(cls, csv_file_content: str) -> Tuple[int, List[str]]:
        """
        Parses CSV batch file and creates Student records.
        """
        imported_count = 0
        errors = []
        reader = csv.DictReader(io.StringIO(csv_file_content))

        for row_idx, row in enumerate(reader, start=1):
            try:
                dept_code = row.get('Department', 'CSE').strip()
                dept = Department.objects.filter(code=dept_code).first()
                if not dept:
                    dept = Department.objects.first()

                username = row.get('Username') or f"stu_{row_idx}_{dept_code.lower()}"
                email = row.get('Email') or f"{username}@campus.edu"

                user, _ = User.objects.get_or_create(
                    username=username,
                    defaults={'email': email, 'role': 'STUDENT'}
                )

                Student.objects.create(
                    user=user,
                    name=row.get('Name', 'Enrolled Student'),
                    student_id=row.get('StudentID') or cls.generate_next_student_id(dept_code, 2026),
                    department=dept,
                    year=int(row.get('Year', 1)),
                    section=row.get('Section', 'A'),
                    phone=row.get('Phone', '+1 555-0100'),
                )
                imported_count += 1
            except Exception as e:
                errors.append(f"Row {row_idx}: {str(e)}")

        return imported_count, errors
