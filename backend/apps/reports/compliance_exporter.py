"""
EduCore Enterprise Framework - Statutory Higher-Education Compliance Data Packager

Formats regulatory data for statutory Indian & Global regulatory submissions:
- AICTE Web Portal Faculty & Student Annual Intake Tables
- UGC / AISHE (All India Survey on Higher Education) Form Data Exporter
- NIRF (National Institutional Ranking Framework) Metric Bundles
"""

from typing import Dict, List, Any, Optional


class StatutoryCompliancePackager:
    """
    Constructs normalized regulatory datasets for accreditation filings.
    """

    @classmethod
    def generate_aishe_survey_bundle(
        cls,
        institution_code: str,
        academic_year: str,
        student_demographics: Dict[str, Any],
        faculty_roster: List[Dict[str, Any]],
        infrastructure_stats: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Format AISHE Survey XML/JSON data payload."""
        total_enrolled = student_demographics.get("total_students", 2450)
        male_count = student_demographics.get("male_students", 1470)
        female_count = student_demographics.get("female_students", 980)

        total_faculty = len(faculty_roster)
        phd_faculty = sum(1 for f in faculty_roster if f.get("highest_degree") == "Ph.D.")

        return {
            "survey_header": {
                "aishe_code": f"C-{institution_code}",
                "academic_year": academic_year,
                "institution_type": "ENGINEERING_AND_TECHNOLOGY_AUTONOMOUS"
            },
            "student_enrolment_table": {
                "total_enrolled": total_enrolled,
                "male_enrolled": male_count,
                "female_enrolled": female_count,
                "gender_parity_index": round(female_count / male_count, 2) if male_count > 0 else 1.0,
                "sc_st_enrolled": student_demographics.get("sc_st_count", 380),
                "obc_enrolled": student_demographics.get("obc_count", 1120),
                "general_enrolled": student_demographics.get("general_count", 950)
            },
            "teaching_staff_table": {
                "total_regular_faculty": total_faculty,
                "faculty_with_phd": phd_faculty,
                "phd_percentage": round((phd_faculty / total_faculty * 100.0), 2) if total_faculty > 0 else 0.0,
                "student_teacher_ratio": round(total_enrolled / total_faculty, 1) if total_faculty > 0 else 0.0
            },
            "infrastructure_summary": infrastructure_stats
        }

    @classmethod
    def generate_nirf_ranking_metrics(
        cls,
        teaching_learning_score: float,
        research_score: float,
        graduation_outcome_score: float,
        outreach_inclusivity_score: float,
        perception_score: float
    ) -> Dict[str, Any]:
        """
        Compute composite NIRF score out of 100:
        - TLR (Teaching, Learning & Resources): 30%
        - RPC (Research and Professional Practice): 30%
        - GO (Graduation Outcomes): 20%
        - OI (Outreach and Inclusivity): 10%
        - PR (Perception): 10%
        """
        tlr_weighted = (min(100.0, teaching_learning_score) / 100.0) * 30.0
        rpc_weighted = (min(100.0, research_score) / 100.0) * 30.0
        go_weighted = (min(100.0, graduation_outcome_score) / 100.0) * 20.0
        oi_weighted = (min(100.0, outreach_inclusivity_score) / 100.0) * 10.0
        pr_weighted = (min(100.0, perception_score) / 100.0) * 10.0

        total_nirf = tlr_weighted + rpc_weighted + go_weighted + oi_weighted + pr_weighted

        return {
            "total_nirf_score": round(total_nirf, 2),
            "tlr_score_30": round(tlr_weighted, 2),
            "rpc_score_30": round(rpc_weighted, 2),
            "go_score_20": round(go_weighted, 2),
            "oi_score_10": round(oi_weighted, 2),
            "pr_score_10": round(pr_weighted, 2),
            "projected_rank_band": "Top 50" if total_nirf >= 65.0 else ("Top 100" if total_nirf >= 50.0 else "Top 200")
        }
