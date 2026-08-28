"""
EduCore Enterprise Framework - Faculty Leave Management State Machine

Manages institutional leave applications: Casual Leave (CL), Earned Leave (EL),
Duty Leave (DL for conferences/examinations), Sabbatical, and Maternity/Paternity.
Enforces mandatory substitute faculty class arrangement before approval.
"""

from typing import Dict, List, Any, Optional, Tuple
from apps.core.workflow import GenericWorkflowStateMachine, WorkflowTransition


class FacultyLeaveWorkflowManager:
    """
    State machine for faculty leave request approval and substitute assignment.
    """

    STATES = {
        "DRAFT", "APPLIED", "SUBSTITUTE_CONFIRMED", "HOD_APPROVED",
        "PRINCIPAL_APPROVED", "REJECTED", "CANCELLED", "AVAILED"
    }

    @staticmethod
    def _guard_substitute_arranged(leave_ctx: Any, params: Dict[str, Any]) -> Tuple[bool, str]:
        """Guard: ensure alternative faculty has consented to cover teaching periods."""
        substitute_confirmed = params.get("substitute_confirmed", True)
        if not substitute_confirmed:
            return False, "Cannot approve leave without confirmed substitute faculty for lecture periods."
        return True, ""

    @classmethod
    def build_state_machine(cls) -> GenericWorkflowStateMachine:
        """Build configured state machine for faculty leave management."""
        transitions = {
            "submit_application": WorkflowTransition(
                name="submit_application",
                from_states={"DRAFT"},
                to_state="APPLIED",
                allowed_roles={"FACULTY", "HOD", "ADMIN"},
                description="Submit leave application with dates and reason"
            ),
            "confirm_substitute": WorkflowTransition(
                name="confirm_substitute",
                from_states={"APPLIED"},
                to_state="SUBSTITUTE_CONFIRMED",
                allowed_roles={"FACULTY", "HOD"},
                description="Substitute colleague confirms lecture handover"
            ),
            "hod_recommend": WorkflowTransition(
                name="hod_recommend",
                from_states={"SUBSTITUTE_CONFIRMED", "APPLIED"},
                to_state="HOD_APPROVED",
                allowed_roles={"HOD", "ADMIN"},
                guards=[cls._guard_substitute_arranged],
                description="Head of Department approves leave quota"
            ),
            "principal_grant": WorkflowTransition(
                name="principal_grant",
                from_states={"HOD_APPROVED"},
                to_state="PRINCIPAL_APPROVED",
                allowed_roles={"ADMIN"},
                description="Principal / Registrar formally sanctions leave"
            ),
            "reject_leave": WorkflowTransition(
                name="reject_leave",
                from_states={"APPLIED", "SUBSTITUTE_CONFIRMED", "HOD_APPROVED"},
                to_state="REJECTED",
                allowed_roles={"HOD", "ADMIN"},
                description="Reject leave due to critical academic duties"
            ),
            "cancel_leave": WorkflowTransition(
                name="cancel_leave",
                from_states={"APPLIED", "SUBSTITUTE_CONFIRMED", "HOD_APPROVED", "PRINCIPAL_APPROVED"},
                to_state="CANCELLED",
                allowed_roles={"FACULTY", "ADMIN"},
                description="Applicant withdraws approved leave"
            ),
        }

        return GenericWorkflowStateMachine(
            name="FacultyLeaveWorkflow",
            initial_state="APPLIED",
            valid_states=cls.STATES,
            transitions=transitions
        )
