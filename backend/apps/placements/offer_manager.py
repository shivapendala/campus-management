"""
EduCore Enterprise Framework - Placement Offer Letter & Acceptance State Machine

Tracks corporate job offers, manages letter of intent (LOI) uploads,
enforces institutional offer acceptance deadlines, and calculates annual salary statistics.
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
import statistics
from apps.core.workflow import GenericWorkflowStateMachine, WorkflowTransition


class PlacementOfferManager:
    """
    State machine for student job offer acceptance and institutional placement statistics.
    """

    STATES = {"OFFERED", "ACCEPTED", "DECLINED", "RELEASED_FOR_DREAM", "JOINED", "REVOKED"}

    @classmethod
    def calculate_cohort_salary_statistics(cls, accepted_ctc_list: List[float]) -> Dict[str, Any]:
        """
        Compute descriptive metrics on accepted packages (in LPA):
        Highest CTC, Average CTC, Median CTC, Top 10% Average CTC, Top 20% Average CTC.
        """
        if not accepted_ctc_list:
            return {
                "total_placed": 0, "highest_ctc_lpa": 0.0, "average_ctc_lpa": 0.0,
                "median_ctc_lpa": 0.0, "top_10_percent_avg_lpa": 0.0, "top_20_percent_avg_lpa": 0.0
            }

        sorted_ctc = sorted(accepted_ctc_list, reverse=True)
        total = len(sorted_ctc)

        avg_ctc = statistics.mean(sorted_ctc)
        med_ctc = statistics.median(sorted_ctc)
        high_ctc = sorted_ctc[0]

        top_10_count = max(1, int(total * 0.10))
        top_10_avg = statistics.mean(sorted_ctc[:top_10_count])

        top_20_count = max(1, int(total * 0.20))
        top_20_avg = statistics.mean(sorted_ctc[:top_20_count])

        return {
            "total_placed": total,
            "highest_ctc_lpa": round(high_ctc, 2),
            "average_ctc_lpa": round(avg_ctc, 2),
            "median_ctc_lpa": round(med_ctc, 2),
            "top_10_percent_avg_lpa": round(top_10_avg, 2),
            "top_20_percent_avg_lpa": round(top_20_avg, 2)
        }

    @classmethod
    def build_offer_workflow(cls) -> GenericWorkflowStateMachine:
        """Construct workflow state machine for student job offer decisions."""
        transitions = {
            "accept_offer": WorkflowTransition(
                name="accept_offer",
                from_states={"OFFERED"},
                to_state="ACCEPTED",
                allowed_roles={"STUDENT", "ADMIN"},
                description="Student accepts corporate job offer and submits signed LOI"
            ),
            "decline_offer": WorkflowTransition(
                name="decline_offer",
                from_states={"OFFERED"},
                to_state="DECLINED",
                allowed_roles={"STUDENT", "ADMIN"},
                description="Student formally declines offer to pursue other opportunities"
            ),
            "upgrade_to_dream": WorkflowTransition(
                name="upgrade_to_dream",
                from_states={"ACCEPTED"},
                to_state="RELEASED_FOR_DREAM",
                allowed_roles={"ADMIN"},
                description="Institutional placement cell releases earlier offer upon higher tier Dream offer"
            ),
            "confirm_joining": WorkflowTransition(
                name="confirm_joining",
                from_states={"ACCEPTED"},
                to_state="JOINED",
                allowed_roles={"ADMIN", "RECRUITER"},
                description="Company confirms candidate onboarding"
            ),
        }

        return GenericWorkflowStateMachine(
            name="PlacementOfferWorkflow",
            initial_state="OFFERED",
            valid_states=cls.STATES,
            transitions=transitions
        )
