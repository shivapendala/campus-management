"""
EduCore Enterprise Framework - Student Extracurricular Clubs, NSS & NCC Activity Tracker

Logs co-curricular participation for AICTE Mandatory Activity Points (100 points required for B.Tech degree):
- NSS (National Service Scheme) rural camp volunteering
- NCC (National Cadet Corps) parade & firing drills
- Robotics, IEEE, Coding Club, and Fine Arts society achievements
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class ActivityPointRecord:
    """Represents earned AICTE activity points."""
    record_id: str
    student_roll: str
    activity_category: str  # NSS_VOLUNTEERING, NCC_TRAINING, HACKATHON_CHAMPION, SPORTS_TOURNAMENT, CULTURAL_FEST
    activity_title: str
    points_earned: int
    proof_document_verified: bool = True


class ExtracurricularPointsManager:
    """
    Computes cumulative degree activity points compliance.
    """

    STATUTORY_DEGREE_REQUIREMENT = 100

    @classmethod
    def compute_student_points(cls, records: List[ActivityPointRecord]) -> Dict[str, Any]:
        """Aggregate total verified activity points."""
        total = sum(r.points_earned for r in records if r.proof_document_verified)
        is_compliant = total >= cls.STATUTORY_DEGREE_REQUIREMENT

        return {
            "total_points_earned": total,
            "target_required_points": cls.STATUTORY_DEGREE_REQUIREMENT,
            "is_degree_compliant": is_compliant,
            "deficiency_points": max(0, cls.STATUTORY_DEGREE_REQUIREMENT - total),
            "verified_activities_count": sum(1 for r in records if r.proof_document_verified)
        }
