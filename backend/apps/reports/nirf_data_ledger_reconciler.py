"""
EduCore Framework - NIRF Data Ledger Reconciler

Reconciles compiled metrics lists against database statistics.
"""

from typing import Dict, List, Any

class NIRFDataLedgerReconciler:
    def __init__(self, target_year: str):
        self.target_year = target_year
        self.anomalies: List[Dict[str, Any]] = []

    def reconcile_metrics(self, ledger_records: List[Dict[str, Any]], computed_statistics: Dict[str, float]) -> List[Dict[str, Any]]:
        for record in ledger_records:
            cat = record["category"]
            ledger_pct = record["graduation_percentage"]
            
            stat_pct = computed_statistics.get(cat, 0.0)
            if abs(ledger_pct - stat_pct) > 0.01:
                self.anomalies.append({
                    "category": cat,
                    "ledger_percentage": ledger_pct,
                    "statistics_percentage": stat_pct,
                    "status": "NIRF_GRADUATION_METRICS_DISCREPANCY"
                })
        return self.anomalies
