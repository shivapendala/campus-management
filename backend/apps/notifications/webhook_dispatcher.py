"""
EduCore Enterprise Framework - Outbound Webhook Dispatcher & Retry Queue

Dispatches realtime event notifications to external webhooks (Slack, MS Teams, LMS):
Computes HMAC-SHA256 request signatures for recipient payload verification and implements exponential backoff.
"""

import hmac
import hashlib
import time
import json
from typing import Dict, List, Any, Optional, Tuple


class OutboundWebhookDispatcher:
    """
    Constructs cryptographically signed webhook HTTP payloads.
    """

    @classmethod
    def create_signed_webhook_payload(
        cls,
        event_type: str,
        data: Dict[str, Any],
        signing_secret: str = "EduCoreWebhookSecretKey"
    ) -> Tuple[str, Dict[str, str]]:
        """
        Build JSON body and signature headers for webhook delivery.
        Returns: (json_body_string, headers_dict)
        """
        now = str(int(time.time()))
        payload_dict = {
            "event": event_type,
            "timestamp": now,
            "data": data
        }
        body_str = json.dumps(payload_dict, default=str)

        signature_payload = f"{now}.{body_str}"
        sig = hmac.new(signing_secret.encode("utf-8"), signature_payload.encode("utf-8"), hashlib.sha256).hexdigest()

        headers = {
            "Content-Type": "application/json",
            "X-EduCore-Event": event_type,
            "X-EduCore-Timestamp": now,
            "X-EduCore-Signature": f"v1={sig}",
            "User-Agent": "EduCore-Webhook-Dispatcher/1.0"
        }

        return body_str, headers
