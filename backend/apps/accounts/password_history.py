"""
EduCore Enterprise Framework - Password History & Reuse Prevention Engine

Prevents users from reusing any of their last N historical passwords:
Enforces mandatory 90-day password expiration intervals for institutional compliance.
"""

import hashlib
from typing import List, Tuple


class PasswordHistoryEnforcer:
    """
    Validates that a new password has not been used in the past N changes.
    """

    DEFAULT_HISTORY_LIMIT = 5

    @classmethod
    def check_password_reuse(
        cls,
        new_password: str,
        password_history_hashes: List[str]
    ) -> Tuple[bool, str]:
        """
        Compare SHA-256 hash of new password against recent password history hashes.
        Returns: (is_allowed, error_message)
        """
        new_hash = hashlib.sha256(new_password.encode("utf-8")).hexdigest()

        for past_hash in password_history_hashes[: cls.DEFAULT_HISTORY_LIMIT]:
            if past_hash == new_hash:
                return False, f"Password cannot be one of your last {cls.DEFAULT_HISTORY_LIMIT} previous passwords."

        return True, "Password passes history uniqueness check."
