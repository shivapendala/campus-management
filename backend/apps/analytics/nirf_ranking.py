"""
EduCore Enterprise Framework - National Institutional Ranking Framework (NIRF) 5-Parameter BI Engine

Calculates institutional NIRF score across 5 statutory parameters (Total: 100 Marks):
1. Teaching, Learning & Resources (TLR - 30 Marks): Student strength, faculty-student ratio (FSR), faculty cadre & PhD qualifications.
2. Research and Professional Practice (RPC - 30 Marks): Scopus/Web of Science publications, citations per paper, funded projects, patents.
3. Graduation Outcomes (GO - 20 Marks): Metric for university examinations (GUE), median placement salary (GMS), higher studies track.
4. Outreach and Inclusivity (OI - 10 Marks): Region diversity (RD), women diversity (WD), economically/socially challenged students (ESCS), physically challenged facilities (PCS).
5. Perception (PR - 10 Marks): Academic peers and employer survey perception index.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class NIRFInputParameters:
    """Institutional raw telemetry metrics for NIRF computation."""
    total_sanctioned_approved_intake: int = 2400
    total_enrolled_students: int = 2350
    total_phd_students_enrolled: int = 120
    full_time_faculty_count: int = 160
    faculty_with_phd_count: int = 128  # 80%
    faculty_with_experience_over_8yrs: int = 110
    total_scopus_publications_3yrs: int = 420
    total_scopus_citations_3yrs: int = 2150
    sponsored_research_grants_3yrs_inr: float = 45000000.0  # Rs. 4.50 Cr
    consultancy_projects_3yrs_inr: float = 18500000.0  # Rs. 1.85 Cr
    patents_published_3yrs: int = 18
    patents_granted_3yrs: int = 6
    graduating_students_count: int = 580
    placed_students_count: int = 485
    median_placement_salary_lpa: float = 9.8
    higher_studies_admitted_count: int = 65
    students_from_outside_state: int = 480
    students_from_outside_country: int = 25
    female_students_count: int = 890
    female_faculty_count: int = 58
    economically_backward_scholarship_students: int = 420
    barrier_free_infrastructure_score: float = 20.0  # Out of 20
    peer_perception_score_100: float = 78.5


class NIRFRankingEvaluationEngine:
    """
    Computes NIRF Overall and Engineering category benchmark scores.
    """

    @classmethod
    def compute_tlr_score(cls, p: NIRFInputParameters) -> Tuple[float, Dict[str, float]]:
        """
        Teaching, Learning & Resources (TLR - Max 30 Marks):
        - SS (Student Strength): 20 marks
        - FSR (Faculty-Student Ratio): 30 marks (Norm 1:15)
        - FQ (Faculty Qualification & Experience): 20 marks
        - FRU (Financial Resources Utilization): 30 marks
        Normalized to 30.
        """
        # Student Strength (SS) - Max 20
        ss_score = min(20.0, (p.total_enrolled_students / p.total_sanctioned_approved_intake) * 18.0 + (p.total_phd_students_enrolled / 100.0) * 2.0)

        # FSR - Max 30 (Ideal 1:15)
        ratio = p.total_enrolled_students / p.full_time_faculty_count if p.full_time_faculty_count > 0 else 30.0
        fsr_score = min(30.0, max(0.0, 30.0 * (15.0 / ratio))) if ratio > 0 else 0.0

        # Faculty Qualification (FQ) - Max 20
        phd_ratio = p.faculty_with_phd_count / p.full_time_faculty_count if p.full_time_faculty_count > 0 else 0.0
        fq_score = phd_ratio * 20.0

        # Financial Utilization (FRU) - Max 30
        fru_score = 26.5  # Standard accredited high-performing institution benchmark

        raw_tlr = (ss_score + fsr_score + fq_score + fru_score)  # Out of 100
        normalized_tlr = (raw_tlr / 100.0) * 30.0  # Weighted to 30

        return round(normalized_tlr, 2), {
            "student_strength_ss": round(ss_score, 2),
            "faculty_student_ratio_fsr": round(fsr_score, 2),
            "faculty_qualification_fq": round(fq_score, 2),
            "financial_utilization_fru": fru_score,
            "weighted_tlr_score": round(normalized_tlr, 2)
        }

    @classmethod
    def compute_rpc_score(cls, p: NIRFInputParameters) -> Tuple[float, Dict[str, float]]:
        """
        Research and Professional Practice (RPC - Max 30 Marks):
        - PU (Combined Metric for Publications): 35 marks
        - QP (Quality of Publications / Citations): 35 marks
        - IPR (Patents Granted & Published): 15 marks
        - FPPP (Footprint of Projects & Professional Practice): 15 marks
        """
        fac = p.full_time_faculty_count
        pu_score = min(35.0, (p.total_scopus_publications_3yrs / (fac * 3.0)) * 35.0)
        citations_per_pub = p.total_scopus_citations_3yrs / p.total_scopus_publications_3yrs if p.total_scopus_publications_3yrs > 0 else 0.0
        qp_score = min(35.0, (citations_per_pub / 6.0) * 35.0)

        ipr_score = min(15.0, (p.patents_published_3yrs * 0.5 + p.patents_granted_3yrs * 2.0))
        fppp_score = min(15.0, (p.sponsored_research_grants_3yrs_inr / 50000000.0) * 10.0 + (p.consultancy_projects_3yrs_inr / 20000000.0) * 5.0)

        raw_rpc = pu_score + qp_score + ipr_score + fppp_score
        normalized_rpc = (raw_rpc / 100.0) * 30.0

        return round(normalized_rpc, 2), {
            "publications_metric_pu": round(pu_score, 2),
            "quality_citations_qp": round(qp_score, 2),
            "patents_metric_ipr": round(ipr_score, 2),
            "projects_fppp": round(fppp_score, 2),
            "weighted_rpc_score": round(normalized_rpc, 2)
        }

    @classmethod
    def compute_graduation_outcome_score(cls, p: NIRFInputParameters) -> Tuple[float, Dict[str, float]]:
        """
        Graduation Outcomes (GO - Max 20 Marks):
        - GUE (University Exams Passing Rate): 60 marks
        - GMS (Median Salary Placement): 40 marks
        """
        pass_rate = (p.graduating_students_count / (p.total_enrolled_students / 4.0)) if p.total_enrolled_students > 0 else 0.95
        gue_score = min(60.0, pass_rate * 60.0)

        placement_rate = (p.placed_students_count + p.higher_studies_admitted_count) / p.graduating_students_count if p.graduating_students_count > 0 else 0.8
        salary_factor = min(1.0, p.median_placement_salary_lpa / 12.0)
        gms_score = min(40.0, placement_rate * salary_factor * 40.0)

        raw_go = gue_score + gms_score
        normalized_go = (raw_go / 100.0) * 20.0

        return round(normalized_go, 2), {
            "university_exams_gue": round(gue_score, 2),
            "placement_salary_gms": round(gms_score, 2),
            "weighted_go_score": round(normalized_go, 2)
        }

    @classmethod
    def compute_outreach_inclusivity_score(cls, p: NIRFInputParameters) -> Tuple[float, Dict[str, float]]:
        """
        Outreach and Inclusivity (OI - Max 10 Marks):
        - RD (Regional Diversity): 30 marks
        - WD (Women Diversity): 30 marks
        - ESCS (Economically & Socially Challenged): 20 marks
        - PCS (Physically Challenged Facilities): 20 marks
        """
        total = p.total_enrolled_students
        outside_pct = (p.students_from_outside_state + p.students_from_outside_country) / total if total > 0 else 0.0
        rd_score = min(30.0, (outside_pct / 0.30) * 30.0)

        female_pct = p.female_students_count / total if total > 0 else 0.0
        wd_score = min(30.0, (female_pct / 0.40) * 30.0)

        escs_pct = p.economically_backward_scholarship_students / total if total > 0 else 0.0
        escs_score = min(20.0, (escs_pct / 0.20) * 20.0)
        pcs_score = p.barrier_free_infrastructure_score

        raw_oi = rd_score + wd_score + escs_score + pcs_score
        normalized_oi = (raw_oi / 100.0) * 10.0

        return round(normalized_oi, 2), {
            "region_diversity_rd": round(rd_score, 2),
            "women_diversity_wd": round(wd_score, 2),
            "economically_challenged_escs": round(escs_score, 2),
            "facilities_pcs": round(pcs_score, 2),
            "weighted_oi_score": round(normalized_oi, 2)
        }

    @classmethod
    def compute_perception_score(cls, p: NIRFInputParameters) -> Tuple[float, Dict[str, float]]:
        """
        Perception (PR - Max 10 Marks):
        - Academic Peers and Employer Perception Survey Index
        """
        normalized_pr = (p.peer_perception_score_100 / 100.0) * 10.0
        return round(normalized_pr, 2), {
            "peer_perception_score_100": p.peer_perception_score_100,
            "weighted_pr_score": round(normalized_pr, 2)
        }

    @classmethod
    def evaluate_full_nirf_score(cls, p: Optional[NIRFInputParameters] = None) -> Dict[str, Any]:
        """
        Calculate grand total composite NIRF score out of 100 and forecast national ranking band.
        """
        params = p or NIRFInputParameters()

        tlr_val, tlr_breakdown = cls.compute_tlr_score(params)
        rpc_val, rpc_breakdown = cls.compute_rpc_score(params)
        go_val, go_breakdown = cls.compute_graduation_outcome_score(params)
        oi_val, oi_breakdown = cls.compute_outreach_inclusivity_score(params)
        pr_val, pr_breakdown = cls.compute_perception_score(params)

        grand_total = round(tlr_val + rpc_val + go_val + oi_val + pr_val, 2)

        if grand_total >= 75.0:
            ranking_band = "Top 25 National Band (Tier 1)"
        elif grand_total >= 65.0:
            ranking_band = "Rank 26 - 50 National Band"
        elif grand_total >= 55.0:
            ranking_band = "Rank 51 - 100 National Band"
        elif grand_total >= 45.0:
            ranking_band = "Rank 101 - 150 National Band"
        else:
            ranking_band = "Rank 151 - 200 Participating Band"

        return {
            "grand_total_nirf_score_100": grand_total,
            "forecasted_ranking_band": ranking_band,
            "parameters": {
                "TLR_Teaching_Learning_Resources": {"score": tlr_val, "max": 30.0, "details": tlr_breakdown},
                "RPC_Research_Professional_Practice": {"score": rpc_val, "max": 30.0, "details": rpc_breakdown},
                "GO_Graduation_Outcomes": {"score": go_val, "max": 20.0, "details": go_breakdown},
                "OI_Outreach_Inclusivity": {"score": oi_val, "max": 10.0, "details": oi_breakdown},
                "PR_Perception": {"score": pr_val, "max": 10.0, "details": pr_breakdown},
            }
        }
