"""
EduCore Enterprise Framework - AICTE Annual Performance & Compliance Report (APCR)

Generates standardized regulatory data tables for annual AICTE approval extension:
- Approved vs Admitted Intake by Discipline
- Faculty Cadre Ratio (1:2:6 Professor : Associate : Assistant)
- Laboratory Area & Equipment Investment Tables
"""

from typing import Dict, List, Any, Optional


class AICTEComplianceReportGenerator:
    """
    Constructs statutory AICTE Annual Performance & Compliance Report data tables.
    """

    @classmethod
    def generate_intake_compliance_table(
        cls,
        programs_data: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Aggregate sanctioned intake vs actual admissions."""
        total_sanctioned = sum(int(p.get("sanctioned_intake", 60)) for p in programs_data)
        total_admitted = sum(int(p.get("admitted_students", 55)) for p in programs_data)

        fill_rate = (total_admitted / total_sanctioned * 100.0) if total_sanctioned > 0 else 0.0

        return {
            "total_sanctioned_intake": total_sanctioned,
            "total_admitted_students": total_admitted,
            "admissions_fill_rate_pct": round(fill_rate, 2),
            "is_within_sanction_cap": total_admitted <= total_sanctioned,
            "program_wise_intake": programs_data
        }
