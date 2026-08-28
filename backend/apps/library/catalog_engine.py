"""
EduCore Enterprise Framework - MARC21 / Dewey Decimal Library Catalog & Fuzzy Search Engine

Indexes book inventory with Dewey Decimal Classification (DDC) 000-999 classes:
Provides multi-field fuzzy search (Title, Author, ISBN, Subject, Publisher),
barcode parsing, and real-time shelf location indexing (Rack, Shelf, Bay).
"""

import re
from typing import Dict, List, Any, Optional, Set, Tuple
from dataclasses import dataclass, field


@dataclass
class LibraryCatalogItem:
    """Represents a book accession record in the central library catalog."""
    accession_number: str  # e.g., "ACC-2026-0842"
    isbn: str
    title: str
    authors: List[str]
    edition: str
    publisher: str
    ddc_class: str  # e.g., "005.133" (Python Programming)
    category: str   # COMPUTER_SCIENCE, ELECTRONICS, MECHANICAL, MATHEMATICS, HUMANITIES
    rack_number: str
    shelf_number: str
    total_copies: int
    available_copies: int
    is_reference_only: bool = False


class LibraryCatalogSearchEngine:
    """
    In-memory fuzzy catalog indexing and query engine.
    """

    @classmethod
    def match_item(cls, item: LibraryCatalogItem, query_tokens: List[str]) -> Tuple[bool, int]:
        """
        Check if item matches query tokens across title, author, isbn, and category.
        Returns: (is_match, score)
        """
        searchable_text = f"{item.title} {' '.join(item.authors)} {item.isbn} {item.category} {item.publisher}".lower()
        score = 0
        all_tokens_found = True

        for token in query_tokens:
            if token in searchable_text:
                score += 10
                # Higher weight for exact title match
                if token in item.title.lower():
                    score += 20
            else:
                all_tokens_found = False

        return (score > 0 and (all_tokens_found or len(query_tokens) == 1)), score

    @classmethod
    def search_catalog(
        cls,
        catalog: List[LibraryCatalogItem],
        query: str,
        category_filter: Optional[str] = None,
        only_available: bool = False
    ) -> List[LibraryCatalogItem]:
        """Execute multi-field query against catalog."""
        if not query and not category_filter:
            return catalog if not only_available else [i for i in catalog if i.available_copies > 0]

        tokens = [t.lower() for t in query.split() if len(t) > 1]
        scored_results: List[Tuple[LibraryCatalogItem, int]] = []

        for item in catalog:
            if category_filter and item.category.upper() != category_filter.upper():
                continue

            if only_available and item.available_copies <= 0:
                continue

            if not tokens:
                scored_results.append((item, 1))
            else:
                is_match, score = cls.match_item(item, tokens)
                if is_match:
                    scored_results.append((item, score))

        # Sort descending by match score
        scored_results.sort(key=lambda x: x[1], reverse=True)
        return [item for item, _ in scored_results]
