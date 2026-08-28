from typing import List, Dict, Any, Optional
from django.db.models import Q
from .models import Course, TimetableEntry
from apps.faculty.models import Faculty


class CourseCurriculumService:
    """
    Domain service for Curriculum Benchmark and Conflict-Free Timetable Scheduling.
    """

    BENCHMARK_CSE_CURRICULUM = [
        {
            'code': 'CSE-101',
            'title': 'Data Structures & Algorithms',
            'credits': 4,
            'semester': 1,
            'description': 'Abstract data types, asymptotic analysis, trees, heaps, balanced trees, and graph algorithms.',
            'units': [
                'Unit 1: Linear Data Structures, Stacks, Queues, Linked Lists',
                'Unit 2: Non-Linear Trees, AVL, Red-Black Trees, Heaps',
                'Unit 3: Graph Traversal, Shortest Paths (Dijkstra, Bellman-Ford)',
                'Unit 4: Dynamic Programming & Greedy Algorithms',
                'Unit 5: String Matching & Advanced NP-Completeness',
            ]
        },
        {
            'code': 'CSE-202',
            'title': 'Database Management Systems (DBMS)',
            'credits': 4,
            'semester': 2,
            'description': 'Relational data model, relational algebra, SQL optimization, normalization, indexing, and ACID transactions.',
            'units': [
                'Unit 1: ER Modeling and Relational Data Models',
                'Unit 2: SQL DDL/DML, Nested Queries, and Aggregations',
                'Unit 3: Normalization (1NF, 2NF, 3NF, BCNF, 4NF)',
                'Unit 4: B+ Tree Indexing & Query Optimizer Pipelines',
                'Unit 5: Concurrency Control, Two-Phase Locking, and Recovery',
            ]
        },
        {
            'code': 'CSE-301',
            'title': 'Operating Systems',
            'credits': 4,
            'semester': 3,
            'description': 'Kernel design, process scheduling, inter-process communication, concurrency, deadlocks, and virtual memory paging.',
            'units': [
                'Unit 1: OS Architecture, System Calls, and Kernel Structures',
                'Unit 2: Process Scheduling, Threads, and Mutex Synchronization',
                'Unit 3: Deadlocks Prevention, Avoidance (Banker Algorithm)',
                'Unit 4: Virtual Memory, Page Replacement (LRU, Optimal)',
                'Unit 5: Disk Scheduling, File Systems, and Access Control',
            ]
        },
        {
            'code': 'CSE-302',
            'title': 'Computer Networks',
            'credits': 4,
            'semester': 4,
            'description': 'OSI and TCP/IP layered architecture, routing algorithms, transport protocols (TCP/UDP), and socket programming.',
            'units': [
                'Unit 1: Network Layering, Physical Media, and Topologies',
                'Unit 2: Data Link Layer, Sliding Window, Error Detection (CRC)',
                'Unit 3: Network Routing (OSPF, BGP, Distance Vector)',
                'Unit 4: Transport Layer, TCP Congestion Control, Flow Control',
                'Unit 5: Application Protocols (HTTP/3, DNS, TLS Security)',
            ]
        },
        {
            'code': 'CSE-401',
            'title': 'Machine Learning & Neural Networks',
            'credits': 4,
            'semester': 5,
            'description': 'Supervised learning, deep feedforward networks, convolutional architectures, backpropagation, and transformer attention.',
            'units': [
                'Unit 1: Statistical Learning, Linear & Logistic Regression',
                'Unit 2: Decision Trees, Ensemble Methods (Random Forest, XGBoost)',
                'Unit 3: Deep Neural Networks & Backpropagation Optimization',
                'Unit 4: Convolutional Neural Networks (CNN) for Computer Vision',
                'Unit 5: Recurrent Architectures & Transformer Attention Engines',
            ]
        },
    ]

    @classmethod
    def detect_timetable_conflicts(cls, day: str, start_time: str, end_time: str, room_number: str, faculty_id: int, section: str, exclude_id: Optional[int] = None) -> Dict[str, Any]:
        """
        Comprehensive conflict checking across Room, Faculty, and Class Section overlaps.
        """
        qs = TimetableEntry.objects.filter(day_of_week=day)
        if exclude_id:
            qs = qs.exclude(id=exclude_id)

        # Overlapping time window filter
        time_overlap = Q(start_time__lt=end_time, end_time__gt=start_time)

        room_conflict = qs.filter(time_overlap, room_number=room_number).first()
        faculty_conflict = qs.filter(time_overlap, faculty_id=faculty_id).first() if faculty_id else None
        section_conflict = qs.filter(time_overlap, section=section).first()

        conflicts = []
        if room_conflict:
            conflicts.append(f"Room Collision: Classroom {room_number} is already occupied by {room_conflict.course.code} ({room_conflict.start_time} - {room_conflict.end_time}).")
        if faculty_conflict:
            conflicts.append(f"Faculty Double-Booking: Instructor {faculty_conflict.faculty.name} is already assigned to section {faculty_conflict.section}.")
        if section_conflict:
            conflicts.append(f"Section Overlap: Cohort {section} already has {section_conflict.course.code} scheduled at this hour.")

        return {
            'has_conflict': len(conflicts) > 0,
            'conflict_count': len(conflicts),
            'messages': conflicts,
        }
