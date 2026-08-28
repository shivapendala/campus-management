"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 11

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for EEE and CIVIL courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED_V9: Dict[str, Dict[str, Any]] = {
    "EE601": {
        "code": "EE601",
        "title": "Power System Protection & Switchgear",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Electrical & Electronics Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Electromagnetic Relays & Fuses",
                "topics": [
                    "Need for protection, faults classifications, zones of protection.",
                    "Fuses: HRC fuses construction and characteristics, selection of fuses.",
                    "Electromagnetic relays: Attracted armature, induction disc and induction cup relays.",
                    "Overcurrent, directional, distance, and differential relays structures."
                ]
            },
            {
                "unit": 2,
                "title": "Circuit Breakers & Arc Interruption",
                "topics": [
                    "Arc initiation and interruption theories: Slepian's and Cassie's theories.",
                    "Restriking voltage, recovery voltage, Rate of Rise of Restriking Voltage (RRRV).",
                    "Types of circuit breakers: Air break, Oil, Minimum Oil, SF6, and Vacuum circuit breakers.",
                    "Testing of circuit breakers, mechanical and electrical properties."
                ]
            },
            {
                "unit": 3,
                "title": "Apparatus Protection",
                "topics": [
                    "Generator protection: Stator faults, rotor faults, unbalanced loading, overspeed protection.",
                    "Transformer protection: Buchholz relay, percentage differential protection, harmonic restraint.",
                    "Motor protection: Stalling, single phasing, thermal overload protection."
                ]
            },
            {
                "unit": 4,
                "title": "Transmission Line Protection",
                "topics": [
                    "Time-graded and current-graded overcurrent protection, 3-zone distance protection.",
                    "Carrier-current protection: Phase comparison and directional comparison schemes.",
                    "Busbar protection: Differential protection, frame leakage protection."
                ]
            },
            {
                "unit": 5,
                "title": "Static & Numerical Relays",
                "topics": [
                    "Static relays: Amplitude and phase comparators, static overcurrent relay.",
                    "Numerical protection: Block diagram of numerical relay, sampling theorem, DSP algorithms.",
                    "Microprocessor-based relay hardware configurations, software flowcharts."
                ]
            }
        ],
        "textbooks": [
            "Badri Ram and D.N. Vishwakarma, 'Power System Protection and Switchgear', Tata McGraw-Hill.",
            "Y.G. Paithankar and S.R. Bhide, 'Fundamentals of Power System Protection', Prentice Hall of India."
        ]
    },
    "CE701": {
        "code": "CE701",
        "title": "Transportation Engineering",
        "credits": 4,
        "ltp": "3-0-2",
        "department": "Civil Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Highway Planning & Alignment",
                "topics": [
                    "History of road development, Jayakar committee recommendations, Nagpur/Bombay/Lucknow road plans.",
                    "Highway classification, highway alignment: Factors controlling alignment, engineering surveys.",
                    "Geometric design of highways: Cross-sectional elements, camber, sight distances (SSD, OSD)."
                ]
            },
            {
                "unit": 2,
                "title": "Horizontal & Vertical Alignment",
                "topics": [
                    "Horizontal alignment: Super-elevation design, transition curves, extra widening on curves.",
                    "Vertical alignment: Gradients, summit and valley curves geometric formulas."
                ]
            },
            {
                "unit": 3,
                "title": "Traffic Engineering & Control",
                "topics": [
                    "Traffic characteristics: Volume, speed, density studies, speed-flow relationships.",
                    "Traffic signs, signals design by Webster's method, road markings, rotary intersections."
                ]
            },
            {
                "unit": 4,
                "title": "Pavement Materials & Design",
                "topics": [
                    "Subgrade soil evaluation: CBR test, plate bearing test, aggregates properties.",
                    "Design of flexible pavements: IRC 37 guidelines, structural layers calculation.",
                    "Design of rigid pavements: IRC 58 guidelines, Westergaard's stress equations."
                ]
            },
            {
                "unit": 5,
                "title": "Highway Construction & Maintenance",
                "topics": [
                    "Construction steps: WBM, WMM, Bituminous concrete, cement concrete roads.",
                    "Pavement failures: Distresses in flexible and rigid pavements, maintenance strategies."
                ]
            }
        ],
        "textbooks": [
            "S.K. Khanna, C.E.G. Justo, and A. Veeraragavan, 'Highway Engineering', Nem Chand & Bros.",
            "L.R. Kadiyali, 'Traffic Engineering and Transportation Planning', Khanna Publishers."
        ]
    }
}
