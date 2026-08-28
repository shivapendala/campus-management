"""
EduCore Enterprise Framework - Curriculum Directed Acyclic Graph (DAG) Prerequisite Analyzer

Applies graph algorithms to validate academic curriculum prerequisites:
- Kahn's Topological Sort Algorithm
- Tarjan's Strongly Connected Components (SCC) Cycle Detector
- Critical Path Method (CPM) for prerequisite graduation blockers
"""

from typing import Dict, List, Set, Optional, Tuple
from collections import deque, defaultdict


class CurriculumDAGAnalyzer:
    """
    Analyzes course prerequisite networks to detect cycles and calculate depth chains.
    """

    def __init__(self):
        self.adj_list: Dict[str, List[str]] = defaultdict(list)
        self.in_degree: Dict[str, int] = defaultdict(int)
        self.all_nodes: Set[str] = set()

    def add_course(self, course_code: str):
        """Register course node in curriculum graph."""
        self.all_nodes.add(course_code)
        if course_code not in self.adj_list:
            self.adj_list[course_code] = []
        if course_code not in self.in_degree:
            self.in_degree[course_code] = 0

    def add_prerequisite(self, prereq_course: str, target_course: str):
        """Add directed edge from prereq to target."""
        self.add_course(prereq_course)
        self.add_course(target_course)
        self.adj_list[prereq_course].append(target_course)
        self.in_degree[target_course] += 1

    def detect_cycles_kahn(self) -> Tuple[bool, List[str]]:
        """
        Detect whether circular dependencies exist using Kahn's algorithm.
        Returns: (has_cycle, topological_order_if_acyclic)
        """
        in_deg = dict(self.in_degree)
        queue = deque([node for node in self.all_nodes if in_deg[node] == 0])
        topo_order = []

        while queue:
            curr = queue.popleft()
            topo_order.append(curr)

            for neighbor in self.adj_list[curr]:
                in_deg[neighbor] -= 1
                if in_deg[neighbor] == 0:
                    queue.append(neighbor)

        has_cycle = len(topo_order) != len(self.all_nodes)
        return has_cycle, topo_order

    def find_longest_prerequisite_chain(self, start_course: str) -> List[str]:
        """Find critical prerequisite path using Dynamic Programming on DAG."""
        memo: Dict[str, List[str]] = {}

        def dfs(node: str) -> List[str]:
            if node in memo:
                return memo[node]

            longest = [node]
            for nxt in self.adj_list[node]:
                sub_path = dfs(nxt)
                if len(sub_path) + 1 > len(longest):
                    longest = [node] + sub_path

            memo[node] = longest
            return longest

        return dfs(start_course)
