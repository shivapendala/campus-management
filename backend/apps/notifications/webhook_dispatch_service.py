"""
EduCore Framework - Webhook Event Dispatcher Service

Serializes and signs payload event notifications (e.g., student admission, fee paid)
and sends them to registered institutional endpoints.
"""

import hmac
import hashlib
import json
import datetime
from typing import Dict, List, Any, Tuple

class WebhookDispatchService:
    def __init__(self, dispatcher_id: str, signing_secret: str):
        self.dispatcher_id = dispatcher_id
        self.signing_secret = signing_secret.encode('utf-8')
        self.dispatch_history: List[Dict[str, Any]] = []

    def sign_payload(self, payload: Dict[str, Any]) -> str:
        """
        Signs the JSON serialized payload using HMAC-SHA256 signature scheme.
        """
        serialized = json.dumps(payload, sort_keys=True)
        sig = hmac.new(self.signing_secret, serialized.encode('utf-8'), hashlib.sha256).hexdigest()
        return sig

    def prepare_dispatch(self, target_url: str, event_type: str, payload_data: Dict[str, Any]) -> Tuple[Dict[str, str], str]:
        event_envelope = {
            "event_type": event_type,
            "timestamp": datetime.datetime.now().isoformat(),
            "data": payload_data
        }
        
        signature = self.sign_payload(event_envelope)
        headers = {
            "Content-Type": "application/json",
            "X-EduCore-Signature": signature,
            "X-EduCore-Dispatcher": self.dispatcher_id
        }
        
        self.dispatch_history.append({
            "target_url": target_url,
            "event_type": event_type,
            "signature": signature,
            "status": "QUEUED"
        })
        
        return headers, json.dumps(event_envelope)
