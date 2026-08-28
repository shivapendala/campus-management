"""
EduCore Framework - Examination Paper Moderation & Difficulty Balancer

Analyzes cognitive complexity metrics based on Bloom's Taxonomy, marks distribution,
and applies normal curve marks moderation adjustment models for examination boards.
"""

import math
from typing import Dict, List, Any

class ExaminationModerationEngine:
    def __init__(self, course_code: str, exam_type: str, total_marks: float):
        self.course_code = course_code
        self.exam_type = exam_type
        self.total_marks = total_marks
        self.question_paper_blueprint: List[Dict[str, Any]] = []

    def add_blueprint_question(self, q_id: str, marks: float, blooms_level: str, co_mapped: str) -> None:
        """
        Blooms level can be: L1 (Remember), L2 (Understand), L3 (Apply), L4 (Analyze), L5 (Evaluate), L6 (Create)
        """
        self.question_paper_blueprint.append({
            "q_id": q_id,
            "marks": marks,
            "blooms_level": blooms_level,
            "co_mapped": co_mapped
        })

    def analyze_cognitive_distribution(self) -> Dict[str, Dict[str, Any]]:
        """
        Checks the weightage distribution across low-order (L1, L2) and high-order (L3-L6) cognitive skills.
        Recommended targets: L1-L2 (40%), L3-L4 (40%), L5-L6 (20%)
        """
        total_weight = 0.0
        cognitive_sums: Dict[str, float] = {"L1": 0.0, "L2": 0.0, "L3": 0.0, "L4": 0.0, "L5": 0.0, "L6": 0.0}
        
        for q in self.question_paper_blueprint:
            blooms = q["blooms_level"]
            marks = q["marks"]
            total_weight += marks
            cognitive_sums[blooms] = cognitive_sums.get(blooms, 0.0) + marks
            
        results: Dict[str, Dict[str, Any]] = {}
        for level, sum_marks in cognitive_sums.items():
            pct = (sum_marks / total_weight * 100.0) if total_weight > 0 else 0.0
            results[level] = {
                "marks_allocated": sum_marks,
                "percentage_weight": round(pct, 2)
            }
            
        return results

    def simulate_marks_moderation(self, raw_marks_list: List[float], target_mean: float = 65.0, target_std_dev: float = 12.0) -> Dict[str, Any]:
        """
        Applies a Gaussian (normal curve) translation algorithm to moderate marks,
        ensuring they match target distribution metrics while capping grades at total exam marks.
        """
        if not raw_marks_list:
            return {"moderated_marks": [], "metrics": {}}
            
        n = len(raw_marks_list)
        raw_mean = sum(raw_marks_list) / n
        
        # Calculate raw standard deviation
        variance = sum((x - raw_mean) ** 2 for x in raw_marks_list) / n
        raw_std_dev = math.sqrt(variance)
        
        moderated_marks: List[float] = []
        for x in raw_marks_list:
            if raw_std_dev == 0:
                # If zero variance, shift linearly to target mean
                y = x + (target_mean - raw_mean)
            else:
                # Standardize to normal distribution, then scale to target parameters
                z_score = (x - raw_mean) / raw_std_dev
                y = (z_score * target_std_dev) + target_mean
                
            # Clamp between 0.0 and maximum exam marks
            y_clamped = max(0.0, min(y, self.total_marks))
            moderated_marks.append(round(y_clamped, 2))
            
        # Calculate new metrics
        mod_mean = sum(moderated_marks) / n
        mod_variance = sum((x - mod_mean) ** 2 for x in moderated_marks) / n
        mod_std_dev = math.sqrt(mod_variance)
        
        return {
            "moderated_marks": moderated_marks,
            "metrics": {
                "raw_mean": round(raw_mean, 2),
                "raw_std_dev": round(raw_std_dev, 2),
                "moderated_mean": round(mod_mean, 2),
                "moderated_std_dev": round(mod_std_dev, 2)
            }
        }
