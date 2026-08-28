"""
EduCore Framework - NEP Outcome Attainment Ledger Reporter Helper

Generates summaries of program outcome attainment helper utilities.
"""

from typing import Dict, List, Any

class NEPOutcomeAttainmentLedgerReporterHelper:
    def __init__(self, regulation_code: str):
        self.regulation_code = regulation_code

    def format_log(self, po_code: str, score: float) -> str:
        return f"PO: {po_code} - Attainment: {score}%"
