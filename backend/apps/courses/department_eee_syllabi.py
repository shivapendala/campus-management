"""
EduCore Enterprise Framework - Department of Electrical & Electronics Engineering (EEE) Course Syllabi

Complete 5-unit syllabus specifications, learning outcomes, and laboratory manuals for EEE core courses:
- EE301: Electric Circuit Analysis & Network Synthesis
- EE302: DC Machines & Transformers
- EE401: AC Electrical Machines & Synchronous Drives
- EE402: Power Electronics & Industrial Drives
- EE501: Power System Analysis & Load Flow
- EE502: Control Systems Engineering & State Variable Models
- EE601: Power System Protection & Switchgear
- EE602: Renewable Energy Systems & Microgrid Dynamics
- EE701: High Voltage Engineering & Dielectric Testing
- EE702: Electric Vehicle Powertrain & Battery Management Systems
"""

from typing import Dict, List, Any

EEE_DEPARTMENT_COURSES_SPECIFICATION: Dict[str, Dict[str, Any]] = {
    "EE301": {
        "code": "EE301",
        "title": "Electric Circuit Analysis & Network Synthesis",
        "credits": 4,
        "regulation": "R23",
        "department": "Electrical & Electronics Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Basic Circuit Analysis & Network Topology",
                "hours": 9,
                "blooms": "L1_REMEMBER/L2_UNDERSTAND",
                "co": "CO1",
                "topics": "Review of KCL, KVL, and Ohm's Law, Independent and dependent voltage and current sources, Source transformation, Mesh and Nodal analysis with dependent and independent sources, Supermesh and Supernode techniques, Network Graph Theory concepts, Graph, Tree, Co-tree, Incidence matrix, Fundamental Cut-Set matrix, Fundamental Tie-Set matrix, Formulation of equilibrium equations on loop and node bases, Duality and dual networks."
            },
            {
                "unit": 2,
                "title": "Network Theorems for DC and AC Circuits",
                "hours": 9,
                "blooms": "L2_UNDERSTAND/L3_APPLY",
                "co": "CO2",
                "topics": "Linearly independent circuits, Superposition Theorem, Thevenin's Theorem, Norton's Theorem, Maximum Power Transfer Theorem for DC and AC sinusoidal steady-state circuits, Reciprocity Theorem, Millman's Theorem, Tellegen's Theorem, Substitution Theorem, Star-Delta and Delta-Star impedance transformations, Application of network theorems to circuits containing coupled inductors and operational amplifiers."
            },
            {
                "unit": 3,
                "title": "Transient Analysis in Time Domain & Laplace Domain",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO3",
                "topics": "Initial and final conditions in circuit elements (Resistor, Inductor, Capacitor), Differential equation approach for first-order RL and RC circuits, Zero-input response (ZIR), Zero-state response (ZSR), Step, Ramp, and Impulse responses, Second-order series and parallel RLC circuits, Overdamped, Critically damped, and Underdamped natural responses, Quality factor and damping ratio, Laplace Transform in circuit analysis, Transform impedance of R, L, and C elements, Solution of circuit differential equations using Laplace transform, Transfer functions of linear networks, Poles and Zeros in the s-plane."
            },
            {
                "unit": 4,
                "title": "AC Resonance & Magnetically Coupled Circuits",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO4",
                "topics": "Series Resonance, Resonant frequency, Impedance and admittance variations with frequency, Bandwidth, Selectivity, Quality factor (Q) of series resonant circuit, Half-power frequencies, Parallel Resonance (Anti-resonance), Dynamic resistance, Frequency response of parallel resonant circuits, Mutual inductance, Coefficient of coupling (k), Dot convention for coupled coils, Series and parallel connections of coupled coils, Conductively coupled equivalent circuits, Analysis of single-tuned and double-tuned coupled circuits, Ideal and practical linear transformers."
            },
            {
                "unit": 5,
                "title": "Two-Port Network Parameters & Synthesis of Driving-Point Functions",
                "hours": 9,
                "blooms": "L4_ANALYZE/L5_EVALUATE",
                "co": "CO5",
                "topics": "Two-port network representations, Impedance (Z) parameters, Admittance (Y) parameters, Transmission (ABCD) parameters, Inverse Transmission (A'B'C'D') parameters, Hybrid (h) parameters, Inverse Hybrid (g) parameters, Relationships and conversions between parameter sets, Interconnection of two-port networks (Series, Parallel, Cascade), Symmetrical and Reciprocal two-port networks, Image parameters, Characteristic impedance (Z0), Positive Real (PR) functions, Properties of PR functions, Synthesis of LC, RC, and RL driving-point immittance functions using Foster I, Foster II, Cauer I, and Cauer II canonical forms."
            }
        ],
        "textbooks": [
            "William H. Hayt, Jack E. Kemmerly, and Steven M. Durbin, 'Engineering Circuit Analysis', 9th Edition, McGraw-Hill, 2018.",
            "Charles K. Alexander and Matthew N.O. Sadiku, 'Fundamentals of Electric Circuits', 7th Edition, McGraw-Hill, 2021."
        ]
    }
}
