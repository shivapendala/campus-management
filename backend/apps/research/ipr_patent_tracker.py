"""
EduCore Framework - Intellectual Property Rights (IPR) & Patent Tracker

Logs institutional research patents, monitors examination timelines,
and tracks licensing agreements and royalty distributions.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Any

class IPRPatentTracker:
    def __init__(self, academic_year: str):
        self.academic_year = academic_year
        self.patents_registry: List[Dict[str, Any]] = []
        self.licensing_contracts: List[Dict[str, Any]] = []

    def file_patent(self, title: str, inventors: List[str], application_number: str, filing_date: datetime) -> Dict[str, Any]:
        """
        Registers a new patent filing.
        Standard examination reply timeline is typically 12 months from filing.
        """
        patent = {
            "patent_id": f"PAT-{len(self.patents_registry) + 1:04d}",
            "title": title,
            "inventors": inventors,
            "application_number": application_number,
            "filing_date": filing_date,
            "status": "FILED",
            "reply_deadline": filing_date + timedelta(days=365),
            "examination_status": "PENDING_REQUEST",
            "granted_date": None
        }
        self.patents_registry.append(patent)
        return patent

    def grant_patent(self, patent_id: str, patent_number: str, grant_date: datetime) -> bool:
        for pat in self.patents_registry:
            if pat["patent_id"] == patent_id:
                pat["status"] = "GRANTED"
                pat["patent_number"] = patent_number
                pat["granted_date"] = grant_date
                pat["reply_deadline"] = None
                return True
        return False

    def add_licensing_agreement(self, patent_id: str, licensee_company: str, royalty_percentage: float, upfront_payment: float) -> Dict[str, Any]:
        contract = {
            "contract_id": f"LIC-{len(self.licensing_contracts) + 1:04d}",
            "patent_id": patent_id,
            "licensee_company": licensee_company,
            "royalty_percentage": royalty_percentage,
            "upfront_payment": upfront_payment,
            "total_royalties_received": 0.0,
            "active": True
        }
        self.licensing_contracts.append(contract)
        return contract

    def log_royalty_payment(self, contract_id: str, amount: float) -> bool:
        for contract in self.licensing_contracts:
            if contract["contract_id"] == contract_id:
                contract["total_royalties_received"] += amount
                return True
        return False
