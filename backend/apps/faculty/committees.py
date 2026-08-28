"""
EduCore Enterprise Framework - Institutional Governance & Committee Portfolio Manager

Tracks faculty statutory and non-statutory committee memberships:
Internal Quality Assurance Cell (IQAC), Academic Council, Board of Studies (BOS),
Library Committee, Sports Council, Examination Moderation Committee.
"""

from typing import Dict, List, Any, Optional
import datetime
from dataclasses import dataclass, field


@dataclass
class CommitteeMembership:
    """Represents a faculty appointment to an institutional committee."""
    membership_id: str
    committee_code: str
    committee_name: str
    faculty_id: int
    faculty_name: str
    role_in_committee: str  # CONVENER, CO_CONVENER, MEMBER_SECRETARY, MEMBER
    start_date: str
    end_date: str
    is_active: bool = True
    meetings_attended_count: int = 0
    total_meetings_held: int = 0


class InstitutionalCommitteeManager:
    """
    Computes faculty governance participation index for annual appraisal.
    """

    @classmethod
    def calculate_governance_score(cls, memberships: List[CommitteeMembership]) -> Dict[str, Any]:
        """Compute attendance and contribution metrics across committee roles."""
        if not memberships:
            return {"total_roles": 0, "governance_score": 0.0, "role_breakdown": []}

        total_roles = len(memberships)
        convener_roles = sum(1 for m in memberships if m.role_in_committee in ("CONVENER", "MEMBER_SECRETARY"))
        regular_roles = total_roles - convener_roles

        total_attended = sum(m.meetings_attended_count for m in memberships)
        total_held = sum(m.total_meetings_held for m in memberships)

        attendance_pct = (total_attended / total_held * 100.0) if total_held > 0 else 100.0

        # Convener: 15 pts, Regular Member: 5 pts
        raw_score = (convener_roles * 15.0) + (regular_roles * 5.0)
        governance_score = round(min(50.0, raw_score * (attendance_pct / 100.0)), 1)

        return {
            "total_committee_roles": total_roles,
            "convener_positions_held": convener_roles,
            "meetings_attendance_pct": round(attendance_pct, 1),
            "governance_appraisal_score_out_of_50": governance_score
        }
