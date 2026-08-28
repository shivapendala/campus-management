"""
EduCore Framework - Outcome Based Education (OBE) Attainment Calculator

Provides data structures, calculations, and validators for direct and indirect attainment metrics,
course outcomes (COs), program outcomes (POs), and program specific outcomes (PSOs).
"""

from typing import Dict, List, Any

class OutcomeAttainmentCalculator:
    def __init__(self, course_id: str, section: str):
        self.course_id = course_id
        self.section = section
        self.co_list: List[str] = []
        self.student_marks: Dict[str, Dict[str, float]] = {}
        self.co_max_marks: Dict[str, Dict[str, float]] = {}
        self.direct_weight: float = 0.8
        self.indirect_weight: float = 0.2

    def setup_co_max_marks(self, assessment_type: str, max_marks_by_co: Dict[str, float]) -> None:
        """
        Set up the maximum marks allocated per Course Outcome for a specific assessment.
        e.g., assessment_type='MID_SEM', max_marks_by_co={'CO1': 15.0, 'CO2': 15.0}
        """
        self.co_max_marks[assessment_type] = max_marks_by_co
        for co in max_marks_by_co.keys():
            if co not in self.co_list:
                self.co_list.append(co)

    def record_student_marks(self, student_id: str, assessment_type: str, marks_by_co: Dict[str, float]) -> None:
        """
        Record a student's marks scored per Course Outcome for a specific assessment.
        """
        if student_id not in self.student_marks:
            self.student_marks[student_id] = {}
        
        for co, score in marks_by_co.items():
            if co not in self.co_list:
                raise ValueError(f"CO '{co}' is not declared in the maximum marks setup.")
            key = f"{assessment_type}_{co}"
            self.student_marks[student_id][key] = score

    def calculate_direct_co_attainment(self, threshold_percentage: float = 60.0) -> Dict[str, Dict[str, Any]]:
        """
        Calculate direct CO attainment percentages.
        Returns percentage of students who scored above the threshold (e.g., >= 60%) of max marks.
        """
        co_attainment_rates: Dict[str, Dict[str, Any]] = {}
        
        for co in self.co_list:
            total_students_attempted = 0
            students_above_threshold = 0
            
            for student_id, assessments in self.student_marks.items():
                total_student_co_score = 0.0
                total_student_co_max = 0.0
                
                for assessment, max_marks_by_co in self.co_max_marks.items():
                    if co in max_marks_by_co:
                        key = f"{assessment}_{co}"
                        student_score = assessments.get(key, 0.0)
                        max_score = max_marks_by_co[co]
                        
                        total_student_co_score += student_score
                        total_student_co_max += max_score
                
                if total_student_co_max > 0:
                    total_students_attempted += 1
                    pct_scored = (total_student_co_score / total_student_co_max) * 100.0
                    if pct_scored >= threshold_percentage:
                        students_above_threshold += 1
            
            attainment_pct = (students_above_threshold / total_students_attempted * 100.0) if total_students_attempted > 0 else 0.0
            
            # Map percentage to standard NBA 3-level scale:
            # >= 70%: Level 3
            # >= 60% and < 70%: Level 2
            # >= 50% and < 60%: Level 1
            # < 50%: Level 0
            attainment_level = 0
            if attainment_pct >= 70.0:
                attainment_level = 3
            elif attainment_pct >= 60.0:
                attainment_level = 2
            elif attainment_pct >= 50.0:
                attainment_level = 1
                
            co_attainment_rates[co] = {
                "attainment_percentage": round(attainment_pct, 2),
                "attainment_level": attainment_level,
                "total_attempted": total_students_attempted,
                "passed_threshold": students_above_threshold
            }
            
        return co_attainment_rates

    def calculate_integrated_attainment(self, direct_attainment: Dict[str, float], indirect_survey_levels: Dict[str, float]) -> Dict[str, float]:
        """
        Combines direct CO attainment levels and indirect survey levels based on institutional weights.
        integrated = (direct * direct_weight) + (indirect * indirect_weight)
        """
        integrated_attainment: Dict[str, float] = {}
        for co in self.co_list:
            dir_level = direct_attainment.get(co, 0.0)
            ind_level = indirect_survey_levels.get(co, 0.0)
            integrated_score = (dir_level * self.direct_weight) + (ind_level * self.indirect_weight)
            integrated_attainment[co] = round(integrated_score, 2)
        return integrated_attainment
