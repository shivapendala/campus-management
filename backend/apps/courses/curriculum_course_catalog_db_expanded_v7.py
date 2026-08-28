"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 8

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for EEE, CIVIL, and MECH courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED_V7: Dict[str, Dict[str, Any]] = {
    "EE502": {
        "code": "EE502",
        "title": "Control Systems Engineering",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Electrical & Electronics Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Control System Modeling",
                "topics": [
                    "Introduction to control systems, open loop and closed loop systems.",
                    "Mathematical modeling of physical systems: Differential equations of translational and rotational mechanical systems.",
                    "Electrical systems, transfer function, block diagram reduction techniques.",
                    "Signal Flow Graph (SFG), Mason's gain formula and applications."
                ]
            },
            {
                "unit": 2,
                "title": "Time Response Analysis",
                "topics": [
                    "Standard test signals: Step, ramp, parabolic, impulse.",
                    "Time response of first-order systems, transient response of second-order systems.",
                    "Time domain specifications: Delay time, rise time, peak time, settling time, peak overshoot.",
                    "Steady-state errors, error constants (Kp, Kv, Ka) for Type 0, 1, 2 systems.",
                    "Effects of proportional, integral, and derivative (PID) control actions."
                ]
            },
            {
                "unit": 3,
                "title": "Stability in Time Domain",
                "topics": [
                    "Concept of stability, absolute, relative, and conditional stability.",
                    "Routh-Hurwitz stability criterion: Necessary and sufficient conditions, special cases.",
                    "Root Locus technique: Rules for construction of root loci, determination of stability from root locus."
                ]
            },
            {
                "unit": 4,
                "title": "Frequency Response Analysis",
                "topics": [
                    "Frequency domain specifications: Resonant peak, resonant frequency, bandwidth.",
                    "Bode plots: Determination of gain margin, phase margin, and stability.",
                    "Polar plots, Nyquist stability criterion, relative stability using Nyquist plot."
                ]
            },
            {
                "unit": 5,
                "title": "State Variable Analysis",
                "topics": [
                    "State space representation of continuous-time systems: State equations, state transition matrix.",
                    "Computation of state transition matrix, transfer function from state model.",
                    "Concepts of controllability and observability: Kalman's and Gilbert's tests.",
                    "State feedback controller design, pole placement techniques."
                ]
            }
        ],
        "textbooks": [
            "I.J. Nagrath and M. Gopal, 'Control Systems Engineering', New Age International.",
            "Benjamin C. Kuo, 'Automatic Control Systems', John Wiley & Sons."
        ]
    },
    "CE601": {
        "code": "CE601",
        "title": "Design of Steel Structures",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Civil Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Structural Fasteners",
                "topics": [
                    "Properties of structural steel, rolled steel sections, limit state design philosophy.",
                    "Bolted connections: Types of bolts, behavior of bolted joints, design of strength of joint, efficiency.",
                    "Welded connections: Types and behavior of welds, design of fillet and butt welds, eccentric connections."
                ]
            },
            {
                "unit": 2,
                "title": "Tension Members",
                "topics": [
                    "Behavior of tension members, modes of failure: yielding of gross section, rupture of critical section, block shear.",
                    "Design of plate and angle tension members, lug angles application."
                ]
            },
            {
                "unit": 3,
                "title": "Compression Members",
                "topics": [
                    "Elastic buckling of columns, Euler's formula, effective length configurations.",
                    "Design of compression members, built-up columns, design of lacings and battens.",
                    "Design of column bases: Slab base, gusseted base design."
                ]
            },
            {
                "unit": 4,
                "title": "Flexural Members & Beams",
                "topics": [
                    "Behavior of beams in bending, plastic moment capacity, lateral torsional buckling.",
                    "Design of laterally supported and laterally unsupported beams, built-up beams.",
                    "Web buckling, web crippling, design of bearing plates."
                ]
            },
            {
                "unit": 5,
                "title": "Plate Girders & Roof Trusses",
                "topics": [
                    "Plate girder components: Web, flange, stiffeners (bearing, intermediate, longitudinal).",
                    "Design of plate girders under bending and shear limit states.",
                    "Roof trusses: Loads, design of purlins, design of truss members."
                ]
            }
        ],
        "textbooks": [
            "N. Subramanian, 'Design of Steel Structures', Oxford University Press.",
            "S.K. Duggal, 'Limit State Design of Steel Structures', Tata McGraw-Hill."
        ]
    }
}
