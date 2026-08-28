"""
EduCore Enterprise Framework - Grievance SLA Escalation & Timer Engine

Enforces statutory UGC Grievance Redressal Regulations (2023) SLA escalation ladders:
- Level 1: Departmental Warden / Course Coordinator (Resolution SLA: 48 Hours)
- Level 2: Head of Department / Hostel Chief Warden (Resolution SLA: 96 Hours)
- Level 3: Institutional Ombudsman / Principal / Disciplinary Committee (Resolution SLA: 168 Hours)
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
from dataclasses import dataclass


@dataclass
class GrievanceSLAStatus:
    """Represents real-time SLA tracking for a student grievance."""
    complaint_id: str
    category: str
    current_level: int  # 1, 2, 3
    hours_elapsed: float
    hours_remaining_in_level: float
    is_breached: bool
    requires_escalation: bool
    target_assignee_role: str
    urgency_status: str  # ON_TRACK, AT_RISK, BREACHED_ESCALATING


class GrievanceSLAEngine:
    """
    Computes elapsed resolution hours and determines multi-tier escalation triggers.
    """

    LEVEL_SLAS_HOURS = {
        1: (48, "DEPARTMENT_WARDEN"),
        2: (96, "HEAD_OF_DEPARTMENT"),
        3: (168, "INSTITUTIONAL_OMBUDSMAN"),
    }

    # Severe categories (Harassment / Anti-Ragging) bypass L1 directly to L3
    IMMEDIATE_ESCALATION_CATEGORIES = {"ANTI_RAGGING", "GENDER_HARASSMENT", "DISCIPLINARY"}

    @classmethod
    def evaluate_sla(
        cls,
        complaint_id: str,
        category: str,
        filed_at_iso: str,
        current_level: int = 1,
        evaluation_time_iso: Optional[str] = None
    ) -> GrievanceSLAStatus:
        """
        Evaluate grievance against SLA thresholds and determine if auto-escalation is needed.
        """
        cat_upper = category.upper()
        if cat_upper in cls.IMMEDIATE_ESCALATION_CATEGORIES:
            effective_level = 3
        else:
            effective_level = min(3, max(1, current_level))

        max_hours, target_role = cls.LEVEL_SLAS_HOURS[effective_level]

        filed_dt = datetime.datetime.fromisoformat(filed_at_iso)
        eval_dt = datetime.datetime.fromisoformat(evaluation_time_iso) if evaluation_time_iso else datetime.datetime.now(datetime.timezone.utc)

        elapsed_seconds = (eval_dt - filed_dt).total_seconds()
        elapsed_hours = round(max(0.0, elapsed_seconds / 3600.0), 1)

        remaining_hours = round(max(0.0, max_hours - elapsed_hours), 1)
        is_breached = elapsed_hours > max_hours
        requires_escalation = is_breached and effective_level < 3

        if is_breached:
            urgency = "BREACHED_ESCALATING"
        elif remaining_hours <= 12:
            urgency = "AT_RISK"
        else:
            urgency = "ON_TRACK"

        return GrievanceSLAStatus(
            complaint_id=complaint_id,
            category=category,
            current_level=effective_level,
            hours_elapsed=elapsed_hours,
            hours_remaining_in_level=remaining_hours,
            is_breached=is_breached,
            requires_escalation=requires_escalation,
            target_assignee_role=target_role,
            urgency_status=urgency
        )
