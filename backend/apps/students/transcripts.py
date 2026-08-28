"""
EduCore Enterprise Framework - Student Digital Transcript Generator & Academic Audit

Formats formal academic transcripts with institutional seal, cryptographic checksum,
SGPA/CGPA progression tables, semester credit breakdowns, and distinction accolades.
"""

from typing import Dict, List, Any, Optional
import datetime
from apps.core.security import CryptographicSignatureManager


class StudentTranscriptFormatter:
    """
    Constructs multi-semester institutional transcript tables with official seals.
    """

    @classmethod
    def generate_full_academic_transcript(
        cls,
        student_id: int,
        roll_number: str,
        student_name: str,
        father_name: str,
        mother_name: str,
        department_name: str,
        program_name: str,  # e.g., "Bachelor of Technology in Computer Science and Engineering"
        admission_year: int,
        graduation_year: int,
        semester_records: List[Dict[str, Any]],
        cgpa: float,
        division: str
    ) -> Dict[str, Any]:
        """
        Generate complete verifiable transcript bundle with digital watermark token.
        """
        transcript_serial = f"EDU-TRN-{admission_year}-{roll_number}"
        issue_date = datetime.date.today().isoformat()

        # Build raw string for HMAC cryptographic verification
        raw_seal_data = f"{transcript_serial}:{roll_number}:{cgpa}:{division}:{issue_date}"
        signature = CryptographicSignatureManager.generate_document_signature(raw_seal_data)

        total_credits_earned = sum(sem.get("credits_earned", 0) for sem in semester_records)

        return {
            "transcript_serial": transcript_serial,
            "student_details": {
                "student_id": student_id,
                "roll_number": roll_number,
                "student_name": student_name,
                "father_name": father_name,
                "mother_name": mother_name,
                "department": department_name,
                "program": program_name,
                "admission_year": admission_year,
                "graduation_year": graduation_year,
            },
            "academic_metrics": {
                "cumulative_cgpa": cgpa,
                "total_credits_earned": total_credits_earned,
                "final_division": division,
                "total_semesters_completed": len(semester_records),
            },
            "semester_wise_breakdown": semester_records,
            "security_verification": {
                "issue_date": issue_date,
                "digital_seal_signature": signature,
                "qr_verify_endpoint": f"https://educore.campus.edu/verify/transcript?serial={transcript_serial}&hash={signature[:16]}",
                "issuer_authority": "Office of the Controller of Examinations",
                "status": "OFFICIALLY_CONFERRED"
            }
        }
