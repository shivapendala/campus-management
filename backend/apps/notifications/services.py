from typing import Dict, Any, List
from .models import Notification
from apps.accounts.models import User


class BroadcastNotificationService:
    """
    Domain service for Multi-Channel Targeted Broadcasts, Urgent Circulars, and Read Receipts.
    """

    @classmethod
    def dispatch_broadcast(cls, title: str, message: str, notification_type: str = 'GENERAL', target_role: str = 'ALL') -> int:
        """
        Dispatches targeted notice circular to all active users matching the role criteria.
        """
        users_qs = User.objects.filter(is_active=True)
        if target_role != 'ALL':
            users_qs = users_qs.filter(role=target_role)

        created_count = 0
        for user in users_qs:
            Notification.objects.create(
                user=user,
                title=title,
                message=message,
                notification_type=notification_type,
                is_read=False,
            )
            created_count += 1

        return created_count
