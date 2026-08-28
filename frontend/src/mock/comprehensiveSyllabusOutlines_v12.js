/**
 * Comprehensive Course Syllabi and Session Plans for all departments - Part 12
 * Mapped to UGC and NBA guidelines.
 */

export const comprehensiveSyllabusOutlines_v12 = {
  MECH: {
    semesters: [
      {
        semester: 5,
        courses: [
          {
            code: "ME303",
            title: "Fluid Mechanics & Hydraulic Machinery",
            units: [
              {
                unit: 1,
                title: "Fluid Properties & Statics",
                topics: [
                  "Fluid definition, properties: density, specific weight, specific volume, viscosity, surface tension, capillarity.",
                  "Fluid statics: Pascal's law, hydrostatic equation, pressure measurement using manometers.",
                  "Hydrostatic forces on submerged plane and curved surfaces, buoyancy, metacentric height stability."
                ],
                learning_objectives: "Verify metacentric heights for floating bodies and calculate hydrostatic force vectors."
              },
              {
                unit: 2,
                title: "Fluid Kinematics & Dynamics",
                topics: [
                  "Types of fluid flow: steady/unsteady, uniform/non-uniform, laminar/turbulent, 1D/2D/3D flows.",
                  "Streamlines, pathlines, streaklines, continuity equation in Cartesian coordinates.",
                  "Fluid dynamics: Euler's equation of motion, Bernoulli's equation derivation and limitations, Venturimeter, Orificemeter."
                ],
                learning_objectives: "Derive differential continuity equations and analyze stream flow rates using venturimeters."
              },
              {
                unit: 3,
                title: "Flow Through Pipes & Boundary Layer",
                topics: [
                  "Laminar flow through circular pipes (Hagen-Poiseuille law), turbulent flow, Darcy-Weisbach equation.",
                  "Minor losses in pipes: sudden expansion, sudden contraction, bends, fittings.",
                  "Boundary layer concepts: thickness, drag and lift, boundary layer separation control."
                ],
                learning_objectives: "Compute friction head losses in pipe networks and apply boundary layer displacement heights."
              },
              {
                unit: 4,
                title: "Impact of Jets & Hydraulic Turbines",
                topics: [
                  "Force exerted by fluid jet on stationary and moving flat and curved vanes, velocity triangles.",
                  "Hydraulic turbines: Classification, Pelton wheel, Francis turbine, Kaplan turbine construction and design.",
                  "Draft tube theory, cavitation in turbines, unit and specific speed parameters."
                ],
                learning_objectives: "Draw inlet/outlet velocity triangles and calculate hydraulic efficiency of Francis runners."
              },
              {
                unit: 5,
                title: "Hydraulic Pumps",
                topics: [
                  "Centrifugal pumps: Working principle, work done, manometric efficiency, minimum starting speed, priming.",
                  "Reciprocating pumps: Working principle, slip, indicator diagram, air vessels."
                ],
                learning_objectives: "Evaluate manometric pump curves and design reciprocating indicator configurations."
              }
            ],
            textbooks: [
              "Frank M. White, 'Fluid Mechanics', McGraw-Hill.",
              "R.K. Bansal, 'A Textbook of Fluid Mechanics and Hydraulic Machines'."
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
            code: "EC501",
            title: "Digital Signal Processing",
            units: [
              {
                unit: 1,
                title: "Discrete Fourier Transform",
                topics: [
                  "Discrete Fourier Transform (DFT): definition, properties (linearity, periodicity, circular convolution).",
                  "Fast Fourier Transform (FFT): Decimation-in-time (DIT) and Decimation-in-frequency (DIF) radix-2 algorithms.",
                  "Linear filtering using DFT: overlap-add and overlap-save methods."
                ],
                learning_objectives: "Derive radix-2 decimation signal flows and compute circular convolution matrices."
              },
              {
                unit: 2,
                title: "IIR Filter Design",
                topics: [
                  "Analog filter approximations: Butterworth and Chebyshev approximations.",
                  "Design of Infinite Impulse Response (IIR) digital filters: impulse invariant transformation, bilinear transformation.",
                  "Realization structures for IIR filters: direct form I, direct form II, cascade, parallel forms."
                ],
                learning_objectives: "Map analog Butterworth poles to discrete z-plane coordinates via bilinear transformation."
              },
              {
                unit: 3,
                title: "FIR Filter Design",
                topics: [
                  "Symmetric and anti-symmetric Finite Impulse Response (FIR) filters, linear phase characteristics.",
                  "Design of FIR filters using windowing techniques: Rectangular, Hamming, Hanning, Blackman, Kaiser windows.",
                  "Frequency sampling method for FIR design, realization structures: direct form, cascade, linear phase."
                ],
                learning_objectives: "Design linear phase FIR windows and realize structures in cascaded modes."
              },
              {
                unit: 4,
                title: "Finite Word Length Effects",
                topics: [
                  "Quantization noise, coefficient quantization errors, product round-off noise.",
                  "Limit cycle oscillations in recursive systems, scaling to prevent overflow."
                ],
                learning_objectives: "Evaluate coefficient quantization noise bounds and prevent limit cycle oscillations."
              },
              {
                unit: 5,
                title: "Multirate DSP & Processors",
                topics: [
                  "Decimation, interpolation, sampling rate conversion by rational factor.",
                  "Applications of multirate DSP: subband coding, filter banks.",
                  "DSP processors architecture: Harvard architecture, pipelining, MAC units."
                ],
                learning_objectives: "Construct polyphase decimation filters and explain Harvard execution pipe stages."
              }
            ],
            textbooks: [
              "John G. Proakis and Dimitris G. Manolakis, 'Digital Signal Processing: Principles, Algorithms, and Applications'.",
              "Alan V. Oppenheim and Ronald W. Schafer, 'Discrete-Time Signal Processing'."
            ]
          }
        ]
      }
    ]
  }
};

export default comprehensiveSyllabusOutlines_v12;
