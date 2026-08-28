"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 4

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for MECH, ECE, EEE, and CIVIL courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED_V3: Dict[str, Dict[str, Any]] = {
    "ME602": {
        "code": "ME602",
        "title": "Automobile Engineering",
        "credits": 4,
        "ltp": "3-0-0",
        "department": "Mechanical Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Vehicle Structure & Engines",
                "topics": [
                    "Chassis layouts, frame types, structural components, body styles.",
                    "IC Engine configurations, valve operating mechanisms, fuel injection systems (MPFI, CRDI).",
                    "Engine cooling and lubrication systems, turbocharging and supercharging principles.",
                    "Emission standards (Bharat Stage BS-VI), catalytic converters, exhaust gas recirculation (EGR)."
                ]
            },
            {
                "unit": 2,
                "title": "Transmission Systems",
                "topics": [
                    "Clutch mechanisms: Single plate, multi-plate, cone, and centrifugal clutches.",
                    "Gearboxes: Sliding mesh, constant mesh, synchromesh gearboxes, planetary gear systems.",
                    "Automatic transmission: Fluid coupling, torque converter, continuously variable transmission (CVT).",
                    "Propeller shaft, universal joints, slip joint, differential mechanism, live and dead axles."
                ]
            },
            {
                "unit": 3,
                "title": "Steering & Suspension Systems",
                "topics": [
                    "Steering geometry: Castor, camber, kingpin inclination, toe-in, toe-out.",
                    "Steering gearboxes: Recirculating ball, rack and pinion, power steering systems.",
                    "Suspension systems: Rigid axle and independent suspensions (MacPherson strut, double wishbone).",
                    "Shock absorbers, leaf springs, coil springs, torsion bars, active suspensions."
                ]
            },
            {
                "unit": 4,
                "title": "Braking & Electrical Systems",
                "topics": [
                    "Braking systems: Mechanical, hydraulic, pneumatic, and vacuum brakes.",
                    "Disc and drum brakes, Anti-lock Braking System (ABS), Electronic Brakeforce Distribution (EBD).",
                    "Automotive electricals: Battery construction, alternator, starter motor, ignition systems (electronic and distributorless).",
                    "Vehicle lighting, dashboard instruments, wiring harnesses."
                ]
            },
            {
                "unit": 5,
                "title": "Electric & Hybrid Vehicles",
                "topics": [
                    "Introduction to electric vehicles (EVs) and hybrid electric vehicles (HEVs).",
                    "EV architecture, traction motors (BLDC, PMSM, Induction motors), motor controllers.",
                    "Energy storage: Lithium-ion battery packs, Battery Management Systems (BMS).",
                    "Regenerative braking, charging infrastructure (AC and DC fast charging), safety norms."
                ]
            }
        ],
        "textbooks": [
            "Kirpal Singh, 'Automobile Engineering (Vol 1 & 2)', Standard Publishers.",
            "William H. Crouse and Donald L. Anglin, 'Automotive Mechanics', Tata McGraw-Hill."
        ]
    },
    "EC601": {
        "code": "EC601",
        "title": "VLSI Design",
        "credits": 4,
        "ltp": "3-0-2",
        "department": "Electronics & Communication Engineering",
        "units": [
            {
                "unit": 1,
                "title": "IC Fabrication & MOS Transistor",
                "topics": [
                    "Introduction to VLSI technology, Moore's Law, IC fabrication steps (oxidation, diffusion, ion implantation, photolithography).",
                    "MOS transistor structure, enhancement and depletion mode MOSFET operations, threshold voltage equation.",
                    "Drain-to-source current (Ids) vs drain-to-source voltage (Vds) relationships in non-saturated and saturated regions.",
                    "MOS transistor transconductance (gm) and output conductance (gds), figure of merit."
                ]
            },
            {
                "unit": 2,
                "title": "MOS Inverter Circuits",
                "topics": [
                    "MOS Inverter with resistive load, enhancement/depletion load, Noise Margin definition.",
                    "CMOS Inverter: Circuit schematic, static and dynamic characteristics, switching speed, power dissipation.",
                    "BiCMOS Inverter: Circuit schematic, comparison with CMOS, latch-up in CMOS and prevention methods."
                ]
            },
            {
                "unit": 3,
                "title": "VLSI Circuit Design Rules & Layouts",
                "topics": [
                    "VLSI design flow, stick diagrams: NMOS, PMOS, CMOS design rules.",
                    "Lambda-based design rules for contact cuts, transistors, wires, sheet resistance and area capacitance concept.",
                    "Wiring delay estimations, buffer scaling, scaling models for device parameters."
                ]
            },
            {
                "unit": 4,
                "title": "Gate Level Design & Subsystems",
                "topics": [
                    "Static CMOS logic gates: NAND, NOR, XOR, transmission gates, Pass Transistor Logic (PTL).",
                    "Structured design of subsystems: Adders (Ripple Carry, Carry Look-Ahead), Multipliers (Array, Booth).",
                    "Memory array design: SRAM cell, DRAM cell, ROM design."
                ]
            },
            {
                "unit": 5,
                "title": "FPGA Architectures & HDL Modeling",
                "topics": [
                    "Programmable Logic Devices (PLDs): PLA, PAL, CPLD, FPGA internal architecture (Configurable Logic Blocks CLB, I/O blocks).",
                    "Hardware Description Languages: Verilog HDL behavioral, dataflow, and structural modeling of logic gates and adders.",
                    "Design for Testability (DFT): Ad-hoc testing, scan-based paths, Built-In Self-Test (BIST)."
                ]
            }
        ],
        "textbooks": [
            "Kamran Eshraghian and Douglas A. Pucknell, 'Essentials of VLSI Circuits and Systems', Prentice Hall.",
            "Neil H.E. Weste and David Money Harris, 'CMOS VLSI Design: A Circuits and Systems Perspective', Pearson, 4th Edition."
        ]
    }
}
