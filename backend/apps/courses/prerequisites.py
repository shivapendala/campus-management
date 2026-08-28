"""
EduCore Enterprise Framework - Course Prerequisite Directed Acyclic Graph (DAG) Engine

Validates academic course dependencies, prevents circular prerequisite deadlocks,
and audits student eligibility before course registration.
"""

from typing import Dict, List, Set, Optional, Tuple
import collections


class PrerequisiteDAGCycleError(Exception):
    """Raised when a circular dependency is detected in the curriculum."""
    pass


class CoursePrerequisiteEngine:
    """
    DAG validator for course prerequisite chains.
    """

    @classmethod
    def detect_cycles(cls, prerequisite_graph: Dict[str, List[str]]) -> Tuple[bool, List[str]]:
        """
        Detect circular dependencies in prerequisite graph using Tarjan / DFS cycle detection.
        prerequisite_graph: { "CS301": ["CS201", "CS101"], "CS201": ["CS101"] }
        Returns: (has_cycle, cycle_path)
        """
        visited: Dict[str, int] = {}  # 0: unvisited, 1: visiting (in recursion stack), 2: visited
        parent_map: Dict[str, str] = {}
        all_nodes = set(prerequisite_graph.keys())
        for prereqs in prerequisite_graph.values():
            all_nodes.update(prereqs)

        for node in all_nodes:
            visited[node] = 0

        def dfs(node: str, stack: List[str]) -> Optional[List[str]]:
            visited[node] = 1
            stack.append(node)

            for neighbor in prerequisite_graph.get(node, []):
                if visited.get(neighbor, 0) == 1:
                    # Cycle found
                    cycle_start_idx = stack.index(neighbor)
                    return stack[cycle_start_idx:] + [neighbor]
                elif visited.get(neighbor, 0) == 0:
                    result = dfs(neighbor, stack)
                    if result:
                        return result

            visited[node] = 2
            stack.pop()
            return None

        for node in all_nodes:
            if visited[node] == 0:
                cycle = dfs(node, [])
                if cycle:
                    return True, cycle

        return False, []

    @classmethod
    def get_all_transitive_prerequisites(
        cls,
        course_code: str,
        prerequisite_graph: Dict[str, List[str]]
    ) -> Set[str]:
        """Retrieve all direct and indirect prerequisites for a course."""
        all_prereqs: Set[str] = set()
        queue = collections.deque(prerequisite_graph.get(course_code, []))

        while queue:
            curr = queue.popleft()
            if curr not in all_prereqs:
                all_prereqs.add(curr)
                for next_prereq in prerequisite_graph.get(curr, []):
                    if next_prereq not in all_prereqs:
                        queue.append(next_prereq)

        return all_prereqs

    @classmethod
    def verify_student_eligibility(
        cls,
        student_passed_courses: Set[str],
        target_course: str,
        prerequisite_graph: Dict[str, List[str]]
    ) -> Tuple[bool, List[str]]:
        """
        Check if student has successfully completed all direct prerequisites for target course.
        Returns: (is_eligible, missing_prerequisites)
        """
        direct_prereqs = prerequisite_graph.get(target_course, [])
        missing = [c for c in direct_prereqs if c not in student_passed_courses]
        return len(missing) == 0, missing
