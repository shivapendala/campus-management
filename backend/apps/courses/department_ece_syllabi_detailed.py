"""
EduCore Framework - Department of Electronics & Communication Engineering (ECE) Detailed Course Syllabi

Complete 5-unit syllabus specifications, learning outcomes, and textbooks for advanced ECE courses:
- EC402: Electromagnetic Fields & Transmission Lines (EMFT)
- EC601: VLSI Design & CMOS Microelectronics (VLSI)
"""

from typing import Dict, Any

ECE_DETAILED_COURSES_CATALOG: Dict[str, Dict[str, Any]] = {
    "EC402": {
        "code": "EC402",
        "title": "Electromagnetic Fields & Transmission Lines",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Electrostatics",
                "topics": [
                    "Coordinate systems: Cartesian, Cylindrical, Spherical transformations",
                    "Coulomb's Law, Electric Field Intensity (EFI), field due to line, sheet, and volume charge distributions",
                    "Electric Flux Density (EFD), Gauss's Law and its applications, divergence theorem",
                    "Electric potential, relationship between E and V, Maxwell's two equations for electrostatic fields",
                    "Energy density in electrostatic fields, boundary conditions for dielectrics and conductors, capacitance"
                ]
            },
            {
                "unit": 2,
                "title": "Magnetostatics",
                "topics": [
                    "Biot-Savart's Law, Magnetic Field Intensity (MFI) due to straight, circular, and infinite line currents",
                    "Ampere's Circuital Law and its applications, curl, Stokes' theorem",
                    "Magnetic Flux Density (MFD), Lorentz force equation, self and mutual inductance",
                    "Magnetic boundary conditions, energy density in magnetic fields, force and torque on current loops"
                ]
            },
            {
                "unit": 3,
                "title": "Maxwell's Equations & Electromagnetic Waves",
                "topics": [
                    "Faraday's Law of electromagnetic induction, transformer and motional EMF",
                    "Displacement current density derivation, Maxwell's equations in point and integral forms",
                    "Electromagnetic wave propagation in free space, lossy and lossless dielectrics, conductors",
                    "Wave equations, skin depth, Poynting vector and Poynting theorem, reflection and refraction of plane waves"
                ]
            },
            {
                "unit": 4,
                "title": "Transmission Lines - General Slabs",
                "topics": [
                    "Transmission line parameters, primary and secondary constants, transmission line general equations",
                    "Infinite line concept, input impedance, standing waves, Standing Wave Ratio (SWR)",
                    "Wavelength, phase velocity, group velocity, distortion-less line conditions, loading of lines"
                ]
            },
            {
                "unit": 5,
                "title": "RF and Microwave Transmission Lines",
                "topics": [
                    "RF transmission lines, input impedance of loss-free lines, short-circuited and open-circuited lines",
                    "Smith chart: construction, mapping of reflection coefficient, impedance matching using single and double stubs",
                    "Waveguides: Rectangular waveguides, TE and TM modes analysis, cutoff frequency, guide wavelength"
                ]
            }
        ],
        "textbooks": [
            "Matthew N.O. Sadiku, 'Elements of Electromagnetics', Oxford University Press, 6th Edition.",
            "William H. Hayt and John A. Buck, 'Engineering Electromagnetics', McGraw-Hill, 8th Edition."
        ]
    },
    "EC601": {
        "code": "EC601",
        "title": "VLSI Design",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "IC Fabrication & MOS Transistor",
                "topics": [
                    "Introduction to VLSI technology, Moore's Law, IC fabrication steps (oxidation, diffusion, ion implantation, photolithography)",
                    "MOS transistor structure, enhancement and depletion mode MOSFET operations, threshold voltage equation",
                    "Drain-to-source current (Ids) vs drain-to-source voltage (Vds) relationships in non-saturated and saturated regions",
                    "MOS transistor transconductance (gm) and output conductance (gds), figure of merit"
                ]
            },
            {
                "unit": 2,
                "title": "MOS Inverter Circuits",
                "topics": [
                    "MOS Inverter with resistive load, enhancement/depletion load, Noise Margin definition",
                    "CMOS Inverter: Circuit schematic, static and dynamic characteristics, switching speed, power dissipation",
                    "BiCMOS Inverter: Circuit schematic, comparison with CMOS, latch-up in CMOS and prevention methods"
                ]
            },
            {
                "unit": 3,
                "title": "VLSI Circuit Design Slabs & Layouts",
                "topics": [
                    "VLSI design flow, stick diagrams: NMOS, PMOS, CMOS design rules",
                    "Lambda-based design rules for contact cuts, transistors, wires, sheet resistance and area capacitance concept",
                    "Wiring delay estimations, buffer scaling, scaling models for device parameters"
                ]
            },
            {
                "unit": 4,
                "title": "Gate Level Design & Subsystems",
                "topics": [
                    "Static CMOS logic gates: NAND, NOR, XOR, transmission gates, Pass Transistor Logic (PTL)",
                    "Structured design of subsystems: Adders (Ripple Carry, Carry Look-Ahead), Multipliers (Array, Booth)",
                    "Memory array design: SRAM cell, DRAM cell, ROM design"
                ]
            },
            {
                "unit": 5,
                "title": "FPGA Architectures & HDL Modeling",
                "topics": [
                    "Programmable Logic Devices (PLDs): PLA, PAL, CPLD, FPGA internal architecture (Configurable Logic Blocks CLB, I/O blocks)",
                    "Hardware Description Languages: Verilog HDL behavioral, dataflow, and structural modeling of logic gates and adders",
                    "Design for Testability (DFT): Ad-hoc testing, scan-based paths, Built-In Self-Test (BIST)"
                ]
            }
        ],
        "textbooks": [
            "Kamran Eshraghian and Douglas A. Pucknell, 'Essentials of VLSI Circuits and Systems', Prentice Hall.",
            "Neil H.E. Weste and David Money Harris, 'CMOS VLSI Design: A Circuits and Systems Perspective', Pearson, 4th Edition."
        ]
    }
}
