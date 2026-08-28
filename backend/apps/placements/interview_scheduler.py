"""
EduCore Enterprise Framework - Corporate Interview Slot Allocator

Schedules multi-round interviews (Online Assessment -> Technical Round 1 -> Technical Round 2 -> HR Round):
Matches student availability with corporate interviewer panels and assigned interview suites.
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
from dataclasses import dataclass, field


@dataclass
class InterviewSlotBooking:
    """Represents a scheduled candidate interview."""
    slot_id: str
    drive_id: str
    company_name: str
    round_name: str  # OA, TECH_ROUND_1, TECH_ROUND_2, HR_ROUND
    candidate_id: int
    candidate_roll: str
    panel_number: int
    room_number: str
    start_time: str
    end_time: str
    is_completed: bool = False
    interviewer_rating: Optional[float] = None
    verdict: str = "PENDING"  # PENDING, SHORTLISTED, REJECTED


class CorporateInterviewScheduler:
    """
    Allocates interview time blocks to shortlisted candidates.
    """

    SLOT_DURATION_MINUTES = 45
    BREAK_BETWEEN_SLOTS_MINUTES = 15

    @classmethod
    def generate_candidate_interview_slots(
        cls,
        drive_id: str,
        company_name: str,
        round_name: str,
        candidate_rolls: List[str],
        num_panels: int = 3,
        start_time_iso: Optional[str] = None
    ) -> List[InterviewSlotBooking]:
        """
        Distribute shortlisted candidate interviews across parallel interview panels.
        """
        import uuid
        start_dt = datetime.datetime.fromisoformat(start_time_iso) if start_time_iso else datetime.datetime.now().replace(hour=9, minute=0, second=0, microsecond=0)

        slots: List[InterviewSlotBooking] = []
        step_delta = datetime.timedelta(minutes=(cls.SLOT_DURATION_MINUTES + cls.BREAK_BETWEEN_SLOTS_MINUTES))
        duration_delta = datetime.timedelta(minutes=cls.SLOT_DURATION_MINUTES)

        for idx, roll in enumerate(candidate_rolls):
            panel_idx = (idx % num_panels) + 1
            slot_seq = idx // num_panels

            slot_start = start_dt + (step_delta * slot_seq)
            slot_end = slot_start + duration_delta

            slots.append(InterviewSlotBooking(
                slot_id=f"INT-{str(uuid.uuid4())[:8]}",
                drive_id=drive_id,
                company_name=company_name,
                round_name=round_name,
                candidate_id=idx + 1,
                candidate_roll=roll,
                panel_number=panel_idx,
                room_number=f"Interview Suite {panel_idx}",
                start_time=slot_start.isoformat(),
                end_time=slot_end.isoformat()
            ))

        return slots
