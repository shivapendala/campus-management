"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 12

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for ECE courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED_V10: Dict[str, Dict[str, Any]] = {
    "EC302": {
        "code": "EC302",
        "title": "Network Analysis & Synthesis",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Electronics & Communication Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Basic Circuit Concepts & Loop Analysis",
                "topics": [
                    "Voltage and current sources, independent and dependent sources, Ohm's law, Kirchhoff's laws.",
                    "Mesh analysis and nodal analysis with dependent and independent sources, supermesh and supernode concepts.",
                    "Network graph theory: Graph, tree, co-tree, incidence matrix, basic loop and cut-set matrices.",
                    "Duality and dual networks, source transformations, star-delta transformations."
                ]
            },
            {
                "unit": 2,
                "title": "Circuit Theorems & AC Applications",
                "topics": [
                    "Superposition theorem, Thevenin's and Norton's theorems, maximum power transfer theorem.",
                    "Reciprocity theorem, Millman's theorem, Tellegen's theorem, substitution theorem.",
                    "Application of theorems to DC and AC steady-state circuits, operational amplifier circuits analysis."
                ]
            },
            {
                "unit": 3,
                "title": "Transient Analysis in Laplace Domain",
                "topics": [
                    "Transient response of RL, RC, and RLC circuits under DC and AC excitations, initial and final conditions.",
                    "Differential equation approach, Laplace transform method, step, ramp, and impulse response analysis.",
                    "S-plane representation, transfer functions, poles and zeros, stability definitions."
                ]
            },
            {
                "unit": 4,
                "title": "AC Resonance & Coupled Induction",
                "topics": [
                    "Series resonance: Bandwidth, quality factor, selectivty, half-power frequencies.",
                    "Parallel resonance: Tank circuit characteristics, dynamic impedance.",
                    "Coupled circuits: Self and mutual inductance, coefficient of coupling, dot convention.",
                    "Analysis of conductively coupled and magnetically coupled circuits, linear transformers."
                ]
            },
            {
                "unit": 5,
                "title": "Two-Port Parameters & Functions Synthesis",
                "topics": [
                    "Z, Y, ABCD, inverse ABCD, hybrid, and inverse hybrid parameters, parameter conversions.",
                    "Interconnection of two-port networks (series, parallel, cascade).",
                    "Positive Real (PR) functions, synthesis of driving point impedance functions using Foster and Cauer forms."
                ]
            }
        ],
        "textbooks": [
            "William H. Hayt, Jack E. Kemmerly, and Steven M. Durbin, 'Engineering Circuit Analysis', McGraw-Hill.",
            "Charles K. Alexander and Matthew N.O. Sadiku, 'Fundamentals of Electric Circuits', McGraw-Hill."
        ]
    },
    "EC303": {
        "code": "EC303",
        "title": "Signals & Systems",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Electronics & Communication Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Signal Classification & Operations",
                "topics": [
                    "Continuous-time and discrete-time signals: step, ramp, impulse, sinusoidal, exponential, signum, sinc functions.",
                    "Operations on signals: time shifting, scaling, reversal, amplitude scaling, addition, multiplication.",
                    "Signal classifications: periodic/aperiodic, even/odd, energy/power, deterministic/random."
                ]
            },
            {
                "unit": 2,
                "title": "Linear Time-Invariant Systems",
                "topics": [
                    "System properties: linearity, time-invariance, causality, stability, memory, invertibility.",
                    "Continuous-time LTI systems: convolution integral, impulse response representation.",
                    "Discrete-time LTI systems: convolution sum, evaluation of linear convolution."
                ]
            },
            {
                "unit": 3,
                "title": "Fourier Analysis of Continuous-Time Signals",
                "topics": [
                    "Fourier series representation of periodic signals, trigonometric and exponential forms.",
                    "Continuous-Time Fourier Transform (CTFT): Dirichlet conditions, properties, Fourier transform of standard signals.",
                    "Frequency response of LTI systems, filtering, modulation theorem."
                ]
            },
            {
                "unit": 4,
                "title": "Laplace Transform & System Stability",
                "topics": [
                    "Laplace transform: definition, Region of Convergence (ROC), properties, inverse Laplace transform.",
                    "Analysis of LTI systems using Laplace transform, system transfer function, stability criteria."
                ]
            },
            {
                "unit": 5,
                "title": "Z-Transform & Discrete-Time Analysis",
                "topics": [
                    "Z-transform: definition, Region of Convergence (ROC) properties, inverse Z-transform.",
                    "Analysis of discrete-time LTI systems using Z-transform, system transfer function, pole-zero mapping."
                ]
            }
        ],
        "textbooks": [
            "Alan V. Oppenheim, Alan S. Willsky, and S. Hamid Nawab, 'Signals and Systems', Pearson.",
            "Simon Haykin and Barry Van Veen, 'Signals and Systems', John Wiley & Sons."
        ]
    }
}
