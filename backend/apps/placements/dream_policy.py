"""
EduCore Enterprise Framework - Dream & Super Dream Job Placement Policy Matrix

Enforces institutional One-Student-One-Job policy with tier upgrades:
- Regular Offer (< 6 LPA): Student eligible for Dream & Super Dream
- Dream Offer (6 - 12 LPA): Student eligible only for Super Dream (>= 1.5x CTC)
- Super Dream Offer (> 12 LPA): Student blocked from further campus drives
"""

from typing import Dict, List, Any, Optional, Tuple


class DreamPolicyRuleMatrix:
    """
    Evaluates student entitlement to attend subsequent recruitment drives.
    """

    @classmethod
    def check_drive_eligibility_by_policy(
        cls,
        existing_offer_ctc_lpa: float,
        target_company_ctc_lpa: float
    ) -> Tuple[bool, str]:
        """
        Evaluate Dream upgrade rules.
        """
        if existing_offer_ctc_lpa <= 0.0:
            return True, "No existing offer; fully eligible for all drive tiers."

        if existing_offer_ctc_lpa >= 12.0:
            return False, f"Blocked by Super Dream Policy: Already placed at {existing_offer_ctc_lpa} LPA."

        min_upgrade_ctc = existing_offer_ctc_lpa * 1.5
        if target_company_ctc_lpa >= min_upgrade_ctc:
            return True, f"Eligible under Dream Upgrade Policy ({target_company_ctc_lpa} LPA >= 1.5x of {existing_offer_ctc_lpa} LPA)."
        else:
            return False, f"Ineligible: Target CTC ({target_company_ctc_lpa} LPA) does not meet mandatory 1.5x multiplier ({min_upgrade_ctc:.1f} LPA)."
