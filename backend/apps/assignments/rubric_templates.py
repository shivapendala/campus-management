"""
EduCore Enterprise Framework - Standardized Assignment Rubric Templates

Maintains pre-configured assessment rubrics for:
- Programming Project Rubric
- Research Term Paper Rubric
- Engineering Laboratory Experiment Rubric
- Capstone Senior Design Rubric
"""

from typing import Dict, List, Any, Optional
from apps.assignments.rubrics import RubricCriterion, RubricCriterionLevel


class StandardRubricLibrary:
    """
    Standard institutional assessment rubric definitions.
    """

    @classmethod
    def get_programming_project_rubric(cls) -> List[RubricCriterion]:
        """Fetch standardized programming evaluation rubric."""
        return [
            RubricCriterion(
                criterion_code="CORRECTNESS",
                criterion_title="Functional Correctness & Test Case Pass Rate",
                weightage_percentage=40.0,
                max_marks=40.0,
                levels=[
                    RubricCriterionLevel("EXEMPLARY", 1.0, "Passes 100% of all public and hidden test suites"),
                    RubricCriterionLevel("PROFICIENT", 0.75, "Passes all public tests and majority of edge cases"),
                    RubricCriterionLevel("DEVELOPING", 0.50, "Passes basic cases but fails edge boundaries"),
                    RubricCriterionLevel("BEGINNER", 0.25, "Fails basic logic or compilation errors"),
                ]
            ),
            RubricCriterion(
                criterion_code="CODE_QUALITY",
                criterion_title="Modularity, Clean Code & Style Compliance",
                weightage_percentage=30.0,
                max_marks=30.0,
                levels=[
                    RubricCriterionLevel("EXEMPLARY", 1.0, "Clean architecture, PEP-8/ESLint compliant, clear docstrings"),
                    RubricCriterionLevel("PROFICIENT", 0.75, "Good modularity with minor stylistic issues"),
                    RubricCriterionLevel("DEVELOPING", 0.50, "Monolithic functions with poor variable naming"),
                    RubricCriterionLevel("BEGINNER", 0.25, "Spaghetti code without comments or documentation"),
                ]
            ),
            RubricCriterion(
                criterion_code="EFFICIENCY",
                criterion_title="Time & Space Complexity Optimization",
                weightage_percentage=30.0,
                max_marks=30.0,
                levels=[
                    RubricCriterionLevel("EXEMPLARY", 1.0, "Optimal asymptotic complexity O(N) or O(N log N)"),
                    RubricCriterionLevel("PROFICIENT", 0.75, "Acceptable complexity with small optimization opportunities"),
                    RubricCriterionLevel("DEVELOPING", 0.50, "Suboptimal quadratic O(N^2) approach"),
                    RubricCriterionLevel("BEGINNER", 0.25, "Exponential time complexity causing timeout"),
                ]
            ),
        ]
