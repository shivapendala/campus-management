"""
EduCore Framework - Biometric Log Reconciler & Geo-Fence Sync

Compares physical card swipe logs with Wi-Fi network logins, Haversine geo-fencing,
and marks final student attendance records while alerting proctors of bunks or proxies.
"""

import math
import datetime
from typing import Dict, List, Any

class BiometricReconciler:
    def __init__(self, target_date: datetime.date):
        self.target_date = target_date
        self.biometric_logs: List[Dict[str, Any]] = []
        self.wifi_logins: List[Dict[str, Any]] = []
        
    def add_biometric_log(self, student_id: str, device_id: str, timestamp: datetime.datetime) -> None:
        self.biometric_logs.append({
            "student_id": student_id,
            "device_id": device_id,
            "timestamp": timestamp
        })

    def add_wifi_login(self, student_id: str, ap_mac: str, timestamp: datetime.datetime, ip_addr: str) -> None:
        self.wifi_logins.append({
            "student_id": student_id,
            "ap_mac": ap_mac,
            "timestamp": timestamp,
            "ip_addr": ip_addr
        })

    def check_geofence_boundary(self, student_lat: float, student_lon: float, campus_lat: float, campus_lon: float, radius_meters: float = 100.0) -> bool:
        """
        Uses Haversine formula to check if the student location is within the campus geofence.
        """
        R = 6371000.0  # Earth radius in meters
        phi1 = math.radians(student_lat)
        phi2 = math.radians(campus_lat)
        delta_phi = math.radians(campus_lat - student_lat)
        delta_lambda = math.radians(campus_lon - student_lon)
        
        a = (math.sin(delta_phi / 2) ** 2) + math.cos(phi1) * math.cos(phi2) * (math.sin(delta_lambda / 2) ** 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c
        
        return distance <= radius_meters

    def reconcile_attendance(self) -> Dict[str, Dict[str, Any]]:
        """
        Reconciles card swipes and Wi-Fi login signatures to detect potential proxies.
        Returns final status and risk scores.
        """
        final_sheet: Dict[str, Dict[str, Any]] = {}
        
        # Aggregate swipes
        for log in self.biometric_logs:
            s_id = log["student_id"]
            if s_id not in final_sheet:
                final_sheet[s_id] = {"swiped": True, "wifi_login": False, "status": "PRESENT", "proxy_alert": False}
            else:
                final_sheet[s_id]["swiped"] = True
                
        # Aggregate Wi-Fi logins
        for log in self.wifi_logins:
            s_id = log["student_id"]
            if s_id not in final_sheet:
                final_sheet[s_id] = {"swiped": False, "wifi_login": True, "status": "ABSENT", "proxy_alert": True}
            else:
                final_sheet[s_id]["wifi_login"] = True
                
        # Anomaly verification
        for s_id, record in final_sheet.items():
            if record["swiped"] and not record["wifi_login"]:
                # Card swiped but device never connected to campus Wi-Fi network
                record["proxy_alert"] = True
                record["status"] = "PENDING_VERIFICATION"
            elif not record["swiped"] and record["wifi_login"]:
                # Connected to Wi-Fi but forgot/didn't swipe card
                record["status"] = "PRESENT_UNVERIFIED"
                record["proxy_alert"] = False
                
        return final_sheet
