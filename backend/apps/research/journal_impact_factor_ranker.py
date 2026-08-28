"""
EduCore Framework - Journal Impact Factor & Quality Ranker

Validates publication journals against international indexes (Scopus, Web of Science, UGC Care),
and matches them to institutional incentive slabs.
"""

from typing import Dict, List, Any

class JournalImpactFactorRanker:
    def __init__(self):
        # Slabs define rewards for research publications
        self.incentive_slabs: Dict[str, float] = {
            "WOS_Q1": 50000.0,   # Rs. 50,000 cash award
            "WOS_Q2": 30000.0,   # Rs. 30,000 cash award
            "WOS_Q3": 20000.0,   # Rs. 20,000 cash award
            "SCOPUS_Q1": 15000.0,
            "SCOPUS_Q2": 10000.0,
            "UGC_CARE": 5000.0
        }

    def determine_journal_quartile(self, rank: int, total_journals_in_category: int) -> str:
        """
        Calculates quartile placement based on category ranks.
        """
        if total_journals_in_category <= 0:
            return "Q4"
            
        ratio = rank / total_journals_in_category
        if ratio <= 0.25:
            return "Q1"
        elif ratio <= 0.50:
            return "Q2"
        elif ratio <= 0.75:
            return "Q3"
        return "Q4"

    def calculate_faculty_incentive(self, index_type: str, quartile: str, first_author: bool) -> float:
        """
        Computes the final cash incentive based on journal standing and authorship position.
        First authors get 100% of the incentive, co-authors get 50% split.
        """
        slab_key = f"{index_type}_{quartile}"
        if index_type == "UGC_CARE":
            slab_key = "UGC_CARE"
            
        base_incentive = self.incentive_slabs.get(slab_key, 0.0)
        
        if not first_author:
            return base_incentive * 0.5
        return base_incentive
