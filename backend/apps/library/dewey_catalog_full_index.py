"""
EduCore Enterprise Framework - Dewey Decimal Classification (DDC) Library Shelf Indexer

Comprehensive indexing table mapping standard Dewey Decimal subdivisions to physical shelf coordinates:
- 000 Computer Science, Knowledge & Systems
- 300 Social Sciences, Economics, Law & Education
- 500 Mathematics, Physics & Chemistry
- 600 Technology, Applied Science & Engineering Slabs
- 621 Applied Physics, Mechanical, Electrical & Electronic Engineering subdivisions
- 624 Structural Civil Engineering subdivisions
"""

from typing import Dict, List, Any, Optional


class LibraryShelfIndexer:
    """
    Computes shelf placement coordinates for library physical inventory.
    """

    DDC_DETAILED_SPECIALTIES: Dict[str, Dict[str, Any]] = {
        "004": {
            "name": "Data Processing & Computer Science",
            "aisle": "Aisle CSE-1",
            "racks": ["Rack A", "Rack B", "Rack C"]
        },
        "005.1": {
            "name": "Programming & Algorithm Design",
            "aisle": "Aisle CSE-2",
            "racks": ["Rack A", "Rack B"]
        },
        "005.133": {
            "name": "Programming Languages (C, C++, Java, Python)",
            "aisle": "Aisle CSE-2",
            "racks": ["Rack C", "Rack D"]
        },
        "005.43": {
            "name": "Systems Software & Operating Systems",
            "aisle": "Aisle CSE-3",
            "racks": ["Rack A", "Rack B"]
        },
        "005.74": {
            "name": "Data Files & Databases",
            "aisle": "Aisle CSE-3",
            "racks": ["Rack C", "Rack D"]
        },
        "006.3": {
            "name": "Artificial Intelligence & Computational Intelligence",
            "aisle": "Aisle CSE-4",
            "racks": ["Rack A", "Rack B", "Rack C"]
        },
        "340": {
            "name": "Law (Statutes, Constitution, POSH & RTI)",
            "aisle": "Aisle LAW-1",
            "racks": ["Rack A", "Rack B"]
        },
        "510": {
            "name": "Mathematics & Linear Algebra",
            "aisle": "Aisle SCI-1",
            "racks": ["Rack A", "Rack B", "Rack C", "Rack D"]
        },
        "530": {
            "name": "Physics & Quantum Engineering",
            "aisle": "Aisle SCI-2",
            "racks": ["Rack A", "Rack B"]
        },
        "621.3815": {
            "name": "Electronic Circuit Design",
            "aisle": "Aisle ECE-1",
            "racks": ["Rack A", "Rack B", "Rack C"]
        },
        "621.395": {
            "name": "VLSI Circuit Design",
            "aisle": "Aisle ECE-2",
            "racks": ["Rack A", "Rack B"]
        },
        "621.4021": {
            "name": "Thermodynamics & Heat Transfer",
            "aisle": "Aisle MECH-1",
            "racks": ["Rack A", "Rack B"]
        },
        "624.17": {
            "name": "Structural Analysis & Mechanics",
            "aisle": "Aisle CIVIL-1",
            "racks": ["Rack A", "Rack B"]
        }
    }

    @classmethod
    def get_shelf_coordinates(cls, ddc_code: str) -> Dict[str, Any]:
        """Resolve physical location coordinates for a book based on DDC code."""
        # Find exact or prefix match
        matched_spec = cls.DDC_DETAILED_SPECIALTIES.get(ddc_code)
        if not matched_spec:
            # Check prefixes (e.g. 005.133 -> 005.1 -> 004 -> 000)
            parts = ddc_code.split(".")
            if len(parts) > 1:
                prefix = parts[0]
                matched_spec = cls.DDC_DETAILED_SPECIALTIES.get(prefix)

        if not matched_spec:
            return {
                "subject_name": "General Technology & Engineering",
                "physical_location": "Main Stacks - Central Engineering Row",
                "aisle": "Aisle GEN-ENG",
                "racks": ["Rack 1", "Rack 2"]
            }

        return {
            "subject_name": matched_spec["name"],
            "physical_location": f"Main Stacks - {matched_spec['aisle']}",
            "aisle": matched_spec["aisle"],
            "racks": matched_spec["racks"]
        }
