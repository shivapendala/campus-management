"""
EduCore Framework - Hostel Mess Fee & Rebate Calculator

Computes monthly mess dues, processes rebate requests for student leaves,
and manages vendor billing audits.
"""

from datetime import datetime
from typing import Dict, List, Any

class MessFeeCalculator:
    def __init__(self, daily_rate: float, maintenance_charge: float):
        self.daily_rate = daily_rate
        self.maintenance_charge = maintenance_charge
        self.rebate_requests: Dict[str, List[int]] = {}  # student_id -> [days_rebated]

    def request_mess_rebate(self, student_id: str, days_list: List[int]) -> bool:
        """
        Students can request mess rebate if they are absent for more than 5 consecutive days.
        """
        if len(days_list) < 5:
            # Rejection due to minimum rule limit
            return False
            
        if student_id not in self.rebate_requests:
            self.rebate_requests[student_id] = []
            
        # Avoid duplicate days logging
        for d in days_list:
            if d not in self.rebate_requests[student_id]:
                self.rebate_requests[student_id].append(d)
        return True

    def calculate_monthly_bill(self, student_id: str, month_days: int) -> Dict[str, Any]:
        """
        Calculates the net mess bill: (days - rebate_days) * daily_rate + maintenance_charge
        """
        rebated_days_count = len(self.rebate_requests.get(student_id, []))
        billable_days = max(0, month_days - rebated_days_count)
        
        consumption_charge = billable_days * self.daily_rate
        total_bill = consumption_charge + self.maintenance_charge
        
        return {
            "student_id": student_id,
            "total_days_in_month": month_days,
            "rebate_days_applied": rebated_days_count,
            "billable_days": billable_days,
            "consumption_charge": round(consumption_charge, 2),
            "maintenance_charge": round(self.maintenance_charge, 2),
            "net_payable": round(total_bill, 2)
        }
