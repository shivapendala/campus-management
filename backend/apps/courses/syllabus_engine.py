"""
EduCore Enterprise Framework - 5-Unit Syllabus Revision & Versioning Engine

Manages curriculum unit structures, Bloom's Revised Taxonomy levels for topics,
prescribed textbooks, reference materials, and syllabus revision tracking (R20, R23 regulations).
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field


@dataclass
class SyllabusUnit:
    """Represents one of the 5 standard institutional syllabus units."""
    unit_number: int  # 1 to 5
    unit_title: str
    lecture_hours_required: int
    topics: List[str]
    blooms_taxonomy_levels: List[str]
    co_mapped: str  # e.g., "CO1", "CO2"


@dataclass
class CourseCurriculumSchema:
    """Complete 5-unit curriculum structure for a subject."""
    course_code: str
    course_title: str
    regulation_code: str  # R20, R22, R24
    credits: int
    lecture_hours: int
    tutorial_hours: int
    practical_hours: int
    total_contact_hours: int
    units: List[SyllabusUnit]
    textbooks: List[str]
    references: List[str]
    prerequisites: List[str] = field(default_factory=list)


class SyllabusVersioningManager:
    """
    Standard curriculum templates and version comparison engine.
    """

    CSE_BENCHMARK_CURRICULUM = {
        "CS201": {
            "title": "Data Structures & Algorithms",
            "credits": 4,
            "units": [
                ("Unit 1: Linear Data Structures", ["Arrays", "Stacks", "Queues", "Linked Lists"], ["L1_REMEMBER", "L2_UNDERSTAND", "L3_APPLY"], "CO1"),
                ("Unit 2: Non-Linear Data Structures - Trees", ["Binary Trees", "AVL Trees", "Red-Black Trees", "B-Trees"], ["L2_UNDERSTAND", "L3_APPLY", "L4_ANALYZE"], "CO2"),
                ("Unit 3: Graphs & Graph Algorithms", ["Graph Traversals BFS/DFS", "Dijkstra", "Prim/Kruskal", "Topological Sort"], ["L3_APPLY", "L4_ANALYZE"], "CO3"),
                ("Unit 4: Sorting and Searching", ["QuickSort", "MergeSort", "HeapSort", "Hash Tables", "Collision Resolution"], ["L2_UNDERSTAND", "L3_APPLY"], "CO4"),
                ("Unit 5: Advanced Algorithm Design", ["Dynamic Programming", "Greedy Method", "Backtracking", "NP-Completeness"], ["L4_ANALYZE", "L5_EVALUATE"], "CO5"),
            ],
            "textbooks": [
                "Mark Allen Weiss, Data Structures and Algorithm Analysis in C++, 4th Edition, Pearson, 2014.",
                "Ellis Horowitz, Sartaj Sahni, Fundamentals of Data Structures, Universities Press, 2008."
            ],
            "references": [
                "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Introduction to Algorithms, MIT Press, 3rd Edition, 2009."
            ]
        },
        "CS301": {
            "title": "Database Management Systems",
            "credits": 4,
            "units": [
                ("Unit 1: Database Architecture & ER Model", ["File Systems vs DBMS", "Three-Schema Architecture", "ER Modeling", "Extended ER"], ["L1_REMEMBER", "L2_UNDERSTAND"], "CO1"),
                ("Unit 2: Relational Model & SQL", ["Relational Algebra", "Tuple Calculus", "Advanced SQL Queries", "Triggers", "Views"], ["L2_UNDERSTAND", "L3_APPLY"], "CO2"),
                ("Unit 3: Normalization & Schema Refinement", ["Functional Dependencies", "1NF", "2NF", "3NF", "BCNF", "Multivalued Dependencies (4NF)"], ["L3_APPLY", "L4_ANALYZE"], "CO3"),
                ("Unit 4: Transaction Processing & Concurrency", ["ACID Properties", "Serializability", "Two-Phase Locking (2PL)", "Deadlock Handling"], ["L3_APPLY", "L4_ANALYZE"], "CO4"),
                ("Unit 5: Indexing & Storage Systems", ["B+ Tree Indexing", "Hashing Techniques", "Query Optimization", "NoSQL Foundations"], ["L4_ANALYZE", "L5_EVALUATE"], "CO5"),
            ],
            "textbooks": [
                "Abraham Silberschatz, Henry F. Korth, S. Sudarshan, Database System Concepts, 7th Edition, McGraw-Hill, 2019."
            ],
            "references": [
                "Raghu Ramakrishnan, Johannes Gehrke, Database Management Systems, 3rd Edition, McGraw-Hill, 2003."
            ]
        }
    }

    @classmethod
    def get_benchmark_syllabus(cls, course_code: str) -> Optional[CourseCurriculumSchema]:
        """Fetch standard 5-unit curriculum structure for benchmark courses."""
        data = cls.CSE_BENCHMARK_CURRICULUM.get(course_code)
        if not data:
            return None

        units = []
        for idx, (title, topics, blooms, co) in enumerate(data["units"], start=1):
            units.append(SyllabusUnit(
                unit_number=idx,
                unit_title=title,
                lecture_hours_required=9,
                topics=topics,
                blooms_taxonomy_levels=blooms,
                co_mapped=co
            ))

        return CourseCurriculumSchema(
            course_code=course_code,
            course_title=data["title"],
            regulation_code="R23",
            credits=data["credits"],
            lecture_hours=3,
            tutorial_hours=1,
            practical_hours=0,
            total_contact_hours=45,
            units=units,
            textbooks=data["textbooks"],
            references=data["references"]
        )
