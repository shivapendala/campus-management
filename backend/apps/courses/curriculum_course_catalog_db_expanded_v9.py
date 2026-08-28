"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 10

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for MECH and ECE courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED_V8: Dict[str, Dict[str, Any]] = {
    "ME501": {
        "code": "ME501",
        "title": "Design of Machine Elements",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Mechanical Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Design Philosophy & Simple Stresses",
                "topics": [
                    "Design process, design considerations, standards and codes, selection of materials.",
                    "Stress-strain relationships, direct, bending, and torsional shear stresses.",
                    "Factor of safety, design of components under static loads, theories of elastic failure.",
                    "Stress concentration: Causes, factors, mitigation methods.",
                    "Design of keys, cotter joints (socket and spigot, sleeve and cotter), knuckle joints."
                ]
            },
            {
                "unit": 2,
                "title": "Design of Shafts and Couplings",
                "topics": [
                    "Transmission shafts: Design under axial, bending, and torsional loads, combined loads.",
                    "Design of shafts based on strength and stiffness, ASME code for shaft design.",
                    "Keys: Types, design of rectangular, square, and woodruff keys.",
                    "Couplings: Rigid couplings (muff, split muff, flange couplings).",
                    "Flexible couplings: Bush-pin type flexible coupling design and safety parameters."
                ]
            },
            {
                "unit": 3,
                "title": "Design of Fasteners and Welded Joints",
                "topics": [
                    "Threaded fasteners: Bolt designations, initial tension, stresses in bolted joints.",
                    "Design of bolted joints under eccentric loading configurations.",
                    "Welded joints: Types of welded joints, strength of transverse and parallel fillet welds.",
                    "Design of eccentrically loaded welded joints, structural welding requirements."
                ]
            },
            {
                "unit": 4,
                "title": "Design of Springs and Knuckle Joints",
                "topics": [
                    "Helical springs: Terminology, stress deflection equations, Wahl factor.",
                    "Design of helical compression and tension springs under static and fatigue loads.",
                    "Leaf springs: Semi-elliptic leaf spring design, graduation of leaves, nipping.",
                    "Belleville springs, torsion springs overview."
                ]
            },
            {
                "unit": 5,
                "title": "Power Screws & Threaded Elements",
                "topics": [
                    "Power screws: Thread profiles (Square, Acme, Trapezoidal), torque requirements for lifting and lowering.",
                    "Self-locking and overhauling screws, efficiency of power screws.",
                    "Design of screw jack, differential screw jack mechanisms.",
                    "Stresses in power screws, wear and lubrication considerations."
                ]
            }
        ],
        "textbooks": [
            "V.B. Bhandari, 'Design of Machine Elements', Tata McGraw-Hill, 4th Edition.",
            "Joseph E. Shigley, 'Mechanical Engineering Design', McGraw-Hill, 10th Edition."
        ]
    },
    "EC301": {
        "code": "EC301",
        "title": "Electronic Circuits & Devices",
        "credits": 4,
        "ltp": "3-0-2",
        "department": "Electronics & Communication Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Semiconductor Physics & PN Diodes",
                "topics": [
                    "Energy bands in semiconductors, Intrinsic and extrinsic semiconductors, carrier concentrations.",
                    "Drift and diffusion currents, continuity equation, PN junction diode forward and reverse bias.",
                    "Diode current equation, transition and diffusion capacitances, reverse recovery time.",
                    "Zener diode breakdown mechanisms, tunnel diode, varactor diode, Schottky diode."
                ]
            },
            {
                "unit": 2,
                "title": "BJT Configurations & Biasing",
                "topics": [
                    "BJT physical structure and operation, CB, CE, CC configurations, input and output curves.",
                    "Transistor as an amplifier and switch, need for biasing, Q-point stabilization.",
                    "Biasing methods: Fixed bias, collector-to-base, voltage divider / self bias.",
                    "Thermal runaway, stability factors S, S', S'', thermal stabilization."
                ]
            },
            {
                "unit": 3,
                "title": "Field Effect Transistors",
                "topics": [
                    "JFET physical structure, pinch-off voltage, drain and transfer characteristics.",
                    "JFET small signal model, MOSFET: Enhancement and depletion mode operations.",
                    "Threshold voltage, output characteristics, subthreshold conduction, short-channel effects.",
                    "Comparison between BJT, JFET, and MOSFET parameters."
                ]
            },
            {
                "unit": 4,
                "title": "Low-Frequency Small Signal Amplifiers",
                "topics": [
                    "BJT hybrid (h-parameter) model, analysis of CE, CB, CC amplifiers.",
                    "Calculation of Av, Ai, Zi, Zo parameters using exact and approximate h-models.",
                    "MOSFET small signal low-frequency model, CS, CD, CG amplifiers analysis.",
                    "Biasing configurations of CS/CD amplifiers."
                ]
            },
            {
                "unit": 5,
                "title": "Power and Tuned Amplifiers",
                "topics": [
                    "Power amplifier classification: Class A, B, AB, C, D efficiency limits.",
                    "Transformer-coupled Class A amplifier, Class B push-pull and complementary symmetry.",
                    "Crossover distortion, heat sinks, tuned amplifiers: Single-tuned and double-tuned designs."
                ]
            }
        ],
        "textbooks": [
            "Robert L. Boylestad and Louis Nashelsky, 'Electronic Devices and Circuit Theory', Pearson.",
            "Jacob Millman and Christos Halkias, 'Electronic Devices and Circuits', Tata McGraw-Hill."
        ]
    }
}
