"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 5

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for EEE, CIVIL, and AIML courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED_V4: Dict[str, Dict[str, Any]] = {
    "EE501": {
        "code": "EE501",
        "title": "Power System Analysis",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Electrical & Electronics Engineering",
        "units": [
            {
                "unit": 1,
                "title": "System Modeling & Per-Unit Representation",
                "topics": [
                    "Structure of power systems, generation, transmission, distribution.",
                    "Single-line diagram, impedance and admittance diagrams.",
                    "Per-unit system: Base values, change of base formulas, advantages.",
                    "Modeling of generator, transformer, transmission lines, and loads in per-unit.",
                    "Numerical calculations of per-unit networks under normal conditions."
                ]
            },
            {
                "unit": 2,
                "title": "Network Matrices & Admittance Formulations",
                "topics": [
                    "Bus admittance matrix (Ybus): Formulation by inspection and singular transformation methods.",
                    "Modification of Ybus for network changes (addition/removal of lines, transformer taps).",
                    "Bus impedance matrix (Zbus): Building algorithm, step-by-step addition of links and branches.",
                    "Zbus modification, node elimination by Kron reduction."
                ]
            },
            {
                "unit": 3,
                "title": "Load Flow Studies",
                "topics": [
                    "Bus classification: PQ, PV, Slack (Swing) buses.",
                    "Static load flow equations, derivation and non-linear characteristics.",
                    "Gauss-Seidel method: Iteration algorithm, acceleration factor, handling of PV buses.",
                    "Newton-Raphson method: Jacobian matrix formulation, polar coordinates, convergence properties.",
                    "Fast Decoupled load flow method, comparison of load flow algorithms."
                ]
            },
            {
                "unit": 4,
                "title": "Symmetrical Fault Analysis",
                "topics": [
                    "Symmetrical three-phase faults, transients in RL series circuits, short-circuit capacity.",
                    "Internal voltages of loaded machines under fault conditions: Sub-transient, transient, steady-state reactances.",
                    "Short-circuit currents calculations using Zbus, selection of circuit breakers."
                ]
            },
            {
                "unit": 5,
                "title": "Unsymmetrical Fault Analysis",
                "topics": [
                    "Symmetrical components transformation, positive, negative, and zero sequence components.",
                    "Sequence impedances and sequence networks of generators, transformers, and lines.",
                    "Analysis of unsymmetrical faults: Single Line-to-Ground (LG), Line-to-Line (LL), Double Line-to-Ground (LLG) faults.",
                    "Interconnection of sequence networks for fault calculations."
                ]
            }
        ],
        "textbooks": [
            "John J. Grainger and William D. Stevenson Jr., 'Power System Analysis', McGraw-Hill.",
            "Hadi Saadat, 'Power System Analysis', Tata McGraw-Hill, 3rd Edition."
        ]
    },
    "CE602": {
        "code": "CE602",
        "title": "Environmental Engineering",
        "credits": 4,
        "ltp": "3-0-2",
        "department": "Civil Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Water Demand & Sources",
                "topics": [
                    "Water supply schemes: Objectives and planning components.",
                    "Water demand: Per capita consumption, design periods, population forecasting methods.",
                    "Sources of water: Surface and groundwater sources, intakes structures.",
                    "Water quality parameters: Physical, chemical, and biological characteristics, drinking water standards (IS 10500)."
                ]
            },
            {
                "unit": 2,
                "title": "Water Treatment Processes",
                "topics": [
                    "Water treatment flow diagram, screening, aeration principles.",
                    "Sedimentation: Theory of settling, design of plain sedimentation tanks.",
                    "Coagulation and Flocculation: Mechanism, flash mixers, clariflocculator design.",
                    "Filtration: Theory, slow sand filters, rapid sand filters, pressure filters design and operation."
                ]
            },
            {
                "unit": 3,
                "title": "Disinfection & Distribution Systems",
                "topics": [
                    "Disinfection methods: Chlorination, break-point chlorination, ozonation, UV radiation.",
                    "Water softening: Lime-soda process, zeolite process, demineralization.",
                    "Water distribution systems: Layouts (dead end, grid iron, ring, radial systems).",
                    "Design of distribution pipelines, Hardy Cross network analysis method, storage reservoirs."
                ]
            },
            {
                "unit": 4,
                "title": "Wastewater Collection",
                "topics": [
                    "Sanitation systems: Conservancy and water carriage systems, sewer systems and layouts.",
                    "Sewer design principles, flow variations, sewer materials and appurtenances (manholes, catch basins).",
                    "Wastewater quality: BOD, COD, suspended solids, pH, nitrogen compounds, population equivalent."
                ]
            },
            {
                "unit": 5,
                "title": "Wastewater Treatment & Disposal",
                "topics": [
                    "Wastewater treatment flow sheet, primary treatment: screen chambers, grit chambers, primary clarifiers.",
                    "Secondary treatment: Activated Sludge Process (ASP) design, Trickling Filters design.",
                    "Anaerobic digestion of sludge, sludge drying beds, wastewater disposal methods: dilution, land disposal."
                ]
            }
        ],
        "textbooks": [
            "S.K. Garg, 'Water Supply Engineering' and 'Sewage Disposal and Air Pollution Engineering', Khanna Publishers.",
            "B.C. Punmia, Ashok Kumar Jain, and Arun Kumar Jain, 'Environmental Engineering', Laxmi Publications."
        ]
    }
}
