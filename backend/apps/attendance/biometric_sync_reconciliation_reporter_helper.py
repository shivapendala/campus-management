"""
EduCore Framework - Biometric Sync Reconciliation Reporter Helper

Formats device sync packets report summaries.
"""

from typing import Dict, List, Any

class BiometricSyncReconciliationReporterHelper:
    def __init__(self, target_term: str):
        self.target_term = target_term

    def format_summary(self, summary: Dict[str, Any]) -> str:
        return f"Term: {self.target_term} - Total Packets: {summary.get('total_packets')}"
