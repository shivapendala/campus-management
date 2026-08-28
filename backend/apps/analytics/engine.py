"""
EduCore Enterprise Framework - Institutional Business Intelligence (BI) Engine

Calculates multi-dimensional campus metrics, student retention curves,
departmental efficiency benchmarks, faculty-to-student ratios, and executive KPI summaries.
"""

import math
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class DepartmentPerformanceSummary:
    """Departmental key metrics snapshot."""
    department_code: str
    department_name: str
    student_count: int
    faculty_count: int
    faculty_student_ratio: float
    average_cgpa: float
    average_attendance: float
    placement_rate_pct: float
    total_fee_collected: float
    total_fee_pending: float
    research_publications_count: int
    efficiency_score: float = 0.0


class InstitutionalAnalyticsEngine:
    """
    Central BI engine aggregating performance statistics across all campus dimensions.
    """

    @classmethod
    def calculate_faculty_student_ratio(cls, student_count: int, faculty_count: int) -> float:
        """Calculate faculty-to-student ratio (e.g. 1:15 = 0.0667 or 15.0)."""
        if faculty_count <= 0:
            return 0.0
        return round(student_count / faculty_count, 2)

    @classmethod
    def calculate_department_efficiency(
        cls,
        avg_cgpa: float,
        avg_attendance: float,
        placement_rate: float,
        faculty_student_ratio: float
    ) -> float:
        """
        Compute normalized departmental efficiency score out of 100:
        - Academic Excellence (CGPA / 10 * 35%)
        - Attendance Discipline (Attendance % * 25%)
        - Placement Outcome (Placement % * 25%)
        - Staffing Optimization (Ratio ideal 15:1 -> 15%)
        """
        cgpa_score = (min(10.0, max(0.0, avg_cgpa)) / 10.0) * 35.0
        att_score = (min(100.0, max(0.0, avg_attendance)) / 100.0) * 25.0
        plc_score = (min(100.0, max(0.0, placement_rate)) / 100.0) * 25.0

        # Ideal faculty-student ratio is 15:1. Penalize large deviations
        ratio_deviation = abs(faculty_student_ratio - 15.0)
        staff_score = max(0.0, (15.0 - ratio_deviation)) / 15.0 * 15.0

        total_score = cgpa_score + att_score + plc_score + staff_score
        return round(min(100.0, total_score), 2)

    @classmethod
    def generate_campus_kpi_overview(cls, data_context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate executive KPI snapshot for campus administration.
        """
        total_students = data_context.get("total_students", 2450)
        total_faculty = data_context.get("total_faculty", 180)
        total_courses = data_context.get("total_courses", 95)
        total_fees_collected = data_context.get("total_fees_collected", 18500000.0)
        total_fees_pending = data_context.get("total_fees_pending", 3200000.0)
        placement_offers = data_context.get("placement_offers", 145)
        avg_campus_cgpa = data_context.get("avg_campus_cgpa", 7.84)
        avg_campus_attendance = data_context.get("avg_campus_attendance", 83.5)

        fs_ratio = cls.calculate_faculty_student_ratio(total_students, total_faculty)
        collection_rate = (
            (total_fees_collected / (total_fees_collected + total_fees_pending) * 100.0)
            if (total_fees_collected + total_fees_pending) > 0 else 0.0
        )

        return {
            "total_students": total_students,
            "total_faculty": total_faculty,
            "total_courses": total_courses,
            "faculty_student_ratio": f"1:{fs_ratio}",
            "avg_campus_cgpa": avg_campus_cgpa,
            "avg_campus_attendance_pct": avg_campus_attendance,
            "total_fees_collected": total_fees_collected,
            "total_fees_pending": total_fees_pending,
            "fee_collection_rate_pct": round(collection_rate, 2),
            "placement_offers_count": placement_offers,
            "institutional_health_index": round((avg_campus_cgpa * 10 + avg_campus_attendance + collection_rate) / 3, 1)
        }

    @classmethod
    def compute_cohort_retention(cls, cohort_year: int, annual_enrollments: List[int]) -> Dict[str, Any]:
        """
        Compute year-over-year cohort retention rates for 4-year undergraduate degree.
        """
        if not annual_enrollments:
            return {"cohort_year": cohort_year, "retention_rates": [], "overall_retention": 0.0}

        base_enrollment = annual_enrollments[0]
        if base_enrollment <= 0:
            return {"cohort_year": cohort_year, "retention_rates": [], "overall_retention": 0.0}

        retention_rates = []
        for year_idx, count in enumerate(annual_enrollments):
            rate = round((count / base_enrollment) * 100.0, 2)
            retention_rates.append({
                "year_index": year_idx + 1,
                "label": f"Year {year_idx + 1}",
                "enrolled_count": count,
                "retention_rate_pct": rate
            })

        final_retention = retention_rates[-1]["retention_rate_pct"] if retention_rates else 0.0

        return {
            "cohort_year": cohort_year,
            "initial_enrollment": base_enrollment,
            "retention_curve": retention_rates,
            "overall_graduation_retention_pct": final_retention
        }
