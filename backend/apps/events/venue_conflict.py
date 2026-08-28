"""
EduCore Enterprise Framework - Campus Event Venue Collision & Booking Engine

Prevents scheduling conflicts across campus auditoriums, open-air theatres (OAT),
seminar halls, and athletic grounds: Validates setup/teardown buffer intervals.
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
from dataclasses import dataclass


@dataclass
class VenueBookingSlot:
    """Represents a reservation of a campus event venue."""
    booking_id: str
    venue_name: str  # MAIN_AUDITORIUM, SEMINAR_HALL_A, OAT, INDOOR_STADIUM
    event_title: str
    organizer_id: int
    organizer_department: str
    start_time: str
    end_time: str
    is_confirmed: bool = True


class VenueConflictDetector:
    """
    Detects overlapping venue reservations including mandatory 1-hour teardown buffers.
    """

    DEFAULT_BUFFER_MINUTES = 60

    @classmethod
    def check_collision(
        cls,
        new_start_iso: str,
        new_end_iso: str,
        existing_bookings_for_venue: List[VenueBookingSlot],
        buffer_minutes: int = DEFAULT_BUFFER_MINUTES
    ) -> Tuple[bool, Optional[VenueBookingSlot], str]:
        """
        Check if requested interval collides with existing bookings (including teardown buffer).
        Returns: (has_collision, clashing_booking, description)
        """
        req_start = datetime.datetime.fromisoformat(new_start_iso)
        req_end = datetime.datetime.fromisoformat(new_end_iso)
        buffer_delta = datetime.timedelta(minutes=buffer_minutes)

        if req_end <= req_start:
            return True, None, "Event end time must be strictly after start time."

        for booking in existing_bookings_for_venue:
            b_start = datetime.datetime.fromisoformat(booking.start_time) - buffer_delta
            b_end = datetime.datetime.fromisoformat(booking.end_time) + buffer_delta

            if not (req_end <= b_start or req_start >= b_end):
                return True, booking, f"Collision with '{booking.event_title}' ({booking.start_time} - {booking.end_time}) including {buffer_minutes}m buffer."

        return False, None, "Venue is available for booking."
