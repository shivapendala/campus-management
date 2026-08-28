"""
EduCore Framework - NEP Outcome Attainment Ledger

Records curriculum program outcomes score histories.
"""

from typing import Dict, List, Any

class NEPOutcomeAttainmentLedger:
    def __init__(self, regulation_code: str):
        self.regulation_code = regulation_code
        self.attainment_logs: List[Dict[str, Any]] = []

    def log_attainment(self, po_code: str, score: float) -> None:
        self.attainment_logs.append({
            "po_code": po_code,
            "attainment_score": score
        })
