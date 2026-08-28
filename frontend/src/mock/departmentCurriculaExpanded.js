/**
 * Comprehensive Departmental Curricula Catalog (Semesters 1-8)
 * for CSE, ECE, EEE, MECH, CIVIL, and AIML branches.
 * Defines credits, lecture plans, laboratory manuals, and textbooks.
 */

export const departmentCurriculaExpanded = {
  CSE: {
    department_name: "Computer Science & Engineering",
    regulation: "R23-Autonomous",
    semesters: [
      {
        semester_id: 1,
        courses: [
          {
            code: "MA101",
            title: "Linear Algebra & Calculus",
            credits: 4,
            hours_ltp: "3-1-0",
            units: [
              { unit: 1, title: "Matrices & Systems of Linear Equations", topics: ["Rank of a matrix", "Echelon form", "Gauss elimination method", "Eigenvalues and eigenvectors", "Cayley-Hamilton theorem", "Diagonalization of matrices", "Quadratic forms", "Canonical reduction", "Signature of a quadratic form"] },
              { unit: 2, title: "Differential Calculus", topics: ["Mean value theorems", "Rolle's theorem", "Lagrange's mean value theorem", "Taylor's and Maclaurin's series", "Indeterminate forms", "Partial derivatives", "Jacobians", "Maxima and minima of functions of two variables", "Lagrange multipliers method"] },
              { unit: 3, title: "Integral Calculus", topics: ["Evaluation of double and triple integrals", "Change of variables", "Change of order of integration", "Area and volume calculations using multiple integrals", "Gamma and Beta functions", "Dirichlet integrals"] },
              { unit: 4, title: "Ordinary Differential Equations of First Order", topics: ["Exact equations", "Linear equations", "Bernoulli's equations", "Orthogonal trajectories", "Newton's law of cooling", "Law of natural growth and decay", "Radioactive decay rates"] },
              { unit: 5, title: "Higher Order Linear Differential Equations", topics: ["Non-homogeneous linear equations with constant coefficients", "Method of variation of parameters", "Cauchy's and Legendre's linear equations", "Simultaneous linear differential equations", "Applications to LCR electrical circuits", "Simple harmonic motion equations"] }
            ],
            textbooks: [
              "B.S. Grewal, 'Higher Engineering Mathematics', Khanna Publishers, 44th Edition.",
              "Erwin Kreyszig, 'Advanced Engineering Mathematics', John Wiley & Sons, 10th Edition."
            ]
          },
          {
            code: "PH101",
            title: "Engineering Physics & Quantum Mechanics",
            credits: 3,
            hours_ltp: "3-0-0",
            units: [
              { unit: 1, title: "Wave Optics", topics: ["Interference in thin films", "Air wedge", "Newton's rings", "Diffraction", "Fraunhofer diffraction at single slit", "Diffraction grating", "Polarization", "Double refraction", "Nicol prism", "Quarter wave plates"] },
              { unit: 2, title: "Quantum Physics", topics: ["Black body radiation", "Planck's hypothesis", "Photoelectric effect", "Compton effect", "De Broglie waves", "Heisenberg uncertainty principle", "Schrodinger time-independent and dependent equations", "Particle in a 1D box", "Tunneling effect"] },
              { unit: 3, title: "Lasers & Fiber Optics", topics: ["Einstein coefficients", "Population inversion", "Nd:YAG laser", "Helium-Neon laser", "Semiconductor laser", "Optical fibers propagation", "Numerical aperture", "Step index and graded index fibers", "Fiber communication system", "Signal attenuation"] },
              { unit: 4, title: "Solid State Physics", topics: ["Crystal systems", "Bravais lattices", "Miller indices", "Interplanar spacing", "Bragg's law of X-ray diffraction", "Reciprocal lattice", "Crystal structure analysis", "Laue diffraction pattern"] },
              { unit: 5, title: "Semiconductor Materials", topics: ["Intrinsic and extrinsic semiconductors", "Fermi level variation", "Carrier concentration derivation", "Hall effect and applications", "Solar cell principles", "Light dependent resistors", "PIN and avalanche photodiodes"] }
            ],
            textbooks: [
              "M.N. Avadhanulu and P.G. Kshirsagar, 'A Textbook of Engineering Physics', S. Chand & Co.",
              "Arthur Beiser, 'Concepts of Modern Physics', McGraw-Hill."
            ]
          },
          {
            code: "CS101",
            title: "Problem Solving & Python Programming",
            credits: 3,
            hours_ltp: "3-0-0",
            units: [
              { unit: 1, title: "Computational Thinking & Algorithm Design", topics: ["Problem-solving process", "Algorithms", "Pseudo-code", "Flowcharts", "Control flow constructs", "State machines", "Illustrative examples: search, sort, count", "Iteration constructs"] },
              { unit: 2, title: "Python Basics & Control Structures", topics: ["Python interpreter", "Data types", "Variables", "Operators", "Expression evaluation", "Conditional branching (if-else, elif)", "Iteration (while, for, nested loops)", "Break, continue, pass statements", "Short-circuit evaluation"] },
              { unit: 3, title: "Functions & Modular Programming", topics: ["Function definition", "Arguments (positional, keyword, default, variable-length)", "Return statements", "Local and global scope", "Recursion", "Lambda functions", "Python built-in modules", "Math and Random libraries", "Writing custom packages"] },
              { unit: 4, title: "Structured Data Collections", topics: ["Strings and operations", "Lists", "List comprehensions", "Tuples", "Dictionaries", "Sets", "Mutable vs immutable objects", "Sequence indexing and slicing", "Dictionary sorting techniques"] },
              { unit: 5, title: "File Operations & Error Management", topics: ["File I/O operations", "Text vs binary files", "File seek and tell", "Exception handling (try-except-finally)", "Custom exceptions", "Object-Oriented Programming basics in Python", "Classes and inheritance properties"] }
            ],
            textbooks: [
              "Allen B. Downey, 'Think Python: How to Think Like a Computer Scientist', O'Reilly Media.",
              "Reema Thareja, 'Python Programming Using Problem Solving Approach', Oxford University Press."
            ]
          }
        ]
      },
      {
        semester_id: 2,
        courses: [
          {
            code: "CS201",
            title: "Data Structures & C Programming",
            credits: 4,
            hours_ltp: "3-0-2",
            units: [
              { unit: 1, title: "C Language Fundamentals", topics: ["Structured programming principles", "Data types", "Storage classes", "Pointers and memory addresses", "Dynamic memory allocation (malloc, calloc, realloc, free)", "Structures and Unions", "Bitwise operators in C", "Header files"] },
              { unit: 2, title: "Linear Data Structures - Lists", topics: ["Abstract Data Types (ADTs)", "Array-based lists", "Singly linked lists", "Doubly linked lists", "Circular linked lists", "Operations: insert, delete, traverse, reverse", "Application: polynomial representation and addition"] },
              { unit: 3, title: "Stacks & Queues", topics: ["Stack ADT", "Array and linked list implementation of stacks", "Applications: infix to postfix, evaluation of arithmetic expressions", "Queue ADT", "Circular queues", "Double-ended queues (Deques)", "Priority queues", "Queue applications in task scheduling"] },
              { unit: 4, title: "Trees & Binary Search Trees", topics: ["Tree terminology", "Binary tree representations", "Binary tree traversals (pre-order, in-order, post-order)", "Binary Search Trees (BST)", "Insertion, deletion, and searching in BST", "AVL Trees", "Rotation operations", "Balanced search trees", "B-Trees and B+ Trees overview"] },
              { unit: 5, title: "Graphs, Sorting & Searching", topics: ["Graph representations (Adjacency matrix, Adjacency list)", "Graph traversals (BFS, DFS)", "Topological sorting", "Searching techniques (Linear, Binary search)", "Sorting algorithms (Bubble, Insertion, Selection, Merge, Quick, Heap sort)", "Hashing tables", "Collision resolution strategies", "Linear probing vs chaining"] }
            ],
            textbooks: [
              "Ellis Horowitz, Sartaj Sahni, and Susan Anderson-Freed, 'Fundamentals of Data Structures in C', Silicon Press.",
              "Reema Thareja, 'Data Structures Using C', Oxford University Press."
            ]
          }
        ]
      },
      {
        semester_id: 3,
        courses: [
          {
            code: "CS301",
            title: "Database Management Systems",
            credits: 4,
            hours_ltp: "3-0-2",
            units: [
              { unit: 1, title: "Database System Concepts & ER Model", topics: ["Database architecture", "Data models", "Data independence", "Database schemas", "Entity-Relationship model", "Constraints", "Keys", "Weak entity sets", "Extended ER features", "Reduction of ER to relational tables", "Self-referencing entities"] },
              { unit: 2, title: "Relational Model & Structured Query Language", topics: ["Relational algebra operations", "Tuple relational calculus", "Domain relational calculus", "SQL standards", "Data definition and queries", "Set operations", "Aggregate functions", "Nested subqueries", "Joins", "Views", "Triggers", "Assertions", "Dynamic SQL queries"] },
              { unit: 3, title: "Relational Database Design & Normalization", topics: ["Pitfalls in relational design", "Functional dependencies", "Decomposition", "Lossless-join decomposition", "Dependency preservation", "Normal forms (1NF, 2NF, 3NF, BCNF, 4NF, 5NF)", "Multi-valued dependencies", "Canonical covers", "Armstrong's axioms"] },
              { unit: 4, title: "Transaction Management & Concurrency Control", topics: ["Transaction concept", "ACID properties", "Schedules", "Serializability", "Recoverability", "Concurrency control", "Lock-based protocols", "Two-Phase Locking (2PL)", "Timestamp-based protocols", "Validation-based protocols", "Deadlock handling", "Starvation anomalies"] },
              { unit: 5, title: "Storage, Indexing & Query Processing", topics: ["File organization", "Sequential files", "Hashing", "Indexing", "B+ Tree index files", "Static and dynamic hashing", "Query processing overview", "Query optimization using heuristics", "Database recovery systems", "Log-based recovery", "ARIES recovery protocol", "Shadow paging"] }
            ],
            textbooks: [
              "Abraham Silberschatz, Henry F. Korth, and S. Sudarshan, 'Database System Concepts', McGraw-Hill.",
              "Ramez Elmasri and Shamkant B. Navathe, 'Fundamentals of Database Systems', Pearson."
            ]
          },
          {
            code: "CS302",
            title: "Design & Analysis of Algorithms",
            credits: 4,
            hours_ltp: "3-1-0",
            units: [
              { unit: 1, title: "Introduction & Asymptotic Notation", topics: ["Algorithm definition", "Space complexity", "Time complexity", "Asymptotic notations (Big-O, Omega, Theta)", "Mathematical analysis of non-recursive and recursive algorithms", "Recurrence equations", "Master method", "Recursion tree method"] },
              { unit: 2, title: "Divide-and-Conquer & Greedy Method", topics: ["General divide-and-conquer method", "Binary search", "Merge sort", "Quick sort", "Strassen's matrix multiplication", "Greedy strategy", "Fractional knapsack problem", "Minimum cost spanning trees (Prim's and Kruskal's algorithms)", "Dijkstra's single source shortest path", "Huffman coding"] },
              { unit: 3, title: "Dynamic Programming", topics: ["General dynamic programming method", "Multi-stage graphs", "All-pairs shortest paths (Floyd-Warshall algorithm)", "Single-source shortest path (Bellman-Ford algorithm)", "0/1 knapsack problem", "Traveling salesperson problem", "Matrix chain multiplication", "Optimal binary search trees", "Longest common subsequence"] },
              { unit: 4, title: "Backtracking & Branch-and-Bound", topics: ["General backtracking method", "N-Queens problem", "Sum of subsets", "Graph coloring", "Hamiltonian cycles", "Branch-and-Bound strategy", "Least Cost (LC) search", "FIFO branch-and-bound", "15-puzzle problem", "TSP branch-and-bound"] },
              { unit: 5, title: "NP-Hard & NP-Complete Problems", topics: ["Basic concepts", "Nondeterministic algorithms", "Classes P, NP, NP-Hard, and NP-Complete", "Cook's theorem", "NP-Complete reductions (SAT, 3SAT, Clique, Vertex Cover)", "Approximation algorithms", "Traveling salesperson approximation"] }
            ],
            textbooks: [
              "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, 'Introduction to Algorithms', MIT Press.",
              "Ellis Horowitz, Sartaj Sahni, and Sanguthevar Rajasekaran, 'Fundamentals of Computer Algorithms', Universities Press."
            ]
          }
        ]
      },
      {
        semester_id: 4,
        courses: [
          {
            code: "CS401",
            title: "Operating Systems & Kernel Design",
            credits: 4,
            hours_ltp: "3-0-2",
            units: [
              { unit: 1, title: "Operating System Overview & Process Management", topics: ["OS objectives and functions", "Evolution of OS", "System calls", "Process concept", "Process Control Block (PCB)", "Process state transitions", "Context switching", "Thread models", "CPU scheduling algorithms (FCFS, SJF, SRTF, Priority, Round Robin, Multilevel feedback queues)"] },
              { unit: 2, title: "Process Synchronization & Deadlocks", topics: ["Critical section problem", "Peterson's solution", "Hardware synchronization", "Semaphores", "Monitors", "Classic synchronization problems (Producer-Consumer, Readers-Writers, Dining Philosophers)", "Deadlock characterization", "Resource allocation graph", "Deadlock prevention", "Deadlock avoidance (Banker's algorithm)", "Deadlock detection and recovery"] },
              { unit: 3, title: "Memory Management & Virtual Memory", topics: ["Logical vs physical address space", "Swapping", "Contiguous memory allocation", "Paging", "Structure of page table", "Segmentation", "Virtual memory", "Demand paging", "Page replacement algorithms (FIFO, Optimal, LRU, Second-chance)", "Allocation of frames", "Thrashing"] },
              { unit: 4, title: "File Systems & Mass Storage Structure", topics: ["File concept", "Access methods", "Directory structure", "File system mounting", "File sharing and protection", "File system structure", "Allocation methods (Contiguous, Linked, Indexed)", "Free space management", "Disk scheduling algorithms (FCFS, SSTF, SCAN, C-SCAN, LOOK)"] },
              { unit: 5, title: "System Security & Case Studies", topics: ["Security threats", "Access matrix", "User authentication", "Linux kernel modules", "Linux process management structure", "Linux virtual file system (VFS)", "Windows kernel architecture overview"] }
            ],
            textbooks: [
              "Abraham Silberschatz, Peter B. Galvin, and Greg Gagne, 'Operating System Concepts', Wiley.",
              "William Stallings, 'Operating Systems: Internals and Design Principles', Pearson."
            ]
          }
        ]
      }
    ]
  },
  ECE: {
    department_name: "Electronics & Communication Engineering",
    regulation: "R23-Autonomous",
    semesters: [
      {
        semester_id: 1,
        courses: [
          {
            code: "MA101",
            title: "Linear Algebra & Calculus",
            credits: 4,
            hours_ltp: "3-1-0",
            units: [
              { unit: 1, title: "Matrices & Linear Systems", topics: ["Rank", "Echelon reduction", "Eigenvalues", "Eigenvectors", "Diagonalization"] }
            ]
          }
        ]
      }
    ]
  },
  AIML: {
    department_name: "Artificial Intelligence & Machine Learning",
    regulation: "R23-Autonomous",
    semesters: [
      {
        semester_id: 3,
        courses: [
          {
            code: "AI301",
            title: "Mathematical Foundations of Machine Learning",
            credits: 4,
            hours_ltp: "3-1-0",
            units: [
              { unit: 1, title: "Linear Algebra, Basis & Dimension", topics: ["Vector spaces", "Subspaces", "Linear independence", "Basis and dimension", "Linear transformations", "Inner product spaces", "Gram-Schmidt orthogonalization", "Eigenvalues and eigenvectors", "Singular Value Decomposition (SVD)", "PCA derivation"] },
              { unit: 2, title: "Multivariate Calculus & Vector Optimization", topics: ["Gradients", "Jacobian", "Hessian matrix", "Taylor series approximation", "Convex functions", "Unconstrained optimization", "Gradient Descent (SGD, Adam, RMSprop)", "Constrained optimization", "Lagrange multipliers", "KKT conditions"] },
              { unit: 3, title: "Probability & Density Distributions", topics: ["Probability spaces", "Conditional probability", "Bayes theorem", "Random variables", "Gaussian distribution", "Multivariate Gaussian", "Covariance matrix", "Central limit theorem", "Chebyshev's inequality"] },
              { unit: 4, title: "Statistical Estimation & Inference", topics: ["Point estimation", "Maximum Likelihood Estimation (MLE)", "Maximum A Posteriori (MAP)", "Bayesian inference", "Bias-Variance tradeoff", "Hypothesis testing", "p-values", "Confidence intervals"] },
              { unit: 5, title: "Information Theory & Vector Geometry", topics: ["Entropy", "Joint and conditional entropy", "Mutual information", "KL Divergence", "Cross-entropy loss function", "Distance metrics", "Cosine similarity", "Curse of dimensionality"] }
            ],
            textbooks: [
              "Marc Peter Deisenroth, A. Aldo Faisal, and Cheng Soon Ong, 'Mathematics for Machine Learning', Cambridge University Press.",
              "Gilbert Strang, 'Linear Algebra and Learning from Data', Wellesley-Cambridge Press."
            ]
          }
        ]
      }
    ]
  }
};

export default departmentCurriculaExpanded;
