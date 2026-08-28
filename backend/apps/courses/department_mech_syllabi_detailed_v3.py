"""
EduCore Framework - Department of Mechanical Engineering (MECH) Detailed Course Syllabi v3

Complete 5-unit syllabus specifications, learning outcomes, and textbooks for advanced MECH courses:
- ME602: Automobile Engineering (AE)
- ME701: Computer Aided Design & Manufacturing (CAD/CAM)
"""

from typing import Dict, Any

MECH_DETAILED_COURSES_CATALOG_V3: Dict[str, Dict[str, Any]] = {
    "ME602": {
        "code": "ME602",
        "title": "Automobile Engineering",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Vehicle Structure & Engines",
                "topics": [
                    "Chassis layouts, frame types, structural components, body styles",
                    "IC Engine configurations, valve operating mechanisms, fuel injection systems (MPFI, CRDI)",
                    "Engine cooling and lubrication systems, turbocharging and supercharging principles",
                    "Emission standards (Bharat Stage BS-VI), catalytic converters, exhaust gas recirculation (EGR)"
                ]
            },
            {
                "unit": 2,
                "title": "Transmission Systems",
                "topics": [
                    "Clutch mechanisms: Single plate, multi-plate, cone, and centrifugal clutches",
                    "Gearboxes: Sliding mesh, constant mesh, synchromesh gearboxes, planetary gear systems",
                    "Automatic transmission: Fluid coupling, torque converter, continuously variable transmission (CVT)",
                    "Propeller shaft, universal joints, slip joint, differential mechanism, live and dead axles"
                ]
            },
            {
                "unit": 3,
                "title": "Steering & Suspension Systems",
                "topics": [
                    "Steering geometry: Castor, camber, kingpin inclination, toe-in, toe-out",
                    "Steering gearboxes: Recirculating ball, rack and pinion, power steering systems",
                    "Suspension systems: Rigid axle and independent suspensions (MacPherson strut, double wishbone)",
                    "Shock absorbers, leaf springs, coil springs, torsion bars, active suspensions"
                ]
            },
            {
                "unit": 4,
                "title": "Braking & Electrical Systems",
                "topics": [
                    "Braking systems: Mechanical, hydraulic, pneumatic, and vacuum brakes",
                    "Disc and drum brakes, Anti-lock Braking System (ABS), Electronic Brakeforce Distribution (EBD)",
                    "Automotive electricals: Battery construction, alternator, starter motor, ignition systems (electronic and distributorless)",
                    "Vehicle lighting, dashboard instruments, wiring harnesses"
                ]
            },
            {
                "unit": 5,
                "title": "Electric & Hybrid Vehicles",
                "topics": [
                    "Introduction to electric vehicles (EVs) and hybrid electric vehicles (HEVs)",
                    "EV architecture, traction motors (BLDC, PMSM, Induction motors), motor controllers",
                    "Energy storage: Lithium-ion battery packs, Battery Management Systems (BMS)",
                    "Regenerative braking, charging infrastructure (AC and DC fast charging), safety norms"
                ]
            }
        ],
        "textbooks": [
            "Kirpal Singh, 'Automobile Engineering (Vol 1 & 2)', Standard Publishers.",
            "William H. Crouse and Donald L. Anglin, 'Automotive Mechanics', Tata McGraw-Hill."
        ]
    },
    "ME701": {
        "code": "ME701",
        "title": "Computer Aided Design & Manufacturing",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "CAD/CAM Foundations & Computer Graphics",
                "topics": [
                    "Product lifecycle management (PLM), CAD/CAM hardware, product design cycle",
                    "Raster graphics, scan conversion algorithms, coordinate systems",
                    "2D and 3D geometric transformations: Translation, scaling, rotation, shearing, reflection",
                    "Viewing transformations, windowing, clipping algorithms, hidden line removal"
                ]
            },
            {
                "unit": 2,
                "title": "Geometric Modeling",
                "topics": [
                    "Wireframe modeling, surface modeling, solid modeling (CSG, B-Rep)",
                    "Curve representations: Parametric representation of analytic curves, synthetic curves (Bezier, B-Spline, NURBS)",
                    "Surface patches, solid modeling packages, CAD data exchange standards (IGES, STEP)"
                ]
            },
            {
                "unit": 3,
                "title": "NC/CNC Machine Tools",
                "topics": [
                    "Numerical Control (NC) systems, CNC systems, DNC systems, machine coordinates, axes nomenclature",
                    "CNC machine structural components: Ball screws, linear guideways, automatic tool changers (ATC)",
                    "Feedback devices: Rotary encoders, linear scales, servo motors, interpolators"
                ]
            },
            {
                "unit": 4,
                "title": "CNC Part Programming",
                "topics": [
                    "G-codes and M-codes for milling and turning operations",
                    "Manual part programming: Linear and circular interpolation, canned cycles, subroutines",
                    "Computer-assisted part programming: APT language, CAD/CAM integration for toolpath generation"
                ]
            },
            {
                "unit": 5,
                "title": "Group Technology & FMS",
                "topics": [
                    "Group technology: Part families, classification and coding systems (Opitz, MICLASS), cell design",
                    "Flexible Manufacturing Systems (FMS): Workstations, material handling systems, control systems, layouts",
                    "Computer Integrated Manufacturing (CIM), automated guided vehicles (AGVs), automated storage and retrieval systems (ASRS)"
                ]
            }
        ],
        "textbooks": [
            "Mikell P. Groover, 'Automation, Production Systems, and Computer-Integrated Manufacturing', Pearson.",
            "Ibrahim Zeid, 'CAD/CAM: Theory and Practice', Tata McGraw-Hill."
        ]
    }
}
