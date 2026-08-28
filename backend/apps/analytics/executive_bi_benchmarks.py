"""
EduCore Enterprise Framework - Executive Board of Governors BI Benchmarks

Computes strategic intelligence for University Governing Council:
- Return on Academic Investment (ROAI) across departments
- Faculty Research Citation Velocity & h-Index Acceleration
- Annual Financial Operating Surplus vs CAPEX Reinvestment
- Statutory Regulatory Compliance Index (AICTE, UGC, NAAC, NBA, NIRF)
"""

from typing import Dict, List, Any, Optional, Tuple


class ExecutiveBIBenchmarkingEngine:
    """
    Computes top-level institutional key performance indicators (KPIs).
    """

    @classmethod
    def compute_department_efficiency_index(
        cls,
        department_code: str,
        student_count: int,
        faculty_count: int,
        annual_budget_inr: float,
        research_grants_inr: float,
        placement_offers_count: int
    ) -> Dict[str, Any]:
        """
        Calculate composite departmental efficiency score (0 to 100).
        """
        # Faculty-student ratio score (Ideal 1:15)
        fsr = student_count / faculty_count if faculty_count > 0 else 30.0
        fsr_score = min(25.0, max(0.0, 25.0 * (15.0 / fsr))) if fsr > 0 else 0.0

        # Research funding score (Max 25)
        grant_per_faculty = research_grants_inr / faculty_count if faculty_count > 0 else 0.0
        grant_score = min(25.0, (grant_per_faculty / 1000000.0) * 25.0)  # Rs. 10L/faculty = full score

        # Placement outcome score (Max 25)
        graduating_approx = student_count / 4.0
        placement_rate = placement_offers_count / graduating_approx if graduating_approx > 0 else 0.0
        placement_score = min(25.0, placement_rate * 25.0)

        # Budget utilization efficiency (Max 25)
        cost_per_student = annual_budget_inr / student_count if student_count > 0 else 100000.0
        budget_score = min(25.0, max(5.0, 25.0 * (85000.0 / cost_per_student)))

        total_efficiency = round(fsr_score + grant_score + placement_score + budget_score, 1)

        return {
            "department_code": department_code,
            "composite_efficiency_score_100": total_efficiency,
            "sub_scores": {
                "faculty_student_ratio_score": round(fsr_score, 1),
                "research_grant_productivity": round(grant_score, 1),
                "placement_success_score": round(placement_score, 1),
                "cost_efficiency_score": round(budget_score, 1),
            },
            "performance_tier": "TIER_1_EXEMPLARY" if total_efficiency >= 80.0 else ("TIER_2_COMPLIANT" if total_efficiency >= 60.0 else "IMPROVEMENT_REQUIRED")
        }
