"""
EduCore Framework - Hostel Room Allocation Ledger

Manages student hostel allocations, audits vacancy status,
and handles room transfer requests.
"""

from typing import Dict, List, Any

class RoomAllocationLedger:
    def __init__(self, block_name: str, total_rooms: int, capacity_per_room: int):
        self.block_name = block_name
        self.total_rooms = total_rooms
        self.capacity_per_room = capacity_per_room
        self.allocated_beds: Dict[str, List[str]] = {}  # room_no -> [student_id]

    def allocate_room(self, student_id: str, room_no: str) -> bool:
        if room_no not in self.allocated_beds:
            self.allocated_beds[room_no] = []
            
        current_occupancy = len(self.allocated_beds[room_no])
        if current_occupancy >= self.capacity_per_room:
            # Room is full
            return False
            
        # Check if student already allocated elsewhere
        for r_no, occupants in self.allocated_beds.items():
            if student_id in occupants:
                # Student is already in hostel registry
                return False
                
        self.allocated_beds[room_no].append(student_id)
        return True

    def deallocate_room(self, student_id: str) -> bool:
        for r_no, occupants in self.allocated_beds.items():
            if student_id in occupants:
                occupants.remove(student_id)
                return True
        return False

    def request_room_transfer(self, student_id: str, target_room_no: str) -> bool:
        """
        Transfers a student to a new room if vacancy exists.
        """
        # Verify target occupancy
        target_occupants = self.allocated_beds.get(target_room_no, [])
        if len(target_occupants) >= self.capacity_per_room:
            return False
            
        # Deallocate old room
        success = self.deallocate_room(student_id)
        if not success:
            return False
            
        # Allocate new room
        return self.allocate_room(student_id, target_room_no)
