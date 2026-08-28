"""
EduCore Enterprise Framework - Rate Limiting & Throttling Engine

Provides sliding-window log, token-bucket, and fixed-window algorithms
for API throttling, DDoS prevention, login attempt protection, and institutional API quotas.
"""

import time
import collections
from typing import Dict, Deque, Tuple, Optional


class SlidingWindowRateLimiter:
    """
    Sliding window rate limiter storing microsecond timestamps of requests.
    Prevents burst traffic attacks and enforces steady request rates.
    """

    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._history: Dict[str, Deque[float]] = collections.defaultdict(collections.deque)

    def is_allowed(self, client_key: str) -> Tuple[bool, int, float]:
        """
        Check if request is allowed for client_key.
        Returns: (allowed, remaining_requests, reset_after_seconds)
        """
        now = time.time()
        cutoff = now - self.window_seconds
        dq = self._history[client_key]

        # Evict timestamps outside the window
        while dq and dq[0] < cutoff:
            dq.popleft()

        current_count = len(dq)
        if current_count < self.max_requests:
            dq.append(now)
            remaining = self.max_requests - (current_count + 1)
            reset_after = (dq[0] + self.window_seconds - now) if dq else 0.0
            return True, remaining, max(0.0, reset_after)
        else:
            earliest = dq[0]
            retry_after = earliest + self.window_seconds - now
            return False, 0, max(0.0, retry_after)

    def reset(self, client_key: Optional[str] = None) -> None:
        """Reset rate limit history for a client key or all clients."""
        if client_key:
            self._history.pop(client_key, None)
        else:
            self._history.clear()


class TokenBucketRateLimiter:
    """
    Token bucket rate limiter allowing configured bursts with steady refill rates.
    """

    def __init__(self, capacity: int = 60, refill_rate_per_sec: float = 1.0):
        self.capacity = capacity
        self.refill_rate = refill_rate_per_sec
        self._buckets: Dict[str, Tuple[float, float]] = {}  # key -> (tokens, last_refill_time)

    def consume(self, client_key: str, tokens: int = 1) -> bool:
        """Attempt to consume tokens from client bucket."""
        now = time.time()
        current_tokens, last_time = self._buckets.get(client_key, (float(self.capacity), now))

        # Refill tokens based on elapsed time
        elapsed = now - last_time
        current_tokens = min(float(self.capacity), current_tokens + (elapsed * self.refill_rate))

        if current_tokens >= tokens:
            current_tokens -= tokens
            self._buckets[client_key] = (current_tokens, now)
            return True
        else:
            self._buckets[client_key] = (current_tokens, now)
            return False


class TieredCampusRateLimiter:
    """
    Tier-based rate limiter applying different quotas based on user role:
    ADMIN (unlimited), FACULTY (high), STUDENT (normal), ANONYMOUS (strict).
    """

    TIER_LIMITS = {
        "ADMIN": (1000, 60),      # 1000 req / min
        "HOD": (500, 60),         # 500 req / min
        "FACULTY": (300, 60),     # 300 req / min
        "ACCOUNTANT": (300, 60),  # 300 req / min
        "LIBRARIAN": (300, 60),   # 300 req / min
        "STUDENT": (120, 60),     # 120 req / min
        "GUEST": (30, 60),        # 30 req / min
        "ANONYMOUS": (20, 60),    # 20 req / min
    }

    _limiters: Dict[str, SlidingWindowRateLimiter] = {}

    @classmethod
    def check_rate_limit(cls, identifier: str, role: str = "ANONYMOUS") -> Tuple[bool, int, float]:
        """Check rate limit compliance based on role tier."""
        role_key = role.upper()
        if role_key not in cls.TIER_LIMITS:
            role_key = "ANONYMOUS"

        if role_key not in cls._limiters:
            max_req, win_sec = cls.TIER_LIMITS[role_key]
            cls._limiters[role_key] = SlidingWindowRateLimiter(max_requests=max_req, window_seconds=win_sec)

        limiter = cls._limiters[role_key]
        return limiter.is_allowed(identifier)
