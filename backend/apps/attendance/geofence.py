"""
EduCore Enterprise Framework - Mobile Geofence & BLE Beacon Attendance Validator

Validates student mobile GPS coordinates and Bluetooth Low Energy (BLE) beacon signals
against classroom bounding boxes to prevent remote proxy attendance marking.
"""

import math
from typing import Dict, List, Any, Optional, Tuple


class GeofenceAttendanceValidator:
    """
    Computes Haversine great-circle distances between student mobile GPS fixes and classroom centers.
    """

    EARTH_RADIUS_METERS = 6371000.0

    @classmethod
    def calculate_haversine_distance(
        cls,
        lat1: float,
        lon1: float,
        lat2: float,
        lon2: float
    ) -> float:
        """
        Calculate distance between two GPS coordinates in meters.
        """
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = (
            math.sin(delta_phi / 2.0) ** 2 +
            math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
        )
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return round(cls.EARTH_RADIUS_METERS * c, 2)

    @classmethod
    def validate_mobile_checkin(
        cls,
        student_lat: float,
        student_lon: float,
        classroom_lat: float,
        classroom_lon: float,
        max_allowed_radius_meters: float = 30.0,
        ble_beacon_rssi: Optional[int] = None
    ) -> Tuple[bool, str, float]:
        """
        Verify that student is physically inside classroom perimeter.
        Returns: (is_valid, reason, distance_meters)
        """
        distance = cls.calculate_haversine_distance(
            student_lat, student_lon, classroom_lat, classroom_lon
        )

        if distance > max_allowed_radius_meters:
            return False, f"Location rejected: {distance:.1f}m away from classroom (max allowed: {max_allowed_radius_meters}m).", distance

        # If BLE beacon present, verify signal strength (RSSI > -85 dBm)
        if ble_beacon_rssi is not None and ble_beacon_rssi < -85:
            return False, f"BLE Beacon signal too weak ({ble_beacon_rssi} dBm). Ensure you are inside the classroom.", distance

        return True, "Physical presence verified successfully.", distance
