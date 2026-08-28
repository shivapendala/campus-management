from decimal import Decimal
from apps.examinations.models import Exam, ExamResult, ExamStatus
from apps.notifications.models import Notification, NotificationType


def task_broadcast_exam_results_published(exam_id: int):
    """
    Background automated task: Dispatches grade notifications to students upon HOD verification and publishing of examination results.
    """
    exam = Exam.objects.get(id=exam_id)
    if exam.status != ExamStatus.PUBLISHED:
        return 0

    results = ExamResult.objects.filter(exam=exam, is_verified_by_hod=True)
    notifications_count = 0

    for result in results:
        Notification.objects.create(
            recipient=result.student.user,
            title=f"🎓 Exam Results Declared: {exam.name}",
            message=f"Your verified score for {exam.course.code} is {result.marks_obtained}/{exam.max_marks} (Grade: {result.grade} • GP: {result.grade_point}). View your official Grade Card.",
            notification_type=NotificationType.EXAM_ALERT,
        )
        notifications_count += 1

    return notifications_count
