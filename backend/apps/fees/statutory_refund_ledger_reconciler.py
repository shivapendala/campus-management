"""
EduCore Framework - Statutory Refund Ledger Reconciler

Reconciles processed refund payouts with transaction balances.
"""

from typing import Dict, List, Any

class StatutoryRefundLedgerReconciler:
    def __init__(self, academic_year: str):
        self.academic_year = academic_year
        self.reconciliation_anomalies: List[Dict[str, Any]] = []

    def reconcile_ledgers(self, ledger_records: List[Dict[str, Any]], bank_statement_records: Dict[str, float]) -> List[Dict[str, Any]]:
        for record in ledger_records:
            ref = record["payment_reference"]
            amount = record["amount"]
            
            bank_amount = bank_statement_records.get(ref, 0.0)
            if amount != bank_amount:
                self.reconciliation_anomalies.append({
                    "payment_reference": ref,
                    "ledger_amount": amount,
                    "bank_amount": bank_amount,
                    "status": "REFUND_PAYOUT_MISMATCH"
                })
        return self.reconciliation_anomalies
