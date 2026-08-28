"""
EduCore Enterprise Framework - Department of Civil Engineering (CIVIL) Course Syllabi

Complete 5-unit syllabus specifications, learning outcomes, and laboratory manuals for CIVIL core courses:
- CE301: Strength of Materials & Structural Mechanics
- CE302: Fluid Mechanics & Open Channel Hydraulics
- CE401: Structural Analysis & Indeterminate Structures
- CE402: Surveying & Geomatics Engineering
- CE501: Design of Reinforced Concrete Structures (IS 456)
- CE502: Geotechnical Engineering & Soil Mechanics
- CE601: Design of Steel Structures (IS 800)
- CE602: Environmental Engineering & Water Treatment
- CE701: Transportation Engineering & Highway Geometric Design
- CE702: Estimation, Costing & Construction Project Management
"""

from typing import Dict, List, Any

CIVIL_DEPARTMENT_COURSES_SPECIFICATION: Dict[str, Dict[str, Any]] = {
    "CE301": {
        "code": "CE301",
        "title": "Strength of Materials & Structural Mechanics",
        "credits": 4,
        "regulation": "R23",
        "department": "Civil Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Stress, Strain & Elastic Constants",
                "hours": 9,
                "blooms": "L1_REMEMBER/L2_UNDERSTAND",
                "co": "CO1",
                "topics": "Concept of stress and strain, Types of stresses (Tensile, Compressive, Shear), Stress-strain diagram for mild steel, Hooke's Law, Working stress, Factor of safety, Lateral strain, Poisson's ratio, Volumetric strain, Elastic constants (Young's modulus E, Bulk modulus K, Rigidity modulus G), Relationships among elastic constants, Thermal stresses and strains in composite bars and constrained members, Strain energy, Proof resilience, Modulus of resilience, Stresses due to gradually applied, suddenly applied, and impact loads."
            },
            {
                "unit": 2,
                "title": "Shear Force & Bending Moment in Beams",
                "hours": 9,
                "blooms": "L2_UNDERSTAND/L3_APPLY",
                "co": "CO2",
                "topics": "Types of beams (Cantilever, Simply supported, Overhanging, Fixed, Continuous), Types of loadings (Point load, Uniformly distributed load UDL, Uniformly varying load UVL), Concept of Shear Force (SF) and Bending Moment (BM), Sign conventions, Relationship between load intensity, shear force, and bending moment (dF/dx = -w, dM/dx = F), Construction of SFD and BMD for cantilevers, simply supported beams, and overhanging beams with various load combinations, Points of contraflexure and zero shear force."
            },
            {
                "unit": 3,
                "title": "Flexural & Shear Stresses in Beams",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO3",
                "topics": "Theory of simple bending (Pure bending), Assumptions in Euler-Bernoulli beam theory, Derivation of flexural formula (M/I = sigma/y = E/R), Section modulus (Z) for rectangular, circular, hollow, and standard I-sections, Design of beams based on flexural strength, Flitched / Composite beams of two materials, Shear stress distribution across standard cross-sections (Rectangular, Circular, Triangular, T-section, I-section), Derivation of horizontal shear stress formula (tau = V*A*y_bar / (I*b)), Ratio of maximum to average shear stress."
            },
            {
                "unit": 4,
                "title": "Torsion of Circular Shafts & Springs",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO4",
                "topics": "Torsion of solid and hollow circular shafts, Assumptions in pure torsion, Derivation of torsion formula (T/J = tau/r = G*theta/L), Polar section modulus (Zp), Torsional rigidity and torsional stiffness, Power transmitted by a rotating shaft, Design of shafts for strength and torsional rigidity, Shafts in series and parallel, Combined bending and torsion with axial loads, Equivalent bending moment and equivalent twisting moment, Close-coiled and open-coiled helical springs, Deflection and shear stresses in helical springs, Springs in series and parallel."
            },
            {
                "unit": 5,
                "title": "Principal Stresses, Mohr's Circle & Thin Cylinders",
                "hours": 9,
                "blooms": "L4_ANALYZE/L5_EVALUATE",
                "co": "CO5",
                "topics": "Two-dimensional state of stress at a point, Normal and shear stresses on inclined planes, Principal planes and principal stresses, Maximum shear stress and its orientation, Mohr's Circle of Stress (Analytical and Graphical construction), Theories of elastic failure (Maximum Principal Stress Theory / Rankine, Maximum Shear Stress Theory / Tresca-Guest, Maximum Distortion Energy Theory / Von-Mises, Maximum Strain Theory / St. Venant), Thin cylindrical shells subjected to internal fluid pressure, Circumferential (Hoop) stress and Longitudinal stress, Volumetric strain of thin cylinders, Thin spherical shells subjected to internal pressure, Efficiency of longitudinal and circumferential riveted joints in thin shells."
            }
        ],
        "textbooks": [
            "R.K. Rajput, 'Strength of Materials (Mechanics of Solids)', 7th Edition, S. Chand & Company, 2018.",
            "Ferdinand P. Beer, E. Russell Johnston Jr., John T. DeWolf, and David F. Mazurek, 'Mechanics of Materials', 8th Edition, McGraw-Hill, 2020."
        ]
    }
}
