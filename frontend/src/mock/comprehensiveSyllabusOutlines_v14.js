/**
 * Comprehensive Course Syllabi and Session Plans for all departments - Part 14
 * Mapped to UGC and NBA guidelines.
 */

export const comprehensiveSyllabusOutlines_v14 = {
  MECH: {
    semesters: [
      {
        semester: 8,
        courses: [
          {
            code: "ME801",
            title: "Mechanical Vibrations",
            units: [
              {
                unit: 1,
                title: "Single Degree of Freedom Systems - Free Vibrations",
                topics: [
                  "Introduction to vibrations, simple harmonic motion, elements of vibratory systems.",
                  "Undamped free vibrations: Newton's method, energy method, Rayleigh's method.",
                  "Damped free vibrations: Viscous damping, underdamped, critically damped, logarithmic decrement.",
                  "Coulomb damping, dry friction vibration models."
                ],
                learning_objectives: "Formulate differential free-vibration equations and determine logarithmic decrements."
              },
              {
                unit: 2,
                title: "Single Degree of Freedom Systems - Forced Vibrations",
                topics: [
                  "Forced vibration with harmonic excitation, steady-state response, magnification factor.",
                  "Vibration isolation and transmissibility, force transmissibility, motion transmissibility.",
                  "Rotating unbalance, whirling of rotating shafts, support motion excitation.",
                  "Vibration measuring instruments: Seismometer, accelerometer."
                ],
                learning_objectives: "Design vibration isolation systems and compute critical whirling speeds."
              },
              {
                unit: 3,
                title: "Two Degree of Freedom Systems",
                topics: [
                  "Equations of motion for coordinate coupling, natural frequencies and mode shapes.",
                  "Coordinate systems, principal coordinates, orthogonal properties of modes.",
                  "Dynamic vibration absorber design, coordinate coupling transformations."
                ],
                learning_objectives: "Formulate coordinate coupling matrices and design dynamic vibration absorbers."
              },
              {
                unit: 4,
                title: "Multi-Degree of Freedom Systems",
                topics: [
                  "Influence coefficients: Stiffness influence coefficients, flexibility influence coefficients.",
                  "Eigenvalue problem formulation, matrix iteration method for fundamental frequency.",
                  "Approximate methods: Dunkerley's equation, Rayleigh-Ritz method, Holzer's method for torsional vibrations."
                ],
                learning_objectives: "Apply Dunkerley's and Holzer's methods to estimate multi-rotor natural frequencies."
              },
              {
                unit: 5,
                title: "Continuous Systems & Vibration Control",
                topics: [
                  "Vibrations of continuous systems: Transverse vibration of a string, longitudinal vibration of a rod.",
                  "Torsional vibration of a shaft, lateral vibration of a beam.",
                  "Vibration dampers, active vibration control, noise control standards."
                ],
                learning_objectives: "Derive wave equations for strings and beams and select industrial damping treatments."
              }
            ],
            textbooks: [
              "Singiresu S. Rao, 'Mechanical Vibrations'.",
              "G.K. Grover, 'Mechanical Vibrations'."
            ]
          }
        ]
      }
    ]
  },
  CIVIL: {
    semesters: [
      {
        semester: 8,
        courses: [
          {
            code: "CE802",
            title: "Advanced Design of Steel Structures",
            units: [
              {
                unit: 1,
                title: "Plate Girders with Lateral Loading",
                topics: [
                  "Design of gantry girders: Loads, forces, design parameters, deflection checks.",
                  "Plate girders: Web buckling under patch loading, design of end panels, tension field action.",
                  "Stiffeners design: Intermediate stiffeners, load-bearing stiffeners."
                ],
                learning_objectives: "Design industrial gantry girders and verify tension field shear capacities."
              },
              {
                unit: 2,
                title: "Industrial Buildings & Portals",
                topics: [
                  "Design of industrial portal frames, braced and unbraced frames.",
                  "Columns under combined axial force and bending moments, design of column brackets.",
                  "Design of girts and purlins under wind loads."
                ],
                learning_objectives: "Analyze portal frames under combined loads and design eccentric bracket joints."
              },
              {
                unit: 3,
                title: "Steel Water Tanks",
                topics: [
                  "Design of elevated circular and rectangular steel water tanks, design of staging.",
                  "Wind forces and seismic forces calculations on steel water tanks."
                ],
                learning_objectives: "Design elevated structural steel water tanks and stage column bracing."
              },
              {
                unit: 4,
                title: "Plastic Analysis & Design",
                topics: [
                  "Plastic behavior of structural steel, plastic hinge concept, shape factors of sections.",
                  "Upper and lower bound theorems of plastic collapse.",
                  "Plastic analysis of continuous beams, single-bay portal frames, design parameters."
                ],
                learning_objectives: "Compute plastic collapse mechanisms and determine shape factor multipliers."
              },
              {
                unit: 5,
                title: "Light Gauge Steel Structures",
                topics: [
                  "Introduction to cold-formed steel sections, types of sections, design specifications.",
                  "Local buckling of plates, effective width concept, design of light gauge tension and compression members."
                ],
                learning_objectives: "Design cold-formed steel structural panels using effective width calculations."
              }
            ],
            textbooks: [
              "N. Subramanian, 'Design of Steel Structures'.",
              "S.K. Duggal, 'Limit State Design of Steel Structures'."
            ]
          }
        ]
      }
    ]
  }
};

export default comprehensiveSyllabusOutlines_v14;
