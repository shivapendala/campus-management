"""
EduCore Framework - Department of Electrical & Electronics Engineering (EEE) Detailed Course Syllabi v2

Complete 5-unit syllabus specifications, learning outcomes, and textbooks for advanced EEE courses:
- EE501: Power System Analysis (PSA)
- EE502: Control Systems Engineering (CSE)
"""

from typing import Dict, Any

EEE_DETAILED_COURSES_CATALOG_V2: Dict[str, Dict[str, Any]] = {
    "EE501": {
        "code": "EE501",
        "title": "Power System Analysis",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "System Modeling & Per-Unit Representation",
                "topics": [
                    "Structure of power systems, generation, transmission, distribution",
                    "Single-line diagram, impedance and admittance diagrams",
                    "Per-unit system: Base values, change of base formulas, advantages",
                    "Modeling of generator, transformer, transmission lines, and loads in per-unit",
                    "Numerical calculations of per-unit networks under normal conditions"
                ]
            },
            {
                "unit": 2,
                "title": "Network Matrices & Admittance Formulations",
                "topics": [
                    "Bus admittance matrix (Ybus): Formulation by inspection and singular transformation methods",
                    "Modification of Ybus for network changes (addition/removal of lines, transformer taps)",
                    "Bus impedance matrix (Zbus): Building algorithm, step-by-step addition of links and branches",
                    "Zbus modification, node elimination by Kron reduction"
                ]
            },
            {
                "unit": 3,
                "title": "Load Flow Studies",
                "topics": [
                    "Bus classification: PQ, PV, Slack (Swing) buses",
                    "Static load flow equations, derivation and non-linear characteristics",
                    "Gauss-Seidel method: Iteration algorithm, acceleration factor, handling of PV buses",
                    "Newton-Raphson method: Jacobian matrix formulation, polar coordinates, convergence properties",
                    "Fast Decoupled load flow method, comparison of load flow algorithms"
                ]
            },
            {
                "unit": 4,
                "title": "Symmetrical Fault Analysis",
                "topics": [
                    "Symmetrical three-phase faults, transients in RL series circuits, short-circuit capacity",
                    "Internal voltages of loaded machines under fault conditions: Sub-transient, transient, steady-state reactances",
                    "Short-circuit currents calculations using Zbus, selection of circuit breakers"
                ]
            },
            {
                "unit": 5,
                "title": "Unsymmetrical Fault Analysis",
                "topics": [
                    "Symmetrical components transformation, positive, negative, and zero sequence components",
                    "Sequence impedances and sequence networks of generators, transformers, and lines",
                    "Analysis of unsymmetrical faults: Single Line-to-Ground (LG), Line-to-Line (LL), Double Line-to-Ground (LLG) faults",
                    "Interconnection of sequence networks for fault calculations"
                ]
            }
        ],
        "textbooks": [
            "John J. Grainger and William D. Stevenson Jr., 'Power System Analysis', McGraw-Hill.",
            "Hadi Saadat, 'Power System Analysis', Tata McGraw-Hill, 3rd Edition."
        ]
    },
    "EE502": {
        "code": "EE502",
        "title": "Control Systems Engineering",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "System Modeling",
                "topics": [
                    "Introduction to control systems, open loop and closed loop systems",
                    "Mathematical modeling of physical systems: Differential equations of translational and rotational mechanical systems",
                    "Electrical systems, transfer function, block diagram reduction techniques",
                    "Signal Flow Graph (SFG), Mason's gain formula and applications"
                ]
            },
            {
                "unit": 2,
                "title": "Time Response Analysis",
                "topics": [
                    "Standard test signals: Step, ramp, parabolic, impulse",
                    "Time response of first-order systems, transient response of second-order systems",
                    "Time domain specifications: Delay time, rise time, peak time, settling time, peak overshoot",
                    "Steady-state errors, error constants (Kp, Kv, Ka) for Type 0, 1, 2 systems",
                    "Effects of proportional, integral, and derivative (PID) control actions"
                ]
            },
            {
                "unit": 3,
                "title": "Stability in Time Domain",
                "topics": [
                    "Concept of stability, absolute, relative, and conditional stability",
                    "Routh-Hurwitz stability criterion: Necessary and sufficient conditions, special cases",
                    "Root Locus technique: Rules for construction of root loci, determination of stability from root locus"
                ]
            },
            {
                "unit": 4,
                "title": "Frequency Response Analysis",
                "topics": [
                    "Frequency domain specifications: Resonant peak, resonant frequency, bandwidth",
                    "Bode plots: Determination of gain margin, phase margin, and stability",
                    "Polar plots, Nyquist stability criterion, relative stability using Nyquist plot"
                ]
            },
            {
                "unit": 5,
                "title": "State Variable Analysis",
                "topics": [
                    "State space representation of continuous-time systems: State equations, state transition matrix",
                    "Computation of state transition matrix, transfer function from state model",
                    "Concepts of controllability and observability: Kalman's and Gilbert's tests",
                    "State feedback controller design, pole placement techniques"
                ]
            }
        ],
        "textbooks": [
            "I.J. Nagrath and M. Gopal, 'Control Systems Engineering', New Age International.",
            "Benjamin C. Kuo, 'Automatic Control Systems', John Wiley & Sons."
        ]
    }
}
