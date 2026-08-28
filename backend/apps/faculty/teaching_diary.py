"""
EduCore Enterprise Framework - Faculty Teaching Diary & Logbook

Maintains daily lecture conduct records, pedagogical mode, and topics covered:
Provides automatic reconciliation with timetable scheduled periods.
"""

from typing import Dict, List, Any, Optional
import datetime
from dataclasses import dataclass, field


@dataclass
class DailyTeachingLogEntry:
    """Represents a conducted lecture period."""
    log_id: str
    faculty_id: int
    course_code: str
    date: str
    period_slot: str  # "09:00 - 10:00"
    unit_number: int
    topic_delivered: str
    pedagogy_type: str  # BOARD_TEACHING, PPT_PRESENTATION, LAB_DEMO, QUIZ
    students_present_count: int
    total_students_count: int
    remarks: str = ""


class FacultyTeachingDiaryManager:
    """
    Computes lecture completion velocity and student attendance turnout.
    """

    @classmethod
    def summarize_faculty_diary(cls, logs: List[DailyTeachingLogEntry]) -> Dict[str, Any]:
        """Aggregate total conducted lecture periods and average turnout."""
        if not logs:
            return {"total_lectures_conducted": 0, "avg_turnout_pct": 0.0}

        total_lectures = len(logs)
        total_present = sum(l.students_present_count for l in logs)
        total_strength = sum(l.total_students_count for l in logs)

        avg_turnout = (total_present / total_strength * 100.0) if total_strength > 0 else 0.0

        return {
            "total_lectures_conducted": total_lectures,
            "average_student_turnout_pct": round(avg_turnout, 2),
            "log_entries_count": len(logs)
        }
