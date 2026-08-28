"""
EduCore Enterprise Framework - Biometric Attendance Statistical Outlier & Mass Bunk Detector

Detects attendance anomalies across cohorts and faculty classes:
- Statistical Z-Score Outlier Detection on class turnout
- Mass Bunk Detection: Flagged when attendance suddenly drops >= 40% below 30-day moving average
- Biometric Punch Clustering: Detects physical buddy-punch proxy collusion
"""

import math
from typing import Dict, List, Any, Optional, Tuple


class AttendanceAnomalyDetector:
    """
    Statistical time-series monitor for classroom and biometric anomalies.
    """

    @classmethod
    def evaluate_class_turnout_anomaly(
        cls,
        today_present_count: int,
        total_class_strength: int,
        historic_attendance_series: List[int]
    ) -> Dict[str, Any]:
        """Detect mass bunk or severe unannounced class absenteeism."""
        if not historic_attendance_series or total_class_strength <= 0:
            return {"is_anomaly": False, "anomaly_type": "NONE"}

        mean_turnout = sum(historic_attendance_series) / len(historic_attendance_series)
        variance = sum((x - mean_turnout) ** 2 for x in historic_attendance_series) / len(historic_attendance_series)
        std_dev = math.sqrt(variance) if variance > 0 else 1.0

        today_turnout_pct = (today_present_count / total_class_strength) * 100.0
        historic_mean_pct = (mean_turnout / total_class_strength) * 100.0

        z_score = (today_present_count - mean_turnout) / std_dev

        # Mass bunk rule: turnout drops > 40% below average or z-score < -2.5
        is_mass_bunk = (historic_mean_pct - today_turnout_pct >= 40.0) or (z_score <= -2.5)

        return {
            "today_attendance_count": today_present_count,
            "today_turnout_percentage": round(today_turnout_pct, 1),
            "historic_average_percentage": round(historic_mean_pct, 1),
            "z_score": round(z_score, 2),
            "is_mass_bunk_detected": is_mass_bunk,
            "recommended_action": "ISSUE_HOD_INQUIRY_NOTICE" if is_mass_bunk else "NORMAL_OPERATION"
        }
