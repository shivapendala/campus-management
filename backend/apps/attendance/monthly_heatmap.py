"""
EduCore Enterprise Framework - Monthly Calendar Heatmap Grid Generator

Builds calendar day-by-day attendance matrices for student and faculty portals:
Color codes each day (Green = Present, Red = Absent, Yellow = Late, Blue = Holiday).
"""

from typing import Dict, List, Any, Optional
import calendar
import datetime


class MonthlyAttendanceHeatmapBuilder:
    """
    Generates structured calendar monthly attendance grids.
    """

    @classmethod
    def generate_month_grid(
        cls,
        year: int,
        month: int,
        daily_records: Dict[int, str]  # { 1: "PRESENT", 2: "PRESENT", 3: "ABSENT", ... }
    ) -> List[List[Dict[str, Any]]]:
        """
        Build 2D matrix representing standard 7-column calendar (Mon-Sun).
        """
        cal = calendar.monthcalendar(year, month)
        grid = []

        for week in cal:
            week_row = []
            for day in week:
                if day == 0:
                    week_row.append({"day": 0, "status": "OUT_OF_MONTH", "is_active": False})
                else:
                    status = daily_records.get(day, "PRESENT")
                    # Check if Sunday
                    dt = datetime.date(year, month, day)
                    if dt.weekday() == 6:
                        status = "HOLIDAY_SUNDAY"

                    week_row.append({
                        "day": day,
                        "date": dt.isoformat(),
                        "status": status,
                        "is_active": True
                    })
            grid.append(week_row)

        return grid
