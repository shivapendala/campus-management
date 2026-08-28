"""
EduCore Enterprise Framework - Digital Event Merit & Participation Certificate Generator

Generates tamper-evident digital participation and prize winner certificates
with cryptographic HMAC-SHA256 signatures and QR verification endpoints.
"""

from typing import Dict, List, Any, Optional
import datetime
from apps.core.security import CryptographicSignatureManager


class EventCertificateBuilder:
    """
    Constructs verifiable event certificates.
    """

    @classmethod
    def generate_certificate_payload(
        cls,
        event_name: str,
        participant_name: str,
        institution_name: str,
        award_category: str = "PARTICIPATION",  # 1ST_PRIZE, 2ND_PRIZE, PARTICIPATION, BEST_PAPER
        event_date_iso: str = "2026-09-15"
    ) -> Dict[str, Any]:
        """Generate structured certificate document payload."""
        import uuid
        cert_serial = f"CERT-{event_name[:4].upper()}-{str(uuid.uuid4())[:8].upper()}"
        issue_date = datetime.date.today().isoformat()

        raw_payload = f"{cert_serial}:{event_name}:{participant_name}:{award_category}:{issue_date}"
        signature = CryptographicSignatureManager.generate_document_signature(raw_payload)

        return {
            "certificate_serial": cert_serial,
            "event_name": event_name,
            "participant_name": participant_name,
            "institution_name": institution_name,
            "award_category": award_category,
            "event_date": event_date_iso,
            "issued_date": issue_date,
            "digital_signature": signature,
            "qr_verification_url": f"https://educore.campus.edu/verify/cert?id={cert_serial}&sig={signature[:16]}",
            "is_valid": True
        }
