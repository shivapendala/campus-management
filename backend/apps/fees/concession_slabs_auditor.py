"""
EduCore Framework - Fee Concession Slabs Auditor

Audits scholarship roster allocations to identify conflicting or duplicate waivers.
"""

from typing import Dict, List, Any

class ConcessionSlabsAuditor:
    def __init__(self, academic_year: str):
        self.academic_year = academic_year
        self.audit_conflicts: List[Dict[str, Any]] = []

    def verify_no_duplicate_concessions(self, allocated_concessions: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Ensures a student has not been allocated multiple non-cumulative concessions.
        """
        student_mappings: Dict[str, List[str]] = {}
        for record in allocated_concessions:
            s_id = record["student_id"]
            slab = record["slab_key"]
            if s_id not in student_mappings:
                student_mappings[s_id] = []
            student_mappings[s_id].append(slab)
            
        for s_id, slabs in student_mappings.items():
            if len(slabs) > 1:
                self.audit_conflicts.append({
                    "student_id": s_id,
                    "type": "DUPLICATE_CONCESSION_ALLOCATION",
                    "description": f"Student allocated multiple conflicting slabs: {', '.join(slabs)}."
                })
                
        return self.audit_conflicts
