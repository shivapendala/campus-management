"""
EduCore Framework - Grading Rubric & Assessment Validator

Defines, validates, and computes scores for student assignment submissions
based on multi-criteria assessment rubrics.
"""

from typing import Dict, List, Any

class GradingRubricValidator:
    def __init__(self, rubric_id: str, title: str):
        self.rubric_id = rubric_id
        self.title = title
        self.criteria: List[Dict[str, Any]] = []

    def add_criterion(self, name: str, weight: float, max_points: float, description: str = "") -> None:
        """
        Adds a grading criterion (e.g., Code Quality, Documentation, Functionality)
        with specific weights (0.0 to 1.0).
        """
        if not (0.0 <= weight <= 1.0):
            raise ValueError("Weight must be between 0.0 and 1.0.")
        self.criteria.append({
            "name": name,
            "weight": weight,
            "max_points": max_points,
            "description": description
        })

    def validate_weights(self) -> bool:
        """
        Validates that the sum of all criteria weights equals exactly 1.0.
        """
        total_weight = sum(c["weight"] for c in self.criteria)
        return abs(total_weight - 1.0) < 1e-5

    def compute_grade(self, student_scores: Dict[str, float]) -> Dict[str, Any]:
        """
        Computes the final weighted grade based on student scores per criterion.
        student_scores: {'Code Quality': 8.0, 'Documentation': 9.0}
        """
        if not self.validate_weights():
            raise ValueError("Invalid Rubric: Sum of weights must equal 1.0.")
            
        weighted_score = 0.0
        max_possible_weighted = 0.0
        breakdown: Dict[str, Dict[str, Any]] = {}
        
        for c in self.criteria:
            name = c["name"]
            weight = c["weight"]
            max_p = c["max_points"]
            score = student_scores.get(name, 0.0)
            
            if score > max_p:
                score = max_p  # clamp to max points
                
            term_score = score * weight
            term_max = max_p * weight
            
            weighted_score += term_score
            max_possible_weighted += term_max
            
            breakdown[name] = {
                "score_obtained": score,
                "max_points": max_p,
                "weight": weight,
                "weighted_contribution": round(term_score, 2)
            }
            
        overall_percentage = (weighted_score / max_possible_weighted * 100.0) if max_possible_weighted > 0 else 0.0
        
        return {
            "total_weighted_score": round(weighted_score, 2),
            "max_weighted_score": round(max_possible_weighted, 2),
            "overall_percentage": round(overall_percentage, 2),
            "criteria_breakdown": breakdown
        }
