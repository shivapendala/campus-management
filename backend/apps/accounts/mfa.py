"""
EduCore Enterprise Framework - Time-Based One-Time Password (TOTP / RFC 6238) MFA Engine

Provides 2-Factor Authentication (2FA) for privileged institutional roles (ADMIN, HOD, ACCOUNTANT):
- RFC 6238 TOTP code generation and verification (30-second time-step)
- Emergency backup recovery codes generator (Single-use hashed tokens)
- QR Code URI format generation for Google Authenticator / Microsoft Authenticator
"""

import time
import hmac
import hashlib
import struct
import secrets
import base64
from typing import List, Tuple, Optional


class TwoFactorAuthenticationManager:
    """
    Implements RFC 6238 Time-Based One-Time Password algorithm.
    """

    TIME_STEP_SECONDS = 30
    CODE_DIGITS = 6

    @classmethod
    def generate_secret_key(cls, length: int = 20) -> str:
        """Generate random base32 encoded secret key."""
        raw_random = secrets.token_bytes(length)
        return base64.b32encode(raw_random).decode("utf-8").replace("=", "")

    @classmethod
    def generate_totp_code(cls, secret_key_b32: str, timestamp: Optional[float] = None) -> str:
        """Compute 6-digit TOTP code for the current time step."""
        now = timestamp if timestamp is not None else time.time()
        time_counter = int(now // cls.TIME_STEP_SECONDS)

        # Pad base32 string if needed
        padded_secret = secret_key_b32 + "=" * ((8 - len(secret_key_b32) % 8) % 8)
        key = base64.b32decode(padded_secret.encode("utf-8"), casefold=True)

        msg = struct.pack(">Q", time_counter)
        h = hmac.new(key, msg, hashlib.sha1).digest()

        # Dynamic truncation (RFC 4226)
        offset = h[-1] & 0x0F
        binary_code = struct.unpack(">I", h[offset : offset + 4])[0] & 0x7FFFFFFF
        totp_int = binary_code % (10 ** cls.CODE_DIGITS)

        return str(totp_int).zfill(cls.CODE_DIGITS)

    @classmethod
    def verify_totp_code(
        cls,
        secret_key_b32: str,
        submitted_code: str,
        window_steps: int = 1
    ) -> bool:
        """
        Verify submitted TOTP code allowing +/- window_steps clock drift.
        """
        if not submitted_code or len(submitted_code.strip()) != cls.CODE_DIGITS:
            return False

        clean_code = submitted_code.strip()
        now = time.time()

        for step in range(-window_steps, window_steps + 1):
            eval_time = now + (step * cls.TIME_STEP_SECONDS)
            expected_code = cls.generate_totp_code(secret_key_b32, eval_time)
            if hmac.compare_digest(expected_code, clean_code):
                return True

        return False

    @classmethod
    def generate_backup_recovery_codes(cls, count: int = 8) -> Tuple[List[str], List[str]]:
        """
        Generate plaintext single-use recovery codes and their SHA-256 hashes for database storage.
        Returns: (plaintext_codes, hashed_codes)
        """
        plaintext = [f"{secrets.token_hex(4)}-{secrets.token_hex(4)}".upper() for _ in range(count)]
        hashed = [hashlib.sha256(code.encode("utf-8")).hexdigest() for code in plaintext]
        return plaintext, hashed
