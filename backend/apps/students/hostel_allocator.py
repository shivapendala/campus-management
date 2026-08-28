"""
EduCore Enterprise Framework - Student Hostel Room Allocation & Gatepass Manager

Manages campus residential living:
- Room occupancy quotas (Single, Double, Triple sharing)
- Digital biometric curfew gatepass approvals
- Mess food menu preference (Veg, Non-Veg, Jain)
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
import datetime


@dataclass
class HostelRoomAllocation:
    """Represents an active room allotment in campus hostels."""
    allotment_id: str
    hostel_block: str  # BLOCK_A_BOYS, BLOCK_B_BOYS, BLOCK_C_GIRLS, BLOCK_D_GIRLS
    room_number: str
    occupancy_type: str  # SINGLE, DOUBLE, TRIPLE
    student_id: int
    student_roll: str
    allotted_date: str
    is_fee_paid: bool = True
    mess_preference: str = "VEG"


class HostelAllocationManager:
    """
    Allocates rooms preventing over-capacity and tracks digital gatepasses.
    """

    CAPACITY_MAP = {"SINGLE": 1, "DOUBLE": 2, "TRIPLE": 3}

    @classmethod
    def can_allot_room(
        cls,
        current_allotments: List[HostelRoomAllocation],
        room_number: str,
        occupancy_type: str
    ) -> bool:
        """Verify available beds in room."""
        max_cap = cls.CAPACITY_MAP.get(occupancy_type, 2)
        current_count = sum(1 for a in current_allotments if a.room_number == room_number)
        return current_count < max_cap

    @classmethod
    def issue_digital_gatepass(
        cls,
        student_roll: str,
        out_time_iso: str,
        expected_in_time_iso: str,
        destination_reason: str,
        warden_approved: bool = True
    ) -> Dict[str, Any]:
        """Generate verified gatepass token for security guard scanning."""
        import uuid
        gp_id = f"GP-{str(uuid.uuid4())[:8].upper()}"
        return {
            "gatepass_id": gp_id,
            "student_roll": student_roll,
            "out_time": out_time_iso,
            "expected_in_time": expected_in_time_iso,
            "reason": destination_reason,
            "status": "APPROVED" if warden_approved else "PENDING_WARDEN_REVIEW",
            "qr_security_token": f"GATEPASS:{gp_id}:{student_roll}"
        }
