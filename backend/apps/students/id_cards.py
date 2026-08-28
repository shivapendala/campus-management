"""
EduCore Enterprise Framework - Printable Smart Student ID Card Generator

Formats CR80 standard identity card layouts with barcode / QR payload tokens,
blood group, emergency contact, validity period, and RFID chip serial mapping.
"""

from typing import Dict, List, Any, Optional
import datetime
from apps.core.security import CryptographicSignatureManager


class SmartStudentIDCardGenerator:
    """
    Constructs printable CR80 PVC card layouts with security tokens.
    """

    @classmethod
    def generate_id_card_payload(
        cls,
        student_id: int,
        roll_number: str,
        full_name: str,
        department_name: str,
        program_name: str,
        batch_years: str,  # e.g., "2023 - 2027"
        blood_group: str,
        emergency_phone: str
    ) -> Dict[str, Any]:
        """Generate structured ID card structure with security signature."""
        card_serial = f"IDC-{roll_number}-{batch_years[:4]}"
        issue_date = datetime.date.today().isoformat()

        raw_token = f"{card_serial}:{roll_number}:{full_name}:{blood_group}:{issue_date}"
        signature = CryptographicSignatureManager.generate_document_signature(raw_token)

        return {
            "card_serial_number": card_serial,
            "student_id": student_id,
            "roll_number": roll_number,
            "full_name": full_name,
            "department": department_name,
            "program": program_name,
            "batch_validity": batch_years,
            "blood_group": blood_group,
            "emergency_contact": emergency_phone,
            "issue_date": issue_date,
            "qr_verification_code": f"https://educore.campus.edu/verify/idcard?serial={card_serial}&sig={signature[:16]}",
            "barcode_data": roll_number,
            "rfid_mapped": True
        }
