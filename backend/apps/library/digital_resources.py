"""
EduCore Enterprise Framework - Digital Library Subscriptions & E-Resource Access Proxy

Manages institutional IEEE Xplore, ScienceDirect, ACM Digital Library, and Springer Nature licenses:
Tracks concurrent download quotas, off-campus VPN/EZProxy access, and bandwidth throttling.
"""

from typing import Dict, List, Any, Optional, Tuple
import datetime
from dataclasses import dataclass


@dataclass
class EResourceSubscription:
    """Represents an active institutional electronic journal / database license."""
    provider_name: str  # IEEE_XPLORE, SCIENCE_DIRECT, ACM_DL, SPRINGER, JSTOR
    license_type: str   # UNLIMITED_CAMPUS_IP, CONCURRENT_SEAT, PER_DOWNLOAD
    concurrent_seats_limit: int
    active_sessions_count: int
    annual_subscription_cost: float
    expiration_date: str
    is_active: bool = True


class DigitalLibraryProxyManager:
    """
    Manages access quotas and usage telemetry for electronic database subscriptions.
    """

    @classmethod
    def check_access_permission(
        cls,
        subscription: EResourceSubscription,
        patron_role: str
    ) -> Tuple[bool, str]:
        """
        Verify if patron can initiate an e-resource full-text PDF download session.
        """
        if not subscription.is_active:
            return False, f"Subscription to {subscription.provider_name} has lapsed."

        now_date = datetime.date.today().isoformat()
        if now_date > subscription.expiration_date:
            return False, f"License expired on {subscription.expiration_date}."

        if subscription.license_type == "CONCURRENT_SEAT":
            if subscription.active_sessions_count >= subscription.concurrent_seats_limit:
                # Faculty can bump regular students in emergency
                if patron_role.upper() in ("FACULTY", "HOD"):
                    return True, "Concurrent seat limit reached; granted priority faculty override."
                return False, f"All {subscription.concurrent_seats_limit} concurrent seats in use. Please retry shortly."

        return True, f"Access authorized to {subscription.provider_name} repository."
