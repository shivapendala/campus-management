"""
EduCore Enterprise Framework - Faculty Development Program (FDP) & NPTEL Tracker

Tracks faculty participation in AICTE-ATAL, SWAYAM, NPTEL, and IEEE workshops:
Calculates continuing education units (CEU) and CAS promotion credits.
"""

from typing import Dict, List, Any, Optional
import datetime
from dataclasses import dataclass, field


@dataclass
class FDPParticipationRecord:
    """Represents an attended FDP, STTP, or MOOC course."""
    record_id: str
    faculty_id: int
    program_title: str
    organizing_body: str  # AICTE_ATAL, IIT, NIT, IEEE, SWAYAM_NPTEL, INDUSTRY
    start_date: str
    end_date: str
    duration_days: int
    certificate_issued: bool = True
    grade_obtained: Optional[str] = "ELITE_GOLD"


class FacultyFDPTracker:
    """
    Computes annual FDP attendance compliance against AICTE statutory norms (min 10 days/year).
    """

    @classmethod
    def audit_fdp_compliance(cls, records: List[FDPParticipationRecord]) -> Dict[str, Any]:
        """Verify faculty continuing professional development credits."""
        total_days = sum(r.duration_days for r in records)
        nptel_elite_count = sum(1 for r in records if "ELITE" in (r.grade_obtained or ""))

        is_compliant = total_days >= 10

        return {
            "total_fdp_days_attended": total_days,
            "statutory_minimum_days": 10,
            "is_aicte_compliant": is_compliant,
            "nptel_elite_certifications_count": nptel_elite_count,
            "ceu_points_earned": min(25.0, total_days * 2.5)
        }
