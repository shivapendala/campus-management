"""
EduCore Enterprise Framework - Corporate Recruitment Drive Schedule Optimizer

Optimizes corporate recruitment schedules to prevent conflict:
- Day-0 to Day-3 drive slot mapping
- Collision prevention across company assessment times
- Matching room and auditorium availability for pre-placement talks (PPTs)
"""

from typing import Dict, List, Any, Set, Tuple
import datetime


class PlacementDriveScheduler:
    """
    Orchestrates scheduling intervals for placement activities.
    """

    @classmethod
    def check_schedule_conflicts(
        cls,
        proposed_drive: Dict[str, Any],
        existing_schedule: List[Dict[str, Any]]
    ) -> Tuple[bool, List[str]]:
        """
        Verify if a new drive schedule conflicts with existing bookings.
        Each drive format: {
            "company_name": "Google",
            "date": "2026-09-10",
            "start_time": "09:00",
            "end_time": "12:00",
            "venue": "Seminar Hall A"
        }
        """
        conflicts = []
        prop_date = proposed_drive.get("date")
        prop_venue = proposed_drive.get("venue")

        # Convert times to minutes from midnight
        def get_minutes(t_str: str) -> int:
            h, m = map(int, t_str.split(":"))
            return h * 60 + m

        p_start = get_minutes(proposed_drive.get("start_time", "00:00"))
        p_end = get_minutes(proposed_drive.get("end_time", "00:00"))

        for idx, exist in enumerate(existing_schedule):
            if exist.get("date") != prop_date:
                continue

            e_start = get_minutes(exist.get("start_time", "00:00"))
            e_end = get_minutes(exist.get("end_time", "00:00"))

            # Overlap check
            time_overlap = (p_start < e_end) and (p_end > e_start)

            if time_overlap:
                # Venue conflict
                if exist.get("venue") == prop_venue:
                    conflicts.append(
                        f"Venue Conflict: {proposed_drive['company_name']} and {exist['company_name']} "
                        f"both requested {prop_venue} on {prop_date} during overlapping hours."
                    )
                else:
                    # General timing overlap (Warning only, unless same candidate pool)
                    conflicts.append(
                        f"Time Overlap Alert: {proposed_drive['company_name']} overlaps with "
                        f"{exist['company_name']} on {prop_date}. Ensure separate volunteer teams."
                    )

        has_conflict = len(conflicts) > 0
        return has_conflict, conflicts
