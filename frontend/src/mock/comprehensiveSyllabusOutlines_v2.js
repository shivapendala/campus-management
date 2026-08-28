/**
 * Comprehensive Course Syllabi and Session Plans for all departments - Part 2
 * Mapped to UGC and NBA guidelines.
 */

export const comprehensiveSyllabusOutlines_v2 = {
  ECE: {
    semesters: [
      {
        semester: 3,
        courses: [
          {
            code: "EC301",
            title: "Electronic Circuits & Semiconductor Devices",
            units: [
              {
                unit: 1,
                title: "Semiconductor Physics, PN Junction & Special Diodes",
                topics: [
                  "Energy bands in semiconductors, Intrinsic and extrinsic semiconductors, carrier concentrations.",
                  "Drift and diffusion currents, continuity equation, PN junction diode forward and reverse bias.",
                  "Diode current equation, transition and diffusion capacitances, reverse recovery time.",
                  "Zener diode breakdown mechanisms, tunnel diode, varactor diode, Schottky diode.",
                  "Photodiode, Light Emitting Diode (LED) principles and specifications."
                ],
                learning_objectives: "Understand carrier transport in semiconductors and analyze special-purpose diodes."
              },
              {
                unit: 2,
                title: "BJT & Biasing",
                topics: [
                  "BJT physical structure and operation, CB, CE, CC configurations, input and output curves.",
                  "Transistor as an amplifier and switch, need for biasing, Q-point stabilization.",
                  "Biasing methods: Fixed bias, collector-to-base, voltage divider / self bias.",
                  "Thermal runaway, stability factors S, S', S'', thermal stabilization."
                ],
                learning_objectives: "Design stable biasing networks for BJT amplifiers and prevent thermal runaway."
              },
              {
                unit: 3,
                title: "Field Effect Transistors",
                topics: [
                  "JFET physical structure, pinch-off voltage, drain and transfer characteristics.",
                  "JFET small signal model, MOSFET: Enhancement and depletion mode operations.",
                  "Threshold voltage, output characteristics, subthreshold conduction, short-channel effects.",
                  "Comparison between BJT, JFET, and MOSFET parameters."
                ],
                learning_objectives: "Analyze JFET and MOSFET static characteristics and construct small-signal models."
              },
              {
                unit: 4,
                title: "Low-Frequency Small Signal Amplifiers",
                "topics": [
                  "BJT hybrid (h-parameter) model, analysis of CE, CB, CC amplifiers.",
                  "Calculation of Av, Ai, Zi, Zo parameters using exact and approximate h-models.",
                  "MOSFET small signal low-frequency model, CS, CD, CG amplifiers analysis.",
                  "Biasing configurations of CS/CD amplifiers."
                ],
                learning_objectives: "Calculate voltage and current gain for single-stage BJT and MOSFET amplifiers."
              },
              {
                unit: 5,
                title: "Power and Tuned Amplifiers",
                topics: [
                  "Power amplifier classification: Class A, B, AB, C, D efficiency limits.",
                  "Transformer-coupled Class A amplifier, Class B push-pull and complementary symmetry.",
                  "Crossover distortion, heat sinks, tuned amplifiers: Single-tuned and double-tuned designs."
                ],
                learning_objectives: "Analyze efficiency constraints of power amplifiers and design tuned resonant tanks."
              }
            ],
            textbooks: [
              "Robert L. Boylestad and Louis Nashelsky, 'Electronic Devices and Circuit Theory'.",
              "Jacob Millman, Christos Halkias, and Satyabrata Jit, 'Electronic Devices and Circuits'."
            ]
          }
        ]
      }
    ]
  },
  MECH: {
    semesters: [
      {
        semester: 3,
        courses: [
          {
            code: "ME301",
            title: "Engineering Thermodynamics",
            units: [
              {
                unit: 1,
                title: "First Law of Thermodynamics",
                topics: [
                  "Microscopic and macroscopic view, state, properties, process, cyclic configurations.",
                  "First Law applied to non-flow processes (isothermal, adiabatic, polytropic).",
                  "Steady Flow Energy Equation (SFEE) applied to nozzles, diffusers, turbines, and compressors."
                ],
                learning_objectives: "Apply First Law conservation of energy to open and closed thermodynamic systems."
              },
              {
                unit: 2,
                title: "Second Law & Entropy",
                topics: [
                  "Limitations of First Law, Kelvin-Planck and Clausius statements, Carnot cycle.",
                  "Clausius inequality, entropy changes of ideal gases, exergy availability, dead state."
                ],
                learning_objectives: "Analyze thermodynamic cycle reversibility and compute entropy generation."
              },
              {
                unit: 3,
                title: "Pure Substances & Steam Cycles",
                topics: [
                  "Phase change diagrams of water (P-V, T-s, h-s Mollier), dry fraction.",
                  "Vapor power Rankine cycle, reheat and regenerative feed heating.",
                  "Supercritical power cycle configurations, binary vapor cycles."
                ],
                learning_objectives: "Analyze steam power plant efficiency and optimize feedwater heating."
              },
              {
                unit: 4,
                title: "Gas Power Cycles",
                topics: [
                  "Air standard Otto cycle, Diesel cycle, Dual combustion cycles.",
                  "Gas turbine Brayton cycle with regeneration, intercooling, reheat.",
                  "Morse test for multi-cylinder IC engine performance analysis."
                ],
                learning_objectives: "Calculate air-standard efficiency for gas power cycles and evaluate IC engine curves."
              },
              {
                unit: 5,
                title: "Psychrometry & Refrigeration",
                topics: [
                  "Psychrometric charts, sensible heating, cooling dehumidification, bypass factor.",
                  "Vapor Compression Refrigeration System (VCRS) cycle math, COP calculation.",
                  "Vapor Absorption Refrigeration System (VARS) overview, refrigerants selection."
                ],
                learning_objectives: "Design simple air conditioning systems and calculate refrigeration COP."
              }
            ],
            textbooks: [
              "Yunus A. Cengel and Michael A. Boles, 'Thermodynamics: An Engineering Approach'.",
              "P.K. Nag, 'Engineering Thermodynamics', Tata McGraw-Hill."
            ]
          }
        ]
      }
    ]
  }
};

export default comprehensiveSyllabusOutlines_v2;
