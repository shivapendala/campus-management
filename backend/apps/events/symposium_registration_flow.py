"""
EduCore Framework - Symposium Registration & Ticket Sales Flow

Handles delegate registrations, schedules workshops checkins,
and tracks transaction clearances against institutional account ledgers.
"""

import datetime
from typing import Dict, List, Any, Tuple

class SymposiumRegistrationFlow:
    def __init__(self, symposium_id: str, early_bird_deadline: datetime.datetime):
        self.symposium_id = symposium_id
        self.early_bird_deadline = early_bird_deadline
        self.registrations: List[Dict[str, Any]] = []
        self.ticket_pricing: Dict[str, float] = {
            "STUDENT": 500.0,
            "ACADEMICIAN": 1000.0,
            "INDUSTRY_DELEGATE": 2000.0
        }

    def calculate_registration_fee(self, delegate_type: str, registration_time: datetime.datetime) -> float:
        base_rate = self.ticket_pricing.get(delegate_type, 500.0)
        
        # Apply 20% discount for early bird registration
        if registration_time <= self.early_bird_deadline:
            return base_rate * 0.8
        return base_rate

    def register_delegate(self, delegate_id: str, name: str, delegate_type: str, email: str, payment_ref: str) -> Dict[str, Any]:
        """
        Processes a registration and issues a confirmation receipt.
        """
        now = datetime.datetime.now()
        fee = self.calculate_registration_fee(delegate_type, now)
        
        receipt = {
            "receipt_id": f"REC-{self.symposium_id}-{len(self.registrations) + 1:04d}",
            "delegate_id": delegate_id,
            "name": name,
            "delegate_type": delegate_type,
            "email": email,
            "amount_paid": fee,
            "payment_reference": payment_ref,
            "registration_timestamp": now,
            "checked_in": False
        }
        self.registrations.append(receipt)
        return receipt

    def mark_attendance(self, receipt_id: str) -> bool:
        for reg in self.registrations:
            if reg["receipt_id"] == receipt_id:
                reg["checked_in"] = True
                return True
        return False

    def list_checked_in_delegates(self) -> List[Dict[str, Any]]:
        return [r for r in self.registrations if r["checked_in"]]
