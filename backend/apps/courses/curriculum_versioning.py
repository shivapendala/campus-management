"""
EduCore Enterprise Framework - Academic Regulation Versioning & Curriculum Diff Engine

Tracks multi-year curriculum evolution:
- Regulation Editions: R19, R21, R23, R26 Autonomous Schemes
- Course syllabus difference comparator (Topic additions, deletions, credit changes)
- Board of Studies (BOS) and Academic Council approval resolution registry
"""

from typing import Dict, List, Any, Optional, Set


class CurriculumVersioningEngine:
    """
    Computes structural differences and credit equivalence between academic regulations.
    """

    @classmethod
    def compare_course_versions(
        cls,
        old_syllabus_units: List[Dict[str, Any]],
        new_syllabus_units: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """
        Compute percentage syllabus change between regulation versions.
        """
        old_topics = set()
        for u in old_syllabus_units:
            for word in u.get("topics", "").replace(",", " ").split():
                if len(word) > 3:
                    old_topics.add(word.lower())

        new_topics = set()
        for u in new_syllabus_units:
            for word in u.get("topics", "").replace(",", " ").split():
                if len(word) > 3:
                    new_topics.add(word.lower())

        added = new_topics - old_topics
        removed = old_topics - new_topics
        retained = old_topics.intersection(new_topics)

        total_unique = len(old_topics.union(new_topics))
        change_pct = ((len(added) + len(removed)) / total_unique * 100.0) if total_unique > 0 else 0.0

        return {
            "retained_topics_count": len(retained),
            "new_topics_added_count": len(added),
            "old_topics_removed_count": len(removed),
            "syllabus_modification_percentage": round(change_pct, 1),
            "requires_academic_council_approval": change_pct >= 20.0,
            "added_sample": list(added)[:5],
            "removed_sample": list(removed)[:5]
        }
