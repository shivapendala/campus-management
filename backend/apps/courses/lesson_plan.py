"""
EduCore Enterprise Framework - Lesson Plan Tracking & Syllabus Execution Monitor

Tracks lecture-by-lecture lesson plans against actual classroom delivery:
- Scheduled Teaching Date vs Actual Conducted Date
- Unit Topic Coverage
- Pedagogical Delivery Mode (Chalk & Board, PPT, Lab Demo, Case Study)
- Pacing Variance & Deviation Recovery Schedules
"""

from typing import Dict, List, Any, Optional
import datetime
from dataclasses import dataclass, field


@dataclass
class LessonPlanTopicEntry:
    """Represents a planned lecture topic."""
    lecture_number: int  # 1 to 45
    unit_number: int     # 1 to 5
    topic_title: str
    planned_date: str
    actual_conducted_date: Optional[str] = None
    pedagogy_mode: str = "CHALK_AND_TALK"  # PPT_SLIDES, LIVE_CODING, DEMO, FLIPPED_CLASSROOM
    co_mapped: str = "CO1"
    is_completed: bool = False
    faculty_remarks: str = ""


class LessonPlanTracker:
    """
    Computes syllabus pacing progress and deviation from academic calendar.
    """

    @classmethod
    def audit_lesson_plan_progress(
        cls,
        course_code: str,
        faculty_id: int,
        topics: List[LessonPlanTopicEntry]
    ) -> Dict[str, Any]:
        """Compute percentage completion and syllabus pacing lag."""
        if not topics:
            return {"course_code": course_code, "completion_pct": 0.0, "pacing_status": "NO_PLAN"}

        total_topics = len(topics)
        completed_topics = sum(1 for t in topics if t.is_completed)
        completion_pct = round((completed_topics / total_topics * 100.0), 1)

        # Count delayed topics
        today_iso = datetime.date.today().isoformat()
        planned_past_due = [t for t in topics if t.planned_date <= today_iso]
        lagged = [t for t in planned_past_due if not t.is_completed]
        lag_count = len(lagged)

        if lag_count == 0:
            pacing = "ON_SCHEDULE"
        elif lag_count <= 2:
            pacing = "MINOR_LAG"
        else:
            pacing = "CRITICAL_DELAY_EXTRA_CLASSES_REQUIRED"

        return {
            "course_code": course_code,
            "faculty_id": faculty_id,
            "total_planned_lectures": total_topics,
            "conducted_lectures": completed_topics,
            "syllabus_coverage_pct": completion_pct,
            "lagged_lectures_count": lag_count,
            "pacing_status": pacing,
            "extra_tutorial_classes_recommended": max(0, lag_count)
        }
