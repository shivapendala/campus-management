"""
EduCore Enterprise Framework - Attendance Shortage & Condonation Workflow

Evaluates semester end attendance compliance according to university statutes:
- Eligible for Exams: Attendance >= 75.0%
- Condonation Bracket: 65.0% <= Attendance < 75.0% (Permitted with statutory fee & medical certificate)
- Detained / Not Eligible: Attendance < 65.0% (Strict academic detention)
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class AttendanceAuditReport:
    """Semester attendance audit finding for a student."""
    student_id: int
    roll_number: str
    student_name: str
    department: str
    total_classes_held: int
    total_classes_attended: int
    attendance_percentage: float
    eligibility_status: str  # ELIGIBLE, CONDONATION_REQUIRED, DETAINED
    condonation_fee: float = 0.0
    medical_documents_verified: bool = False
    remedial_hours_required: int = 0


class AttendanceCondonationManager:
    """
    Computes statutory condonation fee schedules and generates shortage audit rosters.
    """

    STATUTORY_CONDONATION_FEE_PER_PERCENT = 500.0  # Rs. 500 per percentage point below 75%
    BASE_CONDONATION_FEE = 1500.0

    @classmethod
    def audit_student_attendance(
        cls,
        student_id: int,
        roll_number: str,
        name: str,
        department: str,
        classes_held: int,
        classes_attended: int,
        medical_exemption_verified: bool = False
    ) -> AttendanceAuditReport:
        """Evaluate statutory semester attendance standing."""
        if classes_held <= 0:
            pct = 100.0
        else:
            pct = round((classes_attended / classes_held) * 100.0, 2)

        if pct >= 75.0:
            status = "ELIGIBLE"
            fee = 0.0
            remedial_hours = 0
        elif pct >= 65.0:
            status = "CONDONATION_REQUIRED"
            shortage_points = 75.0 - pct
            fee = cls.BASE_CONDONATION_FEE + (shortage_points * cls.STATUTORY_CONDONATION_FEE_PER_PERCENT)
            remedial_hours = int(shortage_points * 2)
        else:
            status = "DETAINED"
            fee = 0.0
            remedial_hours = 0

        return AttendanceAuditReport(
            student_id=student_id,
            roll_number=roll_number,
            student_name=name,
            department=department,
            total_classes_held=classes_held,
            total_classes_attended=classes_attended,
            attendance_percentage=pct,
            eligibility_status=status,
            condonation_fee=round(fee, 2),
            medical_documents_verified=medical_exemption_verified,
            remedial_hours_required=remedial_hours
        )

    @classmethod
    def generate_semester_shortage_roster(
        cls,
        student_records: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Aggregate department-wide semester shortage statistics."""
        audits = []
        eligible_count = 0
        condonation_count = 0
        detained_count = 0
        total_condonation_revenue = 0.0

        for s in student_records:
            audit = cls.audit_student_attendance(
                student_id=s.get("id", 0),
                roll_number=s.get("roll_number", ""),
                name=s.get("name", ""),
                department=s.get("department", ""),
                classes_held=s.get("classes_held", 100),
                classes_attended=s.get("classes_attended", 80),
                medical_exemption_verified=s.get("medical_exemption", False)
            )
            audits.append(audit)
            if audit.eligibility_status == "ELIGIBLE":
                eligible_count += 1
            elif audit.eligibility_status == "CONDONATION_REQUIRED":
                condonation_count += 1
                total_condonation_revenue += audit.condonation_fee
            else:
                detained_count += 1

        total = len(audits)
        return {
            "total_students_audited": total,
            "eligible_percentage": round((eligible_count / total * 100.0), 2) if total > 0 else 0.0,
            "condonation_students_count": condonation_count,
            "detained_students_count": detained_count,
            "forecasted_condonation_fee_collection": round(total_condonation_revenue, 2),
            "shortage_roster": [
                {
                    "roll_number": a.roll_number,
                    "name": a.student_name,
                    "department": a.department,
                    "percentage": a.attendance_percentage,
                    "status": a.eligibility_status,
                    "condonation_fee": a.condonation_fee
                }
                for a in audits if a.eligibility_status != "ELIGIBLE"
            ]
        }
