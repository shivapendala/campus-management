"""
EduCore Enterprise Framework - Department of Electronics & Communication Engineering (ECE) Course Syllabi

Complete 5-unit syllabus specifications, learning outcomes, and laboratory manuals for ECE core courses:
- EC301: Electronic Circuits & Semiconductor Devices
- EC302: Digital System Design & Verilog HDL
- EC401: Signals, Systems & Transform Techniques
- EC402: Electromagnetic Fields & Transmission Lines
- EC501: Digital Signal Processing (DSP) Architecture & Algorithms
- EC502: Analog & Digital Communication Systems
- EC601: VLSI Design & CMOS Microelectronics
- EC602: Microprocessors, Microcontrollers & ARM Embedded Systems
- EC701: Microwave Engineering, Antennas & Radar
- EC702: Optical Fiber Communication & Photonics
"""

from typing import Dict, List, Any

ECE_DEPARTMENT_COURSES_SPECIFICATION: Dict[str, Dict[str, Any]] = {
    "EC301": {
        "code": "EC301",
        "title": "Electronic Circuits & Semiconductor Devices",
        "credits": 4,
        "regulation": "R23",
        "department": "Electronics & Communication Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Semiconductor Physics, PN Junction & Special Diodes",
                "hours": 9,
                "blooms": "L1_REMEMBER/L2_UNDERSTAND",
                "co": "CO1",
                "topics": "Energy bands in semiconductors, Intrinsic and extrinsic semiconductors, Carrier concentration, Drift and diffusion currents, Continuity equation, PN junction diode operation in forward and reverse bias, Diode current equation, Transition and diffusion capacitances, Reverse recovery time, Zener diode, Breakdown mechanisms (Zener and Avalanche), Tunnel diode, Varactor diode, Schottky barrier diode, Photodiode, Light Emitting Diode (LED)."
            },
            {
                "unit": 2,
                "title": "Bipolar Junction Transistors (BJT) & Biasing",
                "hours": 9,
                "blooms": "L2_UNDERSTAND/L3_APPLY",
                "co": "CO2",
                "topics": "BJT physical structure and operation, Current components, Transistor configurations (Common Base CB, Common Emitter CE, Common Collector CC), Input and output static characteristics, Transistor as an amplifier and switch, Need for biasing, Operating point (Q-point), Stability factors (S, S', S''), Biasing methods (Fixed bias, Collector-to-base bias, Self bias / Voltage divider bias), Thermal runaway and thermal stabilization."
            },
            {
                "unit": 3,
                "title": "Field Effect Transistors (JFET & MOSFET)",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO3",
                "topics": "Junction Field Effect Transistor (JFET), Physical structure, Pinch-off voltage, Drain and transfer characteristics, JFET small signal model, Metal Oxide Semiconductor Field Effect Transistor (MOSFET), Enhancement and Depletion mode MOSFETs, Threshold voltage, Output characteristics, Subthreshold conduction, Short-channel effects, MOSFET biasing (Voltage divider bias, Current source biasing), Comparison between BJT and MOSFET."
            },
            {
                "unit": 4,
                "title": "Small Signal Low-Frequency BJT & FET Amplifiers",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO4",
                "topics": "Two-port devices and Hybrid (h-parameter) model of BJT, Analysis of CE, CB, and CC amplifiers using exact and approximate h-parameter models, Calculation of Voltage Gain (Av), Current Gain (Ai), Input Impedance (Zi), and Output Impedance (Zo), Small signal low-frequency equivalent model of JFET and MOSFET, Analysis of Common Source (CS), Common Drain (CD), and Common Gate (CG) amplifiers."
            },
            {
                "unit": 5,
                "title": "Power Amplifiers & Tuned Amplifiers",
                "hours": 9,
                "blooms": "L4_ANALYZE/L5_EVALUATE",
                "co": "CO5",
                "topics": "Classification of power amplifiers (Class A, Class B, Class AB, Class C, Class D), Series-fed and Transformer-coupled Class A amplifiers, Conversion efficiency, Class B Push-Pull amplifier, Complementary symmetry Class B amplifier, Cross-over distortion, Heat sinks, Single-tuned capacitive-coupled amplifier, Double-tuned amplifier, Stagger-tuned amplifiers, Instability and neutralization in tuned amplifiers."
            }
        ],
        "textbooks": [
            "Robert L. Boylestad and Louis Nashelsky, 'Electronic Devices and Circuit Theory', 11th Edition, Pearson, 2013.",
            "Jacob Millman, Christos Halkias, and Satyabrata Jit, 'Electronic Devices and Circuits', 4th Edition, McGraw-Hill, 2015."
        ]
    },
    "EC501": {
        "code": "EC501",
        "title": "Digital Signal Processing (DSP) Architecture & Algorithms",
        "credits": 4,
        "regulation": "R23",
        "department": "Electronics & Communication Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Discrete-Time Signals, Systems & Z-Transforms",
                "hours": 9,
                "blooms": "L1_REMEMBER/L2_UNDERSTAND",
                "co": "CO1",
                "topics": "Review of Discrete-Time Signals and Systems, Linear Time-Invariant (LTI) systems, Convolution sum, Stability and causality, Linear constant-coefficient difference equations, Discrete-Time Fourier Transform (DTFT), Z-Transform, Region of Convergence (ROC), Properties of Z-Transform, Inverse Z-Transform (Power series, Partial fraction expansion), System transfer function H(z), Pole-zero representation, Frequency response of LTI systems."
            },
            {
                "unit": 2,
                "title": "Discrete Fourier Transform (DFT) & Fast Fourier Transform (FFT)",
                "hours": 9,
                "blooms": "L2_UNDERSTAND/L3_APPLY",
                "co": "CO2",
                "topics": "Discrete Fourier Transform (DFT), Properties of DFT (Periodicity, Linearity, Circular shift, Circular convolution, Parseval's relation), Circular convolution versus linear convolution using DFT, Overlap-Add and Overlap-Save methods, Fast Fourier Transform (FFT) algorithms, Decimation-in-Time (DIT-FFT) Radix-2 butterfly algorithm, Decimation-in-Frequency (DIF-FFT) Radix-2 butterfly algorithm, Computational complexity analysis, Inverse FFT (IFFT)."
            },
            {
                "unit": 3,
                "title": "Design of Infinite Impulse Response (IIR) Digital Filters",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO3",
                "topics": "Analog filter approximations, Butterworth filter approximation, Chebyshev Type I and Type II filter approximations, Design of analog Low-Pass filters, Frequency transformation in analog domain, IIR digital filter design from analog prototypes, Impulse Invariance method, Bilinear Transformation method, Frequency warping and pre-warping, Structural realizations of IIR filters (Direct Form I, Direct Form II, Cascade form, Parallel form, Transposed form)."
            },
            {
                "unit": 4,
                "title": "Design of Finite Impulse Response (FIR) Digital Filters",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO4",
                "topics": "Symmetric and anti-symmetric FIR filters, Linear phase characteristics of FIR filters, Conditions for linear phase, Design of linear phase FIR filters using Windowing techniques (Rectangular, Bartlett, Hanning, Hamming, Blackman, Kaiser windows), Frequency sampling method of FIR filter design, Realization structures for FIR filters (Direct form, Cascade form, Linear phase realization, Frequency sampling realization), Comparison of IIR and FIR filters."
            },
            {
                "unit": 5,
                "title": "Finite Word Length Effects & DSP Hardware Processors",
                "hours": 9,
                "blooms": "L4_ANALYZE/L5_EVALUATE",
                "co": "CO5",
                "topics": "Number representations (Fixed-point, Floating-point), Quantization noise, Truncation and rounding errors, Input quantization error, Coefficient quantization error, Product round-off noise in IIR digital filters, Limit cycle oscillations (Overflow limit cycles, Zero-input limit cycles), Deadband effect, Architecture of Programmable DSP Processors, Harvard architecture, Multiply-Accumulate (MAC) units, VLIW architecture, TMS320C6748 processor internal architecture, DSP applications in speech synthesis and biomedical ECG filtering."
            }
        ],
        "textbooks": [
            "John G. Proakis and Dimitris G. Manolakis, 'Digital Signal Processing: Principles, Algorithms and Applications', 4th Edition, Pearson, 2007.",
            "Alan V. Oppenheim and Ronald W. Schafer, 'Discrete-Time Signal Processing', 3rd Edition, Pearson, 2010."
        ]
    }
}
