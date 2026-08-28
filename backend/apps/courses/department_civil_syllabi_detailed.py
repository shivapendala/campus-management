"""
EduCore Enterprise Framework - Department of Civil Engineering (CIVIL) Detailed Course Syllabi

Complete 5-unit syllabus specifications, learning outcomes, and textbooks for advanced CIVIL courses:
- CE401: Structural Analysis (SA)
- CE501: Design of Reinforced Concrete Structures (DRCS)
- CE502: Geotechnical Engineering (GTE)
- CE601: Design of Steel Structures (DSS)
- CE602: Environmental Engineering (EE)
- CE701: Transportation Engineering (TE)
"""

from typing import Dict, Any

CIVIL_DETAILED_COURSES_CATALOG: Dict[str, Dict[str, Any]] = {
    "CE401": {
        "code": "CE401",
        "title": "Structural Analysis",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Energy Theorems & Deflections of Pin-Jointed Frames",
                "topics": [
                    "Strain energy and complementary energy, Castigliano's theorems for deflections",
                    "Principle of virtual work, unit load method for deflections of beams, frames, and trusses",
                    "Williot-Mohr diagram for truss deflections, Maxwell's reciprocal theorem",
                    "Betti's law, application of energy methods to statically determinate structures"
                ]
            },
            {
                "unit": 2,
                "title": "Influence Lines & Moving Loads",
                "topics": [
                    "Concept of influence lines, influence lines for shear force and bending moment in simply supported beams",
                    "Influence lines for forces in members of pin-jointed trusses",
                    "Moving loads: Maximum bending moment and shear force curves for single point load, UDL, and series of wheel loads",
                    "Muller-Breslau principle and its application to continuous beams"
                ]
            },
            {
                "unit": 3,
                "title": "Arches and Suspension Bridges",
                "topics": [
                    "Analysis of three-hinged and two-hinged arches (parabolic and circular arches)",
                    "Temperature effects, rib shortening, and yielding of supports in arches",
                    "Suspension cables: Tension, length of cable, anchor cables, forces on support towers",
                    "Three-hinged stiffening girder suspension bridges, shear force and bending moment diagrams"
                ]
            },
            {
                "unit": 4,
                "title": "Displacement Methods: Slope Deflection & Moment Distribution",
                "topics": [
                    "Slope-deflection equations, formulation and application to continuous beams and portal frames",
                    "Sway and non-sway analysis of frames using slope deflection method",
                    "Moment distribution method: Stiffness, carry-over factor, distribution factors",
                    "Analysis of continuous beams, portal frames with and without side sway, symmetrical and asymmetrical frames"
                ]
            },
            {
                "unit": 5,
                "title": "Matrix Methods of Structural Analysis",
                "topics": [
                    "Introduction to flexibility and stiffness matrices, static and kinematic indeterminacy",
                    "Element coordinate system, global coordinate system, transformation matrix",
                    "Analysis of continuous beams, pin-jointed trusses, and rigid frames using stiffness matrix method",
                    "Implementation of boundary conditions, node load vectors, and reactions"
                ]
            }
        ],
        "textbooks": [
            "C.S. Reddy, 'Basic Structural Analysis', Tata McGraw-Hill, 3rd Edition.",
            "Devdas Menon, 'Structural Analysis', Narosa Publishing House, 2nd Edition."
        ]
    },
    "CE501": {
        "code": "CE501",
        "title": "Design of Reinforced Concrete Structures",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Limit State Design Philosophy",
                "topics": [
                    "Design philosophies: Working Stress Method, Ultimate Load Method, Limit State Method",
                    "UGC and IS 456 recommendations, characteristic strength, safety factors for materials and loads",
                    "Stress-strain curves for concrete and steel, design stress block parameters",
                    "Limit state of collapse (flexure): Singly reinforced rectangular sections, design parameters and calculation of moment of resistance"
                ]
            },
            {
                "unit": 2,
                "title": "Doubly Reinforced & Flanged Beams",
                "topics": [
                    "Need for doubly reinforced sections, analysis and design of doubly reinforced rectangular beams",
                    "Flanged beams: T-beams and L-beams, effective width of flange, analysis and design of flanged beams under limit state of flexure",
                    "Curtailment of reinforcement, detailing of reinforcement in beams"
                ]
            },
            {
                "unit": 3,
                "title": "Limit State of Collapse (Shear, Torsion, Bond)",
                "topics": [
                    "Shear stress in reinforced concrete beams, diagonal tension, shear reinforcement design",
                    "Torsional resistance of RC members, combined bending, shear, and torsion analysis",
                    "Bond stress: Development length, anchorage bond, flexural bond, splicing of reinforcement",
                    "Limit state of serviceability: Control of deflection and cracking in beams according to IS 456"
                ]
            },
            {
                "unit": 4,
                "title": "Design of Slabs and Stairs",
                "topics": [
                    "Classification of slabs: One-way slab, two-way slab, continuous slab",
                    "Design and reinforcement detailing of one-way slabs and simply supported two-way slabs",
                    "Design of two-way slabs with boundary conditions (restrained slabs using IS code coefficients)",
                    "Design of dog-legged staircases, structural loading calculations and support detailing"
                ]
            },
            {
                "unit": 5,
                "title": "Design of Columns and Footings",
                "topics": [
                    "Types of columns, effective length, slenderness limits, short and long columns",
                    "Design of axially loaded short columns (rectangular and circular with helical reinforcement)",
                    "Short columns subjected to combined axial load and uniaxial bending (using SP-16 charts)",
                    "Types of footings, design of isolated square and rectangular footings for columns subjected to axial load"
                ]
            }
        ],
        "textbooks": [
            "N. Subramanian, 'Design of Reinforced Concrete Structures', Oxford University Press.",
            "S. Ramamrutham, 'Design of Reinforced Concrete Structures', Dhanpat Rai Publishing Company."
        ]
    }
}
