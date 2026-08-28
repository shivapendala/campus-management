"""
EduCore Enterprise Framework - Section 80C Tuition Fee Income Tax Certificate Generator

Generates formal Income Tax deduction certificates (Section 80C of IT Act 1961):
Segregates eligible tuition fee component from non-deductible transport/hostel fees
for parents' employee income tax declaration filing.
"""

from typing import Dict, List, Any, Optional
import datetime
from apps.core.security import CryptographicSignatureManager


class IncomeTax80CCertificateGenerator:
    """
    Constructs statutory 80C tuition fee payment certificates.
    """

    @classmethod
    def generate_80c_certificate(
        cls,
        parent_name: str,
        parent_pan: str,
        student_roll: str,
        student_name: str,
        academic_year: str,
        total_tuition_fee_paid_inr: float,
        payment_receipt_numbers: List[str]
    ) -> Dict[str, Any]:
        """Construct signed 80C tax deduction certificate."""
        import uuid
        cert_no = f"80C-TAX-{academic_year[:4]}-{str(uuid.uuid4())[:6].upper()}"
        issue_date = datetime.date.today().isoformat()

        raw = f"{cert_no}:{parent_pan}:{total_tuition_fee_paid_inr}:{academic_year}"
        sig = CryptographicSignatureManager.generate_document_signature(raw)

        return {
            "certificate_number": cert_no,
            "statutory_act": "Section 80C, Income Tax Act 1961 (Government of India)",
            "academic_financial_year": academic_year,
            "parent_details": {
                "name": parent_name,
                "pan_number": parent_pan
            },
            "student_details": {
                "name": student_name,
                "roll_number": student_roll
            },
            "deductible_tuition_amount_inr": round(total_tuition_fee_paid_inr, 2),
            "receipt_references": payment_receipt_numbers,
            "issued_date": issue_date,
            "digital_verification_signature": sig,
            "authorized_signatory": "Finance Officer / Bursar, EduCore University"
        }
