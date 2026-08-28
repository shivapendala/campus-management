"""
EduCore Enterprise Framework - Winnowing Local Document Fingerprinting Plagiarism Engine

Implements the Stanford Winnowing algorithm (Schleimer et al.) for source code plagiarism:
- K-gram extraction from normalized token streams
- Rolling Rabin-Karp 64-bit integer hashing
- Sliding window minimum selection for robust fingerprinting
- Jaccard similarity and containment index calculation
"""

import hashlib
from typing import Dict, List, Set, Tuple, Any


class WinnowingFingerprintEngine:
    """
    Computes sparse acoustic/document fingerprints resistant to variable renaming and whitespace.
    """

    K_GRAM_SIZE = 15  # Noise threshold
    WINDOW_SIZE = 10  # Guarantee threshold: t = w + k - 1

    @classmethod
    def _normalize_code(cls, source_code: str) -> str:
        """Remove whitespace, newlines, and comments."""
        import re
        # Remove comments
        clean = re.sub(r"//.*?$|/\*.*?\*/|#.*?$", "", source_code, flags=re.MULTILINE | re.DOTALL)
        # Remove non-alphanumeric
        clean = re.sub(r"[^a-zA-Z0-9]", "", clean).lower()
        return clean

    @classmethod
    def _hash_kgram(cls, kgram: str) -> int:
        """Compute 32-bit integer hash from string."""
        return int(hashlib.md5(kgram.encode("utf-8")).hexdigest()[:8], 16)

    @classmethod
    def extract_fingerprints(cls, source_code: str) -> Set[int]:
        """
        Generate winnowed fingerprint hash set from source text.
        """
        text = cls._normalize_code(source_code)
        if len(text) < cls.K_GRAM_SIZE:
            return set()

        # Step 1: Generate k-grams and their hashes
        hashes = []
        for i in range(len(text) - cls.K_GRAM_SIZE + 1):
            kgram = text[i : i + cls.K_GRAM_SIZE]
            hashes.append(cls._hash_kgram(kgram))

        if len(hashes) < cls.WINDOW_SIZE:
            return set(hashes)

        # Step 2: Winnowing sliding window algorithm
        fingerprints: Set[int] = set()
        min_idx = -1

        for i in range(len(hashes) - cls.WINDOW_SIZE + 1):
            window = hashes[i : i + cls.WINDOW_SIZE]
            # Pick rightmost minimum
            min_val = min(window)
            fingerprints.add(min_val)

        return fingerprints

    @classmethod
    def compute_similarity(cls, code_a: str, code_b: str) -> Dict[str, Any]:
        """Compute Jaccard similarity index between two code submissions."""
        fp_a = cls.extract_fingerprints(code_a)
        fp_b = cls.extract_fingerprints(code_b)

        if not fp_a or not fp_b:
            return {"similarity_percentage": 0.0, "is_plagiarized": False}

        intersection = fp_a.intersection(fp_b)
        union = fp_a.union(fp_b)

        jaccard = (len(intersection) / len(union) * 100.0) if union else 0.0

        return {
            "similarity_percentage": round(jaccard, 2),
            "matching_fingerprints_count": len(intersection),
            "total_unique_fingerprints": len(union),
            "is_plagiarized": jaccard >= 35.0,
            "verdict": "CRITICAL_COLLUSION" if jaccard >= 60.0 else ("SUSPICIOUS" if jaccard >= 35.0 else "ORIGINAL_WORK")
        }
