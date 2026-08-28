"""
EduCore Framework - Placements Dream Eligibility Auditor

Audits placement allocations to ensure compliance with the single active offer rule.
"""

from typing import Dict, List, Any

class DreamEligibilityAuditor:
    def __init__(self):
        self.policy_violations: List[Dict[str, Any]] = []

    def audit_student_offers(self, allocated_offers: Dict[str, List[Dict[str, Any]]]) -> List[Dict[str, Any]]:
        """
        Enforces placement board guidelines:
        - A student cannot hold multiple job offers within the same package tier (e.g. two regular offers).
        - A student placed in dream tier cannot apply for another dream tier.
        """
        for student_id, offers in allocated_offers.items():
            if len(offers) > 1:
                tiers = [o["tier"] for o in offers]
                
                # Check for double regular offers
                regular_count = sum(1 for t in tiers if t == "REGULAR")
                dream_count = sum(1 for t in tiers if t == "DREAM")
                
                if regular_count > 1 or dream_count > 1:
                    self.policy_violations.append({
                        "student_id": student_id,
                        "type": "SINGLE_OFFER_VIOLATION",
                        "description": f"Student holds multiple conflicting offers in same tier: {', '.join(tiers)}."
                    })
        return self.policy_violations
