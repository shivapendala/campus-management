"""
EduCore Enterprise Framework - Financial & Fee Ledger Report Exporter

Generates structured institutional fiscal statements:
- Fee Collection vs Arrears Summary by Department
- Scholarship Disbursements Summary
- Payment Gateway Reconciliation Log
- Annual Audit Balance Sheet
"""

from typing import Dict, List, Any, Optional


class FinancialReportExporter:
    """
    Exports institutional accounting summaries for bursar and statutory auditors.
    """

    @classmethod
    def generate_fee_collection_statement(
        cls,
        department_stats: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Format departmental fee collection ledger statement."""
        total_demand = sum(float(d.get("total_demand", 0.0)) for d in department_stats)
        total_collected = sum(float(d.get("collected_amount", 0.0)) for d in department_stats)
        total_arrears = sum(float(d.get("pending_amount", 0.0)) for d in department_stats)
        total_waivers = sum(float(d.get("waivers_granted", 0.0)) for d in department_stats)

        collection_efficiency = (total_collected / total_demand * 100.0) if total_demand > 0 else 0.0

        return {
            "total_demand": round(total_demand, 2),
            "total_collected": round(total_collected, 2),
            "total_arrears": round(total_arrears, 2),
            "total_waivers_concessions": round(total_waivers, 2),
            "collection_efficiency_pct": round(collection_efficiency, 2),
            "departmental_breakdown": department_stats
        }
