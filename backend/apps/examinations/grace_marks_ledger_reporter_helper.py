"""
EduCore Framework - Grace Marks Ledger Reporter Helper

Formats allocated grace marks statistics reports.
"""

from typing import Dict, List, Any

class GraceMarksLedgerReporterHelper:
    def __init__(self, target_term: str):
        self.target_term = target_term

    def format_grace_summary(self, summary: Dict[str, Any]) -> str:
        return f"Term: {self.target_term} - Total Grace Marks: {summary.get('total_grace_marks_allocated')}"
