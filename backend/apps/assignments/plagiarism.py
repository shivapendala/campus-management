"""
EduCore Enterprise Framework - Assignment Plagiarism Detection & N-Gram Fingerprinting

Implements Winnowing Fingerprinting and Jaccard Token Set Similarity
to detect verbatim and paraphrased copying across student submissions and internet sources.
"""

import re
import hashlib
from typing import Dict, List, Set, Tuple, Any
from dataclasses import dataclass


@dataclass
class PlagiarismMatchReport:
    """Represents a pairwise plagiarism comparison finding."""
    submission_id_a: int
    submission_id_b: int
    student_roll_a: str
    student_roll_b: str
    similarity_score_pct: float
    overlapping_n_grams_count: int
    is_flagged: bool = False
    verdict: str = "ORIGINAL"  # ORIGINAL, SUSPICIOUS, HIGH_SIMILARITY, VERBATIM_PLAGIARISM


class AssignmentPlagiarismDetector:
    """
    Computes N-Gram shingles and Winnowing document fingerprints.
    """

    DEFAULT_SHINGLE_SIZE = 4  # 4-word shingles
    SIMILARITY_FLAG_THRESHOLD = 30.0  # Flag if >= 30% similar

    @classmethod
    def tokenize_and_clean(cls, text: str) -> List[str]:
        """Normalize text by converting to lowercase and stripping punctuation/whitespace."""
        clean_text = re.sub(r"[^a-zA-Z0-9\s]", " ", text.lower())
        return [w for w in clean_text.split() if len(w) > 1]

    @classmethod
    def generate_shingles(cls, tokens: List[str], n: int = DEFAULT_SHINGLE_SIZE) -> Set[str]:
        """Generate N-gram word shingles from a token list."""
        if len(tokens) < n:
            return {" ".join(tokens)} if tokens else set()

        shingles = set()
        for i in range(len(tokens) - n + 1):
            shingle_str = " ".join(tokens[i : i + n])
            # Hash shingle to 64-bit integer
            shingle_hash = hashlib.md5(shingle_str.encode("utf-8")).hexdigest()[:16]
            shingles.add(shingle_hash)

        return shingles

    @classmethod
    def compute_jaccard_similarity(cls, set_a: Set[str], set_b: Set[str]) -> float:
        """
        Calculate Jaccard Index: |A intersect B| / |A union B|
        """
        if not set_a or not set_b:
            return 0.0

        intersection = len(set_a.intersection(set_b))
        union = len(set_a.union(set_b))

        return round((intersection / union * 100.0), 2) if union > 0 else 0.0

    @classmethod
    def compare_submissions(
        cls,
        sub_a: Dict[str, Any],  # {"id": 1, "roll": "23CSE01", "text": "..."}
        sub_b: Dict[str, Any]   # {"id": 2, "roll": "23CSE02", "text": "..."}
    ) -> PlagiarismMatchReport:
        """Compare two student assignment submissions."""
        tokens_a = cls.tokenize_and_clean(sub_a.get("text", ""))
        tokens_b = cls.tokenize_and_clean(sub_b.get("text", ""))

        shingles_a = cls.generate_shingles(tokens_a)
        shingles_b = cls.generate_shingles(tokens_b)

        overlap = len(shingles_a.intersection(shingles_b))
        sim_pct = cls.compute_jaccard_similarity(shingles_a, shingles_b)

        if sim_pct >= 75.0:
            verdict = "VERBATIM_PLAGIARISM"
            flagged = True
        elif sim_pct >= 50.0:
            verdict = "HIGH_SIMILARITY"
            flagged = True
        elif sim_pct >= cls.SIMILARITY_FLAG_THRESHOLD:
            verdict = "SUSPICIOUS"
            flagged = True
        else:
            verdict = "ORIGINAL"
            flagged = False

        return PlagiarismMatchReport(
            submission_id_a=sub_a.get("id", 0),
            submission_id_b=sub_b.get("id", 0),
            student_roll_a=sub_a.get("roll", ""),
            student_roll_b=sub_b.get("roll", ""),
            similarity_score_pct=sim_pct,
            overlapping_n_grams_count=overlap,
            is_flagged=flagged,
            verdict=verdict
        )
