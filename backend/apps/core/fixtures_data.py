"""
EduCore Enterprise Framework - Canonical Institutional Datasets & Fixture Repository

Contains standard academic curricula, course outlines, NBA accreditation criteria benchmarks,
AICTE norms, and institutional baseline parameters for all 15 university modules.
"""

from typing import Dict, List, Any


# -------------------------------------------------------------------------
# 1. 5-Unit Standard Engineering Course Syllabi Repository
# -------------------------------------------------------------------------
STANDARD_COURSE_SYLLABI_REPOSITORY: Dict[str, Dict[str, Any]] = {
    "CS101": {
        "code": "CS101",
        "title": "Problem Solving & Python Programming",
        "credits": 4,
        "regulation": "R23",
        "department": "Computer Science & Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Algorithmic Problem Solving & Python Basics",
                "hours": 9,
                "blooms": "L1_REMEMBER/L2_UNDERSTAND",
                "co": "CO1",
                "topics": "Algorithms, Building blocks of algorithms, Flow charts, Python interpreter, Interactive mode, Variables, Expressions, Statements, Data types, Operators, Precedence, Input/output statements."
            },
            {
                "unit": 2,
                "title": "Control Flow & Functions",
                "hours": 9,
                "blooms": "L2_UNDERSTAND/L3_APPLY",
                "co": "CO2",
                "topics": "Boolean values and operators, Conditional (if, if-else, if-elif-else), Iteration (while, for, break, continue, pass), Function definitions, Parameters, Arguments, Return values, Scope, Recursion, Lambda functions."
            },
            {
                "unit": 3,
                "title": "Compound Data Structures: Lists, Tuples, Dictionaries",
                "hours": 9,
                "blooms": "L3_APPLY",
                "co": "CO3",
                "topics": "Lists, List operations, Slices, Methods, List comprehension, Tuples, Immutability, Tuple assignment, Dictionaries, Keys and values, Dictionary methods, Sets, Set operations."
            },
            {
                "unit": 4,
                "title": "Files, Modules & Packages",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO4",
                "topics": "File handling, Reading and writing files, File pointers, Format operator, Command line arguments, Errors and exceptions, Handling exceptions, Modules, Standard library modules (math, random, os), Creating custom modules, Packages."
            },
            {
                "unit": 5,
                "title": "Object-Oriented Programming & Advanced Topics",
                "hours": 9,
                "blooms": "L4_ANALYZE/L5_EVALUATE",
                "co": "CO5",
                "topics": "Classes and objects, Attributes, Methods, Constructor (__init__), Inheritance, Polymorphism, Encapsulation, Method overriding, Introduction to NumPy, Pandas arrays and DataFrames, Data visualization using Matplotlib."
            }
        ],
        "textbooks": [
            "Allen B. Downey, 'Think Python: How to Think Like a Computer Scientist', 2nd Edition, O'Reilly Publishers, 2016.",
            "Guido van Rossum and Fred L. Drake Jr, 'An Introduction to Python - Revised and updated for Python 3.2', Network Theory Ltd., 2011."
        ]
    },
    "CS201": {
        "code": "CS201",
        "title": "Data Structures & Algorithms",
        "credits": 4,
        "regulation": "R23",
        "department": "Computer Science & Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Linear Data Structures: Stacks and Queues",
                "hours": 9,
                "blooms": "L2_UNDERSTAND/L3_APPLY",
                "co": "CO1",
                "topics": "Abstract Data Types (ADTs), Array-based implementation, Linked list implementation (Singly, Doubly, Circular), Stack ADT, Applications of stacks (Infix to Postfix conversion, Expression evaluation, Parenthesis matching), Queue ADT, Circular queues, Deque, Priority queues."
            },
            {
                "unit": 2,
                "title": "Tree Data Structures & Binary Search Trees",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO2",
                "topics": "Tree terminologies, Binary trees, Binary tree traversals (Inorder, Preorder, Postorder, Level-order), Binary Search Tree (BST) ADT, BST insertion, deletion, searching, Threaded binary trees, Expression trees, AVL trees, Rotations, Balance factor, Red-Black trees."
            },
            {
                "unit": 3,
                "title": "Multi-Way Trees & Heaps",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO3",
                "topics": "B-Trees, B+ Trees, Multi-way search trees, Binary heaps, Min-heap, Max-heap, Heapify operations, Priority queue using heaps, Binomial heaps, Fibonacci heaps, Disjoint set data structures, Union-Find operations."
            },
            {
                "unit": 4,
                "title": "Graph Algorithms",
                "hours": 9,
                "blooms": "L4_ANALYZE/L5_EVALUATE",
                "co": "CO4",
                "topics": "Graph representations (Adjacency Matrix, Adjacency List), Graph traversals (Breadth-First Search, Depth-First Search), Topological sorting, Minimum Spanning Trees (Prim's algorithm, Kruskal's algorithm), Shortest path algorithms (Dijkstra's single source, Bellman-Ford, Floyd-Warshall all-pairs), Network flow (Ford-Fulkerson)."
            },
            {
                "unit": 5,
                "title": "Sorting, Searching & Hashing Techniques",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO5",
                "topics": "Sorting algorithms (Merge sort, Quick sort, Heap sort, Radix sort, Shell sort), Asymptotic time complexity analysis, Searching (Linear search, Binary search, Interpolation search), Hashing, Hash functions, Collision resolution (Separate chaining, Open addressing: Linear probing, Quadratic probing, Double hashing), Universal hashing."
            }
        ],
        "textbooks": [
            "Mark Allen Weiss, 'Data Structures and Algorithm Analysis in C++', 4th Edition, Pearson, 2014.",
            "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, 'Introduction to Algorithms', 3rd Edition, MIT Press, 2009."
        ]
    },
    "CS301": {
        "code": "CS301",
        "title": "Database Management Systems",
        "credits": 4,
        "regulation": "R23",
        "department": "Computer Science & Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Database Architecture & ER Modeling",
                "hours": 9,
                "blooms": "L1_REMEMBER/L2_UNDERSTAND",
                "co": "CO1",
                "topics": "Purpose of Database Systems, View of Data, Data Abstraction, Instances and Schemas, Three-Schema Architecture, Data Models, Database Languages (DDL, DML), Database System Structure, Storage Manager, Query Processor, Entity-Relationship (E-R) Model, Entities, Relationships, Weak Entities, Extended E-R Features (Specialization, Generalization, Aggregation), Conversion of E-R Diagrams to Relational Tables."
            },
            {
                "unit": 2,
                "title": "Relational Model, Relational Algebra & Advanced SQL",
                "hours": 9,
                "blooms": "L2_UNDERSTAND/L3_APPLY",
                "co": "CO2",
                "topics": "Structure of Relational Databases, Relational Algebra Operations (Selection, Projection, Cartesian Product, Join, Division), Integrity Constraints, SQL Fundamentals, DDL Statements, DML Statements, Aggregate Functions, Group By, Having, Nested Subqueries, Set Operations, Join Expressions (Inner, Left Outer, Right Outer, Full Outer), SQL Views, Triggers, Assertions, Stored Procedures, PL/SQL Blocks, Cursors, Exception Handling."
            },
            {
                "unit": 3,
                "title": "Database Normalization & Schema Refinement",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO3",
                "topics": "Informal Design Guidelines for Relational Schemas, Functional Dependencies, Closure of Functional Dependencies, Closure of Attribute Sets, Canonical Cover, Normal Forms based on Primary Keys (1NF, 2NF, 3NF), Boyce-Codd Normal Form (BCNF), Multi-Valued Dependencies and Fourth Normal Form (4NF), Join Dependencies and Fifth Normal Form (5NF), Lossless Decomposition, Dependency Preservation."
            },
            {
                "unit": 4,
                "title": "Transaction Management & Concurrency Control",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO4",
                "topics": "Transaction Concept, ACID Properties, Transaction States, Concurrent Executions, Serializability, Conflict Serializability, View Serializability, Testing for Serializability, Recoverability, Concurrency Control Protocols, Lock-Based Protocols, Two-Phase Locking (2PL), Strict 2PL, Timestamp-Based Protocols, Validation-Based Protocols, Multiple Granularity, Deadlock Handling (Prevention, Detection, Recovery), Database Recovery Techniques, Log-Based Recovery, Checkpoints, Shadow Paging, ARIES Recovery Algorithm."
            },
            {
                "unit": 5,
                "title": "Indexing, Storage & Emerging NoSQL Databases",
                "hours": 9,
                "blooms": "L4_ANALYZE/L5_EVALUATE",
                "co": "CO5",
                "topics": "File Organization, Record Organization, Storage Hierarchy, RAID Levels, Indexing Fundamentals, Dense and Sparse Indices, Primary and Secondary Indices, Multi-level Indexing, B-Trees and B+ Trees Data Structures, Insertion and Deletion in B+ Trees, Static and Dynamic Hashing, Query Optimization (Heuristic and Cost-Based), Introduction to NoSQL Databases, CAP Theorem, BASE Properties, Document Stores (MongoDB), Key-Value Stores (Redis), Column-Family Stores (Cassandra), Graph Databases (Neo4j)."
            }
        ],
        "textbooks": [
            "Abraham Silberschatz, Henry F. Korth, and S. Sudarshan, 'Database System Concepts', 7th Edition, McGraw-Hill, 2020.",
            "Ramez Elmasri and Shamkant B. Navathe, 'Fundamentals of Database Systems', 7th Edition, Pearson, 2017."
        ]
    },
    "CS401": {
        "code": "CS401",
        "title": "Operating Systems & Kernel Architecture",
        "credits": 4,
        "regulation": "R23",
        "department": "Computer Science & Engineering",
        "units": [
            {
                "unit": 1,
                "title": "OS Overview, System Calls & Process Management",
                "hours": 9,
                "blooms": "L1_REMEMBER/L2_UNDERSTAND",
                "co": "CO1",
                "topics": "Operating System Functions, Computer System Organization, OS Operations, Dual-Mode Operation, OS Services, System Calls, System Programs, OS Structure (Monolithic, Microkernel, Layered, Modular), Process Concept, Process State Transition, Process Control Block (PCB), Context Switching, Process Scheduling, Schedulers (Long-term, Short-term, Medium-term), Inter-Process Communication (Pipes, Shared Memory, Message Passing), Client-Server Communication (Sockets, RPC)."
            },
            {
                "unit": 2,
                "title": "Threads, CPU Scheduling & Process Synchronization",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO2",
                "topics": "Multithreading Models (Many-to-One, One-to-One, Many-to-Many), Thread Libraries (POSIX Pthreads, Java Threads), Thread Pools, Implicit Threading, CPU Scheduling Concepts, Scheduling Criteria, Scheduling Algorithms (FCFS, SJF, SRTF, Priority Scheduling, Round Robin, Multilevel Queue, Multilevel Feedback Queue), Critical Section Problem, Peterson's Solution, Hardware Synchronization (Test-and-Set, Compare-and-Swap), Semaphores, Mutex Locks, Classical Synchronization Problems (Bounded-Buffer, Readers-Writers, Dining Philosophers), Monitors."
            },
            {
                "unit": 3,
                "title": "Deadlocks & Memory Management",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO3",
                "topics": "Deadlock Characterization, Necessary Conditions for Deadlock, Resource Allocation Graph, Deadlock Prevention, Deadlock Avoidance, Banker's Algorithm, Deadlock Detection, Recovery from Deadlock, Memory Management Architecture, Logical vs Physical Address Space, Dynamic Loading and Linking, Swapping, Contiguous Memory Allocation (First-Fit, Best-Fit, Worst-Fit), Fragmentation (Internal and External), Paging, Hardware Support for Paging (TLB), Page Table Structures (Hierarchical, Hashed, Inverted), Segmentation."
            },
            {
                "unit": 4,
                "title": "Virtual Memory & Storage Management",
                "hours": 9,
                "blooms": "L4_ANALYZE/L5_EVALUATE",
                "co": "CO4",
                "topics": "Virtual Memory Fundamentals, Demand Paging, Page Fault Handling, Copy-on-Write, Page Replacement Algorithms (FIFO, Optimal, LRU, Second-Chance, Enhanced Second-Chance, Counting-based), Allocation of Frames, Thrashing, Working-Set Model, Page Fault Frequency, Kernel Memory Allocation (Buddy System, Slab Allocator), Mass-Storage Structure, Disk Structure, Disk Attachment, Disk Scheduling Algorithms (FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK), Disk Management, RAID Structures."
            },
            {
                "unit": 5,
                "title": "File Systems, Protection & Security",
                "hours": 9,
                "blooms": "L2_UNDERSTAND/L3_APPLY",
                "co": "CO5",
                "topics": "File Concept, File Attributes, File Operations, Access Methods (Sequential, Direct, Indexed), Directory Structure (Single-level, Two-level, Tree-structured, Acyclic Graph, General Graph), File System Mounting, File Sharing, File Protection, Access Control Lists (ACLs), File System Implementation, Directory Implementation, Allocation Methods (Contiguous, Linked, Indexed), Free Space Management (Bit Vector, Linked List, Grouping, Counting), Linux Virtual File System (VFS), Security and Protection, Domain of Protection, Access Matrix, Cryptographic Access Authentication, Case Study: Linux Kernel Architecture."
            }
        ],
        "textbooks": [
            "Abraham Silberschatz, Peter B. Galvin, and Greg Gagne, 'Operating System Concepts', 10th Edition, Wiley, 2018.",
            "William Stallings, 'Operating Systems: Internals and Design Principles', 9th Edition, Pearson, 2017."
        ]
    },
    "CS501": {
        "code": "CS501",
        "title": "Computer Networks & Internet Protocols",
        "credits": 4,
        "regulation": "R23",
        "department": "Computer Science & Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Physical Layer & Network Architecture",
                "hours": 9,
                "blooms": "L1_REMEMBER/L2_UNDERSTAND",
                "co": "CO1",
                "topics": "Network Architecture, OSI 7-Layer Reference Model, TCP/IP Protocol Suite, Network Topologies, Physical Layer Transmission Media (Twisted Pair, Coaxial Cable, Fiber Optics, Wireless RF), Signal Encoding, Modulation, Multiplexing (FDM, TDM, WDM), Switching Techniques (Circuit Switching, Packet Switching, Virtual Circuit), Transmission Impairments, Nyquist Bandwidth, Shannon Channel Capacity."
            },
            {
                "unit": 2,
                "title": "Data Link Layer & MAC Protocols",
                "hours": 9,
                "blooms": "L2_UNDERSTAND/L3_APPLY",
                "co": "CO2",
                "topics": "Data Link Layer Design Issues, Framing (Character Count, Byte Stuffing, Bit Stuffing), Error Detection and Correction (Parity, Checksum, Cyclic Redundancy Check CRC, Hamming Code), Elementary Data Link Protocols, Sliding Window Protocols (Stop-and-Wait, Go-Back-N, Selective Repeat), Medium Access Control (MAC) Sublayer, Channel Allocation, Multiple Access Protocols (ALOHA, Slotted ALOHA, CSMA, CSMA/CD, CSMA/CA), Ethernet Standards (IEEE 802.3, Fast Ethernet, Gigabit Ethernet), Wireless LANs (IEEE 802.11 Wi-Fi, Architecture, Frame Structure), Bluetooth (IEEE 802.15.1), Bridges, Switches, Spanning Tree Protocol (STP)."
            },
            {
                "unit": 3,
                "title": "Network Layer & Routing Protocols",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO3",
                "topics": "Network Layer Design Issues, Store-and-Forward Packet Switching, IPv4 Addressing, Classful and Classless Addressing (CIDR), Subnetting, Supernetting, IPv4 Header Format, Address Resolution Protocol (ARP), Reverse ARP (RARP), Dynamic Host Configuration Protocol (DHCP), Internet Control Message Protocol (ICMP), Routing Algorithms, Distance Vector Routing, Link State Routing, Hierarchical Routing, Interior Gateway Protocols (RIP, OSPF), Exterior Gateway Protocols (BGP), IPv6 Addressing, IPv6 Header Format, Transition from IPv4 to IPv6 (Dual Stack, Tunneling, Header Translation), Network Address Translation (NAT)."
            },
            {
                "unit": 4,
                "title": "Transport Layer Protocols & Congestion Control",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO4",
                "topics": "Transport Layer Services, Port Numbers, Socket Addressing, User Datagram Protocol (UDP), UDP Header, UDP Checksum, Transmission Control Protocol (TCP), TCP Service Model, TCP Segment Header, TCP Connection Management (Three-Way Handshake, Connection Termination), TCP State Transition Diagram, Flow Control, Sliding Window in TCP, TCP Congestion Control Algorithms (Slow Start, Congestion Avoidance, Fast Retransmit, Fast Recovery - TCP Tahoe, TCP Reno), Timers in TCP (Retransmission, Persistence, Keepalive, Time-Wait), Quality of Service (QoS), Traffic Shaping (Leaky Bucket, Token Bucket), Integrated Services, Differentiated Services."
            },
            {
                "unit": 5,
                "title": "Application Layer & Network Security",
                "hours": 9,
                "blooms": "L4_ANALYZE/L5_EVALUATE",
                "co": "CO5",
                "topics": "Application Layer Paradigms, Domain Name System (DNS), Resource Records, DNS Servers, Electronic Mail (SMTP, POP3, IMAP), Message Formats (MIME), World Wide Web (HTTP/1.1, HTTP/2, HTTPS), Uniform Resource Locators (URLs), Cookies, Web Caching, File Transfer Protocol (FTP), Network Management (SNMP), Network Security Foundations, Symmetric Cryptography (DES, AES), Asymmetric Cryptography (RSA, ECC), Digital Signatures, Public Key Infrastructure (PKI), TLS/SSL Handshake Protocol, IPsec Architecture, Firewalls, Intrusion Detection Systems (IDS)."
            }
        ],
        "textbooks": [
            "Andrew S. Tanenbaum and David J. Wetherall, 'Computer Networks', 5th Edition, Pearson, 2013.",
            "James F. Kurose and Keith W. Ross, 'Computer Networking: A Top-Down Approach', 7th Edition, Pearson, 2017."
        ]
    }
}


# -------------------------------------------------------------------------
# 2. National Board of Accreditation (NBA) Tier-1 Criteria Master
# -------------------------------------------------------------------------
NBA_TIER1_CRITERIA_MASTER: List[Dict[str, Any]] = [
    {
        "criterion_number": 1,
        "title": "Vision, Mission and Program Educational Objectives (PEOs)",
        "marks_weightage": 50,
        "sub_criteria": [
            {"code": "1.1", "name": "State the Vision and Mission of the Department and Institute", "marks": 5},
            {"code": "1.2", "name": "State the Program Educational Objectives (PEOs)", "marks": 5},
            {"code": "1.3", "name": "Establish correlation between PEOs and Mission statements", "marks": 10},
            {"code": "1.4", "name": "Process for defining and reviewing Vision, Mission and PEOs", "marks": 15},
            {"code": "1.5", "name": "Process of dissemination among stakeholders and awareness", "marks": 15}
        ]
    },
    {
        "criterion_number": 2,
        "title": "Program Curriculum and Teaching-Learning Processes",
        "marks_weightage": 100,
        "sub_criteria": [
            {"code": "2.1", "name": "Program Curriculum structure & AICTE model compliance", "marks": 20},
            {"code": "2.2", "name": "Teaching-Learning Processes (Pedagogical innovations, ICT tools)", "marks": 25},
            {"code": "2.3", "name": "Quality of internal semester question papers and assignments", "marks": 20},
            {"code": "2.4", "name": "Quality of student projects, rubrics, and industry relevance", "marks": 25},
            {"code": "2.5", "name": "Industrial training, internships, and industrial visits", "marks": 10}
        ]
    },
    {
        "criterion_number": 3,
        "title": "Course Outcomes and Program Outcomes (CO-PO Attainment)",
        "marks_weightage": 175,
        "sub_criteria": [
            {"code": "3.1", "name": "Establish the correlation between Courses and POs/PSOs", "marks": 25},
            {"code": "3.2", "name": "Attainment of Course Outcomes (Internal assessment + End Sem)", "marks": 50},
            {"code": "3.3", "name": "Attainment of Program Outcomes (Direct & Indirect Assessment)", "marks": 100}
        ]
    },
    {
        "criterion_number": 4,
        "title": "Students' Performance & Graduation Track",
        "marks_weightage": 100,
        "sub_criteria": [
            {"code": "4.1", "name": "Enrolment Ratio (Sanctioned vs Admitted students)", "marks": 20},
            {"code": "4.2", "name": "Success rate without backlogs in stipulated period (4 years)", "marks": 40},
            {"code": "4.3", "name": "Success rate with backlogs in stipulated period", "marks": 20},
            {"code": "4.4", "name": "Academic performance in second and third year examinations", "marks": 10},
            {"code": "4.5", "name": "Placement, higher studies and entrepreneurship record", "marks": 10}
        ]
    },
    {
        "criterion_number": 5,
        "title": "Faculty Information and Contributions",
        "marks_weightage": 200,
        "sub_criteria": [
            {"code": "5.1", "name": "Student-Faculty Ratio (SFR <= 1:15 for maximum marks)", "marks": 20},
            {"code": "5.2", "name": "Faculty Cadre Ratio (1 Professor : 2 Associate : 6 Assistant)", "marks": 25},
            {"code": "5.3", "name": "Faculty Qualification (Ph.D. degree holder ratio >= 60%)", "marks": 25},
            {"code": "5.4", "name": "Faculty Retention and Service Stability", "marks": 25},
            {"code": "5.5", "name": "Faculty Innovations in Teaching and Learning", "marks": 20},
            {"code": "5.6", "name": "Faculty Development Programs (FDPs attended >= 10 days)", "marks": 15},
            {"code": "5.7", "name": "Research and Development (SCI/Scopus Publications & Citations)", "marks": 30},
            {"code": "5.8", "name": "Sponsored Research Grants (DST, SERB, AICTE funded)", "marks": 20},
            {"code": "5.9", "name": "Development activities (Product development, Research labs)", "marks": 10},
            {"code": "5.10", "name": "Consultancy projects and industrial revenue generation", "marks": 10}
        ]
    },
    {
        "criterion_number": 6,
        "title": "Facilities and Technical Support",
        "marks_weightage": 80,
        "sub_criteria": [
            {"code": "6.1", "name": "Adequate and well-equipped laboratories per curriculum", "marks": 30},
            {"code": "6.2", "name": "Maintenance and overall ambiance of academic facilities", "marks": 10},
            {"code": "6.3", "name": "Safety measures in laboratories and hazardous areas", "marks": 10},
            {"code": "6.4", "name": "Project laboratory, Innovation hub and technical support staff", "marks": 30}
        ]
    },
    {
        "criterion_number": 7,
        "title": "Continuous Improvement",
        "marks_weightage": 75,
        "sub_criteria": [
            {"code": "7.1", "name": "Actions taken based on results of evaluation of each PO/PSO", "marks": 30},
            {"code": "7.2", "name": "Academic audit and actions taken thereof (Internal & External)", "marks": 15},
            {"code": "7.3", "name": "Improvement in Placement, Higher Studies and Entrepreneurship", "marks": 15},
            {"code": "7.4", "name": "Improvement in the quality of admitted students rank cutoff", "marks": 15}
        ]
    },
    {
        "criterion_number": 8,
        "title": "First Year Academics",
        "marks_weightage": 50,
        "sub_criteria": [
            {"code": "8.1", "name": "First Year Student-Faculty Ratio (FSR <= 1:15)", "marks": 5},
            {"code": "8.2", "name": "Qualification of Faculty Teaching First Year Common Courses", "marks": 5},
            {"code": "8.3", "name": "First Year Academic Performance and Pass Percentage", "marks": 10},
            {"code": "8.4", "name": "Attainment of Course Outcomes of all first year courses", "marks": 30}
        ]
    },
    {
        "criterion_number": 9,
        "title": "Student Support Systems",
        "marks_weightage": 50,
        "sub_criteria": [
            {"code": "9.1", "name": "Mentoring system to help at individual levels (1:20 ratio)", "marks": 10},
            {"code": "9.2", "name": "Feedback analysis and reward/corrective measures taken", "marks": 10},
            {"code": "9.3", "name": "Feedback on facilities and amenities", "marks": 5},
            {"code": "9.4", "name": "Self-learning facilities, library, Internet, MOOC access", "marks": 10},
            {"code": "9.5", "name": "Career guidance, Training, Placement and Entrepreneurship Cell", "marks": 10},
            {"code": "9.6", "name": "Co-curricular and Extra-curricular activities", "marks": 5}
        ]
    },
    {
        "criterion_number": 10,
        "title": "Governance, Institutional Support and Financial Resources",
        "marks_weightage": 120,
        "sub_criteria": [
            {"code": "10.1", "name": "Organization, Governance and Transparency (Governing Body)", "marks": 40},
            {"code": "10.2", "name": "Budget Allocation, Utilization and Financial Audits", "marks": 30},
            {"code": "10.3", "name": "Library and Internet (Volumes, e-Journals, 1 Gbps Bandwidth)", "marks": 20},
            {"code": "10.4", "name": "Institutional Support for Faculty Higher Studies & Research", "marks": 30}
        ]
    }
]
