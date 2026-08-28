"""
EduCore Framework - Placements Screening Eligibility Auditor

Audits candidate eligibility listings to detect screening bypasses.
"""

from typing import Dict, List, Any

class ScreeningEligibilityAuditor:
    def __init__(self, drive_id: str):
        self.drive_id = drive_id
        self.bypass_records: List[Dict[str, Any]] = []

    def audit_shortlist(self, shortlisted_candidates: List[Dict[str, Any]], cgpa_cutoff: float) -> List[Dict[str, Any]]:
        for cand in shortlisted_candidates:
            s_id = cand["student_id"]
            cgpa = cand["cgpa"]
            if cgpa < cgpa_cutoff:
                self.bypass_records.append({
                    "student_id": s_id,
                    "cgpa": cgpa,
                    "cutoff_required": cgpa_cutoff,
                    "type": "ELIGIBILITY_BYPASS_ALERT"
                })
        return self.bypass_records
