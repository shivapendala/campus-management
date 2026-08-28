"""
EduCore Enterprise Framework - Campus Infrastructure Utilization Engine

Computes room, laboratory, auditorium, and compute facility occupancy rates,
time-slot load distributions, bottleneck detections, and energy efficiency indexes.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class FacilityUtilizationSlot:
    """Represents a scheduled block within a room or facility."""
    day_of_week: str  # Monday, Tuesday, etc.
    slot_start: str   # 09:00
    slot_end: str     # 10:00
    is_occupied: bool
    subject_code: Optional[str] = None
    faculty_code: Optional[str] = None
    student_batch_size: int = 0
    room_capacity: int = 60


class InfrastructureUtilizationEngine:
    """
    Computes utilization rates, capacity saturation, and schedule congestion.
    """

    STANDARD_SLOTS_PER_DAY = 7  # 9 AM to 5 PM (7 teaching periods)
    TEACHING_DAYS_PER_WEEK = 5  # Mon - Fri
    TOTAL_WEEKLY_CAPACITY_SLOTS = STANDARD_SLOTS_PER_DAY * TEACHING_DAYS_PER_WEEK  # 35 slots

    @classmethod
    def calculate_room_utilization(
        cls,
        room_number: str,
        room_type: str,  # CLASSROOM, LAB, SEMINAR_HALL
        room_capacity: int,
        occupied_slots: List[FacilityUtilizationSlot]
    ) -> Dict[str, Any]:
        """
        Compute weekly occupancy rate and seat saturation percentage for a room.
        """
        total_slots_booked = len(occupied_slots)
        time_utilization_pct = min(100.0, (total_slots_booked / cls.TOTAL_WEEKLY_CAPACITY_SLOTS) * 100.0)

        total_seat_capacity = total_slots_booked * room_capacity
        actual_seats_used = sum(slot.student_batch_size for slot in occupied_slots)

        seat_saturation_pct = (
            (actual_seats_used / total_seat_capacity * 100.0)
            if total_seat_capacity > 0 else 0.0
        )

        # Classify utilization health
        if time_utilization_pct >= 85.0:
            status = "CONGESTED"
        elif time_utilization_pct >= 60.0:
            status = "OPTIMAL"
        elif time_utilization_pct >= 30.0:
            status = "UNDER_UTILIZED"
        else:
            status = "IDLE"

        return {
            "room_number": room_number,
            "room_type": room_type,
            "room_capacity": room_capacity,
            "total_slots_available": cls.TOTAL_WEEKLY_CAPACITY_SLOTS,
            "total_slots_booked": total_slots_booked,
            "time_utilization_pct": round(time_utilization_pct, 2),
            "seat_saturation_pct": round(seat_saturation_pct, 2),
            "status": status,
            "efficiency_rating": round((time_utilization_pct + seat_saturation_pct) / 2.0, 1)
        }

    @classmethod
    def campus_wide_utilization_summary(cls, room_reports: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Aggregate campus-wide infrastructure utilization metrics."""
        if not room_reports:
            return {"average_utilization_pct": 0.0, "total_facilities": 0, "status_breakdown": {}}

        total_rooms = len(room_reports)
        avg_time_util = sum(r["time_utilization_pct"] for r in room_reports) / total_rooms
        avg_seat_sat = sum(r["seat_saturation_pct"] for r in room_reports) / total_rooms

        status_counts = {"CONGESTED": 0, "OPTIMAL": 0, "UNDER_UTILIZED": 0, "IDLE": 0}
        for r in room_reports:
            status_counts[r.get("status", "IDLE")] = status_counts.get(r.get("status", "IDLE"), 0) + 1

        return {
            "total_facilities": total_rooms,
            "average_time_utilization_pct": round(avg_time_util, 2),
            "average_seat_saturation_pct": round(avg_seat_sat, 2),
            "composite_campus_utilization": round((avg_time_util * 0.6 + avg_seat_sat * 0.4), 2),
            "status_breakdown": status_counts,
            "congested_facilities_count": status_counts["CONGESTED"]
        }
