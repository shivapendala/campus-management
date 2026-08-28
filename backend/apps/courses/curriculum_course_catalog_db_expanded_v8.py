"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 9

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for MECH and ECE courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED_V8: Dict[str, Dict[str, Any]] = {
    "ME701": {
        "code": "ME701",
        "title": "Computer Aided Design & Manufacturing",
        "credits": 4,
        "ltp": "3-0-2",
        "department": "Mechanical Engineering",
        "units": [
            {
                "unit": 1,
                "title": "CAD/CAM Foundations & Computer Graphics",
                "topics": [
                    "Product lifecycle management (PLM), CAD/CAM hardware, product design cycle.",
                    "Raster graphics, scan conversion algorithms, coordinate systems.",
                    "2D and 3D geometric transformations: Translation, scaling, rotation, shearing, reflection.",
                    "Viewing transformations, windowing, clipping algorithms, hidden line removal."
                ]
            },
            {
                "unit": 2,
                "title": "Geometric Modeling",
                "topics": [
                    "Wireframe modeling, surface modeling, solid modeling (CSG, B-Rep).",
                    "Curve representations: Parametric representation of analytic curves, synthetic curves (Bezier, B-Spline, NURBS).",
                    "Surface patches, solid modeling packages, CAD data exchange standards (IGES, STEP)."
                ]
            },
            {
                "unit": 3,
                "title": "NC/CNC Machine Tools",
                "topics": [
                    "Numerical Control (NC) systems, CNC systems, DNC systems, machine coordinates, axes nomenclature.",
                    "CNC machine structural components: Ball screws, linear guideways, automatic tool changers (ATC).",
                    "Feedback devices: Rotary encoders, linear scales, servo motors, interpolators."
                ]
            },
            {
                "unit": 4,
                "title": "CNC Part Programming",
                "topics": [
                    "G-codes and M-codes for milling and turning operations.",
                    "Manual part programming: Linear and circular interpolation, canned cycles, subroutines.",
                    "Computer-assisted part programming: APT language, CAD/CAM integration for toolpath generation."
                ]
            },
            {
                "unit": 5,
                "title": "Group Technology & FMS",
                "topics": [
                    "Group technology: Part families, classification and coding systems (Opitz, MICLASS), cell design.",
                    "Flexible Manufacturing Systems (FMS): Workstations, material handling systems, control systems, layouts.",
                    "Computer Integrated Manufacturing (CIM), automated guided vehicles (AGVs), automated storage and retrieval systems (ASRS)."
                ]
            }
        ],
        "textbooks": [
            "Mikell P. Groover, 'Automation, Production Systems, and Computer-Integrated Manufacturing', Pearson.",
            "Ibrahim Zeid, 'CAD/CAM: Theory and Practice', Tata McGraw-Hill."
        ]
    },
    "EC701": {
        "code": "EC701",
        "title": "Microwave Engineering & Antennas",
        "credits": 4,
        "ltp": "3-0-2",
        "department": "Electronics & Communication Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Waveguides & Cavity Resonators",
                "topics": [
                    "Introduction to microwave bands, rectangular waveguides: TE and TM modes, power transmission and losses.",
                    "Circular waveguides: TE and TM modes analysis, cutoff frequencies.",
                    "Rectangular and cylindrical cavity resonators, Q factor evaluation, excitation of modes in waveguides."
                ]
            },
            {
                "unit": 2,
                "title": "Microwave Components & Scattering Matrix",
                "topics": [
                    "Scattering parameters: Definition, properties of S-matrix (reciprocity, losslessness).",
                    "Waveguide tees: E-plane tee, H-plane tee, Magic tee, applications.",
                    "Directional couplers, isolators, circulators, phase shifters, attenuators."
                ]
            },
            {
                "unit": 3,
                "title": "Microwave Tubes & Solid State Devices",
                "topics": [
                    "Limitations of conventional tubes, Two-cavity Klystron amplifier, Reflex Klystron oscillator.",
                    "Traveling Wave Tube (TWT) amplifier, Magnetron oscillator (pi-mode, tuning).",
                    "Microwave solid-state devices: Gunn diode (TED), IMPATT diode, TRAPATT diode, tunnel diode."
                ]
            },
            {
                "unit": 4,
                "title": "Antenna Fundamentals & Radiating Elements",
                "topics": [
                    "Antenna parameters: Radiation pattern, directivity, gain, radiation resistance, beamwidth, polarization.",
                    "Radiation fields of Hertzian dipole, half-wave dipole, quarter-wave monopole.",
                    "Loop antennas, folded dipole, slot antennas, patch microstrip antennas."
                ]
            },
            {
                "unit": 5,
                "title": "Antenna Arrays & Propagation",
                "topics": [
                    "Antenna arrays: Broadside array, end-fire array, phased arrays, multiplication of patterns.",
                    "Wave propagation: Ground wave, sky wave, space wave propagation, skip distance, ionosphere characteristics."
                ]
            }
        ],
        "textbooks": [
            "Samuel Y. Liao, 'Microwave Devices and Circuits', Pearson Education.",
            "Constantine A. Balanis, 'Antenna Theory: Analysis and Design', John Wiley & Sons."
        ]
    }
}
