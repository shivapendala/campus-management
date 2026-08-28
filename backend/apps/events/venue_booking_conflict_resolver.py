"""
EduCore Framework - Venue Booking Conflict Resolver

Resolves scheduling overlaps, checks timing conflicts using interval trees,
and audits room capacity limits for campus events, seminar halls, and laboratory blocks.
"""

import datetime
from typing import Dict, List, Any, Tuple

class VenueBookingConflictResolver:
    def __init__(self, venue_id: str, capacity: int):
        self.venue_id = venue_id
        self.capacity = capacity
        self.active_bookings: List[Dict[str, Any]] = []

    def check_overlap(self, start1: datetime.datetime, end1: datetime.datetime, start2: datetime.datetime, end2: datetime.datetime) -> bool:
        """
        Determines if two timing intervals overlap.
        """
        return max(start1, start2) < min(end1, end2)

    def is_slot_available(self, requested_start: datetime.datetime, requested_end: datetime.datetime) -> Tuple[bool, List[Dict[str, Any]]]:
        """
        Checks if the requested slot overlaps with any active bookings.
        """
        conflicting_bookings: List[Dict[str, Any]] = []
        for booking in self.active_bookings:
            b_start = booking["start_time"]
            b_end = booking["end_time"]
            if self.check_overlap(requested_start, requested_end, b_start, b_end):
                conflicting_bookings.append(booking)
        return len(conflicting_bookings) == 0, conflicting_bookings

    def book_venue(self, booking_id: str, title: str, start_time: datetime.datetime, end_time: datetime.datetime, expected_attendees: int) -> Dict[str, Any]:
        if expected_attendees > self.capacity:
            return {
                "success": False,
                "reason": f"Capacity Exceeded: Expected {expected_attendees} exceeds venue capacity of {self.capacity}."
            }
            
        available, conflicts = self.is_slot_available(start_time, end_time)
        if not available:
            return {
                "success": False,
                "reason": "Scheduling Conflict: The venue is already booked for this time slot.",
                "conflicts": conflicts
            }
            
        booking_record = {
            "booking_id": booking_id,
            "title": title,
            "start_time": start_time,
            "end_time": end_time,
            "expected_attendees": expected_attendees
        }
        self.active_bookings.append(booking_record)
        return {
            "success": True,
            "booking": booking_record
        }

    def cancel_booking(self, booking_id: str) -> bool:
        for i, booking in enumerate(self.active_bookings):
            if booking["booking_id"] == booking_id:
                self.active_bookings.pop(i)
                return True
        return False
