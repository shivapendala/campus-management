from decimal import Decimal
from django.utils import timezone
from rest_framework import viewsets, permissions, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Assignment, AssignmentSubmission, SubmissionStatus
from .serializers import AssignmentSerializer, AssignmentSubmissionSerializer
from apps.students.models import Student


class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.select_related('course', 'faculty__user').prefetch_related('submissions__student__user').all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description', 'course__code', 'course__title']
    ordering_fields = ['deadline', 'created_at', 'max_score']

    @action(detail=True, methods=['post'], url_path='submit')
    def submit_solution(self, request, pk=None):
        """
        Flow Step: Student uploads submission.
        """
        assignment = self.get_object()
        student_id = request.data.get('student_id')
        submission_text = request.data.get('submission_text', '')
        submission_file_url = request.data.get('submission_file_url', '')

        student = None
        if student_id:
            student = Student.objects.filter(student_id=student_id).first() or Student.objects.filter(id=student_id).first()
        elif hasattr(request.user, 'student_profile'):
            student = request.user.student_profile
        else:
            student = Student.objects.first()

        if not student:
            return Response({'detail': 'Student not found.'}, status=status.HTTP_404_NOT_FOUND)

        is_late = timezone.now() > assignment.deadline
        sub_status = SubmissionStatus.LATE if is_late else SubmissionStatus.SUBMITTED

        submission, created = AssignmentSubmission.objects.update_or_create(
            assignment=assignment,
            student=student,
            defaults={
                'submission_text': submission_text,
                'submission_file_url': submission_file_url,
                'status': sub_status,
            }
        )

        return Response({
            'detail': 'Assignment solution successfully uploaded and timestamped.',
            'submission_id': submission.id,
            'status': submission.status,
            'is_late': is_late,
            'submitted_at': submission.submitted_at,
        }, status=status.HTTP_200_OK)


class AssignmentSubmissionViewSet(viewsets.ModelViewSet):
    queryset = AssignmentSubmission.objects.select_related('assignment__course', 'student__user').all()
    serializer_class = AssignmentSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['student__student_id', 'student__user__username', 'assignment__title']
    ordering_fields = ['submitted_at', 'score', 'status']

    @action(detail=True, methods=['post'], url_path='grade')
    def grade_submission(self, request, pk=None):
        """
        Flow Step: Faculty reviews submission -> Gives marks -> Adds feedback.
        """
        submission = self.get_object()
        raw_score = request.data.get('score')
        feedback = request.data.get('feedback', '')

        if raw_score is None:
            return Response({'detail': 'Score is required.'}, status=status.HTTP_400_BAD_REQUEST)

        score = Decimal(str(raw_score))
        submission.score = score
        submission.feedback = feedback
        submission.status = SubmissionStatus.GRADED
        submission.save()

        pct = (score / max(Decimal('1.00'), submission.assignment.max_score)) * Decimal('100.00')

        return Response({
            'detail': f'Submission graded successfully ({score}/{submission.assignment.max_score} - {round(pct, 1)}%). Feedback appended.',
            'submission_id': submission.id,
            'score': float(score),
            'max_score': float(submission.assignment.max_score),
            'percentage': round(float(pct), 1),
            'feedback': submission.feedback,
            'status': submission.status,
        }, status=status.HTTP_200_OK)
