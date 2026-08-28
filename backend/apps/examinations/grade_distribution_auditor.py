"""
EduCore Framework - Grade Distribution Auditor

Audits grade distribution charts and checks for variance deviations.
"""

import math
from typing import Dict, List, Any

class GradeDistributionAuditor:
    def __init__(self, course_code: str):
        self.course_code = course_code
        self.anomalies: List[str] = []

    def verify_distribution_variance(self, gpa_list: List[float], expected_mean: float = 6.5) -> Dict[str, Any]:
        n = len(gpa_list)
        if n == 0:
            return {"skewness": 0.0, "normal": True}
            
        mean = sum(gpa_list) / n
        variance = sum((x - mean) ** 2 for x in gpa_list) / n
        std_dev = math.sqrt(variance)
        
        # Calculate skewness indicator
        skewness = 0.0
        if std_dev > 0:
            skewness = sum((x - mean) ** 3 for x in gpa_list) / (n * (std_dev ** 3))
            
        is_skewed = abs(skewness) > 1.0
        if is_skewed:
            self.anomalies.append(f"High skewness detected: {skewness:.2f}")
            
        return {
            "mean_gpa": round(mean, 2),
            "std_dev_gpa": round(std_dev, 2),
            "skewness": round(skewness, 2),
            "normal_distribution": not is_skewed,
            "anomalies": self.anomalies
        }
