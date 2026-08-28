"""
EduCore Framework - NEP Outcome Attainment Ledger Reporter Printer Helper

Prints formatted summaries of program outcome attainment records.
"""

from typing import Dict, List, Any

class NEPOutcomeAttainmentLedgerReporterPrinterHelper:
    def __init__(self):
        pass

    def print_formatted_log(self, label: str, formatted_log: str) -> None:
        print(f"[{label}] {formatted_log}")
