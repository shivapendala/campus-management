/**
 * Comprehensive Course Syllabi and Session Plans for all departments - Part 9
 * Mapped to UGC and NBA guidelines.
 */

export const comprehensiveSyllabusOutlines_v9 = {
  MECH: {
    semesters: [
      {
        semester: 5,
        courses: [
          {
            code: "ME302",
            title: "Kinematics of Machinery",
            units: [
              {
                unit: 1,
                title: "Mechanisms & Machines",
                topics: [
                  "Links, pairs, kinematic chains, degrees of freedom, Kutzbach criterion, Grubler's criterion.",
                  "Inversions of four bar chain, single slider crank chain, double slider crank chain.",
                  "Grashof's law, straight line motion mechanisms, steering gear mechanisms (Davis, Ackerman)."
                ],
                learning_objectives: "Verify degrees of freedom in planar kinematic chains and describe mechanism inversions."
              },
              {
                unit: 2,
                title: "Velocity & Acceleration Analysis",
                topics: [
                  "Relative velocity method, instantaneous center method, Kennedy's theorem.",
                  "Relative acceleration method, Coriolis component of acceleration, Klein's construction."
                ],
                learning_objectives: "Compute velocity and acceleration profiles using relative vector methods."
              },
              {
                unit: 3,
                title: "Cams & Followers",
                topics: [
                  "Classification of cams and followers, radial cam profile generation.",
                  "Follower motions: Uniform velocity, simple harmonic motion (SHM), uniform acceleration and retardation (UARM), cycloidal motion.",
                  "Cams with specified contours: Tangent cam, circular arc cam."
                ],
                learning_objectives: "Draw displacement curves and construct cam profiles for SHM/cycloidal follower motions."
              },
              {
                unit: 4,
                title: "Gears & Gear Trains",
                topics: [
                  "Classification of gears, law of gearing, tooth profiles (involute and cycloidal).",
                  "Interference and undercutting, minimum number of teeth to avoid interference.",
                  "Gear trains: Simple, compound, reverted, epicyclic gear trains, torques in epicyclic gear trains."
                ],
                learning_objectives: "Select gear modules to avoid tooth interference and analyze epicyclic gear train speeds."
              },
              {
                unit: 5,
                title: "Gyroscopic Effects & Governors",
                topics: [
                  "Gyroscopic couple: Effect on naval ships, airplanes, four-wheeled and two-wheeled vehicles.",
                  "Governors: Watt, Porter, Proell, Hartnell governors, sensitivity, stability, hunting, isochronism."
                ],
                learning_objectives: "Calculate gyroscopic couples on naval vessels and determine governor stabilization margins."
              }
            ],
            textbooks: [
              "Thomas Bevan, 'Theory of Machines', Pearson.",
              "S.S. Rattan, 'Theory of Machines', Tata McGraw-Hill."
            ]
          }
        ]
      }
    ]
  },
  ECE: {
    semesters: [
      {
        semester: 5,
        courses: [
          {
            code: "EC502",
            title: "Analog & Digital Communication",
            units: [
              {
                unit: 1,
                title: "Amplitude Modulation",
                topics: [
                  "Need for modulation, Amplitude Modulation (AM): DSB-FC, DSB-SC, SSB-SC, VSB signal generation and demodulation.",
                  "AM transmitters, superheterodyne receivers, envelope detectors, coherent detection, noise in AM systems."
                ],
                learning_objectives: "Analyze power efficiency of amplitude modulation schemes and design envelope detectors."
              },
              {
                unit: 2,
                title: "Angle Modulation",
                topics: [
                  "Frequency Modulation (FM) and Phase Modulation (PM), narrow-band and wide-band FM.",
                  "Generation of FM: Direct and indirect (Armstrong) methods, FM demodulators: Slope detector, ratio detector, Phase Locked Loop (PLL).",
                  "Pre-emphasis and de-emphasis circuits, noise in FM receivers."
                ],
                learning_objectives: "Derive FM spectra and configure phase-locked loop frequency discriminators."
              },
              {
                unit: 3,
                title: "Pulse Modulation & Digitization",
                topics: [
                  "Sampling theorem, anti-aliasing filter, PAM, PWM, PPM generation and detection.",
                  "Pulse Code Modulation (PCM): Quantization noise, companding (A-law, mu-law), Delta Modulation (DM), Adaptive Delta Modulation (ADM)."
                ],
                learning_objectives: "Verify sampling criteria and compute PCM quantization noise signal-to-noise ratios."
              },
              {
                unit: 4,
                title: "Digital Bandpass Modulation",
                topics: [
                  "Binary ASK, FSK, PSK generation and detection, coherent and non-coherent schemes.",
                  "Quadrature Phase Shift Keying (QPSK), Minimum Shift Keying (MSK), Quadrature Amplitude Modulation (QAM).",
                  "Bit Error Rate (BER) calculations, constellation diagrams, eye patterns."
                ],
                learning_objectives: "Plot constellation mappings and calculate bit error probabilities for digital carrier keys."
              },
              {
                unit: 5,
                title: "Information Theory & Coding",
                topics: [
                  "Entropy, information rate, Shannon-Hartley theorem, channel capacity limit.",
                  "Source coding: Huffman coding, Shannon-Fano coding, Error control coding: Linear block codes, cyclic codes, convolutional codes."
                ],
                learning_objectives: "Compute source codes entropy and calculate parity verification cyclic redundancy check blocks."
              }
            ],
            textbooks: [
              "Simon Haykin, 'Communication Systems', John Wiley & Sons.",
              "Herbert Taub and Donald L. Schilling, 'Principles of Communication Systems'."
            ]
          }
        ]
      }
    ]
  }
};

export default comprehensiveSyllabusOutlines_v9;
