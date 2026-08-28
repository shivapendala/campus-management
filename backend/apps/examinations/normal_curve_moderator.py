"""
EduCore Framework - Normal Curve Marks Moderator

Applies dynamic Gaussian and Z-score translation scaling methodologies
to moderate raw class scores towards normal university target spreads.
"""

import math
from typing import Dict, List, Any

class NormalCurveModerator:
    def __init__(self, course_code: str, target_mean: float = 60.0, target_std_dev: float = 10.0):
        self.course_code = course_code
        self.target_mean = target_mean
        self.target_std_dev = target_std_dev
        self.audit_trail: List[str] = []

    def calculate_stats(self, scores: List[float]) -> Dict[str, float]:
        n = len(scores)
        if n == 0:
            return {"mean": 0.0, "variance": 0.0, "std_dev": 0.0}
            
        mean = sum(scores) / n
        variance = sum((x - mean) ** 2 for x in scores) / n
        std_dev = math.sqrt(variance)
        
        return {
            "mean": round(mean, 2),
            "variance": round(variance, 2),
            "std_dev": round(std_dev, 2)
        }

    def moderate_scores(self, raw_scores: List[float], max_marks: float) -> Dict[str, Any]:
        """
        Applies a normal curve transformation to translate scores.
        """
        stats = self.calculate_stats(raw_scores)
        mean = stats["mean"]
        std_dev = stats["std_dev"]
        
        moderated: List[float] = []
        for x in raw_scores:
            if std_dev == 0:
                y = x + (self.target_mean - mean)
            else:
                z = (x - mean) / std_dev
                y = (z * self.target_std_dev) + self.target_mean
                
            # Clamp between 0.0 and max_marks
            y_clamped = max(0.0, min(y, max_marks))
            moderated.append(round(y_clamped, 2))
            
        mod_stats = self.calculate_stats(moderated)
        self.audit_trail.append(
            f"Moderation Complete: Transformed {len(raw_scores)} scores. Mean shifted from {mean} to {mod_stats['mean']}."
        )
        
        return {
            "original_stats": stats,
            "moderated_stats": mod_stats,
            "moderated_scores": moderated,
            "audit_trail": self.audit_trail
        }
