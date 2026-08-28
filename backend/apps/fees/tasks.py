from datetime import date
from decimal import Decimal
from django.utils import timezone
from apps.fees.models import FeePayment, FeeStructure, PaymentStatus
from apps.students.models import Student
from apps.notifications.models import Notification, NotificationType


def task_dispatch_overdue_fee_reminders():
    """
    Background automated task: Scans unpaid fee accounts approaching or past due dates and dispatches reminder notices.
    """
    today = timezone.now().date()
    structures = FeeStructure.objects.filter(due_date__lte=today)
    reminders_sent = 0

    for structure in structures:
        # Find students in target department & semester
        students = Student.objects.filter(department=structure.department, year=((structure.semester + 1) // 2))
        for student in students:
            has_paid = FeePayment.objects.filter(
                student=student,
                fee_structure=structure,
                status=PaymentStatus.SUCCESS
            ).exists()

            if not has_paid:
                Notification.objects.create(
                    recipient=student.user,
                    title="💳 Tuition Fee Payment Past Due Notice",
                    message=f"Outstanding balance of ${structure.amount} for '{structure.title}' was due on {structure.due_date}. Please clear dues to prevent administrative hold.",
                    notification_type=NotificationType.FEE_REMINDER,
                )
                reminders_sent += 1

    return reminders_sent
