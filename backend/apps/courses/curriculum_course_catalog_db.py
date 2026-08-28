"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for CSE, ECE, EEE, MECH, CIVIL, and AIML courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB: Dict[str, Dict[str, Any]] = {
    "CS101": {
        "code": "CS101",
        "title": "Problem Solving and Python Programming",
        "credits": 3,
        "ltp": "3-0-0",
        "department": "Computer Science & Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Introduction to Computers and Algorithms",
                "topics": [
                    "Introduction to computer systems: Hardware, software, memory, ALU, CPU, input-output systems.",
                    "Compilation process: Compilers, interpreters, linkers, loaders, execution modes.",
                    "Problem solving methodologies: Algorithms, flowcharts, pseudo-code syntax structures.",
                    "Visualizing logic: Standard flowchart shapes, input-output symbols, processing indicators.",
                    "Basic algorithms: Sum of N numbers, finding maximum of three numbers, simple sequence checks."
                ]
            },
            {
                "unit": 2,
                "title": "Python Control Flow & Loops",
                "topics": [
                    "Python runtime environment, interactive vs script mode execution.",
                    "Primitive data types: Integers, floating-point numbers, booleans, strings.",
                    "Variable assignments, dynamic typing rules, variable naming conventions.",
                    "Operators: Arithmetic, relational, logical, bitwise operators.",
                    "Conditional selection: if, if-else, nested if-else, if-elif-else cascade.",
                    "Looping statements: while loops, for loops with range parameters.",
                    "Loop control: break, continue, pass statements, infinite loop handling."
                ]
            },
            {
                "unit": 3,
                "title": "Data Types and Collections",
                "topics": [
                    "Strings: Indexing, slicing, concatenation, string methods.",
                    "Lists: Creation, list brackets, indexing, modifying list elements.",
                    "List operations: append, extend, insert, remove, pop, sort, reverse.",
                    "List comprehension: Inline loop syntax, filtering, mapping.",
                    "Tuples: Immutable sequences, tuple packing/unpacking.",
                    "Dictionaries: Key-value pairs, key constraints, operations.",
                    "Sets: Unique element collections, union, intersection, difference."
                ]
            },
            {
                "unit": 4,
                "title": "Modular Design with Functions",
                "topics": [
                    "Defining functions: def keyword, parameters, return statements.",
                    "Arguments: Positional, keyword, default parameters.",
                    "Variable-length arguments: *args list, **kwargs dictionary packaging.",
                    "Scope rules: Local, global, nonlocal scopes, global keyword.",
                    "Recursion: Base case, recursive reduction, call stack trace.",
                    "Lambda functions: Anonymous inline functions syntax."
                ]
            },
            {
                "unit": 5,
                "title": "File I/O & Exception Handling",
                "topics": [
                    "File handling: open(), read(), write(), append() file modes.",
                    "File types: Text files vs binary files, seek(), tell().",
                    "Context managers: with statement for resource safety.",
                    "Exception handling: try-except-finally blocks, catching specific errors.",
                    "Raising exceptions: raise statement, custom exception classes."
                ]
            }
        ],
        "textbooks": [
            "Allen B. Downey, 'Think Python: How to Think Like a Computer Scientist', O'Reilly.",
            "Reema Thareja, 'Python Programming Using Problem Solving Approach', Oxford."
        ]
    },
    "CS201": {
        "code": "CS201",
        "title": "Data Structures and Algorithms in C",
        "credits": 4,
        "ltp": "3-0-2",
        "department": "Computer Science & Engineering",
        "units": [
            {
                "unit": 1,
                "title": "C Pointer Mechanics & Structures",
                "topics": [
                    "Pointers: Addressing, dereferencing, pointer arithmetic.",
                    "Dynamic memory management: malloc, calloc, realloc, and free functions.",
                    "Structures and Unions, nested structures, pointers to structures.",
                    "Self-referential structures: Node creation for linked lists."
                ]
            },
            {
                "unit": 2,
                "title": "Linear Linked Lists",
                "topics": [
                    "Abstract Data Types (ADTs) concepts, linear vs non-linear structures.",
                    "Singly linked list: node structure, insert/delete at head, tail, or middle positions.",
                    "Singly linked list operations: Search, traverse, reverse, length calculation.",
                    "Doubly linked list: prev and next pointers, insertion and deletion.",
                    "Circular linked list: Singly and doubly circular representations, boundary checks."
                ]
            },
            {
                "unit": 3,
                "title": "Stacks and Queues",
                "topics": [
                    "Stack ADT: LIFO principle, array representation, linked list implementation.",
                    "Stack operations: push, pop, peek, overflow and underflow detection.",
                    "Stack applications: Arithmetic expression conversion (infix, prefix, postfix).",
                    "Queue ADT: FIFO principle, array-based circular queue implementation.",
                    "Queue operations: enqueue, dequeue, size, priority queues, double ended queues (Deques)."
                ]
            },
            {
                "unit": 4,
                "title": "Binary Search Trees",
                "topics": [
                    "Tree terminology: Root, parent, child, leaf, height, depth, subtree.",
                    "Binary tree: Representations, recursive pre-order, in-order, post-order traversals.",
                    "Binary Search Tree (BST): Insert, delete, and search operations.",
                    "Balanced trees: AVL tree balancing factor, single and double rotations."
                ]
            },
            {
                "unit": 5,
                "title": "Graphs & Sorting Algorithms",
                "topics": [
                    "Graph concepts: Directed, undirected, weighted graphs, paths, cycles.",
                    "Graph representations: Adjacency matrix and adjacency list structures.",
                    "Graph traversals: Breadth First Search (BFS), Depth First Search (DFS).",
                    "Searching and sorting: Binary search, Quick sort, Merge sort, Heap sort algorithms.",
                    "Hashing: Hash functions, collision resolution strategies (open addressing, chaining)."
                ]
            }
        ],
        "textbooks": [
            "Ellis Horowitz, Sartaj Sahni, and Susan Anderson-Freed, 'Fundamentals of Data Structures in C'.",
            "Reema Thareja, 'Data Structures Using C', Oxford University Press."
        ]
    },
    "CS301": {
        "code": "CS301",
        "title": "Database Management Systems",
        "credits": 4,
        "ltp": "3-0-2",
        "department": "Computer Science & Engineering",
        "units": [
            {
                "unit": 1,
                "title": "DBMS Architecture & E-R Model",
                "topics": [
                    "Database vs File Systems, benefits of database approach.",
                    "Three-Schema Architecture, physical and logical data independence.",
                    "Entity-Relationship (E-R) model: Entities, attributes, relationship sets.",
                    "Constraints: Keys, structural constraints, participation constraints.",
                    "Extended E-R features: Generalization, specialization, aggregation.",
                    "Reduction to relational tables: Rules and mapping guidelines."
                ]
            },
            {
                "unit": 2,
                "title": "Relational Algebra and SQL Queries",
                "topics": [
                    "Relational algebra: Select, project, union, set difference, cartesian product.",
                    "Relational join operations: Theta join, natural join, outer joins.",
                    "Structured Query Language (SQL): Data definition (DDL), Data manipulation (DML).",
                    "SQL queries: Nested queries, subqueries, EXISTS, IN, GROUP BY, HAVING.",
                    "Database views, indexes, dynamic SQL, database triggers."
                ]
            },
            {
                "unit": 3,
                "title": "Functional Dependencies & Normalization",
                "topics": [
                    "Functional dependencies: Closure of FD set, attribute closure.",
                    "Armstrong's Axioms: Reflexivity, augmentation, transitivity.",
                    "Normal forms: First Normal Form (1NF), Second Normal Form (2NF).",
                    "Third Normal Form (3NF), Boyce-Codd Normal Form (BCNF).",
                    "Lossless-join decomposition, dependency preservation analysis."
                ]
            },
            {
                "unit": 4,
                "title": "Transaction Management & Locking",
                "topics": [
                    "Transaction concepts: ACID properties (Atomicity, Consistency, Isolation, Durability).",
                    "Transaction states, serializability: Conflict and view serializability.",
                    "Concurrency control: Lock-based protocols, Two-Phase Locking (2PL).",
                    "Timestamp-based protocols, validation-based protocols.",
                    "Deadlock handling: Prevention, detection, and recovery."
                ]
            },
            {
                "unit": 5,
                "title": "B+ Tree Indexing & Crash Recovery",
                "topics": [
                    "Physical storage organization, block allocations, file systems.",
                    "B+ Tree Indexing: Node structural rules, search, insert, split.",
                    "Database recovery: Log-based recovery, deferred and immediate updates.",
                    "Write-Ahead Logging (WAL) protocol, checkpoints.",
                    "ARIES recovery algorithm: Analysis, Redo, Undo passes."
                ]
            }
        ],
        "textbooks": [
            "Abraham Silberschatz, Henry F. Korth, and S. Sudarshan, 'Database System Concepts'.",
            "Ramez Elmasri and Shamkant B. Navathe, 'Fundamentals of Database Systems'."
        ]
    }
}
