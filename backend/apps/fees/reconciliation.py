"""
EduCore Enterprise Framework - Payment Gateway Settlement & Bank Reconciliation

Reconciles external payment gateway webhook payloads (Razorpay, Stripe, HDFC Bank NEFT)
against institutional internal transaction records to resolve chargebacks and unmatched orders.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass


@dataclass
class GatewaySettlementItem:
    """Payment gateway settlement row."""
    gateway_order_id: str
    gateway_payment_id: str
    amount: float
    fees_deducted: float
    tax_deducted: float
    net_settled_amount: float
    status: str  # CAPTURED, FAILED, REFUNDED


class PaymentReconciliationEngine:
    """
    Matches gateway settlement batch with internal fee invoices.
    """

    @classmethod
    def reconcile_settlement_batch(
        cls,
        gateway_items: List[GatewaySettlementItem],
        internal_invoices: Dict[str, float]  # { order_id: expected_amount }
    ) -> Dict[str, Any]:
        """
        Reconcile payment items and flag discrepancies or missing transactions.
        """
        matched: List[Dict[str, Any]] = []
        discrepancies: List[Dict[str, Any]] = []
        unmatched_gateway: List[GatewaySettlementItem] = []

        for item in gateway_items:
            expected = internal_invoices.get(item.gateway_order_id)
            if expected is None:
                unmatched_gateway.append(item)
            elif abs(expected - item.amount) < 0.01 and item.status == "CAPTURED":
                matched.append({
                    "order_id": item.gateway_order_id,
                    "payment_id": item.gateway_payment_id,
                    "amount": item.amount,
                    "net_settled": item.net_settled_amount,
                    "status": "RECONCILED"
                })
            else:
                discrepancies.append({
                    "order_id": item.gateway_order_id,
                    "expected_amount": expected,
                    "gateway_amount": item.amount,
                    "gateway_status": item.status,
                    "variance": item.amount - (expected or 0.0)
                })

        total_settled = sum(m["net_settled"] for m in matched)

        return {
            "total_processed": len(gateway_items),
            "matched_count": len(matched),
            "discrepancies_count": len(discrepancies),
            "unmatched_count": len(unmatched_gateway),
            "total_settled_amount": round(total_settled, 2),
            "reconciliation_health_pct": round((len(matched) / len(gateway_items) * 100.0), 2) if gateway_items else 0.0,
            "discrepancies": discrepancies
        }
