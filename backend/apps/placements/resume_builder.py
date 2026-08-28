"""
EduCore Enterprise Framework - Standardized University Placement Resume Builder

Generates ATS-friendly structured resumes for campus recruitment:
Calculates keyword density score against target job description (e.g. Python, SQL, React, AWS, Docker).
"""

import re
from typing import Dict, List, Any, Optional, Set, Tuple
from dataclasses import dataclass, field


@dataclass
class StudentResumeProfile:
    """Represents a standardized student placement resume."""
    student_roll: str
    full_name: str
    email: str
    phone: str
    github_url: Optional[str]
    linkedin_url: Optional[str]
    cgpa: float
    skills: List[str]
    projects: List[Dict[str, str]]
    experience: List[Dict[str, str]]
    certifications: List[str]


class PlacementResumeBuilder:
    """
    Computes ATS compatibility score against corporate job descriptions.
    """

    @classmethod
    def evaluate_ats_keyword_match(
        cls,
        resume: StudentResumeProfile,
        job_description_text: str
    ) -> Tuple[float, List[str], List[str]]:
        """
        Compute keyword match percentage between resume skills/projects and JD.
        Returns: (match_score_pct, matched_keywords, missing_keywords)
        """
        jd_clean = job_description_text.lower()
        matched = []
        missing = []

        for skill in resume.skills:
            if skill.lower() in jd_clean:
                matched.append(skill)
            else:
                missing.append(skill)

        total_skills = len(resume.skills)
        match_score = (len(matched) / total_skills * 100.0) if total_skills > 0 else 0.0

        return round(match_score, 1), matched, missing
