"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 3

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for CIVIL, MECH, and ECE branches.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED_V2: Dict[str, Dict[str, Any]] = {
    "CE502": {
        "code": "CE502",
        "title": "Geotechnical Engineering",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Civil Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Soil Formation & Index Properties",
                "topics": [
                    "Soil origin, soil types, three-phase soil system, volume-weight relationships.",
                    "Void ratio, porosity, degree of saturation, moisture content, unit weights, specific gravity definitions.",
                    "Index properties of soils: Grain size distribution, sieve analysis, hydrometer analysis.",
                    "Atterberg limits: Liquid limit, plastic limit, shrinkage limit, plasticity index, consistency indices.",
                    "IS soil classification system, plasticity chart, field identification of soils."
                ]
            },
            {
                "unit": 2,
                "title": "Soil Permeability & Seepage",
                "topics": [
                    "Darcy's Law of flow through soils, coefficient of permeability, validity limits.",
                    "Laboratory determination of permeability: Constant head and falling head methods.",
                    "Permeability of stratified soil deposits, factors affecting permeability.",
                    "Seepage analysis: Seepage velocity, quicksand condition, critical hydraulic gradient.",
                    "Flow nets: Characteristics, construction methods, calculation of seepage loss and uplift pressure."
                ]
            },
            {
                "unit": 3,
                "title": "Stress Distribution & Compaction",
                "topics": [
                    "Geostatic stresses: Effective stress, pore water pressure, total stress, neutral stress concepts.",
                    "Boussinesq's theory for point load, line load, strip load, and circular load stress distribution.",
                    "Westergaard's theory, Newmark's influence chart application.",
                    "Compaction: Mechanism, Proctor compaction test, optimum moisture content, maximum dry density.",
                    "Factors affecting compaction, field compaction methods, compaction control."
                ]
            },
            {
                "unit": 4,
                "title": "Consolidation of Soil",
                "topics": [
                    "Consolidation process, spring analogy, primary and secondary consolidation.",
                    "Terzaghi's one-dimensional consolidation theory: Assumptions and derivation of differential equation.",
                    "Coefficient of consolidation, compression index, pre-consolidation pressure determination.",
                    "Consolidation settlement calculations, time-rate of consolidation."
                ]
            },
            {
                "unit": 5,
                "title": "Shear Strength of Soil",
                "topics": [
                    "Mohr-Coulomb failure criterion, shear strength parameters, total and effective shear parameters.",
                    "Laboratory shear tests: Direct shear test, Triaxial compression test (UU, CU, CD tests).",
                    "Unconfined compression test, Vane shear test, pore pressure parameters.",
                    "Shear strength of cohesive and cohesionless soils, liquefaction overview."
                ]
            }
        ],
        "textbooks": [
            "K.R. Arora, 'Soil Mechanics and Foundation Engineering', Standard Publishers Distributors.",
            "B.C. Punmia, Ashok Kumar Jain, and Arun Kumar Jain, 'Soil Mechanics and Foundations', Laxmi Publications."
        ]
    },
    "ME502": {
        "code": "ME502",
        "title": "Heat & Mass Transfer",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Mechanical Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Conduction Heat Transfer",
                "topics": [
                    "Modes of heat transfer, Fourier's law of conduction, generalized conduction equation in Cartesian, Cylindrical, Spherical coordinates.",
                    "One-dimensional steady-state conduction: Plane wall, cylinder, sphere, composite systems, electrical analogy.",
                    "Critical thickness of insulation, heat generation in solids, transient conduction, lumped parameter analysis."
                ]
            },
            {
                "unit": 2,
                "title": "Extended Surfaces & Fins",
                "topics": [
                    "Need for extended surfaces, governing differential equation for fins, boundary conditions.",
                    "Fin efficiency and fin effectiveness, optimal spacing configurations.",
                    "Transient response of fins, applications in electronics packaging cooling."
                ]
            },
            {
                "unit": 3,
                "title": "Convective Heat Transfer",
                "topics": [
                    "Boundary layer theory: Velocity and thermal boundary layers, drag coefficient and Nusselt number.",
                    "Dimensional analysis for forced and free convection, Buckingham Pi theorem.",
                    "Forced convection: Flow over flat plates, cylinders, and spheres, internal flow through tubes.",
                    "Free convection: Vertical plate, horizontal cylinder, vertical cylinder, Grashof and Rayleigh numbers."
                ]
            },
            {
                "unit": 4,
                "title": "Radiation Heat Transfer",
                "topics": [
                    "Blackbody radiation laws: Stefan-Boltzmann, Planck, Wien's displacement, Kirchhoff's laws.",
                    "Radiation intensity, emissive power, gray body concept, view factor algebra.",
                    "Radiation exchange between diffuse gray surfaces in enclosure, radiation shields."
                ]
            },
            {
                "unit": 5,
                "title": "Heat Exchangers & Mass Transfer",
                "topics": [
                    "Classification of heat exchangers, overall heat transfer coefficient, fouling factor.",
                    "LMTD and Effectiveness-NTU methods for heat exchanger design.",
                    "Fick's law of diffusion, steady-state molecular diffusion, convective mass transfer coefficient."
                ]
            }
        ],
        "textbooks": [
            "Yunus A. Cengel, 'Heat and Mass Transfer: A Practical Approach', Tata McGraw-Hill.",
            "Frank P. Incropera and David P. DeWitt, 'Fundamentals of Heat and Mass Transfer', John Wiley & Sons."
        ]
    }
}
