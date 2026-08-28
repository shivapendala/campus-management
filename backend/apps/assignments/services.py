from decimal import Decimal
from typing import Dict, Any, List
from django.utils import timezone
from .models import Assignment, AssignmentSubmission, SubmissionStatus


class AssignmentEvaluationService:
    """
    Domain service for Assignment Rubrics, Automated Late Submissions Auditing, and Score Weighting.
    """

    @classmethod
    def audit_assignment_turnout(cls, assignment_id: int) -> Dict[str, Any]:
        """
        Computes submission turnout, graded percentage, and average awarded marks.
        """
        assignment = Assignment.objects.prefetch_related('submissions').get(id=assignment_id)
        submissions = assignment.submissions.all()

        total_submitted = submissions.count()
        graded_submissions = submissions.filter(status=SubmissionStatus.GRADED)
        graded_count = graded_submissions.count()

        avg_score = Decimal('0.0')
        if graded_count > 0:
            total_score = sum(s.score for s in graded_submissions if s.score is not None)
            avg_score = (total_score / graded_count).quantize(Decimal('0.1'))

        return {
            'assignment_title': assignment.title,
            'max_score': float(assignment.max_score),
            'total_submissions': total_submitted,
            'graded_count': graded_count,
            'pending_grading_count': total_submitted - graded_count,
            'average_score': float(avg_score),
            'average_score_pct': round(float(avg_score / max(Decimal('1.0'), assignment.max_score)) * 100, 1),
            'is_deadline_passed': timezone.now() > assignment.deadline,
        }
