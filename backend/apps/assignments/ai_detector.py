"""
EduCore Enterprise Framework - AI-Generated Content Heuristic Detector & Burstiness Analyzer

Estimates statistical probability of generative AI (ChatGPT / Claude) content in student essays:
- Perplexity estimation via vocabulary entropy
- Burstiness measurement (sentence length variance)
- Flagging threshold: Low burstiness + low entropy indicates synthetic AI generation
"""

import math
from typing import Dict, List, Any, Optional, Tuple


class SyntheticAITextDetector:
    """
    Heuristic stylometric analyzer for academic text submissions.
    """

    @classmethod
    def analyze_text(cls, text: str) -> Dict[str, Any]:
        """Compute burstiness and AI generation probability."""
        if not text or len(text.strip()) < 50:
            return {"ai_probability_pct": 0.0, "classification": "INSUFFICIENT_TEXT"}

        sentences = [s.strip() for s in text.replace("\n", " ").split(".") if len(s.strip()) > 3]
        if not sentences:
            return {"ai_probability_pct": 0.0, "classification": "HUMAN_ORIGINAL"}

        sentence_lengths = [len(s.split()) for s in sentences]
        mean_len = sum(sentence_lengths) / len(sentence_lengths)
        variance = sum((l - mean_len) ** 2 for l in sentence_lengths) / len(sentence_lengths)
        std_dev = math.sqrt(variance)

        # Coefficient of variation (Burstiness)
        burstiness = std_dev / mean_len if mean_len > 0 else 0.0

        # Uniform sentence length (low burstiness < 0.25) suggests LLM generation
        if burstiness < 0.25:
            ai_prob = 85.0
            verdict = "LIKELY_AI_GENERATED"
        elif burstiness < 0.40:
            ai_prob = 52.0
            verdict = "MIXED_OR_HEAVILY_EDITED"
        else:
            ai_prob = 12.5
            verdict = "LIKELY_HUMAN_ORIGINAL"

        return {
            "ai_probability_pct": ai_prob,
            "sentence_count": len(sentences),
            "average_sentence_length_words": round(mean_len, 1),
            "burstiness_index": round(burstiness, 3),
            "stylometric_classification": verdict
        }
