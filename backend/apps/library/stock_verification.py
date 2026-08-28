"""
EduCore Enterprise Framework - Annual Library Physical Stock Verification Engine

Performs barcode scanner stock audits:
- Reconciles physical scanned barcodes against accession master catalog
- Identifies missing, damaged, or unreturned volumes
- Generates statutory physical verification audit certificate for NAAC Criterion 4
"""

from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass, field


@dataclass
class StockAuditFindings:
    """Findings of an annual library inventory audit."""
    academic_year: str
    total_catalog_accessions: int
    scanned_physical_count: int
    matched_count: int
    missing_count: int
    damaged_weeded_out_count: int
    loss_percentage: float
    is_within_ugc_loss_tolerance: bool  # UGC permits loss <= 3 to 5 books per 1000 issued


class LibraryStockVerificationManager:
    """
    Computes stock discrepancy metrics.
    """

    @classmethod
    def execute_stock_reconciliation(
        cls,
        academic_year: str,
        catalog_accession_ids: Set[str],
        scanned_physical_barcodes: Set[str],
        damaged_accession_ids: Set[str],
        total_books_issued_during_year: int
    ) -> StockAuditFindings:
        """Calculate catalog reconciliation metrics."""
        total_accessions = len(catalog_accession_ids)
        matched = catalog_accession_ids.intersection(scanned_physical_barcodes)
        matched_count = len(matched)

        missing = catalog_accession_ids - (scanned_physical_barcodes.union(damaged_accession_ids))
        missing_count = len(missing)
        damaged_count = len(damaged_accession_ids)

        loss_pct = (missing_count / total_accessions * 100.0) if total_accessions > 0 else 0.0

        # UGC permissible loss: <= 3 per 1000 issued
        max_tolerable_missing = int((total_books_issued_during_year / 1000.0) * 3)
        within_tolerance = missing_count <= max(5, max_tolerable_missing)

        return StockAuditFindings(
            academic_year=academic_year,
            total_catalog_accessions=total_accessions,
            scanned_physical_count=len(scanned_physical_barcodes),
            matched_count=matched_count,
            missing_count=missing_count,
            damaged_weeded_out_count=damaged_count,
            loss_percentage=round(loss_pct, 2),
            is_within_ugc_loss_tolerance=within_tolerance
        )
