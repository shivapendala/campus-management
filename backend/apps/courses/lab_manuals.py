"""
EduCore Enterprise Framework - Practical Laboratory Experiment Catalog & Rubrics

Maintains laboratory syllabus manuals, experiment list (12 experiments),
hardware/software tooling prerequisites, and continuous lab viva rubrics.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class LabExperimentItem:
    """Represents a scheduled laboratory practical experiment."""
    experiment_number: int  # 1 to 12
    title: str
    objective: str
    software_hardware_tools: List[str]
    max_marks: int = 10
    co_mapped: str = "CO1"
    is_completed: bool = False


class LaboratoryManualManager:
    """
    Standard experiment repository for CSE, ECE, MECH, and CIVIL practicals.
    """

    DBMS_LAB_EXPERIMENTS = [
        LabExperimentItem(1, "E-R Modeling for College Management System", "Design Entity-Relationship Diagram using draw.io/ERwin", ["Draw.io", "MySQL Workbench"], co_mapped="CO1"),
        LabExperimentItem(2, "DDL and DML SQL Queries", "Create tables, primary keys, foreign keys, and perform CRUD operations", ["PostgreSQL 16", "pgAdmin"], co_mapped="CO2"),
        LabExperimentItem(3, "Complex Nested Queries & Joins", "Execute Inner, Left, Right, Full Outer Joins, and Correlated Subqueries", ["PostgreSQL 16"], co_mapped="CO2"),
        LabExperimentItem(4, "Database Views and Triggers", "Implement automatic audit triggers and security views", ["PL/pgSQL"], co_mapped="CO3"),
        LabExperimentItem(5, "Stored Procedures & Cursors", "Write parametric stored functions with explicit cursors and error handling", ["PL/pgSQL"], co_mapped="CO3"),
        LabExperimentItem(6, "B+ Tree Indexing Performance Analysis", "Benchmark query execution plan (EXPLAIN ANALYZE) before and after indexing", ["PostgreSQL 16"], co_mapped="CO4"),
    ]

    @classmethod
    def get_lab_experiments(cls, lab_course_code: str) -> List[LabExperimentItem]:
        """Fetch standardized 6-12 experiment schedule."""
        return cls.DBMS_LAB_EXPERIMENTS
