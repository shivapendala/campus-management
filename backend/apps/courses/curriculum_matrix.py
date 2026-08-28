"""
EduCore Enterprise Framework - Curriculum Credit Matrix & Degree Structure Validator

Audits statutory AICTE model curriculum credit distributions:
- Humanities and Social Sciences (HSMC): ~12 credits
- Basic Science Courses (BSC): ~25 credits
- Engineering Science Courses (ESC): ~24 credits
- Professional Core Courses (PCC): ~48 credits
- Professional Elective Courses (PEC): ~18 credits
- Open Electives (OEC): ~18 credits
- Project / Internship (PROJ): ~15 credits
Total B.Tech Degree: ~160 credits
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class CurriculumCategoryCreditSummary:
    """Credit allocation for a specific curriculum category."""
    category_code: str
    category_name: str
    target_minimum_credits: int
    actual_offered_credits: int
    attainment_status: str  # SATISFIED, DEFICIENT, SURPLUS


class CurriculumMatrixValidator:
    """
    Validates B.Tech degree curriculum against AICTE / UGC statutory framework.
    """

    AICTE_MODEL_CREDIT_DISTRIBUTION = {
        "HSMC": ("Humanities and Social Sciences including Management", 12),
        "BSC": ("Basic Science Courses (Physics, Chemistry, Maths)", 25),
        "ESC": ("Engineering Science Courses (Workshop, Mechanics, C)", 24),
        "PCC": ("Professional Core Courses", 48),
        "PEC": ("Professional Elective Courses", 18),
        "OEC": ("Open Elective Courses from other disciplines", 18),
        "PROJ": ("Project Work, Seminar and Internship in Industry", 15),
        "MC": ("Mandatory Non-Credit Courses (Environmental, Constitution)", 0),
    }

    TARGET_TOTAL_CREDITS = 160

    @classmethod
    def audit_curriculum_structure(
        cls,
        degree_name: str,
        department_code: str,
        courses: List[Dict[str, Any]]  # [{"code": "CS201", "category": "PCC", "credits": 4}, ...]
    ) -> Dict[str, Any]:
        """Validate whether curriculum satisfies AICTE category minimums."""
        category_totals: Dict[str, int] = {k: 0 for k in cls.AICTE_MODEL_CREDIT_DISTRIBUTION.keys()}

        for c in courses:
            cat = c.get("category", "PCC").upper()
            credits = int(c.get("credits", 3))
            category_totals[cat] = category_totals.get(cat, 0) + credits

        breakdown = []
        deficiencies = []
        total_credits = sum(category_totals.values())

        for cat_code, (name, target) in cls.AICTE_MODEL_CREDIT_DISTRIBUTION.items():
            actual = category_totals.get(cat_code, 0)
            if actual >= target:
                status = "SATISFIED"
            else:
                status = "DEFICIENT"
                deficiencies.append(f"{cat_code} ({name}): {actual} credits offered < {target} required.")

            breakdown.append(CurriculumCategoryCreditSummary(
                category_code=cat_code,
                category_name=name,
                target_minimum_credits=target,
                actual_offered_credits=actual,
                attainment_status=status
            ))

        is_compliant = len(deficiencies) == 0 and total_credits >= cls.TARGET_TOTAL_CREDITS

        return {
            "degree_program": degree_name,
            "department": department_code,
            "total_curriculum_credits": total_credits,
            "aicte_target_credits": cls.TARGET_TOTAL_CREDITS,
            "is_aicte_compliant": is_compliant,
            "deficiencies": deficiencies,
            "category_breakdown": [
                {
                    "category_code": b.category_code,
                    "category_name": b.category_name,
                    "target_credits": b.target_minimum_credits,
                    "actual_credits": b.actual_offered_credits,
                    "status": b.attainment_status
                }
                for b in breakdown
            ]
        }
