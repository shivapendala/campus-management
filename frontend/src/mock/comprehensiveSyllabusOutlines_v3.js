/**
 * Comprehensive Course Syllabi and Session Plans for all departments - Part 3
 * Mapped to UGC and NBA guidelines.
 */

export const comprehensiveSyllabusOutlines_v3 = {
  EEE: {
    semesters: [
      {
        semester: 3,
        courses: [
          {
            code: "EE301",
            title: "Electric Circuit Analysis",
            units: [
              {
                unit: 1,
                title: "Basic Circuit Concepts & Topology",
                topics: [
                  "Voltage and current sources, independent and dependent sources, Ohm's law, Kirchhoff's laws.",
                  "Mesh analysis and nodal analysis with dependent and independent sources, supermesh and supernode concepts.",
                  "Network graph theory: Graph, tree, co-tree, incidence matrix, basic loop and cut-set matrices.",
                  "Duality and dual networks, source transformations, star-delta transformations."
                ],
                learning_objectives: "Model physical electric systems and write steady-state loop/node equations."
              },
              {
                unit: 2,
                title: "Network Theorems",
                topics: [
                  "Superposition theorem, Thevenin's and Norton's theorems, maximum power transfer theorem.",
                  "Reciprocity theorem, Millman's theorem, Tellegen's theorem, substitution theorem.",
                  "Application of theorems to DC and AC steady-state circuits, operational amplifier circuits analysis."
                ],
                learning_objectives: "Apply network theorems to simplify linear bilateral electrical networks."
              },
              {
                unit: 3,
                title: "Transient Analysis",
                topics: [
                  "Transient response of RL, RC, and RLC circuits under DC and AC excitations, initial and final conditions.",
                  "Differential equation approach, Laplace transform method, step, ramp, and impulse response analysis.",
                  "S-plane representation, transfer functions, poles and zeros, stability definitions."
                ],
                learning_objectives: "Analyze transient voltages and currents in time and Laplace domains."
              },
              {
                unit: 4,
                title: "AC Resonance & Coupled Circuits",
                topics: [
                  "Series resonance: Bandwidth, quality factor, selectivty, half-power frequencies.",
                  "Parallel resonance: Tank circuit characteristics, dynamic impedance.",
                  "Coupled circuits: Self and mutual inductance, coefficient of coupling, dot convention.",
                  "Analysis of conductively coupled and magnetically coupled circuits, linear transformers."
                ],
                learning_objectives: "Calculate resonant parameters and model dot conventions in magnetic circuits."
              },
              {
                unit: 5,
                title: "Two-Port Network Parameters & Synthesis",
                topics: [
                  "Z, Y, ABCD, inverse ABCD, hybrid, and inverse hybrid parameters, parameter conversions.",
                  "Interconnection of two-port networks (series, parallel, cascade).",
                  "Positive Real (PR) functions, synthesis of driving point impedance functions using Foster and Cauer forms."
                ],
                learning_objectives: "Characterize two-port networks and synthesize driving-point functions."
              }
            ],
            textbooks: [
              "William H. Hayt, Jack E. Kemmerly, and Steven M. Durbin, 'Engineering Circuit Analysis'.",
              "Charles K. Alexander and Matthew N.O. Sadiku, 'Fundamentals of Electric Circuits'."
            ]
          }
        ]
      }
    ]
  },
  CIVIL: {
    semesters: [
      {
        semester: 3,
        courses: [
          {
            code: "CE301",
            title: "Strength of Materials",
            units: [
              {
                unit: 1,
                title: "Simple Stresses & Strains",
                topics: [
                  "Concept of stress, strain, Hooke's law, elastic constants (E, G, K, Poisson's ratio) and their relations.",
                  "Stress-strain curve for mild steel, working stress, factor of safety.",
                  "Thermal stresses and strains in simple and composite bars, elastic deformation under axial loads.",
                  "Strain energy under gradual, sudden, and impact loads, resilience, proof resilience."
                ],
                learning_objectives: "Calculate axial deformation and evaluate relationships among elastic constants."
              },
              {
                unit: 2,
                title: "Shear Force & Bending Moment in Beams",
                topics: [
                  "Types of beams, loads, supports, shear force and bending moment definitions.",
                  "Relationship between load, shear force, and bending moment.",
                  "SFD and BMD for cantilevers, simply supported, and overhanging beams under point loads, UDL, and UVL.",
                  "Point of contraflexure, maximum bending moment coordinates."
                ],
                learning_objectives: "Construct shear force and bending moment diagrams for statically determinate beams."
              },
              {
                unit: 3,
                title: "Flexural & Shear Stresses in Beams",
                topics: [
                  "Theory of simple bending, assumptions, derivation of bending formula (M/I = f/y = E/R).",
                  "Section modulus of rectangular, circular, I, T, and channel sections.",
                  "Shear stress distribution in beams: Derivation of shear stress formula, shear stress profile across standard sections."
                ],
                learning_objectives: "Evaluate bending and shear stresses across engineering cross-sections."
              },
              {
                unit: 4,
                title: "Torsion of Circular Shafts & Helical Springs",
                topics: [
                  "Theory of pure torsion, assumptions, derivation of torsion equation (T/J = fs/r = C*theta/L).",
                  "Power transmission in solid and hollow circular shafts, design of shafts for strength and rigidity.",
                  "Helical springs: Close-coiled and open-coiled helical springs, deflection and stiffness equations."
                ],
                learning_objectives: "Design power transmission shafts and calculate helical spring parameters."
              },
              {
                unit: 5,
                title: "Principal Stresses & Thin Cylinders",
                topics: [
                  "Principal planes and principal stresses, analytical and graphical (Mohr's circle) methods.",
                  "Theories of elastic failure: Maximum principal stress, maximum shear stress, maximum distortion energy theories.",
                  "Thin cylinders and spheres: Hoop stress, longitudinal stress, volumetric strain under internal fluid pressure."
                ],
                learning_objectives: "Compute principal stresses and design thin-walled pressure vessels."
              }
            ],
            textbooks: [
              "R.K. Rajput, 'Strength of Materials (Mechanics of Solids)'.",
              "Ferdinand P. Beer, E. Russell Johnston Jr., and David F. Mazurek, 'Mechanics of Materials'."
            ]
          }
        ]
      }
    ]
  }
};

export default comprehensiveSyllabusOutlines_v3;
