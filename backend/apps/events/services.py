from typing import Dict, Any, List
from .models import Event, EventRegistration


class CampusEventService:
    """
    Domain service for Venue Allocation, Capacity Management, and Registration Ticketing.
    """

    @classmethod
    def check_venue_availability(cls, venue: str, start_time, end_time, exclude_event_id: int = None) -> bool:
        """
        Ensures no two campus events collide in the same auditorium/hall.
        """
        qs = Event.objects.filter(venue=venue, start_time__lt=end_time, end_time__gt=start_time)
        if exclude_event_id:
            qs = qs.exclude(id=exclude_event_id)
        return not qs.exists()

    @classmethod
    def get_event_engagement_metrics(cls, event_id: int) -> Dict[str, Any]:
        """
        Computes seat capacity claimed and remaining attendance quota.
        """
        event = Event.objects.prefetch_related('registrations').get(id=event_id)
        reg_count = event.registrations.count()

        return {
            'event_title': event.title,
            'venue': event.venue,
            'capacity': event.capacity,
            'registered_attendees': reg_count,
            'seats_remaining': max(0, event.capacity - reg_count),
            'capacity_claimed_pct': round((reg_count / max(1, event.capacity)) * 100, 1),
            'is_sold_out': reg_count >= event.capacity,
        }
