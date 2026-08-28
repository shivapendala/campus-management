"""
EduCore Enterprise Framework - Inter-Departmental Resource Sharing Coordinator

Schedules and coordinates shared institutional research infrastructure:
Central High-Performance Computing (HPC) Clusters, Scanning Electron Microscopes (SEM),
3D Prototyping Labs, and Virtual Wind Tunnels across CSE, ECE, MECH, and CIVIL departments.
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
from dataclasses import dataclass, field


@dataclass
class SharedEquipmentBooking:
    """Represents a reservation for institutional shared apparatus."""
    booking_id: str
    apparatus_code: str
    apparatus_name: str
    owning_department: str
    borrowing_department: str
    researcher_id: int
    start_time: str
    end_time: str
    is_confirmed: bool = False
    purpose: str = "Research Project / M.Tech Thesis"


class InterDepartmentResourceCoordinator:
    """
    Manages resource booking conflict checks and usage billing.
    """

    @classmethod
    def check_booking_conflict(
        cls,
        new_start: datetime.datetime,
        new_end: datetime.datetime,
        existing_bookings: List[SharedEquipmentBooking]
    ) -> Tuple[bool, Optional[SharedEquipmentBooking]]:
        """
        Detect time collisions for shared scientific apparatus.
        Returns: (has_conflict, conflicting_booking)
        """
        for booking in existing_bookings:
            b_start = datetime.datetime.fromisoformat(booking.start_time)
            b_end = datetime.datetime.fromisoformat(booking.end_time)

            # Collision exists if intervals overlap
            if not (new_end <= b_start or new_start >= b_end):
                return True, booking

        return False, None

    @classmethod
    def schedule_apparatus_slot(
        cls,
        apparatus_code: str,
        apparatus_name: str,
        owning_dept: str,
        borrowing_dept: str,
        researcher_id: int,
        start_time_iso: str,
        end_time_iso: str,
        existing_bookings: List[SharedEquipmentBooking]
    ) -> Tuple[bool, str, Optional[SharedEquipmentBooking]]:
        """Attempt to schedule a slot on shared equipment."""
        import uuid
        start_dt = datetime.datetime.fromisoformat(start_time_iso)
        end_dt = datetime.datetime.fromisoformat(end_time_iso)

        if end_dt <= start_dt:
            return False, "End time must be after start time.", None

        has_conflict, clash = cls.check_booking_conflict(start_dt, end_dt, existing_bookings)
        if has_conflict and clash:
            return False, f"Time slot conflicts with existing booking {clash.booking_id} by {clash.borrowing_department}.", None

        booking = SharedEquipmentBooking(
            booking_id=f"RES-{str(uuid.uuid4())[:8]}",
            apparatus_code=apparatus_code,
            apparatus_name=apparatus_name,
            owning_department=owning_dept,
            borrowing_department=borrowing_dept,
            researcher_id=researcher_id,
            start_time=start_time_iso,
            end_time=end_time_iso,
            is_confirmed=True
        )

        return True, "Apparatus slot successfully reserved.", booking
