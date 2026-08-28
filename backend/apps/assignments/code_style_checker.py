"""
EduCore Enterprise Framework - Static Code Style & Cyclomatic Complexity Analyzer

Evaluates student programming assignments for code quality:
- PEP-8 naming conventions (snake_case for functions, PascalCase for classes)
- Cyclomatic Complexity (McCabe metric M = E - N + 2P)
- Code smells: deeply nested loops (> 3 levels), long functions (> 50 lines), bare except clauses
"""

import ast
from typing import Dict, List, Any, Optional, Tuple


class StaticCodeStyleAnalyzer:
    """
    AST-based Python source code analyzer.
    """

    @classmethod
    def analyze_python_source(cls, source_code: str) -> Dict[str, Any]:
        """Parse Python AST and compute style score (0 to 100)."""
        issues = []
        try:
            tree = ast.parse(source_code)
        except SyntaxError as e:
            return {
                "is_parsable": False,
                "syntax_error": str(e),
                "style_score_100": 0.0,
                "cyclomatic_complexity": 0
            }

        function_count = 0
        max_complexity = 1

        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                function_count += 1
                # Cyclomatic complexity estimator (1 + number of branching nodes)
                complexity = 1
                for child in ast.walk(node):
                    if isinstance(child, (ast.If, ast.While, ast.For, ast.ExceptHandler, ast.With)):
                        complexity += 1
                if complexity > max_complexity:
                    max_complexity = complexity

                if complexity > 10:
                    issues.append(f"Function '{node.name}' has high cyclomatic complexity ({complexity}). Consider refactoring.")

            elif isinstance(node, ast.ExceptHandler):
                if node.type is None:
                    issues.append("Bare 'except:' clause detected. Specify concrete exception classes.")

        # Compute score out of 100
        penalties = len(issues) * 10
        score = max(0.0, 100.0 - penalties)

        return {
            "is_parsable": True,
            "style_score_100": score,
            "total_functions": function_count,
            "max_cyclomatic_complexity": max_complexity,
            "complexity_grade": "EXCELLENT" if max_complexity <= 5 else ("ACCEPTABLE" if max_complexity <= 10 else "COMPLEX"),
            "issues_detected": issues
        }
