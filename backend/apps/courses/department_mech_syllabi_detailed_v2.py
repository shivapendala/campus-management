"""
EduCore Framework - Department of Mechanical Engineering (MECH) Detailed Course Syllabi v2

Complete 5-unit syllabus specifications, learning outcomes, and textbooks for advanced MECH courses:
- ME501: Design of Machine Elements (DME)
- ME601: Finite Element Analysis (FEA)
"""

from typing import Dict, Any

MECH_DETAILED_COURSES_CATALOG_V2: Dict[str, Dict[str, Any]] = {
    "ME501": {
        "code": "ME501",
        "title": "Design of Machine Elements",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Design Philosophy & Simple Stresses",
                "topics": [
                    "Design process, design considerations, standards and codes, selection of materials",
                    "Stress-strain relationships, direct, bending, and torsional shear stresses",
                    "Factor of safety, design of components under static loads, theories of elastic failure",
                    "Stress concentration: Causes, factors, mitigation methods",
                    "Design of keys, cotter joints (socket and spigot, sleeve and cotter), knuckle joints"
                ]
            },
            {
                "unit": 2,
                "title": "Design of Shafts and Couplings",
                "topics": [
                    "Transmission shafts: Design under axial, bending, and torsional loads, combined loads",
                    "Design of shafts based on strength and stiffness, ASME code for shaft design",
                    "Keys: Types, design of rectangular, square, and woodruff keys",
                    "Couplings: Rigid couplings (muff, split muff, flange couplings)",
                    "Flexible couplings: Bush-pin type flexible coupling design and safety parameters"
                ]
            },
            {
                "unit": 3,
                "title": "Design of Fasteners and Welded Joints",
                "topics": [
                    "Threaded fasteners: Bolt designations, initial tension, stresses in bolted joints",
                    "Design of bolted joints under eccentric loading configurations",
                    "Welded joints: Types of welded joints, strength of transverse and parallel fillet welds",
                    "Design of eccentrically loaded welded joints, structural welding requirements"
                ]
            },
            {
                "unit": 4,
                "title": "Design of Springs and Knuckle Joints",
                "topics": [
                    "Helical springs: Terminology, stress deflection equations, Wahl factor",
                    "Design of helical compression and tension springs under static and fatigue loads",
                    "Leaf springs: Semi-elliptic leaf spring design, graduation of leaves, nipping",
                    "Belleville springs, torsion springs overview"
                ]
            },
            {
                "unit": 5,
                "title": "Power Screws & Threaded Elements",
                "topics": [
                    "Power screws: Thread profiles (Square, Acme, Trapezoidal), torque requirements for lifting and lowering",
                    "Self-locking and overhauling screws, efficiency of power screws",
                    "Design of screw jack, differential screw jack mechanisms",
                    "Stresses in power screws, wear and lubrication considerations"
                ]
            }
        ],
        "textbooks": [
            "V.B. Bhandari, 'Design of Machine Elements', Tata McGraw-Hill, 4th Edition.",
            "Joseph E. Shigley, 'Mechanical Engineering Design', McGraw-Hill, 10th Edition."
        ]
    },
    "ME601": {
        "code": "ME601",
        "title": "Finite Element Analysis",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Fundamental Concepts",
                "topics": [
                    "Historical background, basic steps in finite element method",
                    "Stresses and equilibrium, boundary conditions, strain-displacement relations",
                    "Rayleigh-Ritz method, Galerkin method, weighted residual techniques",
                    "Variational formulation, minimum potential energy principle"
                ]
            },
            {
                "unit": 2,
                "title": "One-Dimensional Problems",
                "topics": [
                    "Bar element: Coordinates, shape functions, stiffness matrix derivation, load vector",
                    "Assembly of global stiffness matrix and load vector, boundary conditions (elimination and penalty methods)",
                    "Quadratic shape functions, temperature effects in 1D bar elements",
                    "Truss element: Transformation matrix, local and global coordinates, stiffness matrix for plane trusses"
                ]
            },
            {
                "unit": 3,
                "title": "Two-Dimensional CST & LST Elements",
                "topics": [
                    "Constant Strain Triangle (CST) element: Shape functions, strain-displacement matrix (B), stiffness matrix",
                    "Linear Strain Triangle (LST) element overview, plane stress and plane strain conditions",
                    "Axisymmetric elements: Formulation, stiffness matrix, load vectors for axisymmetric bodies"
                ]
            },
            {
                "unit": 4,
                "title": "Beams & Isoparametric Formulations",
                "topics": [
                    "Beam element: Hermite shape functions, stiffness matrix derivation, load vectors for UDL and point loads",
                    "Isoparametric elements: Natural coordinates, quadrilaterals, shape functions, Jacobian matrix",
                    "Numerical integration: Gauss quadrature evaluation for 1D and 2D integrals"
                ]
            },
            {
                "unit": 5,
                "title": "Dynamic Analysis & Heat Transfer",
                "topics": [
                    "Mass matrices: Consistent and lumped mass matrices, eigen value problems, natural frequencies",
                    "One-dimensional steady-state heat conduction: Formulation, stiffness matrix, boundary conditions",
                    "Fin heat transfer analysis using FEM, transient heat transfer overview",
                    "FEA software integration: Mesh generation, pre-processing, post-processing paradigms"
                ]
            }
        ],
        "textbooks": [
            "Tirupathi R. Chandrupatla and Ashok D. Belegundu, 'Introduction to Finite Elements in Engineering', Pearson.",
            "David V. Hutton, 'Fundamentals of Finite Element Analysis', Tata McGraw-Hill."
        ]
    }
}
