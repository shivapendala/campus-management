from decimal import Decimal
from typing import Tuple, Dict, Any, List
from .models import Exam, ExamResult, ExamStatus


class ExaminationGradingService:
    """
    Standard 10-Point Institutional Grading & SGPA Calculation Engine.
    Converts composite marks into academic grades and grade points.
    """

    GRADE_SCALE = [
        (Decimal('90.0'), 'A+', Decimal('10.0'), 'Outstanding'),
        (Decimal('80.0'), 'A', Decimal('9.0'), 'Excellent'),
        (Decimal('70.0'), 'B+', Decimal('8.0'), 'Very Good'),
        (Decimal('60.0'), 'B', Decimal('7.0'), 'Good'),
        (Decimal('50.0'), 'C', Decimal('6.0'), 'Average'),
        (Decimal('40.0'), 'P', Decimal('4.0'), 'Pass'),
        (Decimal('0.0'), 'F', Decimal('0.0'), 'Fail'),
    ]

    @classmethod
    def calculate_grade_and_points(cls, total_marks: Decimal, max_marks: Decimal) -> Tuple[str, Decimal, str]:
        """
        Calculates letter grade, grade point, and descriptor.
        """
        if max_marks <= Decimal('0.0'):
            return 'F', Decimal('0.0'), 'Fail'

        pct = (total_marks / max_marks) * Decimal('100.0')
        for threshold, letter_grade, grade_point, description in cls.GRADE_SCALE:
            if pct >= threshold:
                return letter_grade, grade_point, description
        return 'F', Decimal('0.0'), 'Fail'

    @classmethod
    def calculate_semester_sgpa(cls, results: List[ExamResult]) -> Decimal:
        """
        Calculates Semester Grade Point Average (SGPA) based on credits and grade points:
        SGPA = Sum(Credits * GradePoint) / Sum(Credits)
        """
        if not results:
            return Decimal('0.00')

        total_credit_points = Decimal('0.0')
        total_credits = Decimal('0.0')

        for r in results:
            credits = Decimal(str(r.exam.course.credits if r.exam.course else 4))
            gp = r.grade_point if r.grade_point is not None else Decimal('0.0')
            total_credit_points += credits * gp
            total_credits += credits

        if total_credits == Decimal('0.0'):
            return Decimal('0.00')

        return (total_credit_points / total_credits).quantize(Decimal('0.01'))
