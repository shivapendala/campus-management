"""
EduCore Framework - Disciplinary Committee Hearings & Actions

Mainages the scheduling, logging, and actions of the university disciplinary committee
against misconduct, violations, or campus rules infractions.
"""

from datetime import datetime, timedelta
from typing import Dict, List, Any

class DisciplinaryCommitteeHearings:
    def __init__(self, academic_year: str):
        self.academic_year = academic_year
        self.hearings_list: List[Dict[str, Any]] = []
        self.disciplinary_slabs: Dict[str, Dict[str, Any]] = {
            "CAT_A_MINOR": {"fine": 500.0, "suspension_days": 0, "parental_call": False},
            "CAT_B_MEDIUM": {"fine": 2000.0, "suspension_days": 3, "parental_call": True},
            "CAT_C_SEVERE": {"fine": 10000.0, "suspension_days": 15, "parental_call": True},
            "CAT_D_EXPULSION": {"fine": 0.0, "suspension_days": 365, "parental_call": True}
        }

    def schedule_hearing(self, student_id: str, incident_code: str, description: str, hearing_date: datetime) -> Dict[str, Any]:
        hearing = {
            "case_id": f"DISC-CASE-{len(self.hearings_list) + 1:04d}",
            "student_id": student_id,
            "incident_code": incident_code,
            "description": description,
            "hearing_date": hearing_date,
            "status": "SCHEDULED",
            "findings": "",
            "action_recommended": "NONE",
            "appeal_deadline": None
        }
        self.hearings_list.append(hearing)
        return hearing

    def finalize_hearing(self, case_id: str, findings: str, severity: str) -> Dict[str, Any]:
        """
        Finalizes a case and computes appeal timelines (normally 14 days from decision).
        """
        for case in self.hearings_list:
            if case["case_id"] == case_id:
                case["status"] = "DECIDED"
                case["findings"] = findings
                case["action_recommended"] = severity
                
                slab = self.disciplinary_slabs.get(severity, {"fine": 0.0, "suspension_days": 0, "parental_call": False})
                case["fine_imposed"] = slab["fine"]
                case["suspension_days"] = slab["suspension_days"]
                case["parental_notified"] = slab["parental_call"]
                
                # Appeal deadline is 14 days from today
                case["appeal_deadline"] = datetime.now() + timedelta(days=14)
                return case
        raise ValueError(f"Case '{case_id}' was not found in disciplinary records.")

    def record_appeal(self, case_id: str, student_statement: str) -> bool:
        """
        Submits an appeal request before the deadline check.
        """
        for case in self.hearings_list:
            if case["case_id"] == case_id:
                if case["status"] != "DECIDED":
                    return False
                
                deadline = case["appeal_deadline"]
                if deadline and datetime.now() > deadline:
                    # Appeal window closed
                    return False
                    
                case["status"] = "APPEAL_SUBMITTED"
                case["appeal_statement"] = student_statement
                return True
        return False
