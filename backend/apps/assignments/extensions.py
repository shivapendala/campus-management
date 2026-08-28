"""
EduCore Enterprise Framework - Assignment Deadline Extension Workflow

Manages student deadline extension requests with faculty approval and late penalty deduction:
- Standard late penalty: 10% deduction per 24 hours overdue
- Approved medical extension: 0% penalty with revised submission window
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
from apps.core.workflow import GenericWorkflowStateMachine, WorkflowTransition


class AssignmentExtensionEngine:
    """
    State machine and penalty calculator for assignment submission deadlines.
    """

    STATES = {"REQUESTED", "FACULTY_APPROVED", "REJECTED", "EXPIRED"}
    HOURLY_PENALTY_RATE = 0.5  # 0.5% per hour overdue (max 50%)

    @classmethod
    def calculate_late_deduction(
        cls,
        deadline_iso: str,
        submission_time_iso: Optional[str] = None,
        has_approved_extension: bool = False
    ) -> Tuple[float, int, bool]:
        """
        Calculate late submission penalty percentage and overdue hours.
        Returns: (penalty_percentage, overdue_hours, is_late)
        """
        if has_approved_extension:
            return 0.0, 0, False

        deadline_dt = datetime.datetime.fromisoformat(deadline_iso)
        sub_dt = datetime.datetime.fromisoformat(submission_time_iso) if submission_time_iso else datetime.datetime.now(datetime.timezone.utc)

        if sub_dt <= deadline_dt:
            return 0.0, 0, False

        overdue_seconds = (sub_dt - deadline_dt).total_seconds()
        overdue_hours = int(overdue_seconds // 3600)

        # 10% penalty per 24h block, capped at 50%
        days_late = (overdue_hours // 24) + (1 if overdue_hours % 24 > 0 else 0)
        penalty_pct = min(50.0, days_late * 10.0)

        return penalty_pct, overdue_hours, True
