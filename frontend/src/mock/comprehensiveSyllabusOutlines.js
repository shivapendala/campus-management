/**
 * Comprehensive Course Syllabi and Session Plans for all departments
 * Mapped to UGC and NBA guidelines.
 */

export const comprehensiveSyllabusOutlines = {
  CSE: {
    semesters: [
      {
        semester: 1,
        courses: [
          {
            code: "CS101",
            title: "Programming in Python",
            units: [
              {
                unit: 1,
                title: "Introduction to Python and Algorithms",
                topics: [
                  "Computer basics, hardware components, CPU, memory, registers",
                  "Compiler, interpreter, assembler, linker loader definitions",
                  "Algorithmic design: Pseudo-code syntax and execution tracks",
                  "Flowchart notations: Start, end, input, process, decision",
                  "Variables, assignment statements, variable assignment order",
                  "Arithmetic operators: Add, subtract, multiply, divide, modulo",
                  "Relational operators: Less than, greater than, equal to, not equal",
                  "Logical operators: and, or, not logic gates truth tables",
                  "Bitwise operators: shift, and, or, xor operations"
                ],
                learning_objectives: "Understand computational principles and write basic arithmetic expressions in Python."
              },
              {
                unit: 2,
                title: "Control Flow and Iteration",
                topics: [
                  "Conditional selection: Single alternative (if), dual alternative (if-else)",
                  "Multiple choice selection (if-elif-else cascade structures)",
                  "Nested conditions: evaluation order, indentation rules",
                  "Loops: Indefinite iteration using while loop constructs",
                  "Definite iteration using for loop counters and range parameters",
                  "Iterating through ranges: start, stop, step index variations",
                  "Loop control modification: break to terminate, continue to skip",
                  "Pass statement as a syntactic placeholder",
                  "Infinite loops prevention, sentinel controlled variables"
                ],
                learning_objectives: "Apply conditional structures and loop iteration blocks to solve algorithmic problems."
              },
              {
                unit: 3,
                title: "Data Structures - Sequential Types",
                topics: [
                  "Strings: Immutable sequences, string creation, index tracking",
                  "String methods: lower, upper, split, strip, replace, format",
                  "Lists: Mutable sequence collection, list creation, list brackets",
                  "List operations: append, extend, insert, remove, pop, sort",
                  "List comprehension syntax: filters and maps on inline collections",
                  "Tuples: Immutable tuple collections, tuple packing and unpacking",
                  "Sets: Unique collections, union, intersection, difference, symmetric diff",
                  "Dictionaries: Key-value mapping pairs, dict creation, dict keys restriction",
                  "Iterating through dictionaries: items, values, keys methods"
                ],
                learning_objectives: "Utilize sequential structures, lists, tuples, sets, and dictionaries to manage datasets."
              },
              {
                unit: 4,
                title: "Functions and Recursion",
                topics: [
                  "Function definition: def keyword, function name, parameters",
                  "Function call, parameter mapping, positional vs keyword args",
                  "Default argument values, variable length positional arguments (*args)",
                  "Variable length keyword arguments (**kwargs) dictionary packaging",
                  "Scope of variables: local scope, global scope, global keyword",
                  "Return statements: single value, multiple value packaging",
                  "Recursion principles: base case condition, recursive reduction steps",
                  "Stack frames in recursion: visual simulation track",
                  "Lambda functions: anonymous single line calculations"
                ],
                learning_objectives: "Define modular functions, pass arguments, handle scopes, and write basic recursive logic."
              },
              {
                unit: 5,
                title: "File Input Output and Exceptions",
                topics: [
                  "File streams, opening files using open() function with modes",
                  "Read modes: 'r' for text, 'rb' for binary, read lines, chunked reads",
                  "Write modes: 'w' to overwrite, 'a' to append text data",
                  "Context managers: with statement auto-close guarantees",
                  "Exception Handling: exception definition, try block safety",
                  "Catching errors: except block execution, catching specific error types",
                  "Error recovery: finally block execution, else block execution",
                  "Raising exceptions explicitly: raise statement",
                  "Custom Exception Classes: deriving from Exception base"
                ],
                learning_objectives: "Implement file reading and writing streams, and gracefully recover from execution errors."
              }
            ],
            textbooks: [
              "Robert Sedgewick, Kevin Wayne, and Robert Dondero, 'Introduction to Programming in Python', Addison-Wesley.",
              "Charles Severance, 'Python for Everybody: Exploring Data Using Python 3'."
            ]
          }
        ]
      },
      {
        semester: 2,
        courses: [
          {
            code: "CS201",
            title: "Data Structures in C",
            units: [
              {
                unit: 1,
                title: "Arrays, Pointers, and Structures",
                topics: [
                  "Pointers basic concepts, pointer arithmetic, double pointers",
                  "Dynamic memory management: malloc, calloc, realloc, free functions",
                  "Structures, arrays of structures, nested structures definition",
                  "Self-referential structures: nodes configuration for linked lists",
                  "Arrays: 1D and 2D arrays addressing formulas, row-major, column-major"
                ],
                learning_objectives: "Master C pointer mechanics and dynamic memory structures."
              },
              {
                unit: 2,
                title: "Linked Lists ADT",
                topics: [
                  "Abstract Data Types (ADTs) concepts and linear list structures",
                  "Singly linked list: node declaration, insertion at head, tail, middle",
                  "Singly linked list: deletion of nodes, searching, forward/reverse traversal",
                  "Doubly linked list: prev and next pointers configuration, insertion/deletion",
                  "Circular linked lists: boundary checks, loop detection algorithms"
                ],
                learning_objectives: "Construct list models and manage memory nodes dynamically."
              },
              {
                unit: 3,
                title: "Stacks and Queues ADT",
                topics: [
                  "Stack ADT: LIFO principle, array representation, linked list implementation",
                  "Stack operations: push, pop, peek, check overflow and underflow",
                  "Stack applications: prefix, infix, postfix translations, bracket checking",
                  "Queue ADT: FIFO principle, simple queue array index adjustments",
                  "Circular queue: modulo math for empty and full status checks",
                  "Double Ended Queue (Deque) and Priority Queue representations"
                ],
                learning_objectives: "Implement stack and queue buffers to resolve expression and scheduling tasks."
              },
              {
                unit: 4,
                title: "Non-Linear Trees",
                topics: [
                  "Tree definition, parent, child, leaf, sibling, height, depth",
                  "Binary Tree representations: sequential array vs pointer linkages",
                  "Traversals: Recursive pre-order, in-order, post-order routes",
                  "Binary Search Tree (BST): insert, delete, search nodes characteristics",
                  "Balanced Trees: AVL tree rotation factors, single/double rotations"
                ],
                learning_objectives: "Build tree architectures and maintain height-balancing criteria."
              },
              {
                unit: 5,
                title: "Graphs and Sorting",
                topics: [
                  "Graph definition, directed vs undirected, weighted graphs",
                  "Representations: Adjacency Matrix and Adjacency List",
                  "Traversals: Breadth First Search (BFS) and Depth First Search (DFS)",
                  "Sorting: Bubble, Insertion, Selection, Quick, Merge, Heap sort",
                  "Searching: Linear search, Binary search on sorted lists",
                  "Hashing: Hash functions, collision resolution: probing, chaining"
                ],
                learning_objectives: "Traverse graphs and choose optimal search/sorting procedures."
              }
            ],
            textbooks: [
              "Ellis Horowitz, Sartaj Sahni, and Susan Anderson-Freed, 'Fundamentals of Data Structures in C'.",
              "Reema Thareja, 'Data Structures Using C', Oxford."
            ]
          }
        ]
      },
      {
        semester: 3,
        courses: [
          {
            code: "CS301",
            title: "Database Management Systems",
            units: [
              {
                unit: 1,
                title: "ANSI Architecture and ER Diagrams",
                topics: [
                  "Data vs Information, Database vs File Systems disadvantages",
                  "Three-Schema Architecture: external, conceptual, internal levels",
                  "Logical and Physical data independence definitions",
                  "ER Model: Entity, Attribute types, Relationship sets, Key flags",
                  "Cardinality constraints (1:1, 1:N, M:N), participation constraints",
                  "Reduction rules: Converting ER schemas to relational tables"
                ],
                learning_objectives: "Understand database schemas and convert ER models into relation models."
              },
              {
                unit: 2,
                title: "Relational Algebra and SQL",
                topics: [
                  "Relational algebra: Select, project, union, set difference, cartesian product",
                  "Relational joins: theta join, natural join, outer joins (left, right, full)",
                  "SQL DDL: CREATE, ALTER, DROP table statements with constraints",
                  "SQL DML: SELECT, INSERT, UPDATE, DELETE records, where filters",
                  "Complex queries: subqueries, correlated queries, EXISTS, IN operators",
                  "Aggregate functions: SUM, AVG, COUNT, MIN, MAX, GROUP BY, HAVING",
                  "Views, indexes creation, SQL triggers and functions definitions"
                ],
                learning_objectives: "Write relational algebra expressions and complex SQL database queries."
              },
              {
                unit: 3,
                title: "Normalization and Dependencies",
                topics: [
                  "Redundancy anomalies: Insertion, Update, Deletion anomalies",
                  "Functional Dependencies (FDs): closure of FD set, attribute closure",
                  "Armstrong's Axioms: reflexive, augmentation, transitive rules",
                  "First Normal Form (1NF) atomic values rule",
                  "Second Normal Form (2NF) partial dependency elimination",
                  "Third Normal Form (3NF) transitive dependency elimination",
                  "Boyce-Codd Normal Form (BCNF) strict determinant key rule",
                  "Lossless join decomposition, dependency preservation checks"
                ],
                learning_objectives: "Apply normalization rules to design optimal relational databases."
              },
              {
                unit: 4,
                title: "Transactions and Concurrency",
                topics: [
                  "Transaction concepts: ACID properties (Atomicity, Consistency, Isolation, Durability)",
                  "Transaction states: active, partially committed, committed, failed, aborted",
                  "Schedules: serial vs concurrent schedules, conflict serializability",
                  "Precedence graphs: cycles detection for non-serializable runs",
                  "Concurrency controls: Lock-based protocols, Shared/Exclusive locks",
                  "Two-Phase Locking (2PL): growing phase, shrinking phase, strict 2PL",
                  "Deadlock detection, recovery, wait-die and wound-wait schemes"
                ],
                learning_objectives: "Understand transaction states and concurrent execution scheduling protocols."
              },
              {
                unit: 5,
                title: "Storage and Crash Recovery",
                topics: [
                  "Physical disk storage organization, blocks, records allocation",
                  "Indexing: primary, secondary, clustered indexes comparison",
                  "B+ Tree Indexing: Node structural rules, search, insert, split actions",
                  "Database recovery: log-based recovery, deferred and immediate updates",
                  "Write-Ahead Logging (WAL) protocol rules, check-pointing",
                  "ARIES recovery algorithm: Analysis, Redo, Undo passes details"
                ],
                learning_objectives: "Explain storage indexing systems and crash recovery algorithms."
              }
            ],
            textbooks: [
              "Abraham Silberschatz, Henry F. Korth, and S. Sudarshan, 'Database System Concepts', McGraw-Hill.",
              "Raghu Ramakrishnan and Johannes Gehrke, 'Database Management Systems', McGraw-Hill."
            ]
          }
        ]
      },
      {
        semester: 4,
        courses: [
          {
            code: "CS401",
            title: "Operating Systems & Kernel Design",
            units: [
              {
                unit: 1,
                title: "OS System Architecture & Process Control",
                topics: [
                  "Monolithic, microkernel, layered and hybrid system structures",
                  "System calls interface, execution mode switching, user vs kernel space",
                  "Process states transition, Process Control Block (PCB) attributes",
                  "CPU scheduling algorithms: FCFS, SJF, Round Robin, priority queues",
                  "Multicore and multiprocessor scheduling challenges, load balancing"
                ],
                learning_objectives: "Explain operating system execution models and process context switching."
              },
              {
                unit: 2,
                title: "Semaphores and Threads Synchronization",
                topics: [
                  "Critical section problem, busy waiting, software Peterson's solution",
                  "Hardware test-and-set and compare-and-swap atomic operations",
                  "Mutex locks, binary and counting semaphores usage patterns",
                  "Classic concurrency cases: Bounded Buffer, Readers-Writers, Dining Philosophers",
                  "Deadlock handling: safety metrics, Bankers Banker algorithms, resource graphs"
                ],
                learning_objectives: "Design deadlock-free multi-threaded synchronization schemes."
              },
              {
                unit: 3,
                title: "Paging & Memory Allocation Slabs",
                topics: [
                  "Memory partitioning: internal fragmentation, external fragmentation",
                  "Paging ADT: page table structures, Translation Lookaside Buffer (TLB)",
                  "Multi-level page tables, inverted page tables, segmentation model",
                  "Virtual Memory: demand paging, Page Fault handler steps",
                  "Page replacement algorithms: FIFO, Optimal, LRU, Second-Chance"
                ],
                learning_objectives: "Configure virtual memory page tables and replacement criteria."
              },
              {
                unit: 4,
                title: "Virtual Filesystems & Storage Organization",
                topics: [
                  "File metadata, file control block structure, directory traversals",
                  "Disk sector layout, block allocation methods: contiguous, linked, indexed",
                  "Free-space bitmap tracker, FAT, UNIX inode structural analysis",
                  "Virtual Filesystem (VFS) redirection layer in Linux kernel",
                  "Disk scheduling queues: SSTF, SCAN, C-SCAN head movements"
                ],
                learning_objectives: "Analyze filesystem layouts and optimize physical disk head access trajectories."
              },
              {
                unit: 5,
                title: "Security Slabs & System Protection",
                topics: [
                  "Domain protection matrix, Access Control Lists (ACLs)",
                  "System threats: buffer overflows, privilege escalation exploits",
                  "Virtualization: hypervisors Type 1 & 2, sandboxing, Docker namespace separation",
                  "Case studies: UNIX process lifecycle model, Windows Kernel architecture"
                ],
                learning_objectives: "Configure access privilege tables and detail secure container boundaries."
              }
            ],
            textbooks: [
              "Abraham Silberschatz, Peter B. Galvin, and Greg Gagne, 'Operating System Concepts'.",
              "William Stallings, 'Operating Systems: Internals and Design Principles'."
            ]
          }
        ]
      },
      {
        semester: 5,
        courses: [
          {
            code: "CS501",
            title: "Computer Networks & Internet Protocols",
            units: [
              {
                unit: 1,
                title: "OSI Layering and MAC Protocols",
                topics: [
                  "OSI reference model vs TCP/IP suite layer alignments",
                  "Physical layer transmission, Manchester encoding, bandwidth restrictions",
                  "Data Link framing methods, character count, byte stuffing",
                  "Error checks: Hamming distance, Cyclic Redundancy Check (CRC) polynomial math",
                  "CSMA/CD collision detection, CSMA/CA collision avoidance rules"
                ],
                learning_objectives: "Explain physical signaling and MAC coordinate access frames."
              },
              {
                unit: 2,
                title: "IPv4/IPv6 Routing & Subnets",
                topics: [
                  "IPv4 header fields, Classless Inter-Domain Routing (CIDR) masks",
                  "Subnetting: calculating network, broadcast, and host range addresses",
                  "Routing protocols: distance vector RIP, link-state OSPF algorithms",
                  "Border Gateway Protocol (BGP) path-vector configuration",
                  "IPv6 transition: dual-stack, tunneling translation strategies"
                ],
                learning_objectives: "Calculate IP subnets and configure dynamic routing network graphs."
              },
              {
                unit: 3,
                title: "TCP Congestion Control & FlowSlabs",
                topics: [
                  "Transport layer ports, demultiplexing socket connections",
                  "User Datagram Protocol (UDP) lightweight header fields",
                  "Transmission Control Protocol (TCP) sliding window flow bounds",
                  "TCP handshake synchronization, state transitions table",
                  "Congestion controls: Slow Start, Congestion Avoidance, Fast Recovery"
                ],
                learning_objectives: "Trace TCP connection handshakes and congestion window adjustments."
              },
              {
                unit: 4,
                title: "Application Protocol Standards",
                topics: [
                  "Domain Name System (DNS) recursive vs iterative name resolution",
                  "HTTP request/response headers, persistent connections, HTTP/2 multiplexing",
                  "Email systems: SMTP relaying, POP3/IMAP retrieval processes",
                  "FTP active vs passive modes, socket configurations",
                  "Representational State Transfer (REST) architectural principles"
                ],
                learning_objectives: "Detail standard application layer payload exchanges."
              },
              {
                unit: 5,
                title: "Network Security & TLS Encryption",
                topics: [
                  "Public-key encryption (RSA), symmetric encryption (AES)",
                  "Cryptographic hash functions, Message Authentication Codes (MAC)",
                  "Digital Signatures, public key infrastructure, X.509 certificates",
                  "TLS/SSL handshake protocol steps, session key agreement",
                  "IPsec architecture: AH and ESP security protocols"
                ],
                learning_objectives: "Configure secure TLS sockets and verify digital certificate paths."
              }
            ],
            textbooks: [
              "Andrew S. Tanenbaum and David J. Wetherall, 'Computer Networks'.",
              "James F. Kurose and Keith W. Ross, 'Computer Networking: A Top-Down Approach'."
            ]
          }
        ]
      }
    ]
  }
};

export default comprehensiveSyllabusOutlines;
