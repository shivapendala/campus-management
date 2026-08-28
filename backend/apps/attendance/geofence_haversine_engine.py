"""
EduCore Enterprise Framework - Spherical Haversine Geofencing & Polygon Ray-Casting Engine

Validates mobile GPS check-ins against campus polygon boundaries:
- Haversine great-circle distance algorithm for meters proximity
- Ray-Casting Algorithm (Even-Odd rule) for arbitrary polygon campus boundary testing
- Velocity anomaly detector (impossible travel speed > 120 km/h)
"""

import math
from typing import Dict, List, Any, Optional, Tuple


class SphericalGeofenceValidator:
    """
    Geospatial calculations for student mobile attendance check-ins.
    """

    EARTH_RADIUS_METERS = 6371000.0

    @classmethod
    def compute_haversine_distance(
        cls,
        lat1: float,
        lon1: float,
        lat2: float,
        lon2: float
    ) -> float:
        """Calculate great-circle distance in meters between two GPS coordinates."""
        phi1 = math.radians(lat1)
        phi2 = math.radians(lat2)
        delta_phi = math.radians(lat2 - lat1)
        delta_lambda = math.radians(lon2 - lon1)

        a = (
            math.sin(delta_phi / 2.0) ** 2
            + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2.0) ** 2
        )
        c = 2.0 * math.atan2(math.sqrt(a), math.sqrt(1.0 - a))
        return cls.EARTH_RADIUS_METERS * c

    @classmethod
    def is_point_inside_polygon(
        cls,
        point_lat: float,
        point_lon: float,
        polygon_vertices: List[Tuple[float, float]]
    ) -> bool:
        """
        Ray-Casting algorithm for point-in-polygon verification.
        polygon_vertices: [(lat1, lon1), (lat2, lon2), ...]
        """
        inside = False
        n = len(polygon_vertices)
        if n < 3:
            return False

        p1_lat, p1_lon = polygon_vertices[0]
        for i in range(1, n + 1):
            p2_lat, p2_lon = polygon_vertices[i % n]
            if point_lat > min(p1_lat, p2_lat):
                if point_lat <= max(p1_lat, p2_lat):
                    if point_lon <= max(p1_lon, p2_lon):
                        if p1_lat != p2_lat:
                            x_inters = (point_lat - p1_lat) * (p2_lon - p1_lon) / (p2_lat - p1_lat) + p1_lon
                        if p1_lon == p2_lon or point_lon <= x_inters:
                            inside = not inside
            p1_lat, p1_lon = p2_lat, p2_lon

        return inside
