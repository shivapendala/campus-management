"""
EduCore Enterprise Framework - Bloom's Revised Taxonomy Cognitive Classifier

Categorizes examination questions and curriculum objectives into 6 cognitive tiers:
1. Remember (Recall facts: Define, List, State)
2. Understand (Explain concepts: Describe, Summarize, Classify)
3. Apply (Use information: Solve, Demonstrate, Calculate)
4. Analyze (Draw connections: Differentiate, Compare, Contrast)
5. Evaluate (Justify decisions: Appraise, Critique, Defend)
6. Create (Produce original work: Design, Construct, Develop)
"""

from typing import Dict, List, Any, Optional, Tuple


class BloomsTaxonomyClassifier:
    """
    NLP keyword matcher for cognitive complexity levels.
    """

    ACTION_VERBS = {
        "L1_REMEMBER": ["define", "list", "state", "recall", "name", "identify", "show", "label"],
        "L2_UNDERSTAND": ["describe", "explain", "summarize", "classify", "interpret", "translate", "discuss"],
        "L3_APPLY": ["solve", "apply", "calculate", "demonstrate", "illustrate", "execute", "compute"],
        "L4_ANALYZE": ["analyze", "differentiate", "compare", "contrast", "distinguish", "examine", "categorize"],
        "L5_EVALUATE": ["evaluate", "appraise", "critique", "judge", "defend", "justify", "validate"],
        "L6_CREATE": ["design", "construct", "develop", "formulate", "synthesize", "architect", "invent"],
    }

    @classmethod
    def classify_question_text(cls, question_text: str) -> Tuple[str, str]:
        """
        Identify highest Bloom's taxonomy cognitive tier based on action verbs.
        Returns: (blooms_tier_code, description)
        """
        tokens = [w.lower().strip(".,;:?!") for w in question_text.split()]

        for tier in ["L6_CREATE", "L5_EVALUATE", "L4_ANALYZE", "L3_APPLY", "L2_UNDERSTAND", "L1_REMEMBER"]:
            verbs = cls.ACTION_VERBS[tier]
            if any(v in tokens for v in verbs):
                return tier, f"Cognitive Level: {tier}"

        return "L2_UNDERSTAND", "Default Cognitive Level: Understand"
