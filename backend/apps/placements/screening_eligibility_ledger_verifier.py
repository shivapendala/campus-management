"""
EduCore Framework - Placements Screening Eligibility Ledger Verifier

Reconciles drive eligibility registers against shortlist tables.
"""

from typing import Dict, List, Any

class ScreeningEligibilityLedgerVerifier:
    def __init__(self, drive_id: str):
        self.drive_id = drive_id
        self.reconciliation_mismatches: List[Dict[str, Any]] = []

    def verify_shortlist(self, approved_candidates: List[str], final_shortlist: List[str]) -> List[Dict[str, Any]]:
        approved_set = set(approved_candidates)
        shortlist_set = set(final_shortlist)
        
        unauthorized = shortlist_set - approved_set
        for student_id in unauthorized:
            self.reconciliation_mismatches.append({
                "student_id": student_id,
                "type": "UNAUTHORIZED_CANDIDATE_SHORTLIST",
                "description": "Student was shortlisted but never approved in drive screening ledger."
            })
        return self.reconciliation_mismatches
