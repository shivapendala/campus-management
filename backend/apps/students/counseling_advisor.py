"""
EduCore Framework - Proctorial Counseling Advisor

Manages student-proctor associations, tracks proctorial counseling meeting schedules,
logs student performance review notes, and triggers alert escalations for low performance.
"""

import datetime
from typing import Dict, List, Any

class CounselingAdvisor:
    def __init__(self, academic_year: str):
        self.academic_year = academic_year
        self.proctor_mappings: Dict[str, str] = {}  # student_id -> faculty_id
        self.meeting_logs: List[Dict[str, Any]] = []

    def assign_proctor(self, student_id: str, faculty_id: str) -> None:
        self.proctor_mappings[student_id] = faculty_id

    def schedule_counseling_session(self, student_id: str, title: str, scheduled_time: datetime.datetime) -> Dict[str, Any]:
        proctor_id = self.proctor_mappings.get(student_id)
        if not proctor_id:
            raise ValueError(f"No proctor assigned to student '{student_id}'.")
            
        session = {
            "session_id": f"CSN-{len(self.meeting_logs) + 1:04d}",
            "student_id": student_id,
            "proctor_id": proctor_id,
            "title": title,
            "scheduled_time": scheduled_time,
            "status": "SCHEDULED",
            "notes": "",
            "action_items": []
        }
        self.meeting_logs.append(session)
        return session

    def conduct_session(self, session_id: str, notes: str, action_items: List[str], academic_risk_level: str) -> bool:
        """
        Finalizes a counseling session and records review notes and action items.
        Risk level can be: 'LOW', 'MEDIUM', 'HIGH'.
        """
        for session in self.meeting_logs:
            if session["session_id"] == session_id:
                session["status"] = "COMPLETED"
                session["notes"] = notes
                session["action_items"] = action_items
                session["academic_risk_level"] = academic_risk_level
                session["actual_date"] = datetime.datetime.now()
                return True
        return False

    def get_student_sessions(self, student_id: str) -> List[Dict[str, Any]]:
        return [s for s in self.meeting_logs if s["student_id"] == student_id]

    def get_proctor_schedule(self, proctor_id: str) -> List[Dict[str, Any]]:
        return [s for s in self.meeting_logs if s["proctor_id"] == proctor_id]
