"""
EduCore Framework - WiFi AP Signature Tracker

Validates student device login logs against Access Point location registers.
"""

from datetime import datetime
from typing import Dict, List, Any

class WiFiSignatureTracker:
    def __init__(self):
        self.ap_registry: Dict[str, str] = {}  # MAC -> AP Location Description
        self.signature_logs: List[Dict[str, Any]] = []

    def register_access_point(self, ap_mac: str, location_desc: str) -> None:
        self.ap_registry[ap_mac] = location_desc

    def log_signature(self, student_id: str, ap_mac: str, ip_addr: str) -> None:
        location = self.ap_registry.get(ap_mac, "UNKNOWN_AP")
        self.signature_logs.append({
            "student_id": student_id,
            "ap_mac": ap_mac,
            "location": location,
            "ip_address": ip_addr,
            "timestamp": datetime.now()
        })

    def get_student_footprint(self, student_id: str) -> List[Dict[str, Any]]:
        """
        Retrieves all login logs for a specific student.
        """
        return [log for log in self.signature_logs if log["student_id"] == student_id]

    def verify_classroom_congruence(self, student_id: str, expected_room: str, time_window: datetime) -> bool:
        """
        Verifies if the student was connected to the AP of the expected room within the time window.
        """
        logs = self.get_student_footprint(student_id)
        for log in logs:
            if log["location"] == expected_room:
                # Check simple time interval logic
                delta = abs((log["timestamp"] - time_window).total_seconds())
                if delta <= 1800:  # 30-minute window margin
                    return True
        return False
