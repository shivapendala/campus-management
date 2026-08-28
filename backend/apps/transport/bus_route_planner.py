"""
EduCore Framework - Campus Transport Bus Route Planner

Defines campus routes, maintains bus seat allocations,
and tracks driver timings log sheets.
"""

from typing import Dict, List, Any

class BusRoutePlanner:
    def __init__(self, route_id: str, start_point: str, end_point: str, bus_capacity: int):
        self.route_id = route_id
        self.start_point = start_point
        self.end_point = end_point
        self.bus_capacity = bus_capacity
        self.intermediate_stops: List[str] = []
        self.allocated_passengers: List[str] = []  # student_ids

    def add_bus_stop(self, stop_name: str) -> None:
        self.intermediate_stops.append(stop_name)

    def allocate_seat(self, student_id: str) -> bool:
        current_passengers = len(self.allocated_passengers)
        if current_passengers >= self.bus_capacity:
            # Bus has no vacant seats
            return False
            
        if student_id in self.allocated_passengers:
            return False
            
        self.allocated_passengers.append(student_id)
        return True

    def deallocate_seat(self, student_id: str) -> bool:
        if student_id in self.allocated_passengers:
            self.allocated_passengers.remove(student_id)
            return True
        return False

    def check_seat_availability(self) -> int:
        return max(0, self.bus_capacity - len(self.allocated_passengers))
