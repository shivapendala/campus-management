"""
EduCore Framework - Department of Civil Engineering (CIVIL) Detailed Course Syllabi v2

Complete 5-unit syllabus specifications, learning outcomes, and textbooks for advanced CIVIL courses:
- CE502: Geotechnical Engineering (GTE)
- CE602: Environmental Engineering (EE)
"""

from typing import Dict, Any

CIVIL_DETAILED_COURSES_CATALOG_V2: Dict[str, Dict[str, Any]] = {
    "CE502": {
        "code": "CE502",
        "title": "Geotechnical Engineering",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Soil Formation & Index Properties",
                "topics": [
                    "Soil origin, soil types, three-phase soil system, volume-weight relationships",
                    "Void ratio, porosity, degree of saturation, moisture content, unit weights, specific gravity definitions",
                    "Index properties of soils: Grain size distribution, sieve analysis, hydrometer analysis",
                    "Atterberg limits: Liquid limit, plastic limit, shrinkage limit, plasticity index, consistency indices",
                    "IS soil classification system, plasticity chart, field identification of soils"
                ]
            },
            {
                "unit": 2,
                "title": "Soil Permeability & Seepage",
                "topics": [
                    "Darcy's Law of flow through soils, coefficient of permeability, validity limits",
                    "Laboratory determination of permeability: Constant head and falling head methods",
                    "Permeability of stratified soil deposits, factors affecting permeability",
                    "Seepage analysis: Seepage velocity, quicksand condition, critical hydraulic gradient",
                    "Flow nets: Characteristics, construction methods, calculation of seepage loss and uplift pressure"
                ]
            },
            {
                "unit": 3,
                "title": "Stress Distribution & Compaction",
                "topics": [
                    "Geostatic stresses: Effective stress, pore water pressure, total stress, neutral stress concepts",
                    "Boussinesq's theory for point load, line load, strip load, and circular load stress distribution",
                    "Westergaard's theory, Newmark's influence chart application",
                    "Compaction: Mechanism, Proctor compaction test, optimum moisture content, maximum dry density",
                    "Factors affecting compaction, field compaction methods, compaction control"
                ]
            },
            {
                "unit": 4,
                "title": "Consolidation of Soil",
                "topics": [
                    "Consolidation process, spring analogy, primary and secondary consolidation",
                    "Terzaghi's one-dimensional consolidation theory: Assumptions and derivation of differential equation",
                    "Coefficient of consolidation, compression index, pre-consolidation pressure determination",
                    "Consolidation settlement calculations, time-rate of consolidation"
                ]
            },
            {
                "unit": 5,
                "title": "Shear Strength of Soil",
                "topics": [
                    "Mohr-Coulomb failure criterion, shear strength parameters, total and effective shear parameters",
                    "Laboratory shear tests: Direct shear test, Triaxial compression test (UU, CU, CD tests)",
                    "Unconfined compression test, Vane shear test, pore pressure parameters",
                    "Shear strength of cohesive and cohesionless soils, liquefaction overview"
                ]
            }
        ],
        "textbooks": [
            "K.R. Arora, 'Soil Mechanics and Foundation Engineering', Standard Publishers Distributors.",
            "B.C. Punmia, Ashok Kumar Jain, and Arun Kumar Jain, 'Soil Mechanics and Foundations', Laxmi Publications."
        ]
    },
    "CE602": {
        "code": "CE602",
        "title": "Environmental Engineering",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Water Demand & Sources",
                "topics": [
                    "Water supply schemes: Objectives and planning components",
                    "Water demand: Per capita consumption, design periods, population forecasting methods",
                    "Sources of water: Surface and groundwater sources, intakes structures",
                    "Water quality parameters: Physical, chemical, and biological characteristics, drinking water standards (IS 10500)"
                ]
            },
            {
                "unit": 2,
                "title": "Water Treatment Processes",
                "topics": [
                    "Water treatment flow diagram, screening, aeration principles",
                    "Sedimentation: Theory of settling, design of plain sedimentation tanks",
                    "Coagulation and Flocculation: Mechanism, flash mixers, clariflocculator design",
                    "Filtration: Theory, slow sand filters, rapid sand filters, pressure filters design and operation"
                ]
            },
            {
                "unit": 3,
                "title": "Disinfection & Distribution Systems",
                "topics": [
                    "Disinfection methods: Chlorination, break-point chlorination, ozonation, UV radiation",
                    "Water softening: Lime-soda process, zeolite process, demineralization",
                    "Water distribution systems: Layouts (dead end, grid iron, ring, radial systems)",
                    "Design of distribution pipelines, Hardy Cross network analysis method, storage reservoirs"
                ]
            },
            {
                "unit": 4,
                "title": "Wastewater Characteristics & Collection",
                "topics": [
                    "Sanitation systems: Conservancy and water carriage systems, sewer systems and layouts",
                    "Sewer design principles, flow variations, sewer materials and appurtenances (manholes, catch basins)",
                    "Wastewater quality: BOD, COD, suspended solids, pH, nitrogen compounds, population equivalent"
                ]
            },
            {
                "unit": 5,
                "title": "Wastewater Treatment & Disposal",
                "topics": [
                    "Wastewater treatment flow sheet, primary treatment: screen chambers, grit chambers, primary clarifiers",
                    "Secondary treatment: Activated Sludge Process (ASP) design, Trickling Filters design",
                    "Anaerobic digestion of sludge, sludge drying beds, wastewater disposal methods: dilution, land disposal"
                ]
            }
        ],
        "textbooks": [
            "S.K. Garg, 'Water Supply Engineering' and 'Sewage Disposal and Air Pollution Engineering', Khanna Publishers.",
            "B.C. Punmia, Ashok Kumar Jain, and Arun Kumar Jain, 'Environmental Engineering', Laxmi Publications."
        ]
    }
}
