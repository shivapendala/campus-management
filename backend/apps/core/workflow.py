"""
EduCore Enterprise Framework - State Machine & Workflow Orchestration Engine

Provides declarative workflow state-machine management with transition guards,
pre/post execution hooks, validation predicates, role authorization checks, and audit history.
"""

import datetime
from typing import Dict, List, Set, Optional, Callable, Any, Tuple
from dataclasses import dataclass, field


class WorkflowException(Exception):
    """Base exception for workflow state transition errors."""
    pass


class InvalidTransitionError(WorkflowException):
    """Raised when an invalid state transition is requested."""
    pass


class TransitionGuardFailedError(WorkflowException):
    """Raised when a pre-condition guard check fails."""
    pass


class UnauthorizedTransitionError(WorkflowException):
    """Raised when the acting role lacks authorization for transition."""
    pass


@dataclass
class WorkflowTransition:
    """Represents an allowed transition from source to target state."""
    name: str
    from_states: Set[str]
    to_state: str
    allowed_roles: Set[str] = field(default_factory=set)
    guards: List[Callable[[Any, Dict[str, Any]], Tuple[bool, str]]] = field(default_factory=list)
    pre_hooks: List[Callable[[Any, Dict[str, Any]], None]] = field(default_factory=list)
    post_hooks: List[Callable[[Any, Dict[str, Any]], None]] = field(default_factory=list)
    description: str = ""


@dataclass
class TransitionLogEntry:
    """Records an executed state transition."""
    transition_name: str
    from_state: str
    to_state: str
    actor_username: str
    actor_role: str
    timestamp: str
    remarks: str
    metadata: Dict[str, Any] = field(default_factory=dict)


class GenericWorkflowStateMachine:
    """
    Base generic state-machine engine for academic, fee refund,
    leave approval, complaint resolution, and placement workflows.
    """

    def __init__(
        self,
        name: str,
        initial_state: str,
        valid_states: Set[str],
        transitions: Dict[str, WorkflowTransition]
    ):
        self.name = name
        self.initial_state = initial_state
        self.valid_states = valid_states
        self.transitions = transitions

    def validate_transition(
        self,
        current_state: str,
        transition_name: str,
        actor_role: str,
        entity_context: Any = None,
        parameters: Optional[Dict[str, Any]] = None
    ) -> Tuple[bool, Optional[str]]:
        """
        Validate whether a transition is permitted given the current state and actor.
        Returns (is_valid, error_reason).
        """
        params = parameters or {}
        transition = self.transitions.get(transition_name)

        if not transition:
            return False, f"Transition '{transition_name}' is not registered in workflow '{self.name}'."

        if current_state not in transition.from_states:
            return False, f"Transition '{transition_name}' is not allowed from state '{current_state}'. Allowed: {transition.from_states}."

        if transition.allowed_roles and actor_role.upper() not in transition.allowed_roles and "ADMIN" not in actor_role.upper():
            return False, f"Role '{actor_role}' is not authorized to trigger transition '{transition_name}'."

        for guard in transition.guards:
            passed, reason = guard(entity_context, params)
            if not passed:
                return False, f"Transition guard check failed: {reason}"

        return True, None

    def execute_transition(
        self,
        current_state: str,
        transition_name: str,
        actor_username: str,
        actor_role: str,
        remarks: str = "",
        entity_context: Any = None,
        parameters: Optional[Dict[str, Any]] = None
    ) -> Tuple[str, TransitionLogEntry]:
        """
        Execute the transition, run pre/post hooks, and return (new_state, log_entry).
        """
        params = parameters or {}
        is_valid, reason = self.validate_transition(
            current_state, transition_name, actor_role, entity_context, params
        )
        if not is_valid:
            raise InvalidTransitionError(reason)

        transition = self.transitions[transition_name]

        # Execute pre-hooks
        for pre_hook in transition.pre_hooks:
            pre_hook(entity_context, params)

        new_state = transition.to_state

        log_entry = TransitionLogEntry(
            transition_name=transition_name,
            from_state=current_state,
            to_state=new_state,
            actor_username=actor_username,
            actor_role=actor_role,
            timestamp=datetime.datetime.now(datetime.timezone.utc).isoformat(),
            remarks=remarks,
            metadata=params
        )

        # Execute post-hooks
        for post_hook in transition.post_hooks:
            post_hook(entity_context, params)

        return new_state, log_entry
