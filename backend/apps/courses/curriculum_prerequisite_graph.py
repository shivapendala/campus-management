"""
EduCore Enterprise Framework - Canonical Curriculum Prerequisite Graph & PO-PSO Mapping Matrix

Defines structural Directed Acyclic Graphs (DAGs) and NBA (National Board of Accreditation)
mapping tables for all departments:
- Course prerequisite maps
- Credit weighting allocations
- Mapping matrices for 12 Program Outcomes (PO1 to PO12) and 3 PSOs (PSO1 to PSO3)
  with attainment levels: 0 (No Mapping), 1 (Low), 2 (Medium), 3 (High).
"""

from typing import Dict, List, Any, Set, Tuple

# Mapping values: 0 = No correlation, 1 = Low, 2 = Medium, 3 = High
NBA_PO_PSO_MAPS: Dict[str, Dict[str, List[int]]] = {
    "CS301": {
        "title": "Database Management Systems",
        # Maps to PO1-PO12
        "po": [3, 3, 2, 2, 2, 1, 0, 1, 1, 2, 1, 3],
        # Maps to PSO1-PSO3
        "pso": [3, 2, 1]
    },
    "CS302": {
        "title": "Design & Analysis of Algorithms",
        "po": [3, 3, 3, 3, 2, 0, 0, 1, 1, 1, 1, 3],
        "pso": [3, 2, 2]
    },
    "CS401": {
        "title": "Operating Systems & Kernel Architecture",
        "po": [3, 3, 2, 2, 1, 0, 0, 0, 1, 1, 0, 2],
        "pso": [3, 1, 1]
    },
    "EC501": {
        "title": "Digital Signal Processing",
        "po": [3, 3, 2, 3, 3, 1, 0, 0, 1, 2, 1, 3],
        "pso": [3, 2, 1]
    },
    "ME301": {
        "title": "Engineering Thermodynamics",
        "po": [3, 3, 2, 2, 1, 1, 2, 0, 0, 1, 0, 2],
        "pso": [2, 1, 1]
    },
    "CE301": {
        "title": "Strength of Materials",
        "po": [3, 3, 3, 2, 1, 1, 0, 0, 0, 1, 0, 2],
        "pso": [2, 2, 1]
    },
    "EE301": {
        "title": "Electric Circuit Analysis",
        "po": [3, 3, 2, 2, 2, 0, 0, 0, 0, 1, 0, 2],
        "pso": [3, 1, 1]
    },
    "AI301": {
        "title": "Mathematical Foundations of ML",
        "po": [3, 3, 3, 3, 3, 1, 0, 1, 1, 2, 1, 3],
        "pso": [3, 3, 2]
    }
}

CURRICULUM_PREREQUISITE_DEPENDENCIES: Dict[str, List[str]] = {
    # CSE Stream
    "CS101": [],
    "CS201": ["CS101"],
    "CS301": ["CS201"],
    "CS302": ["CS201"],
    "CS401": ["CS201"],
    "CS501": ["CS201"],
    "CS502": ["CS302", "CS403"],
    "CS503": ["CS302"],
    "CS601": ["CS503", "MA401"],
    "CS701": ["CS501", "CS401"],
    # ECE Stream
    "EC301": [],
    "EC401": [],
    "EC501": ["EC401"],
    "EC601": ["EC301"],
    "EC602": ["CS101"],
    # EEE Stream
    "EE301": [],
    "EE302": ["EE301"],
    "EE401": ["EE302"],
    "EE402": ["EE301"],
    "EE501": ["EE401"],
    "EE502": ["EE301"],
    # MECH Stream
    "ME301": [],
    "ME302": [],
    "ME401": [],
    "ME501": ["ME401"],
    "ME502": ["ME301", "ME302"],
    "ME601": ["ME501"],
    "ME701": ["ME601"],
    # CIVIL Stream
    "CE301": [],
    "CE302": [],
    "CE401": ["CE301"],
    "CE501": ["CE401"],
    "CE502": ["CE301", "CE302"],
    "CE601": ["CE401"],
    "CE701": ["CE302"]
}
