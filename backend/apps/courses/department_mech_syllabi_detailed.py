"""
EduCore Enterprise Framework - Department of Mechanical Engineering (MECH) Detailed Course Syllabi

Complete 5-unit syllabus specifications, learning outcomes, and textbooks for advanced MECH courses:
- ME401: Kinematics of Machinery (KOM)
- ME402: Dynamics of Machinery (DOM)
- ME501: Design of Machine Elements (DME)
- ME502: Heat & Mass Transfer (HMT)
- ME601: Finite Element Analysis (FEA)
- ME602: Computer Aided Design & Manufacturing (CAD/CAM)
- ME701: Power Plant Engineering (PPE)
- ME702: Electric & Hybrid Vehicle Engineering (EHV)
"""

from typing import Dict, Any

MECH_DETAILED_COURSES_CATALOG: Dict[str, Dict[str, Any]] = {
    "ME401": {
        "code": "ME401",
        "title": "Kinematics of Machinery",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Mechanisms and Machines",
                "topics": [
                    "Introduction to mechanisms, links, pairs, kinematic chains, degrees of freedom",
                    "Grubler's criterion, Kutzbach criterion for planar mechanisms",
                    "Inversions of four bar chain, single slider crank chain, double slider crank chain",
                    "Quick return mechanisms, toggle joint, straight line generators (Peaucellier, Hart, Watt)",
                    "Hooke's joint, double Hooke's joint, steering gear mechanisms (Ackerman, Davis)"
                ]
            },
            {
                "unit": 2,
                "title": "Velocity and Acceleration Analysis",
                "topics": [
                    "Relative velocity method, instantaneous center method, Kennedy's theorem",
                    "Velocity analysis of four bar and slider crank mechanisms",
                    "Relative acceleration method, Klein's construction for slider crank mechanism",
                    "Coriolis component of acceleration, derivation and direction rules",
                    "Acceleration analysis of planar linkages including slider crank and quick return"
                ]
            },
            {
                "unit": 3,
                "title": "Cams and Followers",
                "topics": [
                    "Classification of cams and followers, nomenclature of cam profile",
                    "Displacement, velocity, and acceleration curves for follower motion",
                    "Follower profiles: Uniform velocity, Simple Harmonic Motion (SHM), Uniform acceleration and retardation, Cycloidal motion",
                    "Construction of cam profiles for knife-edge, roller, and flat-faced followers",
                    "Under-cutting, pressure angle optimization, cams with specified contours"
                ]
            },
            {
                "unit": 4,
                "title": "Gears and Gear Trains",
                "topics": [
                    "Classification of gears, gear terminology, law of gearing",
                    "Involute and cycloidal tooth profiles, path of contact, arc of contact, contact ratio",
                    "Interference and undercutting in involute gears, minimum number of teeth to avoid interference",
                    "Simple, compound, reverted, and epicyclic gear trains",
                    "Algebraic and tabular methods for velocity ratio analysis of epicyclic gear trains, torques in epicyclic gear trains"
                ]
            },
            {
                "unit": 5,
                "title": "Gyroscopic Couples and Control Mechanisms",
                "topics": [
                    "Precessional motion, gyroscopic couple derivation, reactive gyroscopic couple",
                    "Effect of gyroscopic couple on airplanes, naval ships during steering, pitching, and rolling",
                    "Stability analysis of four-wheeled and two-wheeled vehicles moving in a curved path",
                    "Governor classification: Centrifugal governors (Watt, Porter, Proell, Hartnell)",
                    "Sensitiveness, stability, hunting, isochronism, and effort of centrifugal governors"
                ]
            }
        ],
        "textbooks": [
            "S.S. Rattan, 'Theory of Machines', Tata McGraw-Hill, 4th Edition.",
            "Thomas Bevan, 'Theory of Machines', Pearson Education, 3rd Edition."
        ]
    },
    "ME502": {
        "code": "ME502",
        "title": "Heat & Mass Transfer",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Conduction Heat Transfer",
                "topics": [
                    "Modes of heat transfer, Fourier's law of conduction, generalized heat conduction equation in Cartesian, Cylindrical, and Spherical coordinates",
                    "One-dimensional steady-state conduction through plane wall, cylinder, and sphere",
                    "Composite systems, electrical analogy, contact resistance, critical thickness of insulation",
                    "Heat generation in solids (plane wall, cylinder), transient heat conduction, lumped parameter analysis",
                    "Infinite and semi-infinite solids, Heisler charts methodology"
                ]
            },
            {
                "unit": 2,
                "title": "Extended Surfaces & Fins",
                "topics": [
                    "Need for extended surfaces, governing differential equation for fins",
                    "Boundary conditions: Infinitely long fin, fin with insulated tip, fin with convective heat loss from tip",
                    "Fin efficiency and fin effectiveness, design criteria for optimal fin spacing",
                    "Transient response of fins, applications in microelectronics cooling and radiator tubes"
                ]
            },
            {
                "unit": 3,
                "title": "Convective Heat Transfer",
                "topics": [
                    "Boundary layer theory: Velocity and thermal boundary layers, drag coefficient and Nusselt number",
                    "Dimensional analysis for forced and free convection, Buckingham Pi theorem",
                    "Forced convection: Flow over flat plates, cylinders, and spheres, internal flow through tubes and ducts",
                    "Empirical correlations for laminar and turbulent flows",
                    "Free convection: Vertical plate, horizontal cylinder, vertical cylinder, Grashof number, Rayleigh number"
                ]
            },
            {
                "unit": 4,
                "title": "Radiation Heat Transfer & Boiling",
                "topics": [
                    "Blackbody radiation laws: Stefan-Boltzmann, Planck, Wien's displacement, Kirchhoff's laws",
                    "Radiation intensity, emissive power, gray body concept, view factor algebra",
                    "Radiation exchange between diffuse gray surfaces in enclosure, radiation shields",
                    "Modes of pool boiling, pool boiling curve, critical heat flux, film condensation and dropwise condensation"
                ]
            },
            {
                "unit": 5,
                "title": "Heat Exchangers & Mass Transfer",
                "topics": [
                    "Classification of heat exchangers, overall heat transfer coefficient, fouling factor",
                    "Logarithmic Mean Temperature Difference (LMTD) method for parallel and counter flow",
                    "Effectiveness-NTU method for heat exchanger design, compact heat exchangers",
                    "Fick's law of diffusion, steady-state molecular diffusion in fluids, convective mass transfer coefficient"
                ]
            }
        ],
        "textbooks": [
            "Yunus A. Cengel, 'Heat and Mass Transfer: A Practical Approach', Tata McGraw-Hill.",
            "Frank P. Incropera and David P. DeWitt, 'Fundamentals of Heat and Mass Transfer', John Wiley & Sons."
        ]
    }
}
