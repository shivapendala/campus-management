"""
EduCore Enterprise Framework - Faculty Performance Appraisal System (PBAS/API)

Implements UGC / AICTE Academic Performance Indicator (API) score calculator:
- Category I: Teaching, Learning and Evaluation (Max: 100 API points)
- Category II: Co-Curricular, Extension and Professional Development (Max: 50 API points)
- Category III: Research and Academic Contributions (Max: 150 API points)
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class FacultyAppraisalScore:
    """Represents an annual faculty appraisal outcome."""
    faculty_id: int
    faculty_name: str
    academic_year: str
    cat1_teaching_score: float  # Max 100
    cat2_governance_score: float  # Max 50
    cat3_research_score: float  # Max 150
    total_api_score: float  # Max 300
    appraisal_band: str  # OUTSTANDING, VERY_GOOD, GOOD, SATISFACTORY, NEEDS_IMPROVEMENT
    student_feedback_rating: float  # 1.0 to 5.0 scale
    promotion_eligible: bool = False
    comments: str = ""


class FacultyAppraisalEngine:
    """
    Computes annual API scores and evaluates career advancement scheme (CAS) promotion eligibility.
    """

    @classmethod
    def calculate_annual_appraisal(
        cls,
        faculty_id: int,
        name: str,
        academic_year: str,
        syllabus_coverage_pct: float,
        student_feedback_score: float,  # out of 5.0
        fdp_attended_days: int,
        committee_roles_count: int,
        journal_papers_count: int,
        conference_papers_count: int,
        research_grants_amount: float,  # in INR
        phd_students_guided: int
    ) -> FacultyAppraisalScore:
        """Calculate complete API score across all 3 statutory categories."""

        # Category I: Teaching (Max: 100)
        # Syllabus coverage (up to 50 pts) + Student feedback (up to 50 pts)
        teaching_cov_pts = min(50.0, (syllabus_coverage_pct / 100.0) * 50.0)
        feedback_pts = min(50.0, (student_feedback_score / 5.0) * 50.0)
        cat1_score = round(teaching_cov_pts + feedback_pts, 1)

        # Category II: Governance & Extension (Max: 50)
        # FDP days (5 pts/day, max 25) + Committee roles (10 pts/role, max 25)
        fdp_pts = min(25.0, fdp_attended_days * 5.0)
        comm_pts = min(25.0, committee_roles_count * 10.0)
        cat2_score = round(fdp_pts + comm_pts, 1)

        # Category III: Research (Max: 150)
        # Journals (25 pts each) + Conferences (10 pts each) + Grants (1 pt per 50,000 INR) + PhD guided (15 pts each)
        journal_pts = journal_papers_count * 25.0
        conf_pts = conference_papers_count * 10.0
        grant_pts = min(40.0, (research_grants_amount / 50000.0) * 1.0)
        phd_pts = phd_students_guided * 15.0
        cat3_score = round(min(150.0, journal_pts + conf_pts + grant_pts + phd_pts), 1)

        total_api = round(cat1_score + cat2_score + cat3_score, 1)

        # Classify Band
        if total_api >= 240.0:
            band = "OUTSTANDING"
            promo = True
        elif total_api >= 190.0:
            band = "VERY GOOD"
            promo = True
        elif total_api >= 140.0:
            band = "GOOD"
            promo = False
        elif total_api >= 100.0:
            band = "SATISFACTORY"
            promo = False
        else:
            band = "NEEDS IMPROVEMENT"
            promo = False

        return FacultyAppraisalScore(
            faculty_id=faculty_id,
            faculty_name=name,
            academic_year=academic_year,
            cat1_teaching_score=cat1_score,
            cat2_governance_score=cat2_score,
            cat3_research_score=cat3_score,
            total_api_score=total_api,
            appraisal_band=band,
            student_feedback_rating=round(student_feedback_score, 2),
            promotion_eligible=promo,
            comments=f"Evaluated for CAS Promotion. Total API: {total_api}/300 points."
        )
