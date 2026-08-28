"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 6

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for MECH, ECE, and EEE courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED_V5: Dict[str, Dict[str, Any]] = {
    "ME302": {
        "code": "ME302",
        "title": "Kinematics of Machinery",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Mechanical Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Mechanisms & Machines",
                "topics": [
                    "Links, pairs, kinematic chains, degrees of freedom, Kutzbach criterion, Grubler's criterion.",
                    "Inversions of four bar chain, single slider crank chain, double slider crank chain.",
                    "Grashof's law, straight line motion mechanisms, steering gear mechanisms (Davis, Ackerman)."
                ]
            },
            {
                "unit": 2,
                "title": "Velocity & Acceleration Analysis",
                "topics": [
                    "Relative velocity method, instantaneous center method, Kennedy's theorem.",
                    "Relative acceleration method, Coriolis component of acceleration, Klein's construction."
                ]
            },
            {
                "unit": 3,
                "title": "Cams & Followers",
                "topics": [
                    "Classification of cams and followers, radial cam profile generation.",
                    "Follower motions: Uniform velocity, simple harmonic motion (SHM), uniform acceleration and retardation (UARM), cycloidal motion.",
                    "Cams with specified contours: Tangent cam, circular arc cam."
                ]
            },
            {
                "unit": 4,
                "title": "Gears & Gear Trains",
                "topics": [
                    "Classification of gears, law of gearing, tooth profiles (involute and cycloidal).",
                    "Interference and undercutting, minimum number of teeth to avoid interference.",
                    "Gear trains: Simple, compound, reverted, epicyclic gear trains, torques in epicyclic gear trains."
                ]
            },
            {
                "unit": 5,
                "title": "Gyroscopic Effects & Governors",
                "topics": [
                    "Gyroscopic couple: Effect on naval ships, airplanes, four-wheeled and two-wheeled vehicles.",
                    "Governors: Watt, Porter, Proell, Hartnell governors, sensitivity, stability, hunting, isochronism."
                ]
            }
        ],
        "textbooks": [
            "Thomas Bevan, 'Theory of Machines', Pearson Education.",
            "S.S. Rattan, 'Theory of Machines', Tata McGraw-Hill."
        ]
    },
    "EC502": {
        "code": "EC502",
        "title": "Analog & Digital Communication",
        "credits": 4,
        "ltp": "3-0-2",
        "department": "Electronics & Communication Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Amplitude Modulation",
                "topics": [
                    "Need for modulation, Amplitude Modulation (AM): DSB-FC, DSB-SC, SSB-SC, VSB signal generation and demodulation.",
                    "AM transmitters, superheterodyne receivers, envelope detectors, coherent detection, noise in AM systems."
                ]
            },
            {
                "unit": 2,
                "title": "Angle Modulation",
                "topics": [
                    "Frequency Modulation (FM) and Phase Modulation (PM), narrow-band and wide-band FM.",
                    "Generation of FM: Direct and indirect (Armstrong) methods, FM demodulators: Slope detector, ratio detector, Phase Locked Loop (PLL).",
                    "Pre-emphasis and de-emphasis circuits, noise in FM receivers."
                ]
            },
            {
                "unit": 3,
                "title": "Pulse Modulation & Digitization",
                "topics": [
                    "Sampling theorem, anti-aliasing filter, PAM, PWM, PPM generation and detection.",
                    "Pulse Code Modulation (PCM): Quantization noise, companding (A-law, mu-law), Delta Modulation (DM), Adaptive Delta Modulation (ADM)."
                ]
            },
            {
                "unit": 4,
                "title": "Digital Bandpass Modulation",
                "topics": [
                    "Binary ASK, FSK, PSK generation and detection, coherent and non-coherent schemes.",
                    "Quadrature Phase Shift Keying (QPSK), Minimum Shift Keying (MSK), Quadrature Amplitude Modulation (QAM).",
                    "Bit Error Rate (BER) calculations, constellation diagrams, eye patterns."
                ]
            },
            {
                "unit": 5,
                "title": "Information Theory & Coding",
                "topics": [
                    "Entropy, information rate, Shannon-Hartley theorem, channel capacity limit.",
                    "Source coding: Huffman coding, Shannon-Fano coding, Error control coding: Linear block codes, cyclic codes, convolutional codes."
                ]
            }
        ],
        "textbooks": [
            "Simon Haykin, 'Communication Systems', John Wiley & Sons.",
            "Herbert Taub and Donald L. Schilling, 'Principles of Communication Systems', McGraw-Hill."
        ]
    }
}
