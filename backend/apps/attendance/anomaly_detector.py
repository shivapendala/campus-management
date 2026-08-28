"""
EduCore Enterprise Framework - Attendance Anomaly & Mass Absenteeism Detector

Analyzes section-level attendance time-series to detect statistical anomalies:
Mass bunk events, sudden drops following holidays, or anomalous 100% attendance spikes.
"""

from typing import Dict, List, Any, Optional
import statistics


class AttendanceAnomalyDetector:
    """
    Flags unusual batch absenteeism or statistical outliers in lecture attendance.
    """

    @classmethod
    def detect_batch_anomalies(
        cls,
        section_name: str,
        subject_name: str,
        historical_daily_turnout_pct: List[float],
        current_session_turnout_pct: float
    ) -> Dict[str, Any]:
        """
        Detect whether current session turnout deviates significantly from rolling mean (Z-Score > 2.0).
        """
        if not historical_daily_turnout_pct or len(historical_daily_turnout_pct) < 3:
            return {
                "is_anomaly": False,
                "anomaly_type": "INSUFFICIENT_DATA",
                "current_turnout_pct": current_session_turnout_pct,
                "z_score": 0.0
            }

        mean_val = statistics.mean(historical_daily_turnout_pct)
        std_val = statistics.stdev(historical_daily_turnout_pct)

        if std_val == 0.0:
            std_val = 1.0  # Prevent division by zero

        z_score = (current_session_turnout_pct - mean_val) / std_val

        # Detect Mass Bunk (Sudden drop where turnout < 35% and z-score < -2.0)
        if current_session_turnout_pct < 35.0 and z_score <= -2.0:
            is_anomaly = True
            anomaly_type = "MASS_BUNK_DETECTED"
            severity = "HIGH"
            description = f"Sudden mass absenteeism ({current_session_turnout_pct:.1f}% vs {mean_val:.1f}% normal average)."
        # Detect proxy inflation (100% turnout with z-score > 2.5)
        elif current_session_turnout_pct >= 99.0 and mean_val < 70.0:
            is_anomaly = True
            anomaly_type = "SUSPICIOUS_HIGH_TURNOUT"
            severity = "MODERATE"
            description = "Unusually high 100% attendance recorded compared to past average."
        else:
            is_anomaly = False
            anomaly_type = "NORMAL_FLUCTUATION"
            severity = "NONE"
            description = "Attendance is within normal statistical distribution."

        return {
            "section_name": section_name,
            "subject_name": subject_name,
            "current_turnout_pct": current_session_turnout_pct,
            "historical_mean_pct": round(mean_val, 2),
            "historical_std_dev": round(std_val, 2),
            "z_score": round(z_score, 2),
            "is_anomaly": is_anomaly,
            "anomaly_type": anomaly_type,
            "severity": severity,
            "description": description
        }
