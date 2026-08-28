"""
EduCore Enterprise Framework - QS World University & QS Asia Ranking Evaluator

Models standard Quacquarelli Symonds (QS) ranking metrics:
1. Academic Reputation (40% Weight)
2. Employer Reputation (10% Weight)
3. Faculty-Student Ratio (20% Weight)
4. Citations per Faculty (20% Weight)
5. International Faculty Ratio (5% Weight)
6. International Students Ratio (5% Weight)
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class QSInputTelemetry:
    """Input telemetry for QS Global Rankings."""
    academic_reputation_survey_score: float = 72.5
    employer_reputation_survey_score: float = 81.0
    student_faculty_ratio: float = 13.6
    scopus_citations_count: int = 4500
    full_time_faculty_count: int = 180
    international_faculty_count: int = 14
    international_students_count: int = 65
    total_students_count: int = 2450


class QSRankingEvaluator:
    """
    Computes normalized QS indicator marks and global quartile band.
    """

    @classmethod
    def evaluate_qs_score(cls, t: Optional[QSInputTelemetry] = None) -> Dict[str, Any]:
        """Compute 100-point composite QS score."""
        tel = t or QSInputTelemetry()

        # Indicator 1: Academic Reputation (40%)
        ar_score = tel.academic_reputation_survey_score * 0.40

        # Indicator 2: Employer Reputation (10%)
        er_score = tel.employer_reputation_survey_score * 0.10

        # Indicator 3: Faculty-Student Ratio (20%) - Ideal <= 10:1
        fsr_raw = min(100.0, max(0.0, (20.0 / tel.student_faculty_ratio) * 100.0))
        fsr_score = fsr_raw * 0.20

        # Indicator 4: Citations per Faculty (20%)
        cpf_val = tel.scopus_citations_count / tel.full_time_faculty_count if tel.full_time_faculty_count > 0 else 0.0
        cpf_raw = min(100.0, (cpf_val / 30.0) * 100.0)
        cpf_score = cpf_raw * 0.20

        # Indicator 5: International Faculty (5%)
        intl_fac_pct = (tel.international_faculty_count / tel.full_time_faculty_count) * 100.0 if tel.full_time_faculty_count > 0 else 0.0
        if_score = min(5.0, (intl_fac_pct / 10.0) * 5.0)

        # Indicator 6: International Students (5%)
        intl_stu_pct = (tel.international_students_count / tel.total_students_count) * 100.0 if tel.total_students_count > 0 else 0.0
        is_score = min(5.0, (intl_stu_pct / 10.0) * 5.0)

        composite_qs = round(ar_score + er_score + fsr_score + cpf_score + if_score + is_score, 2)

        return {
            "composite_qs_score": composite_qs,
            "indicators": {
                "academic_reputation": {"score": round(ar_score, 2), "max": 40.0},
                "employer_reputation": {"score": round(er_score, 2), "max": 10.0},
                "faculty_student_ratio": {"score": round(fsr_score, 2), "max": 20.0},
                "citations_per_faculty": {"score": round(cpf_score, 2), "max": 20.0},
                "international_faculty": {"score": round(if_score, 2), "max": 5.0},
                "international_students": {"score": round(is_score, 2), "max": 5.0},
            },
            "global_tier": "Top 500 Global Band (Tier 2)" if composite_qs >= 60.0 else "Top 800 Global Band"
        }
