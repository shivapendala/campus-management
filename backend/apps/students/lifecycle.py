"""
EduCore Enterprise Framework - Student Lifecycle State Machine

Orchestrates formal student lifecycle transitions:
PROSPECTIVE -> APPLIED -> ADMITTED -> ENROLLED -> ACTIVE -> PROBATION -> DETAINED -> GRADUATED -> ALUMNUS -> TRANSFERRED / WITHDRAWN
"""

from typing import Dict, List, Any, Optional, Tuple
from apps.core.workflow import GenericWorkflowStateMachine, WorkflowTransition


class StudentLifecycleManager:
    """
    Manages statutory status transitions and validation gates for student records.
    """

    STATES = {
        "PROSPECTIVE", "APPLIED", "ADMITTED", "ENROLLED", "ACTIVE",
        "PROBATION", "DETAINED", "SUSPENDED", "GRADUATED", "ALUMNUS",
        "WITHDRAWN", "EXPELLED"
    }

    @staticmethod
    def _guard_admission_fee_paid(student_ctx: Any, params: Dict[str, Any]) -> Tuple[bool, str]:
        """Guard: verify admission fee paid before active enrollment."""
        fee_cleared = params.get("fee_cleared", True)
        if not fee_cleared:
            return False, "Admission fee must be fully cleared before activating student enrollment."
        return True, ""

    @staticmethod
    def _guard_graduation_clearance(student_ctx: Any, params: Dict[str, Any]) -> Tuple[bool, str]:
        """Guard: verify zero backlogs and no pending library/fee dues before graduation."""
        backlogs = params.get("active_backlogs", 0)
        dues = params.get("pending_dues", 0.0)
        if backlogs > 0:
            return False, f"Cannot graduate with {backlogs} active backlog(s)."
        if dues > 0.0:
            return False, f"Cannot graduate with Rs. {dues:,.2f} pending dues."
        return True, ""

    @classmethod
    def build_state_machine(cls) -> GenericWorkflowStateMachine:
        """Construct configured state machine instance for student lifecycle."""
        transitions = {
            "admit_student": WorkflowTransition(
                name="admit_student",
                from_states={"APPLIED", "PROSPECTIVE"},
                to_state="ADMITTED",
                allowed_roles={"ADMIN", "HOD"},
                description="Formally admit applicant based on merit rank"
            ),
            "enroll_student": WorkflowTransition(
                name="enroll_student",
                from_states={"ADMITTED"},
                to_state="ACTIVE",
                allowed_roles={"ADMIN", "ACCOUNTANT"},
                guards=[cls._guard_admission_fee_paid],
                description="Complete document verification and fee payment to activate student"
            ),
            "put_on_probation": WorkflowTransition(
                name="put_on_probation",
                from_states={"ACTIVE"},
                to_state="PROBATION",
                allowed_roles={"ADMIN", "HOD"},
                description="Flag student for academic probation due to low GPA"
            ),
            "restore_good_standing": WorkflowTransition(
                name="restore_good_standing",
                from_states={"PROBATION"},
                to_state="ACTIVE",
                allowed_roles={"ADMIN", "HOD"},
                description="Restore active standing after remedial improvement"
            ),
            "detain_student": WorkflowTransition(
                name="detain_student",
                from_states={"ACTIVE", "PROBATION"},
                to_state="DETAINED",
                allowed_roles={"ADMIN", "HOD"},
                description="Detain student for academic year due to credit/attendance shortage"
            ),
            "re_admit_detained": WorkflowTransition(
                name="re_admit_detained",
                from_states={"DETAINED"},
                to_state="ACTIVE",
                allowed_roles={"ADMIN", "HOD"},
                description="Re-enroll detained student into repeating academic semester"
            ),
            "graduate_student": WorkflowTransition(
                name="graduate_student",
                from_states={"ACTIVE"},
                to_state="GRADUATED",
                allowed_roles={"ADMIN", "HOD"},
                guards=[cls._guard_graduation_clearance],
                description="Formally confer degree upon full degree requirement fulfillment"
            ),
            "convert_to_alumnus": WorkflowTransition(
                name="convert_to_alumnus",
                from_states={"GRADUATED"},
                to_state="ALUMNUS",
                allowed_roles={"ADMIN"},
                description="Transition graduated student profile into institutional alumni network"
            ),
            "withdraw_student": WorkflowTransition(
                name="withdraw_student",
                from_states={"ACTIVE", "PROBATION", "ADMITTED", "DETAINED"},
                to_state="WITHDRAWN",
                allowed_roles={"ADMIN"},
                description="Process voluntary institutional withdrawal or transfer certificate"
            ),
        }

        return GenericWorkflowStateMachine(
            name="StudentLifecycle",
            initial_state="ACTIVE",
            valid_states=cls.STATES,
            transitions=transitions
        )
