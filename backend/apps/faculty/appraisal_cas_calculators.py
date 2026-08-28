"""
EduCore Framework - UGC Career Advancement Scheme (CAS) Appraisal Calculator

Provides business logic for computing APIs (Academic Performance Indicators)
and PBAS (Performance Based Appraisal System) scores according to UGC guidelines.
"""

from typing import Dict, List, Any

class UGCAppraisalCalculator:
    def __init__(self, faculty_id: str, current_designation: str, department: str):
        self.faculty_id = faculty_id
        self.current_designation = current_designation
        self.department = department
        self.category_1_teaching_hours = 0.0
        self.category_2_administrative_activities: List[Dict[str, Any]] = []
        self.category_3_research_publications: List[Dict[str, Any]] = []
        self.category_3_grants: List[Dict[str, Any]] = []

    def record_teaching_workload(self, target_hours: float, actual_hours: float) -> float:
        """
        Teaching and classes workload score calculation.
        Target hours are normalized to typical UGC minimums (16/14/14).
        """
        self.category_1_teaching_hours = actual_hours
        if target_hours == 0:
            return 0.0
        ratio = actual_hours / target_hours
        score = min(ratio * 50.0, 50.0)  # Max score capping at 50 points
        return round(score, 2)

    def add_administrative_charge(self, activity_name: str, hours_spent: float, level: str) -> None:
        """
        Record institutional and administrative contributions like HOD, Warden, Coordinator etc.
        """
        self.category_2_administrative_activities.append({
            "activity_name": activity_name,
            "hours_spent": hours_spent,
            "level": level
        })

    def calculate_category_2_score(self) -> float:
        """
        Calculate Category II score for co-curricular, extension, and professional activities.
        UGC caps this score at 45 points.
        """
        score = 0.0
        for act in self.category_2_administrative_activities:
            if act["level"] == "INSTITUTIONAL_DEAN_HOD":
                score += min(act["hours_spent"] * 0.5, 20.0)
            elif act["level"] == "DEPARTMENT_COORDINATOR":
                score += min(act["hours_spent"] * 0.3, 15.0)
            else:
                score += min(act["hours_spent"] * 0.2, 10.0)
        return min(score, 45.0)

    def add_research_publication(self, title: str, journal_type: str, first_author: bool, impact_factor: float) -> None:
        """
        Record peer-reviewed publications.
        - UGC Care List: 10 points
        - Scopus/Web of Science: 15 points
        - Additional weight based on JCR impact factor
        """
        self.category_3_research_publications.append({
            "title": title,
            "journal_type": journal_type,
            "first_author": first_author,
            "impact_factor": impact_factor
        })

    def calculate_research_publications_score(self) -> float:
        score = 0.0
        for pub in self.category_3_research_publications:
            base_points = 0.0
            if pub["journal_type"] == "SCOPUS_WOS":
                base_points = 15.0
            elif pub["journal_type"] == "UGC_CARE":
                base_points = 10.0
            else:
                base_points = 5.0
                
            # Impact factor scaling modifiers
            if pub["impact_factor"] > 10.0:
                base_points += 30.0
            elif pub["impact_factor"] > 5.0:
                base_points += 25.0
            elif pub["impact_factor"] > 2.0:
                base_points += 15.0
            elif pub["impact_factor"] > 0.5:
                base_points += 10.0
                
            # Author distribution points
            if not pub["first_author"]:
                base_points = base_points * 0.6  # Secondary author gets 60%
                
            score += base_points
        return round(score, 2)

    def add_research_grant(self, project_title: str, amount_in_lakhs: float, role: str) -> None:
        self.category_3_grants.append({
            "project_title": project_title,
            "amount_in_lakhs": amount_in_lakhs,
            "role": role
        })

    def calculate_research_grants_score(self) -> float:
        score = 0.0
        for grant in self.category_3_grants:
            if grant["role"] == "PRINCIPAL_INVESTIGATOR":
                if grant["amount_in_lakhs"] > 10.0:
                    score += 20.0
                else:
                    score += 15.0
            else:
                if grant["amount_in_lakhs"] > 10.0:
                    score += 10.0
                else:
                    score += 5.0
        return score

    def compile_full_appraisal(self, target_hours: float, actual_hours: float) -> Dict[str, Any]:
        cat1 = self.record_teaching_workload(target_hours, actual_hours)
        cat2 = self.calculate_category_2_score()
        cat3_pub = self.calculate_research_publications_score()
        cat3_grant = self.calculate_research_grants_score()
        total_pbas = cat1 + cat2 + cat3_pub + cat3_grant
        
        return {
            "faculty_id": self.faculty_id,
            "designation": self.current_designation,
            "teaching_attainment_score": cat1,
            "co_curricular_score": cat2,
            "research_publications_score": cat3_pub,
            "research_grants_score": cat3_grant,
            "total_pbas_score": round(total_pbas, 2)
        }
