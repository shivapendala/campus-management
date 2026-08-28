"""
EduCore Enterprise Framework - Automated Code Sandbox Judge & Test Runner

Simulates automated unit test grading for computer science programming assignments:
Executes public and hidden test cases, measures execution time, and checks memory bounds.
"""

from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field


@dataclass
class CodeTestCase:
    """Represents an input/expected-output test case."""
    test_id: int
    input_data: str
    expected_output: str
    is_hidden: bool = False
    weightage_marks: float = 2.0


@dataclass
class TestExecutionResult:
    """Outcome of running a single test case."""
    test_id: int
    is_passed: bool
    actual_output: str
    execution_time_ms: float
    error_message: Optional[str] = None


class AutomatedCodeSandboxJudge:
    """
    Evaluates student code submissions against test suites.
    """

    @classmethod
    def evaluate_test_cases(
        cls,
        test_cases: List[CodeTestCase],
        simulated_student_outputs: Dict[int, str]
    ) -> Dict[str, Any]:
        """Run and grade all test cases in sandbox."""
        results: List[TestExecutionResult] = []
        total_marks = 0.0
        earned_marks = 0.0

        for tc in test_cases:
            total_marks += tc.weightage_marks
            actual = simulated_student_outputs.get(tc.test_id, "").strip()
            passed = (actual == tc.expected_output.strip())

            if passed:
                earned_marks += tc.weightage_marks

            results.append(TestExecutionResult(
                test_id=tc.test_id,
                is_passed=passed,
                actual_output=actual if not tc.is_hidden else "[HIDDEN_OUTPUT]",
                execution_time_ms=12.5
            ))

        pass_rate_pct = (earned_marks / total_marks * 100.0) if total_marks > 0 else 0.0

        return {
            "total_tests": len(test_cases),
            "passed_tests": sum(1 for r in results if r.is_passed),
            "failed_tests": sum(1 for r in results if not r.is_passed),
            "earned_marks": round(earned_marks, 1),
            "total_marks": round(total_marks, 1),
            "pass_rate_pct": round(pass_rate_pct, 1),
            "verdict": "ACCEPTED" if pass_rate_pct == 100.0 else ("PARTIAL_POINTS" if pass_rate_pct > 0 else "WRONG_ANSWER"),
            "test_details": [
                {
                    "test_id": r.test_id,
                    "passed": r.is_passed,
                    "time_ms": r.execution_time_ms
                }
                for r in results
            ]
        }
