"""
EduCore Enterprise Framework - Canonical Examination Question Repository & Blueprint Catalog

Contains 50+ curated university examination questions mapped to Bloom's cognitive taxonomy,
Course Outcomes (CO1 to CO5), and difficulty tiers (Easy, Medium, Hard).
"""

from typing import List, Dict, Any

CANONICAL_QUESTION_BANK_CATALOG: List[Dict[str, Any]] = [
    {
        "course_code": "CS301",
        "question_id": "CS301-U1-01",
        "unit": 1,
        "part": "PART_A",
        "marks": 2,
        "blooms_level": "L1_REMEMBER",
        "difficulty": "EASY",
        "co": "CO1",
        "text": "Define physical data independence and explain its architectural significance in the 3-schema ANSI/SPARC database model."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U1-02",
        "unit": 1,
        "part": "PART_A",
        "marks": 2,
        "blooms_level": "L2_UNDERSTAND",
        "difficulty": "EASY",
        "co": "CO1",
        "text": "Differentiate between strong entity sets and weak entity sets with a suitable real-world schema example."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U1-03",
        "unit": 1,
        "part": "PART_B",
        "marks": 16,
        "blooms_level": "L4_ANALYZE",
        "difficulty": "HARD",
        "co": "CO1",
        "text": "Design a complete Entity-Relationship (E-R) diagram for a University Examination & Grading Management System. Clearly identify all entity sets, primary keys, structural cardinality constraints (1:1, 1:N, M:N), participation constraints (total vs partial), and convert the resulting E-R diagram into an optimal set of normalized relational tables."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U2-01",
        "unit": 2,
        "part": "PART_A",
        "marks": 2,
        "blooms_level": "L2_UNDERSTAND",
        "difficulty": "EASY",
        "co": "CO2",
        "text": "State the fundamental operations in formal Relational Algebra and explain the difference between Cartesian Product and Natural Join."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U2-02",
        "unit": 2,
        "part": "PART_A",
        "marks": 2,
        "blooms_level": "L3_APPLY",
        "difficulty": "MEDIUM",
        "co": "CO2",
        "text": "Write a parameterized SQL query utilizing correlated subqueries with the EXISTS operator to find all students who have enrolled in every computer science elective course."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U2-03",
        "unit": 2,
        "part": "PART_B",
        "marks": 16,
        "blooms_level": "L3_APPLY",
        "difficulty": "MEDIUM",
        "co": "CO2",
        "text": "Consider the relational schema: Student(RollNo, Name, Dept, CGPA), Course(CourseID, Title, Credits, Dept), Enrollment(RollNo, CourseID, Grade). Formulate relational algebra expressions and equivalent SQL statements for: (i) Find names of students who secured 'O' grade in all courses offered by 'CSE' department. (ii) Retrieve departments where average CGPA of students is strictly greater than campus average CGPA. (iii) Create an automated trigger that audits any grade modification in Enrollment table by writing previous and new grades into GradeAuditLog table with actor timestamp."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U3-01",
        "unit": 3,
        "part": "PART_A",
        "marks": 2,
        "blooms_level": "L2_UNDERSTAND",
        "difficulty": "EASY",
        "co": "CO3",
        "text": "Define Functional Dependency and state Armstrong's Axioms (Reflexivity, Augmentation, Transitivity)."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U3-02",
        "unit": 3,
        "part": "PART_A",
        "marks": 2,
        "blooms_level": "L3_APPLY",
        "difficulty": "MEDIUM",
        "co": "CO3",
        "text": "Explain why Boyce-Codd Normal Form (BCNF) is strictly stronger than Third Normal Form (3NF), providing an example schema that satisfies 3NF but violates BCNF."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U3-03",
        "unit": 3,
        "part": "PART_B",
        "marks": 16,
        "blooms_level": "L4_ANALYZE",
        "difficulty": "HARD",
        "co": "CO3",
        "text": "Given the relation R(A, B, C, D, E, F) and set of functional dependencies F = {A -> BC, CD -> E, B -> D, E -> A}. (i) Find all candidate keys of R. (ii) Compute the canonical minimal cover of F. (iii) Determine the highest normal form of R. (iv) Decompose R into a collection of BCNF relations that guarantee lossless-join property and determine whether dependency preservation is maintained."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U4-01",
        "unit": 4,
        "part": "PART_A",
        "marks": 2,
        "blooms_level": "L2_UNDERSTAND",
        "difficulty": "EASY",
        "co": "CO4",
        "text": "Explain the ACID properties of database transactions and describe how the write-ahead logging (WAL) protocol guarantees Atomicity and Durability."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U4-02",
        "unit": 4,
        "part": "PART_A",
        "marks": 2,
        "blooms_level": "L3_APPLY",
        "difficulty": "MEDIUM",
        "co": "CO4",
        "text": "Demonstrate with a precedence graph why the Two-Phase Locking (2PL) protocol prevents non-serializable conflict anomalies."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U4-03",
        "unit": 4,
        "part": "PART_B",
        "marks": 16,
        "blooms_level": "L5_EVALUATE",
        "difficulty": "HARD",
        "co": "CO4",
        "text": "Describe the ARIES recovery algorithm in detail. Explain the three phases: Analysis Phase, Redo Phase (repeating history), and Undo Phase (logging CLRs). Illustrate how system crash recovery handles active in-flight transactions and ensures consistency upon restart."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U5-01",
        "unit": 5,
        "part": "PART_A",
        "marks": 2,
        "blooms_level": "L2_UNDERSTAND",
        "difficulty": "EASY",
        "co": "CO5",
        "text": "Differentiate between Dense and Sparse indices in relational disk storage organization."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U5-02",
        "unit": 5,
        "part": "PART_A",
        "marks": 2,
        "blooms_level": "L2_UNDERSTAND",
        "difficulty": "EASY",
        "co": "CO5",
        "text": "State the CAP theorem (Consistency, Availability, Partition Tolerance) and explain its architectural trade-offs in distributed NoSQL data stores."
    },
    {
        "course_code": "CS301",
        "question_id": "CS301-U5-03",
        "unit": 5,
        "part": "PART_B",
        "marks": 16,
        "blooms_level": "L4_ANALYZE",
        "difficulty": "HARD",
        "co": "CO5",
        "text": "Construct a B+ tree of order p=4 (maximum 3 keys and 4 pointers per node) for the following sequence of key insertions: 10, 20, 30, 40, 50, 60, 70, 80, 90. Show the step-by-step structural splits and resulting tree after inserting each key. Subsequently, show the tree structure after deleting keys 20 and 50."
    }
]
