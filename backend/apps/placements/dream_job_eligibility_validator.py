"""
EduCore Framework - Placements Dream Job Policy Validator

Validates candidate applications against institution-specific hiring policies:
- Dream Option: Students placed in regular company can apply for a dream company.
- Super Dream Option: Students placed in dream company can apply for super dream.
- Single Offer policy rules.
"""

from typing import Dict, Any

class DreamJobEligibilityValidator:
    def __init__(self, dream_ctc_threshold: float = 12.0, super_dream_ctc_threshold: float = 22.0):
        self.dream_ctc_threshold = dream_ctc_threshold
        self.super_dream_ctc_threshold = super_dream_ctc_threshold

    def check_application_permission(self, current_placed_ctc: float, target_company_ctc: float) -> bool:
        """
        Determines if student can apply for a company based on their current package.
        """
        if current_placed_ctc == 0.0:
            # Unplaced student can apply for any company
            return True
            
        # Case 1: Student is placed in a regular company (CTC < 12.0)
        # Can apply for a dream or super dream company (CTC >= 12.0)
        if current_placed_ctc < self.dream_ctc_threshold:
            return target_company_ctc >= self.dream_ctc_threshold
            
        # Case 2: Student is placed in a dream company (12.0 <= CTC < 22.0)
        # Can only apply for a super dream company (CTC >= 22.0)
        if self.dream_ctc_threshold <= current_placed_ctc < self.super_dream_ctc_threshold:
            return target_company_ctc >= self.super_dream_ctc_threshold
            
        # Case 3: Placed in a super dream company (CTC >= 22.0)
        # Cannot apply for any other campus drive
        return False
