"""
EduCore Enterprise Framework - Firebase Cloud Messaging (FCM) & Apple APNs Push Payload Builder

Constructs standardized push notification payloads with rich media, deep links, and sound keys:
- High priority emergency alerts (Exam cancellation, severe weather campus closure)
- Academic grade published notification with direct deep link (`educore://grades/sem5`)
- Fee payment confirmation push receipt
"""

from typing import Dict, List, Any, Optional
import json


class PushNotificationPayloadBuilder:
    """
    Constructs cross-platform push notifications for mobile apps.
    """

    @classmethod
    def build_fcm_payload(
        cls,
        device_token: str,
        title: str,
        body: str,
        deep_link_url: str = "educore://dashboard",
        is_high_priority: bool = False
    ) -> Dict[str, Any]:
        """Construct standard Firebase FCM HTTP v1 JSON message."""
        return {
            "message": {
                "token": device_token,
                "notification": {
                    "title": title,
                    "body": body,
                    "image": "https://educore.campus.edu/assets/logo.png"
                },
                "data": {
                    "deep_link": deep_link_url,
                    "click_action": "FLUTTER_NOTIFICATION_CLICK"
                },
                "android": {
                    "priority": "high" if is_high_priority else "normal",
                    "notification": {
                        "sound": "default",
                        "channel_id": "educore_urgent" if is_high_priority else "educore_general"
                    }
                },
                "apns": {
                    "payload": {
                        "aps": {
                            "sound": "default",
                            "badge": 1
                        }
                    }
                }
            }
        }
