"""
EduCore Framework - National Education Policy (NEP) Program Outcome Engine

Performs structural calculations for program outcomes (PO), credit matrices,
and multi-disciplinary courses mappings.
"""

from typing import Dict, List, Any

class NEPProgramOutcomeEngine:
    def __init__(self, department: str, regulation_code: str):
        self.department = department
        self.regulation_code = regulation_code
        self.registered_pos: Dict[str, str] = {}
        self.registered_psos: Dict[str, str] = {}
        self.course_mappings: Dict[str, Dict[str, Any]] = {}
        self.load_default_pos()

    def load_default_pos(self) -> None:
        """
        Initializes the standard 12 NBA Graduate Attributes / Program Outcomes.
        """
        self.registered_pos = {
            "PO1": "Engineering Knowledge: Apply knowledge of mathematics, science, engineering fundamentals.",
            "PO2": "Problem Analysis: Identify, formulate, research literature, and analyze complex engineering problems.",
            "PO3": "Design/Development of Solutions: Design solutions for complex engineering problems.",
            "PO4": "Conduct Investigations of Complex Problems: Use research-based knowledge and research methods.",
            "PO5": "Modern Tool Usage: Create, select, and apply appropriate techniques, resources, and modern engineering tools.",
            "PO6": "The Engineer and Society: Apply reasoning informed by contextual knowledge to assess societal issues.",
            "PO7": "Environment and Sustainability: Understand the impact of professional engineering solutions.",
            "PO8": "Ethics: Apply ethical principles and commit to professional ethics and responsibilities.",
            "PO9": "Individual and Team Work: Function effectively as an individual, and as a member or leader in diverse teams.",
            "PO10": "Communication: Communicate effectively on complex engineering activities.",
            "PO11": "Project Management and Finance: Demonstrate knowledge and understanding of engineering management principles.",
            "PO12": "Life-long Learning: Recognize the need for, and have the preparation and ability to engage in independent learning."
        }

    def register_pso(self, pso_code: str, description: str) -> None:
        self.registered_psos[pso_code] = description

    def map_course_to_outcomes(self, course_code: str, mappings: Dict[str, float]) -> None:
        """
        Maps a course to POs/PSOs with a weight level between 0.0 and 3.0:
        1: Low correlation
        2: Medium correlation
        3: High correlation
        """
        validated_mappings = {}
        for key, val in mappings.items():
            if key not in self.registered_pos and key not in self.registered_psos:
                raise ValueError(f"Invalid outcome code: '{key}'. Must be in POs or PSOs.")
            if not (0.0 <= val <= 3.0):
                raise ValueError(f"Mapping weight for '{key}' must be between 0.0 and 3.0.")
            validated_mappings[key] = val
            
        self.course_mappings[course_code] = {
            "mappings": validated_mappings,
            "audit_status": "PENDING_VERIFICATION",
            "last_updated_by": "SYSTEM_OBE_ENGINE"
        }

    def calculate_curriculum_po_density(self) -> Dict[str, Dict[str, Any]]:
        """
        Calculates the average mapping weight and coverage percentage of each PO across the curriculum.
        """
        total_courses = len(self.course_mappings)
        density_report: Dict[str, Dict[str, Any]] = {}
        
        for po in list(self.registered_pos.keys()) + list(self.registered_psos.keys()):
            mapped_courses_count = 0
            total_weight = 0.0
            
            for course_code, data in self.course_mappings.items():
                w = data["mappings"].get(po, 0.0)
                if w > 0:
                    mapped_courses_count += 1
                    total_weight += w
                    
            avg_weight = (total_weight / mapped_courses_count) if mapped_courses_count > 0 else 0.0
            coverage_pct = (mapped_courses_count / total_courses * 100.0) if total_courses > 0 else 0.0
            
            density_report[po] = {
                "total_weight": round(total_weight, 2),
                "mapped_courses": mapped_courses_count,
                "average_weight": round(avg_weight, 2),
                "coverage_percentage": round(coverage_pct, 2)
            }
            
        return density_report

    def verify_curriculum_compliance(self) -> Dict[str, Any]:
        """
        Verifies if the mapped curriculum satisfies NBA guidelines:
        - At least 80% coverage on core POs (PO1 - PO5)
        - Average mapping weight of core POs >= 1.5
        """
        report = self.calculate_curriculum_po_density()
        core_pos = ["PO1", "PO2", "PO3", "PO4", "PO5"]
        
        passed_coverage = True
        passed_weight = True
        failed_reasons = []
        
        for po in core_pos:
            metrics = report.get(po, {"coverage_percentage": 0.0, "average_weight": 0.0})
            if metrics["coverage_percentage"] < 80.0:
                passed_coverage = False
                failed_reasons.append(f"{po} coverage is below 80% (Current: {metrics['coverage_percentage']}%).")
            if metrics["average_weight"] < 1.5:
                passed_weight = False
                failed_reasons.append(f"{po} average mapping weight is below 1.5 (Current: {metrics['average_weight']}).")
                
        return {
            "compliant": passed_coverage and passed_weight,
            "reasons": failed_reasons,
            "density_report": report
        }
