/**
 * Comprehensive Course Syllabi and Session Plans for all departments - Part 8
 * Mapped to UGC and NBA guidelines.
 */

export const comprehensiveSyllabusOutlines_v8 = {
  MECH: {
    semesters: [
      {
        semester: 7,
        courses: [
          {
            code: "ME701",
            title: "Computer Aided Design & Manufacturing",
            units: [
              {
                unit: 1,
                title: "CAD/CAM Foundations & Computer Graphics",
                topics: [
                  "Product lifecycle management (PLM), CAD/CAM hardware, product design cycle.",
                  "Raster graphics, scan conversion algorithms, coordinate systems.",
                  "2D and 3D geometric transformations: Translation, scaling, rotation, shearing, reflection.",
                  "Viewing transformations, windowing, clipping algorithms, hidden line removal."
                ],
                learning_objectives: "Apply 2D/3D affine transformation matrices and compute viewing projections."
              },
              {
                unit: 2,
                title: "Geometric Modeling",
                topics: [
                  "Wireframe modeling, surface modeling, solid modeling (CSG, B-Rep).",
                  "Curve representations: Parametric representation of analytic curves, synthetic curves (Bezier, B-Spline, NURBS).",
                  "Surface patches, solid modeling packages, CAD data exchange standards (IGES, STEP)."
                ],
                learning_objectives: "Construct parametric representations of Bezier and B-Spline curves."
              },
              {
                unit: 3,
                title: "NC/CNC Machine Tools",
                topics: [
                  "Numerical Control (NC) systems, CNC systems, DNC systems, machine coordinates, axes nomenclature.",
                  "CNC machine structural components: Ball screws, linear guideways, automatic tool changers (ATC).",
                  "Feedback devices: Rotary encoders, linear scales, servo motors, interpolators."
                ],
                learning_objectives: "Explain CNC mechanical feedback control elements and identify axes coordinates."
              },
              {
                unit: 4,
                title: "CNC Part Programming",
                topics: [
                  "G-codes and M-codes for milling and turning operations.",
                  "Manual part programming: Linear and circular interpolation, canned cycles, subroutines.",
                  "Computer-assisted part programming: APT language, CAD/CAM integration for toolpath generation."
                ],
                learning_objectives: "Write manual G-code and M-code programs for CNC milling/turning paths."
              },
              {
                unit: 5,
                title: "Group Technology & FMS",
                topics: [
                  "Group technology: Part families, classification and coding systems (Opitz, MICLASS), cell design.",
                  "Flexible Manufacturing Systems (FMS): Workstations, material handling systems, control systems, layouts.",
                  "Computer Integrated Manufacturing (CIM), automated guided vehicles (AGVs), automated storage and retrieval systems (ASRS)."
                ],
                learning_objectives: "Design group technology layout cells using classification systems."
              }
            ],
            textbooks: [
              "Mikell P. Groover, 'Automation, Production Systems, and Computer-Integrated Manufacturing'.",
              "Ibrahim Zeid, 'CAD/CAM: Theory and Practice'."
            ]
          }
        ]
      }
    ]
  },
  ECE: {
    semesters: [
      {
        semester: 7,
        courses: [
          {
            code: "EC701",
            title: "Microwave Engineering & Antennas",
            units: [
              {
                unit: 1,
                title: "Waveguides & Cavity Resonators",
                topics: [
                  "Introduction to microwave bands, rectangular waveguides: TE and TM modes, power transmission and losses.",
                  "Circular waveguides: TE and TM modes analysis, cutoff frequencies.",
                  "Rectangular and cylindrical cavity resonators, Q factor evaluation, excitation of modes in waveguides."
                ],
                learning_objectives: "Analyze boundary conditions in rectangular waveguides and calculate cutoff frequencies."
              },
              {
                unit: 2,
                title: "Microwave Components & Scattering Matrix",
                topics: [
                  "Scattering parameters: Definition, properties of S-matrix (reciprocity, losslessness).",
                  "Waveguide tees: E-plane tee, H-plane tee, Magic tee, applications.",
                  "Directional couplers, isolators, circulators, phase shifters, attenuators."
                ],
                learning_objectives: "Derive scattering (S) matrices for waveguide Tees and directional couplers."
              },
              {
                unit: 3,
                title: "Microwave Tubes & Solid State Devices",
                topics: [
                  "Limitations of conventional tubes, Two-cavity Klystron amplifier, Reflex Klystron oscillator.",
                  "Traveling Wave Tube (TWT) amplifier, Magnetron oscillator (pi-mode, tuning).",
                  "Microwave solid-state devices: Gunn diode (TED), IMPATT diode, TRAPATT diode, tunnel diode."
                ],
                learning_objectives: "Explain velocity modulation principles and calculate Gunn diode modes."
              },
              {
                unit: 4,
                title: "Antenna Fundamentals & Radiating Elements",
                topics: [
                  "Antenna parameters: Radiation pattern, directivity, gain, radiation resistance, beamwidth, polarization.",
                  "Radiation fields of Hertzian dipole, half-wave dipole, quarter-wave monopole.",
                  "Loop antennas, folded dipole, slot antennas, patch microstrip antennas."
                ],
                learning_objectives: "Compute radiating electromagnetic fields for half-wave dipoles."
              },
              {
                unit: 5,
                title: "Antenna Arrays & Propagation",
                topics: [
                  "Antenna arrays: Broadside array, end-fire array, phased arrays, multiplication of patterns.",
                  "Wave propagation: Ground wave, sky wave, space wave propagation, skip distance, ionosphere characteristics."
                ],
                learning_objectives: "Design end-fire antenna arrays and calculate ionosphere skip distances."
              }
            ],
            textbooks: [
              "Samuel Y. Liao, 'Microwave Devices and Circuits'.",
              "Constantine A. Balanis, 'Antenna Theory: Analysis and Design'."
            ]
          }
        ]
      }
    ]
  }
};

export default comprehensiveSyllabusOutlines_v8;
