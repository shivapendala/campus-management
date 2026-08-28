"""
EduCore Framework - AICTE Infrastructure Auditor

Audits carpet area allocations and computer ratio guidelines.
"""

from typing import Dict, List, Any

class AICTEInfrastructureAuditor:
    def __init__(self):
        self.compliance_discrepancies: List[str] = []

    def audit_campus_facilities(self, laboratory_carpet_areas: Dict[str, float], total_computers: int, student_capacity: int) -> Dict[str, Any]:
        """
        AICTE specifies:
        - At least 66 square meters carpet area per structural engineering laboratory.
        """
        for lab, area in laboratory_carpet_areas.items():
            if area < 66.0:
                self.compliance_discrepancies.append(
                    f"Carpet area deficit: Laboratory '{lab}' has {area} sqm (minimum standard is 66.0 sqm)."
                )
                
        computer_student_ratio = total_computers / student_capacity if student_capacity > 0 else 0.0
        ratio_ok = computer_student_ratio >= 0.25
        
        if not ratio_ok:
            self.compliance_discrepancies.append(
                f"Computer deficit: Student-to-computer ratio is {computer_student_ratio:.2f} (minimum standard is 0.25)."
            )
            
        return {
            "compliant": len(self.compliance_discrepancies) == 0,
            "computer_to_student_ratio": round(computer_student_ratio, 2),
            "discrepancies": self.compliance_discrepancies
        }
