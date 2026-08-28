"""
EduCore Enterprise Framework - Interactive Academic CGPA Simulator & Degree Honors Auditor

Provides what-if grade modeling for students:
- Target CGPA Goal Seeker: Calculates required average SGPA in remaining semesters to achieve target (e.g. 8.5 for Super Dream placements)
- Degree Honors Eligibility: Checks if CGPA >= 8.5 with 0 historic backlogs and 20 additional MOOC/Honors credits
- Lateral Entry SGPA normalizer (Direct 2nd Year Diploma admissions)
"""

from typing import Dict, List, Any, Optional, Tuple


class AcademicCGPASimulator:
    """
    Simulates academic trajectories and honors degree compliance.
    """

    @classmethod
    def calculate_required_sgpa(
        cls,
        current_cgpa: float,
        earned_credits: int,
        target_cgpa: float,
        remaining_credits: int
    ) -> Dict[str, Any]:
        """
        Calculate required average grade point in remaining courses to achieve target CGPA:
        target_cgpa = (current_cgpa * earned_credits + required_sgpa * remaining_credits) / total_credits
        """
        total_credits = earned_credits + remaining_credits
        if remaining_credits <= 0 or total_credits <= 0:
            return {"achievable": False, "required_sgpa": 0.0, "reason": "No remaining credits."}

        required_quality_points = (target_cgpa * total_credits) - (current_cgpa * earned_credits)
        required_sgpa = required_quality_points / remaining_credits

        is_achievable = 0.0 <= required_sgpa <= 10.0

        return {
            "current_cgpa": current_cgpa,
            "earned_credits": earned_credits,
            "target_cgpa": target_cgpa,
            "remaining_credits": remaining_credits,
            "required_sgpa_average": round(required_sgpa, 2),
            "is_mathematically_achievable": is_achievable,
            "classification": "EASY" if required_sgpa <= 8.0 else ("CHALLENGING" if required_sgpa <= 9.5 else ("NEAR_PERFECT" if required_sgpa <= 10.0 else "IMPOSSIBLE"))
        }

    @classmethod
    def audit_btech_honors_eligibility(
        cls,
        cgpa: float,
        has_any_historic_backlogs: bool,
        honors_credits_earned: int,
        total_regular_credits: int
    ) -> Dict[str, Any]:
        """Verify strict AICTE / Autonomous B.Tech (Honors) degree regulations."""
        cgpa_pass = cgpa >= 8.50
        backlog_pass = not has_any_historic_backlogs
        honors_pass = honors_credits_earned >= 20
        total_pass = total_regular_credits >= 160

        eligible = cgpa_pass and backlog_pass and honors_pass and total_pass

        return {
            "is_honors_eligible": eligible,
            "criteria_status": {
                "cgpa_min_8_5": cgpa_pass,
                "zero_historic_backlogs": backlog_pass,
                "honors_20_credits": honors_pass,
                "regular_160_credits": total_pass
            },
            "awarded_degree_title": "Bachelor of Technology with Honors" if eligible else "Bachelor of Technology"
        }
