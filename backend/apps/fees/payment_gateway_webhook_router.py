"""
EduCore Enterprise Framework - Payment Gateway Webhook Signature Verification Router

Processes payment webhooks (Razorpay, Stripe, PayU) for tuition fees:
- HMAC-SHA256 signature verification to prevent spoofing
- Idempotency ledger verification to prevent double-crediting
- Post-routing ledger updating and receipt printing
"""

import hmac
import hashlib
import json
from typing import Dict, Any, Tuple


class PaymentGatewayWebhookRouter:
    """
    Ingests and validates payment transaction updates.
    """

    @classmethod
    def verify_razorpay_signature(
        cls,
        payload_body: str,
        received_signature: str,
        webhook_secret: str
    ) -> bool:
        """
        Validate Razorpay webhook signature (HMAC-SHA256).
        """
        if not received_signature or not webhook_secret:
            return False

        generated_signature = hmac.new(
            webhook_secret.encode("utf-8"),
            payload_body.encode("utf-8"),
            hashlib.sha256
        ).hexdigest()

        return hmac.compare_digest(generated_signature, received_signature)

    @classmethod
    def process_webhook_payload(
        cls,
        gateway: str,
        payload_body: str,
        signature: str,
        webhook_secret: str,
        processed_transactions_ledger: Dict[str, Any]
    ) -> Tuple[bool, str, Dict[str, Any]]:
        """
        Authenticate signature and process transactional state change.
        """
        # 1. Verify signature
        if gateway.lower() == "razorpay":
            is_valid = cls.verify_razorpay_signature(payload_body, signature, webhook_secret)
        else:
            is_valid = False  # Unimplemented gateway

        if not is_valid:
            return False, "INVALID_SIGNATURE_VERIFICATION_FAILURE", {}

        # 2. Parse payload
        try:
            data = json.loads(payload_body)
        except json.JSONDecodeError:
            return False, "MALFORMED_JSON_PAYLOAD", {}

        # 3. Extract transaction identifier
        tx_id = data.get("payment_id") or data.get("id")
        if not tx_id:
            return False, "MISSING_TRANSACTION_IDENTIFIER", {}

        # 4. Check idempotency
        if tx_id in processed_transactions_ledger:
            return True, "DUPLICATE_TRANSACTION_IGONRED", {
                "transaction_id": tx_id,
                "status": "ALREADY_PROCESSED"
            }

        # 5. Route to accounting ledger
        amount_received = float(data.get("amount", 0)) / 100.0  # Razorpay returns paise
        student_roll = data.get("student_roll")
        fee_head = data.get("fee_head", "TUITION_FEE")

        receipt = {
            "transaction_id": tx_id,
            "student_roll": student_roll,
            "amount_paid": amount_received,
            "fee_head": fee_head,
            "payment_gateway": gateway.upper(),
            "status": "POSTED_TO_STUDENT_LEDGER"
        }

        # Save to ledger
        processed_transactions_ledger[tx_id] = receipt

        return True, "TRANSACTION_SUCCESSFULLY_PROCESSED", receipt
class PaymentGatewayWebhookException(Exception):
    pass
