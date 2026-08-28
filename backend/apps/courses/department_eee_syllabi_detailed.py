"""
EduCore Enterprise Framework - Department of Electrical & Electronics Engineering (EEE) Detailed Course Syllabi

Complete 5-unit syllabus specifications, learning outcomes, and textbooks for advanced EEE courses:
- EE401: AC Electrical Machines (ACEM)
- EE402: Power Electronics (PE)
- EE501: Power System Analysis (PSA)
- EE502: Control Systems Engineering (CSE)
"""

from typing import Dict, Any

EEE_DETAILED_COURSES_CATALOG: Dict[str, Dict[str, Any]] = {
    "EE401": {
        "code": "EE401",
        "title": "AC Electrical Machines",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Three-Phase Induction Motors",
                "topics": [
                    "Constructional details, squirrel cage and slip ring rotors, production of rotating magnetic field",
                    "Principle of operation, slip, rotor frequency, rotor EMF and current under starting and running conditions",
                    "Equivalent circuit, power flow diagram, losses and efficiency, torque equation, torque-slip characteristics",
                    "No-load and blocked rotor tests, determination of equivalent circuit parameters, circle diagram construction",
                    "Starting methods: Direct-On-Line (DOL), Star-Delta, Auto-transformer, rotor resistance starters"
                ]
            },
            {
                "unit": 2,
                "title": "Speed Control & Induction Generators",
                "topics": [
                    "Speed control methods: Stator voltage control, pole changing method, stator frequency control (v/f control)",
                    "Rotor resistance control, slip power recovery schemes (Kramer and Scherbius drives)",
                    "Double cage induction motor: Principle, equivalent circuit, torque speed characteristics",
                    "Induction generator: Principle of operation, self-excited induction generator, applications in wind power"
                ]
            },
            {
                "unit": 3,
                "title": "Synchronous Generators (Alternators)",
                "topics": [
                    "Constructional features, cylindrical and salient pole rotors, armature windings, winding factors (distribution and pitch factors)",
                    "EMF equation, armature reaction, synchronous reactance and synchronous impedance",
                    "Voltage regulation determination: EMF, MMF, Potier (ZPF) methods, ASA method",
                    "Two-reaction theory for salient pole machines, slip test, direct and quadrature reactances",
                    "Parallel operation of alternators, synchronizing current, synchronizing power, active and reactive power sharing"
                ]
            },
            {
                "unit": 4,
                "title": "Synchronous Motors",
                "topics": [
                    "Principle of operation, starting methods (damping windings, pony motor)",
                    "Equivalent circuit, phasor diagram, power developed by synchronous motor",
                    "Effect of varying excitation: V and Inverted V curves, synchronous condenser application",
                    "Power angle characteristics, hunting in synchronous motors, methods of prevention"
                ]
            },
            {
                "unit": 5,
                "title": "Single-Phase & Special Machines",
                "topics": [
                    "Double revolving field theory, equivalent circuit of single-phase induction motor",
                    "Starting methods: Split-phase, capacitor-start, capacitor-run, shaded-pole motors",
                    "Universal motor, stepper motor, brushless DC (BLDC) motor, permanent magnet synchronous motor (PMSM)"
                ]
            }
        ],
        "textbooks": [
            "P.S. Bimbhra, 'Electrical Machinery', Khanna Publishers, 7th Edition.",
            "D.P. Kothari and I.J. Nagrath, 'Electric Machines', Tata McGraw-Hill, 4th Edition."
        ]
    },
    "EE402": {
        "code": "EE402",
        "title": "Power Electronics",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Power Semiconductor Devices",
                "topics": [
                    "Introduction to power semiconductor switches: Power Diode, Thyristor (SCR), TRIAC, Power BJT, Power MOSFET, IGBT",
                    "SCR static V-I characteristics, turn-on and turn-off methods, dynamic characteristics",
                    "Two-transistor analogy of SCR, gate triggering circuits, UJT firing circuit",
                    "Series and parallel operation of SCRs, static and dynamic equalizing networks, snubber circuits"
                ]
            },
            {
                "unit": 2,
                "title": "Phase-Controlled Rectifiers",
                "topics": [
                    "Single-phase half-wave and full-wave controlled rectifiers with R, RL, and RLE loads",
                    "Effect of freewheeling diode, semi-converters and full-converters, derivation of average and RMS voltage",
                    "Three-phase half-wave and full-wave controlled converters with R and RL loads",
                    "Effect of source inductance, displacement factor, power factor, harmonic analysis of input current"
                ]
            },
            {
                "unit": 3,
                "title": "DC-to-DC Converters (Choppers)",
                "topics": [
                    "Principle of step-down and step-up choppers, control strategies: TRC and CLC",
                    "Buck, Boost, Buck-Boost, Cuk regulators: Circuit schematic, continuous conduction mode analysis",
                    "Switching mode regulators, chopper classifications: Class A, B, C, D, E configurations"
                ]
            },
            {
                "unit": 4,
                "title": "Inverters (DC-to-AC Converters)",
                "topics": [
                    "Single-phase half-bridge and full-bridge inverters with R and RL loads",
                    "Three-phase bridge inverters: 180-degree and 120-degree conduction modes",
                    "Voltage control techniques in inverters: Single-pulse, multi-pulse, and Sinusoidal Pulse Width Modulation (SPWM)",
                    "Current source inverters, harmonic reduction methods, space vector modulation overview"
                ]
            },
            {
                "unit": 5,
                "title": "AC-to-AC Converters",
                "topics": [
                    "Single-phase AC voltage controllers with R and RL loads, integral cycle control and phase angle control",
                    "Three-phase AC voltage controllers, cyclo-converters: Single-phase to single-phase, three-phase to single-phase configurations",
                    "Applications of power electronics: UPS, SMPS, HVDC transmission systems, induction heating systems"
                ]
            }
        ],
        "textbooks": [
            "M.H. Rashid, 'Power Electronics: Circuits, Devices and Applications', Pearson Education, 4th Edition.",
            "P.S. Bimbhra, 'Power Electronics', Khanna Publishers, 5th Edition."
        ]
    }
}
