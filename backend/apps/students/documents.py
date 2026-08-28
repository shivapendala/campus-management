"""
EduCore Enterprise Framework - Student Document Repository & Digital Verification

Handles student official records: Transcripts, Transfer Certificates (TC),
Bonafide Certificates, Study Conduct Certificates, and Cryptographic QR Verification.
"""

import datetime
from typing import Dict, List, Any, Optional
from apps.core.security import CryptographicSignatureManager


class StudentDocumentVerificationManager:
    """
    Generates verifiable official documents and signs them with HMAC-SHA256 signatures.
    """

    DOCUMENT_TYPES = {
        "TRANSCRIPT": "Official Cumulative Academic Transcript",
        "BONAFIDE": "Bonafide Student Certificate",
        "TC": "Institutional Transfer and Migration Certificate",
        "CONDUCT": "Character and Conduct Certificate",
        "INTERNSHIP_NOC": "No Objection Certificate for Internship",
        "FEE_ESTIMATE": "Institutional Tuition Fee Estimate for Bank Loans",
    }

    @classmethod
    def generate_bonafide_certificate_payload(
        cls,
        student_id: int,
        roll_number: str,
        full_name: str,
        father_name: str,
        department: str,
        academic_year: str,
        purpose: str = "General Official Verification"
    ) -> Dict[str, Any]:
        """Generate structured payload for digital bonafide certificate with signature."""
        cert_id = f"BON-{roll_number}-{datetime.datetime.now().strftime('%Y%m%d%H%M')}"
        issue_date = datetime.date.today().isoformat()

        raw_payload = f"{cert_id}:{roll_number}:{full_name}:{department}:{academic_year}:{issue_date}"
        signature = CryptographicSignatureManager.generate_document_signature(raw_payload)

        return {
            "certificate_id": cert_id,
            "document_type": "BONAFIDE",
            "student_id": student_id,
            "roll_number": roll_number,
            "full_name": full_name,
            "father_name": father_name,
            "department": department,
            "academic_year": academic_year,
            "purpose": purpose,
            "issue_date": issue_date,
            "cryptographic_signature": signature,
            "verification_url": f"https://educore.campus.edu/verify/document?cert_id={cert_id}&sig={signature[:16]}",
            "is_valid": True
        }

    @classmethod
    def generate_official_transcript_payload(
        cls,
        student_id: int,
        roll_number: str,
        full_name: str,
        department: str,
        semesters_data: List[Dict[str, Any]],
        cgpa: float,
        division: str
    ) -> Dict[str, Any]:
        """Generate structured payload for official academic transcript."""
        transcript_id = f"TRN-{roll_number}-{datetime.datetime.now().strftime('%Y%m%d')}"
        issue_date = datetime.date.today().isoformat()

        raw_payload = f"{transcript_id}:{roll_number}:{cgpa}:{division}:{issue_date}"
        signature = CryptographicSignatureManager.generate_document_signature(raw_payload)

        return {
            "transcript_id": transcript_id,
            "document_type": "TRANSCRIPT",
            "student_id": student_id,
            "roll_number": roll_number,
            "full_name": full_name,
            "department": department,
            "semesters": semesters_data,
            "cumulative_cgpa": cgpa,
            "degree_classification": division,
            "issue_date": issue_date,
            "cryptographic_signature": signature,
            "verification_url": f"https://educore.campus.edu/verify/transcript?id={transcript_id}&sig={signature[:16]}",
            "seal_status": "INSTITUTIONALLY_SIGNED"
        }
