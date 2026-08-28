"""
EduCore Enterprise Framework - Departmental NBA Accreditation Evaluator

Tracks NBA (National Board of Accreditation) Tier-I & Tier-II undergraduate engineering criteria:
- Criterion 1: Vision, Mission and Program Educational Objectives (PEOs)
- Criterion 2: Program Curriculum and Teaching-Learning Processes
- Criterion 3: Course Outcomes (COs) and Program Outcomes (POs)
- Criterion 4: Students' Performance
- Criterion 5: Faculty Information and Contributions
- Criterion 6: Facilities and Technical Support
- Criterion 7: Continuous Improvement
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class NBACriterionScore:
    """Represents an evaluation score for a departmental NBA criterion."""
    criterion_id: int
    name: str
    max_marks: int
    marks_awarded: float
    percentage: float
    deficiencies: List[str] = field(default_factory=list)


class DepartmentalNBATracker:
    """
    Computes departmental NBA accreditation score out of 1000 marks
    and evaluates accreditation status (6 years / 3 years / Not Accredited).
    """

    NBA_CRITERIA = {
        1: ("Vision, Mission and PEOs", 60),
        2: ("Program Curriculum & Teaching-Learning", 120),
        3: ("CO-PO Mapping & Attainment", 120),
        4: ("Students' Performance", 150),
        5: ("Faculty Cadre & Cadre Ratio", 200),
        6: ("Facilities and Technical Support", 80),
        7: ("Continuous Improvement", 50),
        8: ("First Year Academics", 50),
        9: ("Student Support Systems", 50),
        10: ("Governance & Institutional Support", 120),
    }

    @classmethod
    def evaluate_department_nba(
        cls,
        department_code: str,
        student_cadre_ratio: float,
        faculty_phd_ratio: float,
        placement_rate_pct: float,
        co_po_attainment_pct: float
    ) -> Dict[str, Any]:
        """Calculate department NBA marks and status."""
        scores = []
        total_marks = 0.0

        # Criteria evaluations
        c1 = 52.0  # Vision & Mission
        c2 = (co_po_attainment_pct / 100.0) * 120.0
        c3 = (co_po_attainment_pct / 100.0) * 120.0
        c4 = (placement_rate_pct / 100.0) * 150.0

        # Faculty criteria (200 marks)
        cadre_score = min(1.0, 15.0 / max(1.0, student_cadre_ratio)) * 100.0
        phd_score = (faculty_phd_ratio / 100.0) * 100.0
        c5 = cadre_score + phd_score

        c6 = 72.0  # Facilities
        c7 = 44.0  # Continuous improvement
        c8 = 42.0  # First year
        c9 = 45.0  # Support
        c10 = 108.0  # Governance

        all_c_scores = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

        for i, score_val in enumerate(all_c_scores, start=1):
            name, max_pts = cls.NBA_CRITERIA[i]
            awarded = round(min(float(max_pts), max(0.0, score_val)), 1)
            pct = round((awarded / max_pts) * 100.0, 1)
            scores.append(NBACriterionScore(
                criterion_id=i,
                name=name,
                max_marks=max_pts,
                marks_awarded=awarded,
                percentage=pct
            ))
            total_marks += awarded

        total_marks = round(total_marks, 1)

        # Accreditation decision: >= 750 (6 Years), >= 600 (3 Years), < 600 (Not Accredited)
        if total_marks >= 750.0:
            status = "ACCREDITED FOR 6 YEARS (EXCELLENT)"
        elif total_marks >= 600.0:
            status = "ACCREDITED FOR 3 YEARS"
        else:
            status = "NOT ACCREDITED (DEFICIENCIES IDENTIFIED)"

        return {
            "department_code": department_code,
            "total_marks_awarded": total_marks,
            "max_possible_marks": 1000,
            "overall_percentage": round((total_marks / 1000.0) * 100.0, 2),
            "nba_status": status,
            "criteria_breakdown": [
                {
                    "criterion_id": s.criterion_id,
                    "name": s.name,
                    "max_marks": s.max_marks,
                    "marks_awarded": s.marks_awarded,
                    "percentage": s.percentage
                }
                for s in scores
            ]
        }
