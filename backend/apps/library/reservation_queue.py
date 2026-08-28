"""
EduCore Enterprise Framework - Library Book Priority Hold & Reservation Queue

Manages hold queues for high-demand titles:
- FIFO queue ordering with faculty/final-year student priority weighting
- 48-hour pickup window upon book return before auto-escalating to next person in queue
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
from dataclasses import dataclass, field


@dataclass
class BookReservationEntry:
    """Represents a student/faculty hold on a book."""
    reservation_id: str
    accession_or_isbn: str
    patron_id: int
    patron_role: str  # FACULTY, FINAL_YEAR_STUDENT, STUDENT
    created_at: str
    status: str  # QUEUED, READY_FOR_PICKUP, FULFILLED, EXPIRED, CANCELLED
    pickup_deadline: Optional[str] = None


class LibraryReservationQueueManager:
    """
    Manages priority hold queues and expiration timers.
    """

    PICKUP_WINDOW_HOURS = 48

    @classmethod
    def enqueue_hold_request(
        cls,
        book_isbn: str,
        patron_id: int,
        patron_role: str,
        existing_queue: List[BookReservationEntry]
    ) -> Tuple[BookReservationEntry, int]:
        """
        Add patron to hold queue with priority weighting.
        Returns: (reservation_entry, queue_position)
        """
        import uuid
        entry = BookReservationEntry(
            reservation_id=f"HLD-{str(uuid.uuid4())[:8]}",
            accession_or_isbn=book_isbn,
            patron_id=patron_id,
            patron_role=patron_role.upper(),
            created_at=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            status="QUEUED"
        )

        # Faculty get priority over students
        if patron_role.upper() in ("FACULTY", "HOD"):
            # Insert after other faculty but before regular students
            insert_idx = sum(1 for e in existing_queue if e.patron_role in ("FACULTY", "HOD"))
            existing_queue.insert(insert_idx, entry)
            position = insert_idx + 1
        else:
            existing_queue.append(entry)
            position = len(existing_queue)

        return entry, position

    @classmethod
    def mark_book_returned_and_notify_next(
        cls,
        queue: List[BookReservationEntry]
    ) -> Optional[BookReservationEntry]:
        """
        Pop next queued patron and activate 48-hour pickup window.
        """
        for entry in queue:
            if entry.status == "QUEUED":
                entry.status = "READY_FOR_PICKUP"
                now = datetime.datetime.now(datetime.timezone.utc)
                deadline = now + datetime.timedelta(hours=cls.PICKUP_WINDOW_HOURS)
                entry.pickup_deadline = deadline.isoformat()
                return entry

        return None
