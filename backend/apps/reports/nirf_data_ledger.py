"""
EduCore Framework - NIRF Data Ledger

Records graduation outcomes and research parameters.
"""

from typing import Dict, List, Any

class NIRFDataLedger:
    def __init__(self, target_year: str):
        self.target_year = target_year
        self.metrics_registry: List[Dict[str, Any]] = []

    def log_metrics(self, category: str, graduation_pct: float) -> None:
        self.metrics_registry.append({
            "category": category,
            "graduation_percentage": graduation_pct
        })
