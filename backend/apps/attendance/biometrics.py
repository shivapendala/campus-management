"""
EduCore Enterprise Framework - Biometric Log Ingestion & Shift Parser

Ingests raw punch-in logs from fingerprint scanners, RFID gates, and facial recognition devices:
Matches punches against scheduled class periods, pairs IN/OUT timestamps, and resolves missing punches.
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
from dataclasses import dataclass, field


@dataclass
class BiometricRawPunch:
    """Represents a raw hardware punch log from an optical or RFID reader."""
    device_id: str
    card_or_user_id: str
    punch_timestamp: str  # ISO-8601
    punch_type: str  # CHECK_IN, CHECK_OUT, UNKNOWN
    device_location: str  # CSE_BLOCK_ENTRY, LAB_3, MAIN_GATE


@dataclass
class DailyAttendanceRollRecord:
    """Aggregated daily attendance record for a student or faculty member."""
    user_id: str
    date: str
    first_in_time: Optional[str] = None
    last_out_time: Optional[str] = None
    total_hours_present: float = 0.0
    status: str = "ABSENT"  # PRESENT, ABSENT, HALF_DAY, LATE
    periods_attended: List[str] = field(default_factory=list)


class BiometricIngestionProcessor:
    """
    Processes daily punch stream and converts raw logs into institutional attendance records.
    """

    MIN_HOURS_FOR_FULL_DAY = 6.0
    MIN_HOURS_FOR_HALF_DAY = 3.5

    @classmethod
    def process_daily_punches(
        cls,
        user_id: str,
        date_str: str,
        punches: List[BiometricRawPunch]
    ) -> DailyAttendanceRollRecord:
        """
        Process all punches for a single user on a given date.
        """
        if not punches:
            return DailyAttendanceRollRecord(user_id=user_id, date=date_str, status="ABSENT")

        # Sort punches chronologically
        sorted_punches = sorted(
            punches,
            key=lambda p: datetime.datetime.fromisoformat(p.punch_timestamp)
        )

        first_in = sorted_punches[0].punch_timestamp
        last_out = sorted_punches[-1].punch_timestamp

        dt_first = datetime.datetime.fromisoformat(first_in)
        dt_last = datetime.datetime.fromisoformat(last_out)

        total_seconds = (dt_last - dt_first).total_seconds()
        total_hours = round(total_seconds / 3600.0, 2)

        # Evaluate status
        if total_hours >= cls.MIN_HOURS_FOR_FULL_DAY:
            # Check if late (e.g. entered after 9:15 AM)
            if dt_first.hour > 9 or (dt_first.hour == 9 and dt_first.minute > 15):
                status = "LATE"
            else:
                status = "PRESENT"
        elif total_hours >= cls.MIN_HOURS_FOR_HALF_DAY:
            status = "HALF_DAY"
        else:
            status = "ABSENT"

        return DailyAttendanceRollRecord(
            user_id=user_id,
            date=date_str,
            first_in_time=first_in,
            last_out_time=last_out,
            total_hours_present=total_hours,
            status=status
        )
