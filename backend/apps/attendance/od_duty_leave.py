"""
EduCore Enterprise Framework - On-Duty (OD) Sports, Hackathon & Medical Condonation Workflow

Automates official institutional duty leave requests:
- Inter-Collegiate University Sports Tournaments
- Smart India Hackathon & ACM-ICPC Finals
- Paper presentations at IEEE/ACM Conferences
- Multi-tier approval (Faculty Mentor -> HOD -> Physical Education Director -> Dean)
- Automatic attendance credit adjustment
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
import datetime


@dataclass
class OnDutyLeaveApplication:
    """Represents a formal OD attendance adjustment request."""
    application_id: str
    student_roll: str
    reason_category: str  # SPORTS_TOURNAMENT, HACKATHON, IEEE_CONFERENCE, CULTURAL_FEST
    event_title: str
    from_date: str
    to_date: str
    missed_periods_count: int
    mentor_approved: bool = True
    hod_approved: bool = True
    dean_approved: bool = True
    status: str = "APPROVED_CREDIT_GRANTED"


class OnDutyAttendanceManager:
    """
    Adjusts attendance percentages by crediting sanctioned OD hours.
    """

    @classmethod
    def apply_od_credit_to_attendance(
        cls,
        total_conducted_classes: int,
        actual_attended_classes: int,
        sanctioned_od_classes: int
    ) -> Dict[str, Any]:
        """Recalculate effective attendance with OD waiver."""
        raw_pct = (actual_attended_classes / total_conducted_classes * 100.0) if total_conducted_classes > 0 else 0.0
        effective_attended = min(total_conducted_classes, actual_attended_classes + sanctioned_od_classes)
        effective_pct = (effective_attended / total_conducted_classes * 100.0) if total_conducted_classes > 0 else 0.0

        return {
            "total_conducted": total_conducted_classes,
            "raw_attended": actual_attended_classes,
            "sanctioned_od_credit": sanctioned_od_classes,
            "effective_attended": effective_attended,
            "raw_attendance_pct": round(raw_pct, 2),
            "effective_attendance_pct": round(effective_pct, 2),
            "is_exam_eligible": effective_pct >= 75.0
        }
