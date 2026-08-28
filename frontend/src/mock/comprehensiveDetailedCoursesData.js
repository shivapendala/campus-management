/**
 * Comprehensive Course Catalog Database - Multi-Department Curriculum Mapping
 * Defines credits, lecture plans, laboratory manuals, and textbooks for all 8 semesters.
 */

export const comprehensiveDetailedCoursesData = {
  CSE: [
    {
      code: "CS101",
      title: "Problem Solving and Python Programming",
      credits: 3,
      semester: 1,
      units: [
        {
          unit: 1,
          title: "Introduction to Computers and Problem Solving",
          topics: [
            "Introduction to computer systems: Hardware, software, memory, ALU, CPU, I/O devices.",
            "Concept of programming: Compilers, interpreters, linkers, loaders, execution cycles.",
            "Problem-solving methodologies: Algorithms, flowchart structures, pseudo-code syntax.",
            "Visualizing algorithms: Flowchart shape templates, input-output symbols, processing indicators.",
            "Control structures: Sequence, selection (conditional branches), and repetition (loops).",
            "Illustrative problems: Sum of N numbers, finding the maximum of three numbers.",
            "Searching a list: Linear search flowchart and algorithm comparison.",
            "Sorting values: Bubble sort flowchart and algorithm trace."
          ]
        },
        {
          unit: 2,
          title: "Python Programming Basics",
          topics: [
            "Python runtime environment, interactive shell vs script mode execution.",
            "Basic data types: Integers, floating-point numbers, boolean, strings.",
            "Variables, naming conventions, dynamic typing, assignment statements.",
            "Arithmetic operators: Addition, subtraction, multiplication, division, modulo.",
            "Relational operators: Comparison flags, logical operators, short-circuit evaluation.",
            "Control flow: if statements, if-else structures, nested conditional blocks.",
            "Iterative control: while loops, definite loops with for iterator, range function parameters.",
            "Loop control modifiers: break, continue, pass statements."
          ]
        },
        {
          unit: 3,
          title: "Structured Collections & Data Types",
          topics: [
            "Strings: Indexing, slicing, concatenation, string methods (strip, split, join, replace).",
            "Lists: Creating lists, index tracking, modifying values, list operations.",
            "List methods: append, extend, insert, remove, pop, sort, reverse.",
            "List comprehension: Inline loop syntax, filtering, mapping collections.",
            "Tuples: Immutable sequences, tuple packing and unpacking, indexing.",
            "Dictionaries: Key-value pairs, key constraints, dictionary operations.",
            "Sets: Unique element collections, union, intersection, difference, symmetric difference."
          ]
        },
        {
          unit: 4,
          title: "Functions and Modular Design",
          topics: [
            "Defining functions: def keyword, parameters, return statements, none values.",
            "Argument mapping: Positional arguments, keyword arguments, default parameter values.",
            "Variable-length arguments: *args for list packaging, **kwargs for dict packaging.",
            "Scope rules: Local scope, global scope, global variables modification, nonlocal keyword.",
            "Recursive functions: Base case definition, recursive reduction, stack trace.",
            "Lambda functions: Anonymous inline functions syntax and use cases.",
            "Python modules: import statements, aliasing, custom module creation."
          ]
        },
        {
          unit: 5,
          title: "Files and Exception Handling",
          topics: [
            "File handling: open(), read(), write(), append() file modes.",
            "File types: Text files vs binary files, handling file pointers, seek(), tell().",
            "Context managers: with statement for resource safety.",
            "Exception handling: try-except-finally blocks, catching specific errors.",
            "Raising exceptions: raise statement, custom exception classes.",
            "Object-Oriented Programming (OOP) in Python: Class definitions, objects, constructors, inheritance."
          ]
        }
      ],
      textbooks: [
        "Allen B. Downey, 'Think Python: How to Think Like a Computer Scientist', O'Reilly.",
        "Reema Thareja, 'Python Programming Using Problem Solving Approach', Oxford."
      ]
    },
    {
      code: "CS201",
      title: "Data Structures and Algorithms in C",
      credits: 4,
      semester: 2,
      units: [
        {
          unit: 1,
          title: "Pointers and Memory Management in C",
          topics: [
            "Pointers basic concepts: Addressing, dereferencing, pointer arithmetic.",
            "Dynamic memory allocation: malloc, calloc, realloc, and free functions.",
            "Structures and Unions in C, nested structures, pointers to structures.",
            "Self-referential structures: Node creation for dynamic list elements."
          ]
        },
        {
          unit: 2,
          title: "Linear Data Structures - Linked Lists",
          topics: [
            "Abstract Data Types (ADTs) concepts, linear vs non-linear structures.",
            "Singly linked list: node structure, insert/delete at head, tail, or middle positions.",
            "Singly linked list operations: Search, traverse, reverse, length calculation.",
            "Doubly linked list: prev and next pointers, insertion and deletion.",
            "Circular linked list: Singly and doubly circular representations, boundary checks."
          ]
        },
        {
          unit: 3,
          title: "Stacks and Queues",
          topics: [
            "Stack ADT: LIFO principle, array representation, linked list implementation.",
            "Stack operations: push, pop, peek, overflow and underflow detection.",
            "Stack applications: Arithmetic expression conversion (infix, prefix, postfix).",
            "Queue ADT: FIFO principle, array-based circular queue implementation.",
            "Queue operations: enqueue, dequeue, size, priority queues, double ended queues (Deques)."
          ]
        },
        {
          unit: 4,
          title: "Non-Linear Structures - Trees",
          topics: [
            "Tree terminology: Root, parent, child, leaf, height, depth, subtree.",
            "Binary tree: Representations, recursive pre-order, in-order, post-order traversals.",
            "Binary Search Tree (BST): Insert, delete, and search operations.",
            "Balanced trees: AVL tree balancing factor, single and double rotations."
          ]
        },
        {
          unit: 5,
          title: "Graphs and Sorting Techniques",
          topics: [
            "Graph concepts: Directed, undirected, weighted graphs, paths, cycles.",
            "Graph representations: Adjacency matrix and adjacency list structures.",
            "Graph traversals: Breadth First Search (BFS), Depth First Search (DFS).",
            "Searching and sorting: Binary search, Quick sort, Merge sort, Heap sort algorithms.",
            "Hashing: Hash functions, collision resolution strategies (open addressing, chaining)."
          ]
        }
      ],
      textbooks: [
        "Ellis Horowitz, Sartaj Sahni, and Susan Anderson-Freed, 'Fundamentals of Data Structures in C'.",
        "Reema Thareja, 'Data Structures Using C', Oxford University Press."
      ]
    },
    {
      code: "CS301",
      title: "Database Management Systems",
      credits: 4,
      semester: 3,
      units: [
        {
          unit: 1,
          title: "DBMS Architecture & E-R Model",
          topics: [
            "Database vs File Systems, benefits of database approach.",
            "Three-Schema Architecture, physical and logical data independence.",
            "Entity-Relationship (E-R) model: Entities, attributes, relationship sets.",
            "Constraints: Keys, structural constraints, participation constraints.",
            "Extended E-R features: Generalization, specialization, aggregation.",
            "Reduction to relational tables: Rules and mapping guidelines."
          ]
        },
        {
          unit: 2,
          title: "Relational Model & SQL",
          topics: [
            "Relational algebra: Select, project, union, set difference, cartesian product.",
            "Relational join operations: Theta join, natural join, outer joins.",
            "Structured Query Language (SQL): Data definition (DDL), Data manipulation (DML).",
            "SQL queries: Nested queries, subqueries, EXISTS, IN, GROUP BY, HAVING.",
            "Database views, indexes, dynamic SQL, database triggers."
          ]
        },
        {
          unit: 3,
          title: "Database Design & Normalization",
          topics: [
            "Functional dependencies: Closure of FD set, attribute closure.",
            "Armstrong's Axioms: Reflexivity, augmentation, transitivity.",
            "Normal forms: First Normal Form (1NF), Second Normal Form (2NF).",
            "Third Normal Form (3NF), Boyce-Codd Normal Form (BCNF).",
            "Lossless-join decomposition, dependency preservation analysis."
          ]
        },
        {
          unit: 4,
          title: "Transaction Processing & Concurrency",
          topics: [
            "Transaction concepts: ACID properties (Atomicity, Consistency, Isolation, Durability).",
            "Transaction states, serializability: Conflict and view serializability.",
            "Concurrency control: Lock-based protocols, Two-Phase Locking (2PL).",
            "Timestamp-based protocols, validation-based protocols.",
            "Deadlock handling: Prevention, detection, and recovery."
          ]
        },
        {
          unit: 5,
          title: "Indexing, Storage & Crash Recovery",
          topics: [
            "Physical storage organization, block allocations, file systems.",
            "B+ Tree Indexing: Node structural rules, search, insert, split.",
            "Database recovery: Log-based recovery, deferred and immediate updates.",
            "Write-Ahead Logging (WAL) protocol, checkpoints.",
            "ARIES recovery algorithm: Analysis, Redo, Undo passes."
          ]
        }
      ],
      textbooks: [
        "Abraham Silberschatz, Henry F. Korth, and S. Sudarshan, 'Database System Concepts'.",
        "Ramez Elmasri and Shamkant B. Navathe, 'Fundamentals of Database Systems'."
      ]
    },
    {
      code: "CS302",
      title: "Design and Analysis of Algorithms",
      credits: 4,
      semester: 3,
      units: [
        {
          unit: 1,
          title: "Algorithm Analysis & Recurrences",
          topics: [
            "Asymptotic notations: Big-O, Omega, Theta definitions.",
            "Mathematical analysis of non-recursive and recursive algorithms.",
            "Recurrence relations: Master theorem, recursion trees."
          ]
        },
        {
          unit: 2,
          title: "Divide-and-Conquer & Greedy Method",
          topics: [
            "Divide-and-conquer strategy, Merge sort, Quick sort analysis.",
            "Greedy method: Knapsack problem, Minimum Spanning Trees (Prim's, Kruskal's).",
            "Single-source shortest paths: Dijkstra's algorithm."
          ]
        },
        {
          unit: 3,
          title: "Dynamic Programming",
          topics: [
            "Dynamic programming principles, Multi-stage graphs.",
            "All-pairs shortest paths: Floyd-Warshall algorithm.",
            "0/1 Knapsack problem, Traveling Salesperson Problem (TSP).",
            "Matrix chain multiplication, Longest Common Subsequence (LCS)."
          ]
        },
        {
          unit: 4,
          title: "Backtracking & Branch-and-Bound",
          topics: [
            "Backtracking strategy: N-Queens, Sum of Subsets, Graph Coloring.",
            "Branch-and-bound: LC Search, FIFO branch-and-bound.",
            "Traveling salesperson branch-and-bound algorithms."
          ]
        },
        {
          unit: 5,
          title: "NP-Hard & NP-Complete Problems",
          topics: [
            "P, NP, NP-Hard, NP-Complete classes definitions.",
            "Cook's theorem, NP-complete reductions (SAT, Clique, Vertex Cover).",
            "Approximation algorithms: TSP approximation, vertex cover approximation."
          ]
        }
      ],
      textbooks: [
        "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, 'Introduction to Algorithms'.",
        "Ellis Horowitz, Sartaj Sahni, and Sanguthevar Rajasekaran, 'Fundamentals of Computer Algorithms'."
      ]
    },
    {
      code: "CS401",
      title: "Operating Systems",
      credits: 4,
      semester: 4,
      units: [
        {
          unit: 1,
          title: "OS Structures & Process Scheduling",
          topics: [
            "System components: Process, memory, files, shell, GUI interfaces.",
            "System calls: Process control, file management, device management.",
            "Process state transitions, Process Control Block (PCB).",
            "CPU Scheduling: FCFS, SJF, SRTF, Round Robin, Multilevel Feedback Queues."
          ]
        },
        {
          unit: 2,
          title: "Process Synchronization & Deadlocks",
          topics: [
            "Critical Section problem, Peterson's solution, Hardware support.",
            "Semaphores: Binary, counting, classical synchronization problems.",
            "Deadlock metrics: Prevention, avoidance (Banker's), detection, and recovery."
          ]
        },
        {
          unit: 3,
          title: "Memory Management & Paging",
          topics: [
            "Dynamic loading, dynamic linking, address binding, swapping.",
            "Paging: Page tables, TLB cache, page tables inversion.",
            "Virtual memory: Demand paging, page fault handling.",
            "Page replacement: FIFO, Optimal, LRU, Thrashing."
          ]
        },
        {
          unit: 4,
          title: "File Systems & Storage Structure",
          topics: [
            "File operations, access methods, directory structures.",
            "File systems allocation: Contiguous, linked, indexed strategies.",
            "Free-space lists, UNIX inode structure, directory caching.",
            "Disk scheduling: FCFS, SSTF, SCAN, C-SCAN algorithms."
          ]
        },
        {
          unit: 5,
          title: "Kernel Architecture Case Studies",
          topics: [
            "Linux Process management, task_struct representation.",
            "Linux virtual memory management, slab allocator.",
            "Windows kernel architecture: HAL, Executive services, Object Manager."
          ]
        }
      ],
      textbooks: [
        "Abraham Silberschatz, Peter B. Galvin, and Greg Gagne, 'Operating System Concepts'.",
        "William Stallings, 'Operating Systems: Internals and Design Principles'."
      ]
    },
    {
      code: "CS501",
      title: "Computer Networks",
      credits: 4,
      semester: 5,
      units: [
        {
          unit: 1,
          title: "OSI Layering & Data Link Protocols",
          topics: [
            "OSI reference model, TCP/IP protocol suite comparison.",
            "Data link framing, flow control: sliding window protocols.",
            "Error checks: Parity, CRC polynomials, Hamming distance.",
            "Medium access: ALOHA, CSMA/CD, CSMA/CA, Ethernet frames."
          ]
        },
        {
          unit: 2,
          title: "Network Layer & Subnets",
          topics: [
            "IP addressing, Classful vs Classless (CIDR) subnet design.",
            "Subnet masks, network and host range computations.",
            "Routing: Distance vector (RIP), Link state (OSPF) routing.",
            "Border Gateway Protocol (BGP), ARP, ICMP, DHCP, NAT."
          ]
        },
        {
          unit: 3,
          title: "Transport Protocols & Congestion Control",
          topics: [
            "Port numbers, socket multiplexing, UDP segment format.",
            "TCP connection handshake (3-way sync), connection termination.",
            "TCP sliding window flow control, congestion window dynamics.",
            "Congestion algorithms: Slow start, congestion avoidance, fast recovery."
          ]
        },
        {
          unit: 4,
          title: "Application Layer & Protocols",
          topics: [
            "Domain Name System (DNS) namespace and servers hierarchy.",
            "HTTP/HTTPS request-response architecture, persistent connections.",
            "Email: SMTP, POP3, IMAP protocols, MIME attachments.",
            "REST API design concepts, URI, HTTP method verb mappings."
          ]
        },
        {
          unit: 5,
          title: "Network Security & Cryptography",
          topics: [
            "Symmetric (AES) and Asymmetric (RSA) encryption models.",
            "Cryptographic hashing, Message Authentication Codes (MAC).",
            "Digital signatures, public key certificates, TLS/SSL handshake.",
            "IPsec architecture, Firewalls, Intrusion Detection Systems."
          ]
        }
      ],
      textbooks: [
        "Andrew S. Tanenbaum and David J. Wetherall, 'Computer Networks'.",
        "James F. Kurose and Keith W. Ross, 'Computer Networking: A Top-Down Approach'."
      ]
    }
  ],
  ECE: [
    {
      code: "EC301",
      title: "Electronic Circuits & Semiconductor Devices",
      credits: 4,
      semester: 3,
      units: [
        {
          unit: 1,
          title: "Semiconductor Physics & PN Diodes",
          topics: [
            "Energy bands, intrinsic vs extrinsic semiconductors, drift & diffusion current.",
            "PN Junction: Forward & reverse bias, diode current equations.",
            "Varactor diode, Tunnel diode, Schottky diode, Zener diode breakdown."
          ]
        },
        {
          unit: 2,
          title: "Bipolar Junction Transistors",
          topics: [
            "BJT configurations: CB, CE, CC input & output static curves.",
            "Biasing methods: Fixed bias, collector-to-base, voltage divider bias.",
            "Q-point stabilization, thermal runaway prevention, thermal resistance."
          ]
        },
        {
          unit: 3,
          title: "JFET & MOSFET Devices",
          topics: [
            "JFET characteristics, pinch-off voltage, transconductance.",
            "MOSFET: Enhancement vs depletion mode operations, threshold voltage equations.",
            "Short-channel effects, MOSFET small signal equivalent models."
          ]
        },
        {
          unit: 4,
          title: "Small Signal Amplifiers",
          topics: [
            "h-parameter representation of BJT CE, CB, CC configurations.",
            "Small signal low-frequency model of MOSFET CS, CD, CG amplifiers.",
            "Calculation of Av, Ai, Zi, and Zo values, frequency response curves."
          ]
        },
        {
          unit: 5,
          title: "Power & Tuned Amplifiers",
          topics: [
            "Power amplifiers: Class A, B, AB, C, D efficiency limits.",
            "Push-Pull complementary symmetry amplifiers, crossover distortion.",
            "Single-tuned, double-tuned capacitive-coupled tuned amplifiers."
          ]
        }
      ],
      textbooks: [
        "Robert L. Boylestad and Louis Nashelsky, 'Electronic Devices and Circuit Theory'.",
        "Jacob Millman and Christos Halkias, 'Electronic Devices and Circuits'."
      ]
    }
  ],
  MECH: [
    {
      code: "ME301",
      title: "Engineering Thermodynamics",
      credits: 4,
      semester: 3,
      units: [
        {
          unit: 1,
          title: "First Law of Thermodynamics",
          topics: [
            "Thermodynamic state, properties, process, cyclic configurations.",
            "First Law applied to non-flow processes (Isothermal, adiabatic, polytropic).",
            "Steady Flow Energy Equation (SFEE) applied to nozzles and turbines."
          ]
        },
        {
          unit: 2,
          title: "Second Law & Entropy",
          topics: [
            "Kelvin-Planck and Clausius statements, Carnot cycle efficiency.",
            "Clausius inequality, entropy changes of ideal gases.",
            "Exergy availability, dead state, irreversibility calculations."
          ]
        },
        {
          unit: 3,
          title: "Pure Substances & Steam Cycles",
          topics: [
            "Phase change diagrams of water (P-V, T-s, h-s Mollier).",
            "Vapor power Rankine cycle, reheat and regenerative feed heating.",
            "Supercritical power cycle configurations, binary vapor cycles."
          ]
        },
        {
          unit: 4,
          title: "Gas Power Cycles",
          topics: [
            "Air standard Otto cycle, Diesel cycle, Dual combustion cycles.",
            "Gas turbine Brayton cycle with regeneration, intercooling.",
            "Morse test for multi-cylinder IC engine performance."
          ]
        },
        {
          unit: 5,
          title: "Psychrometry & Refrigeration",
          topics: [
            "Psychrometric charts, sensible heating, cooling dehumidification.",
            "Vapor Compression Refrigeration System (VCRS) cycle math.",
            "Vapor Absorption Refrigeration System (VARS) overview."
          ]
        }
      ],
      textbooks: [
        "Yunus A. Cengel and Michael A. Boles, 'Thermodynamics: An Engineering Approach'.",
        "P.K. Nag, 'Engineering Thermodynamics', Tata McGraw-Hill."
      ]
    }
  ]
};

export default comprehensiveDetailedCoursesData;
