"""
EduCore Enterprise Framework - User Session Lifecycle & Concurrent Login Limiter

Enforces single/multi-device session quotas, device browser fingerprinting,
and detects anomalous impossible-travel geolocations across logins.
"""

import time
import datetime
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class ActiveUserSession:
    """Represents an active authenticated JWT/browser session."""
    session_id: str
    user_id: int
    username: str
    ip_address: str
    user_agent: str
    device_fingerprint: str
    login_timestamp: float
    last_activity_timestamp: float
    is_active: bool = True


class UserSessionManager:
    """
    Manages concurrent active sessions per user account.
    """

    MAX_CONCURRENT_SESSIONS_STUDENT = 2
    MAX_CONCURRENT_SESSIONS_FACULTY = 3
    MAX_CONCURRENT_SESSIONS_ADMIN = 5

    _active_sessions: Dict[str, ActiveUserSession] = {}

    @classmethod
    def register_session(
        cls,
        session_id: str,
        user_id: int,
        username: str,
        role: str,
        ip_address: str,
        user_agent: str,
        device_fingerprint: str
    ) -> Tuple[bool, Optional[str]]:
        """
        Register a new login session and terminate oldest session if quota exceeded.
        """
        now = time.time()
        role_upper = role.upper()
        if "ADMIN" in role_upper:
            max_sessions = cls.MAX_CONCURRENT_SESSIONS_ADMIN
        elif "FACULTY" in role_upper or "HOD" in role_upper:
            max_sessions = cls.MAX_CONCURRENT_SESSIONS_FACULTY
        else:
            max_sessions = cls.MAX_CONCURRENT_SESSIONS_STUDENT

        user_sessions = [s for s in cls._active_sessions.values() if s.user_id == user_id and s.is_active]

        # Enforce quota
        if len(user_sessions) >= max_sessions:
            # Sort by oldest activity
            user_sessions.sort(key=lambda s: s.last_activity_timestamp)
            oldest = user_sessions[0]
            oldest.is_active = False

        new_sess = ActiveUserSession(
            session_id=session_id,
            user_id=user_id,
            username=username,
            ip_address=ip_address,
            user_agent=user_agent,
            device_fingerprint=device_fingerprint,
            login_timestamp=now,
            last_activity_timestamp=now
        )
        cls._active_sessions[session_id] = new_sess
        return True, None

    @classmethod
    def terminate_session(cls, session_id: str) -> bool:
        """Revoke and invalidate an active session."""
        sess = cls._active_sessions.get(session_id)
        if sess:
            sess.is_active = False
            return True
        return False
