"""
EduCore Enterprise Framework - Daily & Weekly Notification Digest Aggregator

Aggregates individual low-priority event alerts into single structured morning digests:
Assignments due this week, upcoming exams, fee due dates, and campus event highlights.
"""

from typing import Dict, List, Any, Optional
import datetime
from dataclasses import dataclass, field


@dataclass
class StudentDailyDigest:
    """Compiled daily summary for a student."""
    student_id: int
    date: str
    classes_today: List[Dict[str, str]] = field(default_factory=list)
    assignments_pending: List[Dict[str, str]] = field(default_factory=list)
    unread_announcements: List[str] = field(default_factory=list)
    fee_alerts: List[str] = field(default_factory=list)


class NotificationDigestAggregator:
    """
    Constructs personalized daily briefings for students and faculty.
    """

    @classmethod
    def compile_student_digest(
        cls,
        student_id: int,
        schedule_events: List[Dict[str, str]],
        pending_assignments: List[Dict[str, str]],
        notices: List[str],
        fee_due_messages: List[str]
    ) -> StudentDailyDigest:
        """Aggregate events into cohesive daily digest."""
        today = datetime.date.today().isoformat()
        return StudentDailyDigest(
            student_id=student_id,
            date=today,
            classes_today=schedule_events,
            assignments_pending=pending_assignments,
            unread_announcements=notices,
            fee_alerts=fee_due_messages
        )
