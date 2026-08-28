"""
EduCore Enterprise Framework - Bank Counter Fee Pay-in Challan Generator

Generates triplicate printable bank challans:
- Student Copy
- College Accounts Copy
- Bank Cashier Copy
Formatted with unique challan reference numbers, institutional bank accounts, and IFSC codes.
"""

from typing import Dict, List, Any, Optional
import datetime
from apps.core.security import CryptographicSignatureManager


class BankFeeChallanGenerator:
    """
    Generates standard bank counter pay-in slip structures.
    """

    BANK_NAME = "State Bank of India / HDFC Bank"
    COLLEGE_ACCOUNT_NUMBER = "9823471029384"
    IFSC_CODE = "SBIN0004210"

    @classmethod
    def generate_triplicate_challan(
        cls,
        student_roll: str,
        student_name: str,
        department: str,
        semester: int,
        fee_breakdown: Dict[str, float],
        due_date_iso: str
    ) -> Dict[str, Any]:
        """Format triplicate challan document payload."""
        total_fee = sum(fee_breakdown.values())
        challan_no = f"CHL-{student_roll}-{datetime.datetime.now().strftime('%y%m%d%H%M')}"
        issue_date = datetime.date.today().isoformat()

        raw = f"{challan_no}:{student_roll}:{total_fee}:{due_date_iso}"
        sig = CryptographicSignatureManager.generate_document_signature(raw)

        return {
            "challan_number": challan_no,
            "bank_name": cls.BANK_NAME,
            "account_number": cls.COLLEGE_ACCOUNT_NUMBER,
            "ifsc_code": cls.IFSC_CODE,
            "student_roll": student_roll,
            "student_name": student_name,
            "department": department,
            "semester": semester,
            "fee_breakdown": fee_breakdown,
            "total_amount": round(total_fee, 2),
            "due_date": due_date_iso,
            "issued_date": issue_date,
            "verification_signature": sig,
            "copies": ["STUDENT_COPY", "COLLEGE_ACCOUNTS_COPY", "BANK_CASHIER_COPY"]
        }
