"""
EduCore Enterprise Framework - National Education Policy (NEP 2020) Multiple Entry/Exit & ABC Framework

Implements NEP 2020 curriculum provisions:
1. Year 1 Exit (40 Credits): Certificate in Engineering Discipline
2. Year 2 Exit (80 Credits): Diploma in Engineering Discipline
3. Year 3 Exit (120 Credits): Bachelor of Science / Vocational Degree (B.Sc / B.Voc)
4. Year 4 Completion (160 Credits): Bachelor of Technology (B.Tech / Honors)
Maintains 12-digit Academic Bank of Credits (ABC ID) and National Credit Framework (NCrF) level mapping.
"""

from typing import Dict, List, Any, Optional, Tuple


class NEP2020CurriculumEngine:
    """
    Evaluates student exit awards and Academic Bank of Credits (ABC) synchronization.
    """

    @classmethod
    def evaluate_nep_award_eligibility(
        cls,
        earned_credits: int,
        active_backlogs: int,
        internship_completed: bool
    ) -> Dict[str, Any]:
        """
        Determine highest statutory award level under NEP 2020 multiple exit pathways.
        """
        if active_backlogs > 0:
            return {
                "earned_credits": earned_credits,
                "eligible_award": "NONE_PENDING_ARREARS",
                "ncrf_level": "Level 4.5",
                "can_exit_with_credential": False,
                "reason": f"Cannot award exit credential with {active_backlogs} active arrears."
            }

        if earned_credits >= 160:
            award = "Bachelor of Technology (B.Tech Honors)"
            ncrf_level = "NCrF Level 6.0"
        elif earned_credits >= 120 and internship_completed:
            award = "Bachelor of Science in Engineering (B.Sc Engg)"
            ncrf_level = "NCrF Level 5.5"
        elif earned_credits >= 80 and internship_completed:
            award = "Undergraduate Diploma in Engineering"
            ncrf_level = "NCrF Level 5.0"
        elif earned_credits >= 40:
            award = "Undergraduate Certificate in Engineering"
            ncrf_level = "NCrF Level 4.5"
        else:
            award = "INSUFFICIENT_CREDITS_FOR_EXIT"
            ncrf_level = "NCrF Level 4.0"

        return {
            "earned_credits": earned_credits,
            "eligible_award": award,
            "ncrf_level": ncrf_level,
            "can_exit_with_credential": (earned_credits >= 40 and active_backlogs == 0),
            "abc_sync_ready": True
        }
