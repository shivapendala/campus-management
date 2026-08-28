"""
EduCore Enterprise Framework - Isolated Assignment Code Sandbox Simulator

Simulates automated code submission execution in a containerized sandbox:
- Safety validation (detects system calls like 'subprocess', 'fork', 'exec', '__import__')
- Execution time limits (CPU Timeout: 2.0s) and memory constraints
- Output diffing assertions against standard inputs and expected outputs
"""

import sys
import time
import traceback
from typing import Dict, List, Any, Tuple


class AssignmentCodeSandboxRunner:
    """
    Simulates sandboxed compiler and interpreter executions.
    """

    FORBIDDEN_KEYWORDS = [
        "os.system",
        "subprocess",
        "shutil",
        "ctypes",
        "builtins.open",
        "open(",
        "socket",
        "sys.exit",
        "eval(",
        "exec(",
        "__import__",
        "globals("
    ]

    @classmethod
    def validate_code_safety(cls, code_string: str) -> Tuple[bool, str]:
        """Perform static validation against safety policies."""
        for kw in cls.FORBIDDEN_KEYWORDS:
            if kw in code_string:
                return False, f"Security Violation: Use of forbidden system command or namespace '{kw}' is prohibited."
        return True, "Code passed security containment pre-filters."

    @classmethod
    def execute_python_test(
        cls,
        code_string: str,
        test_inputs: List[str],
        expected_outputs: List[str],
        timeout_seconds: float = 2.0
    ) -> Dict[str, Any]:
        """
        Simulate standard input execution and output verification.
        """
        safety_ok, safety_msg = cls.validate_code_safety(code_string)
        if not safety_ok:
            return {
                "compiled": False,
                "passed": False,
                "verdict": "SECURITY_EXCLUDED",
                "details": safety_msg
            }

        # Create virtual execution environment
        exec_globals: Dict[str, Any] = {}
        exec_locals: Dict[str, Any] = {}

        # Compile string
        try:
            compiled_code = compile(code_string, "<sandbox_exec>", "exec")
        except Exception as e:
            return {
                "compiled": False,
                "passed": False,
                "verdict": "COMPILE_TIME_ERROR",
                "details": f"Compilation Error: {str(e)}"
            }

        passed_tests = 0
        total_tests = len(test_inputs)
        test_details = []

        # Run test cases
        for idx, (inp, exp) in enumerate(zip(test_inputs, expected_outputs)):
            # Capture stdio mocks
            start_time = time.perf_counter()

            # Mock input() function
            input_feed = inp.splitlines()
            input_idx = 0

            def mock_input():
                nonlocal input_idx
                if input_idx < len(input_feed):
                    val = input_feed[input_idx]
                    input_idx += 1
                    return val
                raise EOFError("No further inputs provided by test harness.")

            # Mock print() function
            captured_stdout: List[str] = []

            def mock_print(*args, **kwargs):
                sep = kwargs.get("sep", " ")
                end = kwargs.get("end", "\n")
                msg = sep.join(map(str, args)) + end
                captured_stdout.append(msg.rstrip())

            exec_globals["input"] = mock_input
            exec_globals["print"] = mock_print

            try:
                # Execution with pseudo-timeout check
                # In real env, this is run in a separate subprocess/Docker container
                exec(compiled_code, exec_globals, exec_locals)
                duration = time.perf_counter() - start_time

                if duration > timeout_seconds:
                    test_details.append({
                        "case": idx + 1,
                        "status": "TIME_LIMIT_EXCEEDED",
                        "duration": round(duration, 3)
                    })
                    continue

                actual_output = "\n".join(captured_stdout).strip()
                expected_clean = exp.strip()

                if actual_output == expected_clean:
                    passed_tests += 1
                    test_details.append({
                        "case": idx + 1,
                        "status": "PASS",
                        "duration": round(duration, 3)
                    })
                else:
                    test_details.append({
                        "case": idx + 1,
                        "status": "OUTPUT_MISMATCH",
                        "actual": actual_output,
                        "expected": expected_clean,
                        "duration": round(duration, 3)
                    })

            except Exception as e:
                test_details.append({
                    "case": idx + 1,
                    "status": "RUNTIME_ERROR",
                    "details": traceback.format_exc().splitlines()[-1]
                })

        return {
            "compiled": True,
            "passed": passed_tests == total_tests,
            "verdict": "ALL_TESTS_PASSED" if passed_tests == total_tests else "TESTS_FAILED",
            "passed_count": passed_tests,
            "total_count": total_tests,
            "cases_report": test_details
        }
