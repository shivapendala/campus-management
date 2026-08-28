"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 13

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for MECH and ECE courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED_V11: Dict[str, Dict[str, Any]] = {
    "ME303": {
        "code": "ME303",
        "title": "Fluid Mechanics & Hydraulic Machinery",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Mechanical Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Fluid Properties & Statics",
                "topics": [
                    "Fluid definition, properties: density, specific weight, specific volume, viscosity, surface tension, capillarity.",
                    "Fluid statics: Pascal's law, hydrostatic equation, pressure measurement using manometers.",
                    "Hydrostatic forces on submerged plane and curved surfaces, buoyancy, metacentric height stability."
                ]
            },
            {
                "unit": 2,
                "title": "Fluid Kinematics & Dynamics",
                "topics": [
                    "Types of fluid flow: steady/unsteady, uniform/non-uniform, laminar/turbulent, 1D/2D/3D flows.",
                    "Streamlines, pathlines, streaklines, continuity equation in Cartesian coordinates.",
                    "Fluid dynamics: Euler's equation of motion, Bernoulli's equation derivation and limitations, Venturimeter, Orificemeter."
                ]
            },
            {
                "unit": 3,
                "title": "Flow Through Pipes & Boundary Layer",
                "topics": [
                    "Laminar flow through circular pipes (Hagen-Poiseuille law), turbulent flow, Darcy-Weisbach equation.",
                    "Minor losses in pipes: sudden expansion, sudden contraction, bends, fittings.",
                    "Boundary layer concepts: thickness, drag and lift, boundary layer separation control."
                ]
            },
            {
                "unit": 4,
                "title": "Impact of Jets & Hydraulic Turbines",
                "topics": [
                    "Force exerted by fluid jet on stationary and moving flat and curved vanes, velocity triangles.",
                    "Hydraulic turbines: Classification, Pelton wheel, Francis turbine, Kaplan turbine construction and design.",
                    "Draft tube theory, cavitation in turbines, unit and specific speed parameters."
                ]
            },
            {
                "unit": 5,
                "title": "Hydraulic Pumps",
                "topics": [
                    "Centrifugal pumps: Working principle, work done, manometric efficiency, minimum starting speed, priming.",
                    "Reciprocating pumps: Working principle, slip, indicator diagram, air vessels."
                ]
            }
        ],
        "textbooks": [
            "Frank M. White, 'Fluid Mechanics', McGraw-Hill.",
            "R.K. Bansal, 'A Textbook of Fluid Mechanics and Hydraulic Machines', Laxmi Publications."
        ]
    },
    "EC501": {
        "code": "EC501",
        "title": "Digital Signal Processing",
        "credits": 4,
        "ltp": "3-0-2",
        "department": "Electronics & Communication Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Discrete Fourier Transform",
                "topics": [
                    "Discrete Fourier Transform (DFT): definition, properties (linearity, periodicity, circular convolution).",
                    "Fast Fourier Transform (FFT): Decimation-in-time (DIT) and Decimation-in-frequency (DIF) radix-2 algorithms.",
                    "Linear filtering using DFT: overlap-add and overlap-save methods."
                ]
            },
            {
                "unit": 2,
                "title": "IIR Filter Design",
                "topics": [
                    "Analog filter approximations: Butterworth and Chebyshev approximations.",
                    "Design of Infinite Impulse Response (IIR) digital filters: impulse invariant transformation, bilinear transformation.",
                    "Realization structures for IIR filters: direct form I, direct form II, cascade, parallel forms."
                ]
            },
            {
                "unit": 3,
                "title": "FIR Filter Design",
                "topics": [
                    "Symmetric and anti-symmetric Finite Impulse Response (FIR) filters, linear phase characteristics.",
                    "Design of FIR filters using windowing techniques: Rectangular, Hamming, Hanning, Blackman, Kaiser windows.",
                    "Frequency sampling method for FIR design, realization structures: direct form, cascade, linear phase."
                ]
            },
            {
                "unit": 4,
                "title": "Finite Word Length Effects",
                "topics": [
                    "Quantization noise, coefficient quantization errors, product round-off noise.",
                    "Limit cycle oscillations in recursive systems, scaling to prevent overflow."
                ]
            },
            {
                "unit": 5,
                "title": "Multirate DSP & Processors",
                "topics": [
                    "Decimation, interpolation, sampling rate conversion by rational factor.",
                    "Applications of multirate DSP: subband coding, filter banks.",
                    "DSP processors architecture: Harvard architecture, pipelining, MAC units."
                ]
            }
        ],
        "textbooks": [
            "John G. Proakis and Dimitris G. Manolakis, 'Digital Signal Processing: Principles, Algorithms, and Applications', Pearson.",
            "Alan V. Oppenheim and Ronald W. Schafer, 'Discrete-Time Signal Processing', Pearson."
        ]
    }
}
