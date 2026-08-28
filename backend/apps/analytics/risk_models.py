"""
EduCore Enterprise Framework - Predictive Student Academic Risk Engine

Analyzes academic attendance trends, internal assessment variances, fee arrears,
and behavioral indicators to identify at-risk students for early remedial intervention.
"""

from typing import Dict, List, Any, Tuple
from dataclasses import dataclass


@dataclass
class StudentRiskAssessment:
    """Detailed risk assessment outcome for an individual student."""
    student_id: int
    roll_number: str
    student_name: str
    department: str
    risk_level: str  # LOW, MODERATE, HIGH, CRITICAL
    risk_score: float  # 0.0 to 100.0 (Higher = greater risk of dropout/detention)
    factors: List[Dict[str, Any]]
    recommended_interventions: List[str]


class AcademicRiskPredictionEngine:
    """
    Weighted multi-factor academic risk scoring model:
    - Attendance Shortage Factor (Weight: 35%)
    - CGPA & Internal Assessment Lag (Weight: 35%)
    - Active Backlogs Count (Weight: 20%)
    - Financial Dues Overdue (Weight: 10%)
    """

    ATTENDANCE_WEIGHT = 0.35
    ACADEMIC_WEIGHT = 0.35
    BACKLOG_WEIGHT = 0.20
    FEE_WEIGHT = 0.10

    @classmethod
    def evaluate_student_risk(
        cls,
        student_id: int,
        roll_number: str,
        name: str,
        department: str,
        attendance_pct: float,
        cgpa: float,
        active_backlogs: int,
        fee_balance: float
    ) -> StudentRiskAssessment:
        """Calculate holistic academic risk score and assign risk category."""
        factors = []
        interventions = []

        # 1. Attendance factor (0 to 100 risk score)
        if attendance_pct < 65.0:
            att_risk = 100.0
            factors.append({
                "category": "ATTENDANCE",
                "severity": "CRITICAL",
                "metric": f"{attendance_pct}%",
                "description": "Attendance below statutory 65% condonation limit (Severe detention risk)"
            })
            interventions.append("Issue formal parent attendance shortage notification immediately")
            interventions.append("Schedule mandatory academic counseling session")
        elif attendance_pct < 75.0:
            att_risk = 60.0
            factors.append({
                "category": "ATTENDANCE",
                "severity": "HIGH",
                "metric": f"{attendance_pct}%",
                "description": "Attendance in 65%-75% condonation bracket (Requires medical/official exemption)"
            })
            interventions.append("Send warning SMS/Email alert to student and mentor")
        elif attendance_pct < 80.0:
            att_risk = 25.0
        else:
            att_risk = 0.0

        # 2. Academic / CGPA factor
        if cgpa < 5.0:
            acad_risk = 100.0
            factors.append({
                "category": "ACADEMICS",
                "severity": "CRITICAL",
                "metric": f"CGPA {cgpa}",
                "description": "CGPA in academic probation danger zone (< 5.0)"
            })
            interventions.append("Assign dedicated faculty mentor for peer tutoring")
        elif cgpa < 6.0:
            acad_risk = 60.0
            factors.append({
                "category": "ACADEMICS",
                "severity": "MODERATE",
                "metric": f"CGPA {cgpa}",
                "description": "CGPA below first-division threshold (5.0 - 6.0)"
            })
            interventions.append("Enroll in remedial tutorial batches")
        elif cgpa < 7.0:
            acad_risk = 25.0
        else:
            acad_risk = 0.0

        # 3. Backlog count factor
        if active_backlogs >= 3:
            backlog_risk = 100.0
            factors.append({
                "category": "BACKLOGS",
                "severity": "CRITICAL",
                "metric": f"{active_backlogs} subjects",
                "description": "Multiple active backlogs impeding year progression"
            })
            interventions.append("Mandatory enrollment in remedial crash courses before supplementary exams")
        elif active_backlogs >= 1:
            backlog_risk = 50.0
            factors.append({
                "category": "BACKLOGS",
                "severity": "MODERATE",
                "metric": f"{active_backlogs} subject(s)",
                "description": "Active arrears require supplementary clearing"
            })
        else:
            backlog_risk = 0.0

        # 4. Fee balance factor
        if fee_balance > 50000.0:
            fee_risk = 80.0
            factors.append({
                "category": "FINANCIAL",
                "severity": "HIGH",
                "metric": f"Rs. {fee_balance:,.2f}",
                "description": "Substantial unpaid tuition fees causing exam hall ticket withholding"
            })
            interventions.append("Notify accounts bursar and offer flexible installment plan")
        elif fee_balance > 0.0:
            fee_risk = 30.0
        else:
            fee_risk = 0.0

        # Weighted composite score
        total_risk = (
            (att_risk * cls.ATTENDANCE_WEIGHT) +
            (acad_risk * cls.ACADEMIC_WEIGHT) +
            (backlog_risk * cls.BACKLOG_WEIGHT) +
            (fee_risk * cls.FEE_WEIGHT)
        )
        total_risk = round(min(100.0, max(0.0, total_risk)), 1)

        # Classify level
        if total_risk >= 70.0:
            risk_level = "CRITICAL"
        elif total_risk >= 45.0:
            risk_level = "HIGH"
        elif total_risk >= 20.0:
            risk_level = "MODERATE"
        else:
            risk_level = "LOW"
            if not interventions:
                interventions.append("Maintain good academic standing; eligible for honors track")

        return StudentRiskAssessment(
            student_id=student_id,
            roll_number=roll_number,
            student_name=name,
            department=department,
            risk_level=risk_level,
            risk_score=total_risk,
            factors=factors,
            recommended_interventions=interventions
        )

    @classmethod
    def batch_assess_students(cls, student_records: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Perform batch risk profiling and generate risk tier distribution statistics."""
        assessments = []
        tier_counts = {"LOW": 0, "MODERATE": 0, "HIGH": 0, "CRITICAL": 0}

        for record in student_records:
            assessment = cls.evaluate_student_risk(
                student_id=record.get("id", 0),
                roll_number=record.get("roll_number", ""),
                name=record.get("name", ""),
                department=record.get("department", ""),
                attendance_pct=float(record.get("attendance_pct", 85.0)),
                cgpa=float(record.get("cgpa", 8.0)),
                active_backlogs=int(record.get("active_backlogs", 0)),
                fee_balance=float(record.get("fee_balance", 0.0))
            )
            assessments.append(assessment)
            tier_counts[assessment.risk_level] += 1

        total = len(assessments)
        return {
            "total_assessed": total,
            "distribution": tier_counts,
            "critical_percentage": round((tier_counts["CRITICAL"] / total * 100.0), 2) if total > 0 else 0.0,
            "high_risk_percentage": round((tier_counts["HIGH"] / total * 100.0), 2) if total > 0 else 0.0,
            "at_risk_students": [
                {
                    "student_id": a.student_id,
                    "roll_number": a.roll_number,
                    "name": a.student_name,
                    "department": a.department,
                    "risk_level": a.risk_level,
                    "risk_score": a.risk_score,
                    "factors": a.factors,
                    "interventions": a.recommended_interventions
                }
                for a in assessments if a.risk_level in ("HIGH", "CRITICAL")
            ]
        }
