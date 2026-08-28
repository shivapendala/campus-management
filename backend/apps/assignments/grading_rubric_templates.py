"""
EduCore Framework - Grading Rubric Templates Catalog

Defines standard templates for grading criteria across different assignment categories:
- PROGRAMMING_LAB: Code correctness, efficiency, style, documentation.
- RESEARCH_PAPER: Literature review, methodology, citation style, clarity.
- CAPSTONE_PROJECT: System architecture, testing, presentation, user manual.
"""

from typing import Dict, List, Any

RUBRIC_TEMPLATES_CATALOG: Dict[str, Dict[str, Any]] = {
    "PROGRAMMING_LAB": {
        "title": "Standard Programming Lab Rubric",
        "description": "Evaluation framework for programming lab sheets and code submissions.",
        "criteria": [
            {
                "name": "Code Correctness",
                "weight": 0.40,
                "max_points": 10.0,
                "description": "Passes all static and dynamic test cases successfully."
            },
            {
                "name": "Algorithm Efficiency",
                "weight": 0.20,
                "max_points": 10.0,
                "description": "Meets computational complexity bounds (Time and Space complexity)."
            },
            {
                "name": "Code Formatting & Style",
                "weight": 0.20,
                "max_points": 10.0,
                "description": "Adheres to standard PEP8 style guides and readability metrics."
            },
            {
                "name": "Inline Documentation",
                "weight": 0.20,
                "max_points": 10.0,
                "description": "Docstrings and comments describe execution flows and preconditions."
            }
        ]
    },
    "RESEARCH_PAPER": {
        "title": "Academic Research Paper Rubric",
        "description": "Evaluation framework for literature survey drafts and term papers.",
        "criteria": [
            {
                "name": "Literature Review Depth",
                "weight": 0.30,
                "max_points": 100.0,
                "description": "Synthesizes relevant state-of-the-art publications from index journals."
            },
            {
                "name": "Methodology Rigor",
                "weight": 0.30,
                "max_points": 100.0,
                "description": "Explicitly details mathematical frameworks, experiments, and validations."
            },
            {
                "name": "Citation Standard Alignment",
                "weight": 0.20,
                "max_points": 100.0,
                "description": "Formats bibliography matches IEEE/APA standard schemas correctly."
            },
            {
                "name": "Writing Cohesion",
                "weight": 0.20,
                "max_points": 100.0,
                "description": "Ensures logical transitions between sections and vocabulary clarity."
            }
        ]
    },
    "CAPSTONE_PROJECT": {
        "title": "Engineering Capstone Project Rubric",
        "description": "Rubric for final year capstone thesis, code, and viva-voce.",
        "criteria": [
            {
                "name": "Architecture Design",
                "weight": 0.30,
                "max_points": 50.0,
                "description": "Decoupled structures, database normalizations, scalability margins."
            },
            {
                "name": "Validation & Testing",
                "weight": 0.30,
                "max_points": 50.0,
                "description": "Unit test coverage, integration tests, dynamic regression verification."
            },
            {
                "name": "Thesis & Presentation",
                "weight": 0.20,
                "max_points": 50.0,
                "description": "Clarity of delivery, slide outlines, and response during question hour."
            },
            {
                "name": "Deployment Quality",
                "weight": 0.20,
                "max_points": 50.0,
                "description": "Containerized setups, orchestration pipelines, and operational health checks."
            }
        ]
    }
}
