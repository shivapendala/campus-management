"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 15

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for MECH and CIVIL courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED_V13: Dict[str, Dict[str, Any]] = {
    "ME801": {
        "code": "ME801",
        "title": "Mechanical Vibrations",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Mechanical Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Single Degree of Freedom Systems - Free Vibrations",
                "topics": [
                    "Introduction to vibrations, simple harmonic motion, elements of vibratory systems.",
                    "Undamped free vibrations: Newton's method, energy method, Rayleigh's method.",
                    "Damped free vibrations: Viscous damping, underdamped, overdamped, critically damped systems, logarithmic decrement.",
                    "Coulomb damping, dry friction vibration models."
                ]
            },
            {
                "unit": 2,
                "title": "Single Degree of Freedom Systems - Forced Vibrations",
                "topics": [
                    "Forced vibration with harmonic excitation, steady-state response, magnification factor.",
                    "Vibration isolation and transmissibility, force transmissibility, motion transmissibility.",
                    "Rotating unbalance, whirling of rotating shafts, support motion excitation.",
                    "Vibration measuring instruments: Seismometer, accelerometer."
                ]
            },
            {
                "unit": 3,
                "title": "Two Degree of Freedom Systems",
                "topics": [
                    "Equations of motion for coordinate coupling, natural frequencies and mode shapes.",
                    "Coordinate systems, principal coordinates, orthogonal properties of modes.",
                    "Dynamic vibration absorber design, coordinate coupling transformations."
                ]
            },
            {
                "unit": 4,
                "title": "Multi-Degree of Freedom Systems",
                "topics": [
                    "Influence coefficients: Stiffness influence coefficients, flexibility influence coefficients.",
                    "Eigenvalue problem formulation, matrix iteration method for fundamental frequency.",
                    "Approximate methods: Dunkerley's equation, Rayleigh-Ritz method, Holzer's method for torsional vibrations."
                ]
            },
            {
                "unit": 5,
                "title": "Continuous Systems & Vibration Control",
                "topics": [
                    "Vibrations of continuous systems: Transverse vibration of a string, longitudinal vibration of a rod.",
                    "Torsional vibration of a shaft, lateral vibration of a beam.",
                    "Vibration dampers, active vibration control, industrial noise control standards."
                ]
            }
        ],
        "textbooks": [
            "Singiresu S. Rao, 'Mechanical Vibrations', Pearson Education, 6th Edition.",
            "G.K. Grover, 'Mechanical Vibrations', Nem Chand & Bros."
        ]
    },
    "CE802": {
        "code": "CE802",
        "title": "Advanced Design of Steel Structures",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Civil Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Plate Girders with Lateral Loading",
                "topics": [
                    "Design of gantry girders: Loads, forces, design parameters, deflection checks.",
                    "Plate girders: Web buckling under patch loading, design of end panels, tension field action.",
                    "Stiffeners design: Intermediate stiffeners, load-bearing stiffeners."
                ]
            },
            {
                "unit": 2,
                "title": "Industrial Buildings & Portals",
                "topics": [
                    "Design of industrial portal frames, braced and unbraced frames.",
                    "Columns under combined axial force and bending moments, design of column brackets.",
                    "Design of girts and purlins under wind loads."
                ]
            },
            {
                "unit": 3,
                "title": "Steel Water Tanks",
                "topics": [
                    "Design of elevated circular and rectangular steel water tanks, design of staging.",
                    "Wind forces and seismic forces calculations on steel water tanks."
                ]
            },
            {
                "unit": 4,
                "title": "Plastic Analysis & Design",
                "topics": [
                    "Plastic behavior of structural steel, plastic hinge concept, shape factors of sections.",
                    "Upper and lower bound theorems of plastic collapse.",
                    "Plastic analysis of continuous beams, single-bay portal frames, design parameters."
                ]
            },
            {
                "unit": 5,
                "title": "Light Gauge Steel Structures",
                "topics": [
                    "Introduction to cold-formed steel sections, types of sections, design specifications.",
                    "Local buckling of plates, effective width concept, design of light gauge tension and compression members."
                ]
            }
        ],
        "textbooks": [
            "N. Subramanian, 'Design of Steel Structures', Oxford University Press.",
            "S.K. Duggal, 'Limit State Design of Steel Structures', Tata McGraw-Hill."
        ]
    }
}
