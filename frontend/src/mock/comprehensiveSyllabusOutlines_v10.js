/**
 * Comprehensive Course Syllabi and Session Plans for all departments - Part 10
 * Mapped to UGC and NBA guidelines.
 */

export const comprehensiveSyllabusOutlines_v10 = {
  EEE: {
    semesters: [
      {
        semester: 6,
        courses: [
          {
            code: "EE601",
            title: "Power System Protection & Switchgear",
            units: [
              {
                unit: 1,
                title: "Electromagnetic Relays & Fuses",
                topics: [
                  "Need for protection, faults classifications, zones of protection.",
                  "Fuses: HRC fuses construction and characteristics, selection of fuses.",
                  "Electromagnetic relays: Attracted armature, induction disc and induction cup relays.",
                  "Overcurrent, directional, distance, and differential relays structures."
                ],
                learning_objectives: "Classify fault types and select appropriate HRC fuse ratings for simple networks."
              },
              {
                unit: 2,
                title: "Circuit Breakers & Arc Interruption",
                topics: [
                  "Arc initiation and interruption theories: Slepian's and Cassie's theories.",
                  "Restriking voltage, recovery voltage, Rate of Rise of Restriking Voltage (RRRV).",
                  "Types of circuit breakers: Air break, Oil, Minimum Oil, SF6, and Vacuum circuit breakers.",
                  "Testing of circuit breakers, mechanical and electrical properties."
                ],
                learning_objectives: "Derive formulas for RRRV and explain the physical principles of SF6 arc quenching."
              },
              {
                unit: 3,
                title: "Apparatus Protection",
                topics: [
                  "Generator protection: Stator faults, rotor faults, unbalanced loading, overspeed protection.",
                  "Transformer protection: Buchholz relay, percentage differential protection, harmonic restraint.",
                  "Motor protection: Stalling, single phasing, thermal overload protection."
                ],
                learning_objectives: "Design differential protection circuits for three-phase power transformers."
              },
              {
                unit: 4,
                title: "Transmission Line Protection",
                topics: [
                  "Time-graded and current-graded overcurrent protection, 3-zone distance protection.",
                  "Carrier-current protection: Phase comparison and directional comparison schemes.",
                  "Busbar protection: Differential protection, frame leakage protection."
                ],
                learning_objectives: "Calculate time-multiplier settings for overcurrent relay cascades."
              },
              {
                unit: 5,
                title: "Static & Numerical Relays",
                topics: [
                  "Static relays: Amplitude and phase comparators, static overcurrent relay.",
                  "Numerical protection: Block diagram of numerical relay, sampling theorem, DSP algorithms.",
                  "Microprocessor-based relay hardware configurations, software flowcharts."
                ],
                learning_objectives: "Implement basic discrete algorithms for numerical overcurrent filtering."
              }
            ],
            textbooks: [
              "Badri Ram and D.N. Vishwakarma, 'Power System Protection and Switchgear'.",
              "Y.G. Paithankar and S.R. Bhide, 'Fundamentals of Power System Protection'."
            ]
          }
        ]
      }
    ]
  },
  CIVIL: {
    semesters: [
      {
        semester: 7,
        courses: [
          {
            code: "CE701",
            title: "Transportation Engineering",
            units: [
              {
                unit: 1,
                title: "Highway Planning & Alignment",
                topics: [
                  "History of road development, Jayakar committee recommendations, Nagpur/Bombay/Lucknow road plans.",
                  "Highway classification, highway alignment: Factors controlling alignment, engineering surveys.",
                  "Geometric design of highways: Cross-sectional elements, camber, sight distances (SSD, OSD)."
                ],
                learning_objectives: "Plan highway layouts and compute stopping sight distances on horizontal straights."
              },
              {
                unit: 2,
                title: "Horizontal & Vertical Alignment",
                topics: [
                  "Horizontal alignment: Super-elevation design, transition curves, extra widening on curves.",
                  "Vertical alignment: Gradients, summit and valley curves geometric formulas."
                ],
                learning_objectives: "Design transition curves and calculate summit curve lengths for target speeds."
              },
              {
                unit: 3,
                title: "Traffic Engineering & Control",
                topics: [
                  "Traffic characteristics: Volume, speed, density studies, speed-flow relationships.",
                  "Traffic signs, signals design by Webster's method, road markings, rotary intersections."
                ],
                learning_objectives: "Evaluate speed-density distributions and design traffic light phase timers."
              },
              {
                unit: 4,
                title: "Pavement Materials & Design",
                topics: [
                  "Subgrade soil evaluation: CBR test, plate bearing test, aggregates properties.",
                  "Design of flexible pavements: IRC 37 guidelines, structural layers calculation.",
                  "Design of rigid pavements: IRC 58 guidelines, Westergaard's stress equations."
                ],
                learning_objectives: "Design asphalt and rigid concrete structural pavement thicknesses."
              },
              {
                unit: 5,
                title: "Highway Construction & Maintenance",
                topics: [
                  "Construction steps: WBM, WMM, Bituminous concrete, cement concrete roads.",
                  "Pavement failures: Distresses in flexible and rigid pavements, maintenance strategies."
                ],
                learning_objectives: "Select maintenance overlays and diagnose pavement cracking/rutting failures."
              }
            ],
            textbooks: [
              "S.K. Khanna, C.E.G. Justo, and A. Veeraragavan, 'Highway Engineering'.",
              "L.R. Kadiyali, 'Traffic Engineering and Transportation Planning'."
            ]
          }
        ]
      }
    ]
  }
};

export default comprehensiveSyllabusOutlines_v10;
