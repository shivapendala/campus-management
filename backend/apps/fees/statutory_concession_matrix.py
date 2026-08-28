"""
EduCore Framework - Statutory Fee Concessions & Scholarship Matrix

Calculates eligible fee waivers, concessions, and governmental scholarships
based on income certificates, social categories, and academic performance.
"""

from typing import Dict, List, Any

class StatutoryConcessionMatrix:
    def __init__(self, academic_year: str):
        self.academic_year = academic_year
        self.income_slabs_upper_limits: Dict[str, float] = {
            "SLAB_A": 100000.0,   # 100% concession
            "SLAB_B": 250000.0,   # 50% concession
            "SLAB_C": 600000.0,   # 25% concession
            "SLAB_D": 800000.0    # 10% concession
        }
        self.social_category_concessions: Dict[str, float] = {
            "SC": 1.00,  # 100% waiver on tuition
            "ST": 1.00,  # 100% waiver on tuition
            "OBC_NCL": 0.50,
            "EWS": 0.50,
            "GENERAL": 0.00
        }

    def verify_income_concession_slab(self, annual_income: float) -> str:
        """
        Suggests the concession slab based on family annual income certificate thresholds.
        """
        if annual_income <= self.income_slabs_upper_limits["SLAB_A"]:
            return "SLAB_A"
        elif annual_income <= self.income_slabs_upper_limits["SLAB_B"]:
            return "SLAB_B"
        elif annual_income <= self.income_slabs_upper_limits["SLAB_C"]:
            return "SLAB_C"
        elif annual_income <= self.income_slabs_upper_limits["SLAB_D"]:
            return "SLAB_D"
        return "NO_CONCESSION"

    def calculate_tuition_waiver(self, base_tuition: float, annual_income: float, social_category: str, cpa_points: float) -> Dict[str, Any]:
        """
        Calculates integrated statutory tuition waiver based on income, category, and merit.
        Waivers are non-cumulative; the maximum single waiver applies.
        """
        income_slab = self.verify_income_concession_slab(annual_income)
        
        # Concession from income slab
        income_pct = 0.0
        if income_slab == "SLAB_A":
            income_pct = 1.00
        elif income_slab == "SLAB_B":
            income_pct = 0.50
        elif income_slab == "SLAB_C":
            income_pct = 0.25
        elif income_slab == "SLAB_D":
            income_pct = 0.10
            
        # Concession from social category
        category_pct = self.social_category_concessions.get(social_category, 0.0)
        
        # Merit-based concession
        merit_pct = 0.0
        if cpa_points >= 9.5:
            merit_pct = 0.50
        elif cpa_points >= 9.0:
            merit_pct = 0.25
        elif cpa_points >= 8.5:
            merit_pct = 0.15
            
        # Maximum waiver selection
        final_concession_pct = max(income_pct, category_pct, merit_pct)
        concession_amount = base_tuition * final_concession_pct
        net_payable = base_tuition - concession_amount
        
        return {
            "base_tuition": base_tuition,
            "income_slab": income_slab,
            "concession_percentage": round(final_concession_pct * 100.0, 2),
            "concession_amount": round(concession_amount, 2),
            "net_payable_tuition": round(net_payable, 2),
            "merit_applied": merit_pct > 0.0 and final_concession_pct == merit_pct
        }
