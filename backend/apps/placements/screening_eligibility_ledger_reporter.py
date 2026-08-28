"""
EduCore Framework - Placements Screening Eligibility Ledger Reporter

Generates summaries of candidate screening eligibility.
"""

from typing import Dict, List, Any

class ScreeningEligibilityLedgerReporter:
    def __init__(self, drive_id: str):
        self.drive_id = drive_id

    def generate_eligibility_summary(self, records: List[Dict[str, Any]]) -> Dict[str, Any]:
        eligible_count = sum(1 for r in records if r["status"] == "ELIGIBLE")
        ineligible_count = sum(1 for r in records if r["status"] == "INELIGIBLE")
        
        return {
            "drive_id": self.drive_id,
            "total_candidates": len(records),
            "eligible_candidates": eligible_count,
            "ineligible_candidates": ineligible_count
        }
