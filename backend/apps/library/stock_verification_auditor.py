"""
EduCore Framework - Library Stock Verification Auditor

Compares active physical shelf scans with system catalog accession records,
logs inventory mismatches, identifies missing volumes, and flags misplaced books.
"""

from datetime import datetime
from typing import Dict, List, Set, Any

class StockVerificationAuditor:
    def __init__(self, audit_id: str, auditor_name: str):
        self.audit_id = audit_id
        self.auditor_name = auditor_name
        self.audit_date = datetime.now()
        self.catalog_accession_numbers: Set[str] = set()
        self.scanned_records: List[Dict[str, Any]] = []

    def load_system_catalog(self, accession_list: List[str]) -> None:
        """
        Loads the active accession list from the main catalog database.
        """
        self.catalog_accession_numbers = set(accession_list)

    def record_physical_scan(self, accession_number: str, shelf_scanned: str, condition: str) -> None:
        """
        Logs a scanned book during physical stock verification.
        """
        self.scanned_records.append({
            "accession_number": accession_number,
            "shelf_scanned": shelf_scanned,
            "condition": condition,
            "scan_time": datetime.now()
        })

    def perform_audit_reconciliation(self, shelf_mappings: Dict[str, str]) -> Dict[str, Any]:
        """
        Reconciles system records and physical scans.
        Identifies:
        - Missing Books: In catalog but not physically scanned.
        - Misplaced Books: Scanned on a shelf different from the registered shelf.
        - Uncataloged Books: Scanned but not found in the catalog.
        """
        scanned_accessions = {r["accession_number"] for r in self.scanned_records}
        
        missing_books = self.catalog_accession_numbers - scanned_accessions
        uncataloged_books = scanned_accessions - self.catalog_accession_numbers
        
        misplaced_books: List[Dict[str, Any]] = []
        intact_books_count = 0
        
        for record in self.scanned_records:
            acc_no = record["accession_number"]
            if acc_no in self.catalog_accession_numbers:
                expected_shelf = shelf_mappings.get(acc_no)
                actual_shelf = record["shelf_scanned"]
                
                if expected_shelf and expected_shelf != actual_shelf:
                    misplaced_books.append({
                        "accession_number": acc_no,
                        "expected_shelf": expected_shelf,
                        "actual_shelf": actual_shelf
                    })
                else:
                    intact_books_count += 1
                    
        discrepancy_rate = 0.0
        total_catalog = len(self.catalog_accession_numbers)
        if total_catalog > 0:
            total_discrepancies = len(missing_books) + len(misplaced_books)
            discrepancy_rate = (total_discrepancies / total_catalog) * 100.0
            
        return {
            "audit_id": self.audit_id,
            "audit_run_at": self.audit_date,
            "total_catalog_count": total_catalog,
            "total_scanned_count": len(self.scanned_records),
            "missing_books_count": len(missing_books),
            "missing_accessions": list(missing_books),
            "misplaced_books_count": len(misplaced_books),
            "misplaced_records": misplaced_books,
            "uncataloged_books_count": len(uncataloged_books),
            "uncataloged_accessions": list(uncataloged_books),
            "audit_intact_count": intact_books_count,
            "discrepancy_percentage": round(discrepancy_rate, 2)
        }
