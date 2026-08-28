"""
EduCore Enterprise Framework - Department of Computer Science & Engineering (CSE) Detailed Course Syllabi

Complete 5-unit syllabus specifications, learning outcomes, and textbooks for advanced CSE courses:
- CS501: Computer Networks (CN)
- CS502: Compiler Design (CD)
- CS601: Software Engineering (SE)
- CS701: Cloud Computing (CC)
"""

from typing import Dict, Any

CSE_DETAILED_COURSES_CATALOG: Dict[str, Dict[str, Any]] = {
    "CS501": {
        "code": "CS501",
        "title": "Computer Networks",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Physical Layer & Media Access",
                "topics": [
                    "Data communication components, network topologies, OSI 7-layer architecture, TCP/IP protocol suite",
                    "Transmission media: Guided (Twisted pair, Coaxial, Fiber optic) and Unguided (Radio, Microwave)",
                    "Data link framing, flow control (Stop-and-wait, Sliding window), error detection (CRC, Checksum)",
                    "Multiple access protocols: ALOHA, CSMA/CD, CSMA/CA, token ring, Ethernet standard frames"
                ]
            },
            {
                "unit": 2,
                "title": "Network Layer & Routing",
                "topics": [
                    "IP addressing schemes: Classful and Classless (CIDR) addressing, subnetting, supernetting",
                    "IPv4 header structure, IPv6 address format and header enhancements",
                    "Routing algorithms: Distance vector routing (RIP), Link state routing (OSPF), Path vector routing (BGP)",
                    "Address Resolution Protocol (ARP), DHCP, ICMP diagnostics, Network Address Translation (NAT)"
                ]
            },
            {
                "unit": 3,
                "title": "Transport Layer Protocols",
                "topics": [
                    "Transport layer services, port numbers, multiplexing and demultiplexing",
                    "User Datagram Protocol (UDP): Segment structure, connectionless transmission characteristics",
                    "Transmission Control Protocol (TCP): Connection establishment (3-way handshake), termination, segment format",
                    "TCP reliability, sliding window flow control, congestion control algorithms (Slow start, Congestion avoidance, Fast retransmit)"
                ]
            },
            {
                "unit": 4,
                "title": "Application Layer Services",
                "topics": [
                    "Domain Name System (DNS): Hierarchical namespace, name resolution process",
                    "HyperText Transfer Protocol (HTTP): Request/Response structure, persistent connections, HTTPS security wrapper",
                    "Mail protocols: SMTP, POP3, IMAP, File Transfer Protocol (FTP) active and passive modes",
                    "Peer-to-Peer file sharing systems, Bittorrent protocol mechanics"
                ]
            },
            {
                "unit": 5,
                "title": "Network Security & Cryptography",
                "topics": [
                    "Symmetric key cryptography (DES, AES), public key cryptography (RSA algorithm, mathematical foundations)",
                    "Cryptographic hash functions (MD5, SHA-256), digital signatures, certificates",
                    "Transport Layer Security (TLS/SSL), IPsec architecture, firewalls, Intrusion Detection Systems (IDS)"
                ]
            }
        ],
        "textbooks": [
            "Andrew S. Tanenbaum and David J. Wetherall, 'Computer Networks', Pearson, 5th Edition.",
            "Behrouz A. Forouzan, 'Data Communications and Networking', McGraw-Hill, 5th Edition."
        ]
    },
    "CS502": {
        "code": "CS502",
        "title": "Compiler Design",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Lexical Analysis",
                "topics": [
                    "Compiler structure, translation phases, front-end vs back-end compiler organization",
                    "Lexical analysis: Role of lexical analyzer, tokens, patterns, lexemes",
                    "Regular expressions, transition diagrams, finite automata (NFA, DFA), subset construction algorithm",
                    "Lexical analyzer generators: Lex / Flex utility specifications"
                ]
            },
            {
                "unit": 2,
                "title": "Syntax Analysis & Parsing",
                "topics": [
                    "Context-Free Grammars (CFG), parse trees, ambiguity, left recursion elimination, left factoring",
                    "Top-down parsing: Recursive descent parser, LL(1) parsing, computation of First and Follow sets",
                    "Bottom-up parsing: Shift-reduce parser, operator precedence parsing",
                    "LR parsing algorithms: SLR(1), Canonical LR(1), LALR(1) parser construction, Yacc utility"
                ]
            },
            {
                "unit": 3,
                "title": "Syntax-Directed Translation & Semantics",
                "topics": [
                    "Syntax-Directed Definitions (SDD), synthesized and inherited attributes, dependency graphs",
                    "Evaluation orders of SDDs, S-attributed and L-attributed definitions",
                    "Type systems, type checking, type equivalence, run-time environments, activation records"
                ]
            },
            {
                "unit": 4,
                "title": "Intermediate Code Generation",
                "topics": [
                    "Intermediate languages: Graphical representations, Syntax Trees, Directed Acyclic Graphs (DAG)",
                    "Three-address code formats: Quadruples, triples, indirect triples",
                    "Translation of expressions, Boolean expressions, short-circuit code generation, backpatching, control flow statements"
                ]
            },
            {
                "unit": 5,
                "title": "Code Optimization & Generation",
                "topics": [
                    "Principal sources of optimization: Loop optimization, common subexpression elimination, constant folding, dead-code elimination",
                    "Data flow analysis, basic blocks, flow graphs, register allocation and assignment, code generation design issues"
                ]
            }
        ],
        "textbooks": [
            "Alfred V. Aho, Monica S. Lam, Ravi Sethi, and Jeffrey D. Ullman, 'Compilers: Principles, Techniques, and Tools', Pearson, 2nd Edition.",
            "K.D. Cooper and Linda Torczon, 'Engineering a Compiler', Morgan Kaufmann, 2nd Edition."
        ]
    }
}
