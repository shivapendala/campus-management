"""
EduCore Enterprise Framework - Department of Mechanical Engineering (MECH) Course Syllabi

Complete 5-unit syllabus specifications, learning outcomes, and laboratory manuals for MECH core courses:
- ME301: Engineering Thermodynamics & Applied Heat Transfer
- ME302: Fluid Mechanics & Hydraulic Machinery
- ME401: Kinematics & Dynamics of Machinery
- ME402: Manufacturing Technology & Machine Tools
- ME501: Design of Machine Elements & Mechanical Drives
- ME502: Heat & Mass Transfer Processes
- ME601: Finite Element Analysis (FEA) & Computational Mechanics
- ME602: Automobile Engineering & Electric Vehicle Dynamics
- ME701: Computer Aided Design & Manufacturing (CAD/CAM/CIM)
- ME702: Power Plant Engineering & Renewable Energy Systems
"""

from typing import Dict, List, Any

MECH_DEPARTMENT_COURSES_SPECIFICATION: Dict[str, Dict[str, Any]] = {
    "ME301": {
        "code": "ME301",
        "title": "Engineering Thermodynamics & Applied Heat Transfer",
        "credits": 4,
        "regulation": "R23",
        "department": "Mechanical Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Basic Concepts & First Law of Thermodynamics",
                "hours": 9,
                "blooms": "L1_REMEMBER/L2_UNDERSTAND",
                "co": "CO1",
                "topics": "Microscopic and Macroscopic viewpoints, Thermodynamic systems (Closed, Open, Isolated), State, Property, Process, Cycle, Thermodynamic equilibrium, Quasi-static process, Temperature and Zeroth Law of Thermodynamics, Work and Heat transfer, First Law applied to non-flow processes (Constant volume, Constant pressure, Constant temperature, Adiabatic, Polytropic), First Law applied to open steady-flow systems, Steady Flow Energy Equation (SFEE), Applications of SFEE to Nozzles, Diffusers, Turbines, Compressors, Throttling valves, and Heat Exchangers."
            },
            {
                "unit": 2,
                "title": "Second Law of Thermodynamics & Entropy",
                "hours": 9,
                "blooms": "L2_UNDERSTAND/L3_APPLY",
                "co": "CO2",
                "topics": "Limitations of First Law, Thermal energy reservoirs, Heat engines, Refrigerators, Heat pumps, Kelvin-Planck and Clausius statements of Second Law, Equivalence of statements, Reversible and Irreversible processes, Causes of irreversibility, Carnot cycle and theorem, Thermodynamic temperature scale, Clausius inequality, Concept of Entropy, Principle of increase of entropy, T-s diagrams, Entropy changes of ideal gases and pure substances during thermodynamic processes, Available and Unavailable energy, Exergy / Availability analysis, Helmholtz and Gibbs functions."
            },
            {
                "unit": 3,
                "title": "Properties of Pure Substances & Steam Power Cycles",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO3",
                "topics": "Pure substance concept, Phase change processes of water, P-V, T-s, and h-s (Mollier) diagrams for water, Dryness fraction, Steam tables, Measurement of steam quality (Throttling and Separating-and-Throttling calorimeters), Vapor power cycles, Carnot vapor cycle, Rankine cycle, Methods to improve Rankine cycle efficiency, Reheat Rankine cycle, Regenerative Rankine cycle with Open and Closed Feedwater Heaters, Supercritical power plant cycles, Binary vapor cycles."
            },
            {
                "unit": 4,
                "title": "Gas Power Cycles & IC Engine Performance",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO4",
                "topics": "Air standard assumptions, Otto cycle (Constant volume), Diesel cycle (Constant pressure), Dual combustion cycle, Comparison of Otto, Diesel, and Dual cycles for same compression ratio and heat input, Brayton gas turbine cycle, Brayton cycle with Regeneration, Reheating, and Intercooling, Real gas turbine cycles, Internal Combustion Engines terminology, Four-stroke and Two-stroke engines, Indicated Power (IP), Brake Power (BP), Mechanical efficiency, Thermal efficiency, Specific fuel consumption, Morse test, Heat balance sheet."
            },
            {
                "unit": 5,
                "title": "Psychrometry & Refrigeration Cycles",
                "hours": 9,
                "blooms": "L4_ANALYZE/L5_EVALUATE",
                "co": "CO5",
                "topics": "Psychrometric properties, Dry-bulb temperature (DBT), Wet-bulb temperature (WBT), Dew-point temperature (DPT), Relative humidity (RH), Specific humidity, Enthalpy of moist air, Psychrometric chart, Basic psychrometric processes (Sensible heating/cooling, Humidification/Dehumidification, Cooling and dehumidification, Evaporative cooling, Adiabatic mixing of air streams), Summer and Winter air conditioning systems, Vapor Compression Refrigeration System (VCRS), Standard VCRS cycle on P-h and T-s diagrams, COP calculation, Subcooling and Superheating, Environmentally friendly refrigerants (R134a, R410A, R290, R600a, ODP, GWP), Vapor Absorption Refrigeration System (VARS) overview."
            }
        ],
        "textbooks": [
            "Yunus A. Cengel and Michael A. Boles, 'Thermodynamics: An Engineering Approach', 9th Edition, McGraw-Hill, 2019.",
            "P.K. Nag, 'Engineering Thermodynamics', 6th Edition, McGraw-Hill Education, 2017."
        ]
    }
}
