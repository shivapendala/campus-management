"""
EduCore Enterprise Framework - Outcome-Based Education (OBE) & CO-PO Attainment Engine

Computes direct and indirect attainment of Course Outcomes (CO1 to CO6)
and their weighted mapping to 12 Program Outcomes (PO1 to PO12) + PSOs.
- Direct Attainment (80% weight): Internal Mid-Terms + End-Semester Exams + Assignments
- Indirect Attainment (20% weight): Course End Survey / Student Feedback
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class CourseOutcomeMapping:
    """Represents a Course Outcome (CO) and its correlation strength to POs (1 to 3)."""
    co_code: str  # CO1, CO2, CO3, CO4, CO5, CO6
    description: str
    blooms_level: str  # L1_REMEMBER, L2_UNDERSTAND, L3_APPLY, L4_ANALYZE, L5_EVALUATE, L6_CREATE
    po_correlations: Dict[str, int]  # e.g. {"PO1": 3, "PO2": 2, "PO3": 1, "PSO1": 3}
    direct_attainment_score: float = 0.0  # 0.0 to 3.0 scale
    indirect_attainment_score: float = 0.0
    final_attainment_score: float = 0.0


class OBEAttainmentEngine:
    """
    Computes NBA compliant CO-PO attainment matrices.
    Attainment Levels:
    - Level 3: >= 70% students score >= 60% marks in target question
    - Level 2: >= 60% students score >= 60% marks
    - Level 1: >= 50% students score >= 60% marks
    - Level 0: < 50% students score >= 60% marks
    """

    DIRECT_WEIGHT = 0.80
    INDIRECT_WEIGHT = 0.20

    @classmethod
    def calculate_co_attainment(
        cls,
        student_scores_pct: List[float],
        benchmark_target_pct: float = 60.0,
        survey_rating: float = 2.4  # out of 3.0
    ) -> Tuple[float, float, float]:
        """
        Calculate direct, indirect, and composite CO attainment score (0.0 to 3.0 scale).
        """
        if not student_scores_pct:
            return 0.0, 0.0, 0.0

        total_students = len(student_scores_pct)
        passed_benchmark = sum(1 for s in student_scores_pct if s >= benchmark_target_pct)
        student_percentage_met = (passed_benchmark / total_students) * 100.0

        if student_percentage_met >= 70.0:
            direct_level = 3.0
        elif student_percentage_met >= 60.0:
            direct_level = 2.0
        elif student_percentage_met >= 50.0:
            direct_level = 1.0
        else:
            direct_level = (student_percentage_met / 50.0) * 1.0

        indirect_level = min(3.0, max(0.0, survey_rating))

        composite = (direct_level * cls.DIRECT_WEIGHT) + (indirect_level * cls.INDIRECT_WEIGHT)
        return round(direct_level, 2), round(indirect_level, 2), round(composite, 2)

    @classmethod
    def compute_po_attainment_matrix(
        cls,
        co_mappings: List[CourseOutcomeMapping],
        program_outcomes: Optional[List[str]] = None
    ) -> Dict[str, float]:
        """
        Compute weighted PO attainment:
        PO_Attainment = Sum(CO_Attainment * CO_PO_Correlation) / Sum(CO_PO_Correlation)
        """
        pos = program_outcomes or [f"PO{i}" for i in range(1, 13)] + ["PSO1", "PSO2"]
        po_attainment_results: Dict[str, float] = {}

        for po in pos:
            weighted_sum = 0.0
            correlation_sum = 0

            for co in co_mappings:
                corr = co.po_correlations.get(po, 0)
                if corr > 0:
                    weighted_sum += (co.final_attainment_score * corr)
                    correlation_sum += corr

            if correlation_sum > 0:
                attained_value = weighted_sum / correlation_sum
                po_attainment_results[po] = round(attained_value, 2)
            else:
                po_attainment_results[po] = 0.0

        return po_attainment_results
