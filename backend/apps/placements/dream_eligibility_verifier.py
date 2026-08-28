"""
EduCore Framework - Placements Dream Eligibility Verifier

Logs student job offers and evaluates permissions to participate
in premium (Dream / Super Dream) campus recruitment drives.
"""

from typing import Dict, List, Any

class DreamEligibilityVerifier:
    def __init__(self, regulation_code: str):
        self.regulation_code = regulation_code
        self.placed_offers: Dict[str, List[Dict[str, Any]]] = {}  # student_id -> [offers]

    def record_job_offer(self, student_id: str, company: str, ctc_lpa: float, tier: str) -> None:
        offer = {
            "company": company,
            "ctc_lpa": ctc_lpa,
            "tier": tier,
            "recorded_at": "SYSTEM_PLACEMENTS_RECORDS"
        }
        if student_id not in self.placed_offers:
            self.placed_offers[student_id] = []
        self.placed_offers[student_id].append(offer)

    def is_eligible_for_drive(self, student_id: str, target_company_ctc: float) -> bool:
        offers = self.placed_offers.get(student_id, [])
        if not offers:
            # Unplaced student is eligible
            return True
            
        # Get highest offer CTC
        highest_ctc = max(o["ctc_lpa"] for o in offers)
        
        # Super dream threshold is 22 LPA, Dream threshold is 12 LPA
        if highest_ctc >= 22.0:
            # Already placed in Super Dream. No further drives allowed.
            return False
            
        if 12.0 <= highest_ctc < 22.0:
            # Placed in Dream. Can only participate if target company is Super Dream.
            return target_company_ctc >= 22.0
            
        # Placed in regular. Can participate if target company is Dream or Super Dream.
        return target_company_ctc >= 12.0
