"""
EduCore Enterprise Framework - Statutory Attendance Shortage Condonation & Detention Auditor

Audits student attendance against university standards:
- Regular Clearance: Attendance >= 75.0% (No fine, allowed for exams)
- Condonation Slabs: 65.0% <= Attendance < 75.0%
  - Genuine Medical Ground Required with Certificate
  - Condonation Fee Slabs (e.g., 65-70%: Rs. 1500, 70-75%: Rs. 1000)
- Detention Slabs: Attendance < 65.0%
  - Detained from examinations; must repeat course in subsequent academic year
"""

from typing import Dict, List, Any, Tuple
import datetime


class StatutoryAttendanceAuditor:
    """
    Evaluates attendance clearance status for hall ticket issuance.
    """

    CONDONATION_MIN_PCT = 65.0
    REGULAR_MIN_PCT = 75.0

    @classmethod
    def audit_student_clearance(
        cls,
        student_roll: str,
        student_name: str,
        course_code: str,
        classes_conducted: int,
        classes_attended: int,
        has_medical_certificate: bool = False
    ) -> Dict[str, Any]:
        """
        Evaluate statutory clearance, calculate condonation fines, or flag for detention.
        """
        if classes_conducted <= 0:
            return {
                "attendance_percentage": 0.0,
                "clearance_status": "DATA_ERROR",
                "condonation_fee_inr": 0.0,
                "is_permitted_for_exam": False
            }

        att_pct = round((classes_attended / classes_conducted) * 100.0, 2)

        if att_pct >= cls.REGULAR_MIN_PCT:
            status = "CLEARED_REGULAR"
            fee = 0.0
            permitted = True
            remark = "Cleared for examinations under regular attendance quota."
        elif cls.CONDONATION_MIN_PCT <= att_pct < cls.REGULAR_MIN_PCT:
            if has_medical_certificate:
                status = "CONDONATION_ELIGIBLE"
                # Slabs calculation
                if att_pct < 70.0:
                    fee = 1500.0
                else:
                    fee = 1000.0
                permitted = True
                remark = f"Condonation approved on medical grounds. Fee of Rs. {fee} applicable."
            else:
                status = "CONDONATION_PENDING_DOCUMENTS"
                fee = 2000.0  # Penalty fee without documentation
                permitted = False
                remark = "Attendance falls in condonation band, but medical documents are missing."
        else:
            status = "DETAINED_SHORTAGE"
            fee = 0.0
            permitted = False
            remark = "Detained due to critical attendance shortage. Must re-register for the course."

        return {
            "student_roll": student_roll,
            "student_name": student_name,
            "course_code": course_code,
            "classes_conducted": classes_conducted,
            "classes_attended": classes_attended,
            "attendance_percentage": att_pct,
            "clearance_status": status,
            "condonation_fee_inr": fee,
            "is_permitted_for_exam": permitted,
            "remarks": remark
        }
