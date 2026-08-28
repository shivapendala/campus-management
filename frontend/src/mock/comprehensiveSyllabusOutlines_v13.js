/**
 * Comprehensive Course Syllabi and Session Plans for all departments - Part 13
 * Mapped to UGC and NBA guidelines.
 */

export const comprehensiveSyllabusOutlines_v13 = {
  EEE: {
    semesters: [
      {
        semester: 7,
        courses: [
          {
            code: "EE701",
            title: "High Voltage Engineering",
            units: [
              {
                unit: 1,
                title: "Conduction & Breakdown in Gases",
                topics: [
                  "Gases as insulating media, collision processes, ionization processes.",
                  "Townsend's criterion for breakdown, Townsend's primary and secondary ionization coefficients.",
                  "Streamer theory of breakdown in gases, Paschen's law and its limitations.",
                  "Breakdown in non-uniform fields and corona discharges, post-breakdown phenomenon."
                ],
                learning_objectives: "Verify primary and secondary ionization coefficients and apply Paschen's Law bounds."
              },
              {
                unit: 2,
                title: "Conduction & Breakdown in Liquids & Solids",
                topics: [
                  "Liquid dielectrics: Pure and commercial liquids, conduction and breakdown in pure liquids.",
                  "Breakdown mechanisms in commercial liquids: suspended particle, cavity, and electroconvection mechanisms.",
                  "Solid dielectrics: Intrinsic breakdown, electromechanical breakdown, thermal breakdown.",
                  "Chemical and electrochemical deterioration, treeing and tracking, partial discharges."
                ],
                learning_objectives: "Identify solid dielectric breakdown mechanisms and design tracking-free insulation."
              },
              {
                unit: 3,
                title: "Generation of High Voltages & Currents",
                topics: [
                  "Generation of high DC voltages: Half-wave and full-wave rectifier circuits, Cockcroft-Walton voltage multiplier.",
                  "Generation of high AC voltages: Cascaded transformers, resonant transformers.",
                  "Generation of impulse voltages: Single-stage and multi-stage Marx impulse generator circuits.",
                  "Generation of impulse currents, tripping and control of impulse generators."
                ],
                learning_objectives: "Design Marx generator circuit loops and calculate output impulse wavefront steps."
              },
              {
                unit: 4,
                title: "Measurement of High Voltages & Currents",
                topics: [
                  "Peak voltage measurements: Sphere gaps, electrostatic voltmeters.",
                  "Generating voltmeters, peak reading AC voltmeters, voltage dividers (resistive, capacitive).",
                  "Measurement of high DC, AC, and impulse currents: Hall generators, Rogowski coils, shunts."
                ],
                learning_objectives: "Configure capacitive voltage dividers and calibrate sphere gap measurement spacings."
              },
              {
                unit: 5,
                title: "High Voltage Testing & Insulation Coordination",
                topics: [
                  "Testing of insulators, bushings, cables, and transformers: destructive and non-destructive tests.",
                  "Radio interference measurements, insulation coordination: statistical approach, surge arresters."
                ],
                learning_objectives: "Formulate surge arrester coordination curves and perform non-destructive tests."
              }
            ],
            textbooks: [
              "M.S. Naidu and V. Kamaraju, 'High Voltage Engineering'.",
              "C.L. Wadhwa, 'High Voltage Engineering', New Age International."
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
            code: "EC702",
            title: "Radar & Satellite Communication",
            units: [
              {
                unit: 1,
                title: "Radar Equations & Types",
                topics: [
                  "Radar basic principles, range equation, radar block diagram, operation frequencies.",
                  "Minimum detectable signal, receiver noise, radar cross-section of targets.",
                  "Pulse repetition frequency, range ambiguities, system losses.",
                  "CW and Frequency-Modulated Radar: Doppler effect, FMCW radar, altimeters."
                ],
                learning_objectives: "Calculate target radar cross sections and solve maximum radar range formulas."
              },
              {
                unit: 2,
                title: "MTI & Tracking Radar",
                topics: [
                  "MTI radar: Delay-line cancelers, blind speeds, double cancellation, staggered PRFs.",
                  "Muser-limiter, tracking radars: Sequential lobing, conical scan, monopulse tracking (amplitude and phase)."
                ],
                learning_objectives: "Compute blind speed bounds in MTI systems and analyze monopulse tracking feeds."
              },
              {
                unit: 3,
                title: "Satellite Orbits & Kepler's Laws",
                topics: [
                  "Satellite history, orbital mechanics, Kepler's laws of planetary motion.",
                  "Locating the satellite in orbit, look angles (elevation and azimuth angles) calculation.",
                  "Orbital perturbations, launches and launch vehicles, geostationary orbit parameters."
                ],
                learning_objectives: "Calculate satellite look angles and compute orbital perturbation periods."
              },
              {
                unit: 4,
                title: "Satellite Subsystems & Space Link",
                topics: [
                  "Subsystems: Attitude and orbit control, telemetry, tracking, command, power systems, transponders.",
                  "Satellite link design: Basic transmission theory, system noise temperature, G/T ratio.",
                  "Design of downlinks and uplinks under rain fade conditions, link budgets calculations."
                ],
                learning_objectives: "Formulate uplink/downlink link budgets and compute equivalent system G/T ratios."
              },
              {
                unit: 5,
                title: "GPS & Satellite Services",
                topics: [
                  "Global Positioning System (GPS): Segment organization, GPS codes, position determination.",
                  "Direct Broadcast Satellite (DBS) television, satellite internet services, VSAT networks."
                ],
                learning_objectives: "Explain GPS triangulation methods and configure VSAT network topology."
              }
            ],
            textbooks: [
              "Merrill I. Skolnik, 'Introduction to Radar Systems'.",
              "Dennis Roddy, 'Satellite Communications'."
            ]
          }
        ]
      }
    ]
  }
};

export default comprehensiveSyllabusOutlines_v13;
