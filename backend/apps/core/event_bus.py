"""
EduCore Enterprise Framework - In-Memory Asynchronous Event Bus

Provides decoupled event publish/subscribe architecture for domain events:
StudentEnrolled, FeePaid, ExamResultsPublished, AssignmentSubmitted, GrievanceFiled.
"""

import time
import logging
from typing import Dict, List, Callable, Any, Optional, Tuple
from dataclasses import dataclass, field

logger = logging.getLogger("EduCore.EventBus")


@dataclass
class DomainEvent:
    """Base domain event encapsulating payload and metadata."""
    event_type: str
    payload: Dict[str, Any]
    timestamp: float = field(default_factory=time.time)
    event_id: str = ""

    def __post_init__(self):
        if not self.event_id:
            import uuid
            self.event_id = str(uuid.uuid4())


EventHandler = Callable[[DomainEvent], None]


class InstitutionalEventBus:
    """
    Central event broker routing domain events to synchronous and asynchronous handlers.
    """

    _subscribers: Dict[str, List[Tuple[EventHandler, int]]] = {}  # event_type -> [(handler, priority)]
    _event_history: List[DomainEvent] = []
    MAX_HISTORY = 1000

    @classmethod
    def subscribe(cls, event_type: str, handler: EventHandler, priority: int = 100) -> None:
        """Register a subscriber handler for a specific event type with priority."""
        if event_type not in cls._subscribers:
            cls._subscribers[event_type] = []
        cls._subscribers[event_type].append((handler, priority))
        # Sort by priority ascending (lower number = higher priority)
        cls._subscribers[event_type].sort(key=lambda item: item[1])

    @classmethod
    def publish(cls, event: DomainEvent) -> int:
        """
        Publish a domain event to all registered listeners.
        Returns the count of successfully executed handlers.
        """
        cls._event_history.append(event)
        if len(cls._event_history) > cls.MAX_HISTORY:
            cls._event_history.pop(0)

        handlers = cls._subscribers.get(event.event_type, [])
        # Also include wildcard handlers
        wildcard_handlers = cls._subscribers.get("*", [])
        all_handlers = sorted(handlers + wildcard_handlers, key=lambda x: x[1])

        success_count = 0
        for handler_tuple in all_handlers:
            handler, _ = handler_tuple
            try:
                handler(event)
                success_count += 1
            except Exception as exc:
                logger.error("Error executing handler %s for event %s: %s", handler, event.event_type, exc)

        return success_count

    @classmethod
    def get_history(cls, event_type: Optional[str] = None, limit: int = 50) -> List[DomainEvent]:
        """Retrieve recent published events matching optional event_type."""
        if event_type:
            filtered = [e for e in cls._event_history if e.event_type == event_type]
            return filtered[-limit:]
        return cls._event_history[-limit:]

    @classmethod
    def clear_subscribers(cls) -> None:
        """Clear all registered event subscribers."""
        cls._subscribers.clear()
