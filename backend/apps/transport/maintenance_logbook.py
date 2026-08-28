"""
EduCore Framework - Campus Transport Fleet Maintenance Logbook

Tracks scheduled bus service logs, monitors fitness certificate validity,
and estimates fuel efficiency averages.
"""

import datetime
from typing import Dict, List, Any

class FleetMaintenanceLogbook:
    def __init__(self, vehicle_number: str, registration_date: datetime.date):
        self.vehicle_number = vehicle_number
        self.registration_date = registration_date
        self.service_history: List[Dict[str, Any]] = []
        self.fuel_logs: List[Dict[str, Any]] = []

    def record_service_event(self, description: str, cost: float, mileage: float, service_date: datetime.date) -> Dict[str, Any]:
        event = {
            "event_id": f"SRV-{self.vehicle_number}-{len(self.service_history) + 1:03d}",
            "description": description,
            "cost": cost,
            "mileage": mileage,
            "service_date": service_date,
            "next_due_date": service_date + datetime.timedelta(days=180)  # Standard 6-month checkup cycle
        }
        self.service_history.append(event)
        return event

    def log_fuel_purchase(self, liters: float, total_cost: float, start_mileage: float, end_mileage: float) -> float:
        """
        Logs fuel receipt and returns calculated km per liter.
        """
        distance = end_mileage - start_mileage
        if liters <= 0 or distance <= 0:
            return 0.0
            
        efficiency = distance / liters
        self.fuel_logs.append({
            "liters": liters,
            "total_cost": total_cost,
            "distance": distance,
            "efficiency": round(efficiency, 2),
            "timestamp": datetime.datetime.now()
        })
        return round(efficiency, 2)

    def calculate_total_operational_costs(self) -> float:
        service_cost = sum(event["cost"] for event in self.service_history)
        fuel_cost = sum(log["total_cost"] for log in self.fuel_logs)
        return round(service_cost + fuel_cost, 2)
