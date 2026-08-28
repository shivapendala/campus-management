/**
 * Comprehensive Course Syllabi and Session Plans for all departments - Part 7
 * Mapped to UGC and NBA guidelines.
 */

export const comprehensiveSyllabusOutlines_v7 = {
  EEE: {
    semesters: [
      {
        semester: 6,
        courses: [
          {
            code: "EE502",
            title: "Control Systems Engineering",
            units: [
              {
                unit: 1,
                title: "Control System Modeling",
                topics: [
                  "Introduction to control systems, open loop and closed loop systems.",
                  "Mathematical modeling of physical systems: Differential equations of translational and rotational mechanical systems.",
                  "Electrical systems, transfer function, block diagram reduction techniques.",
                  "Signal Flow Graph (SFG), Mason's gain formula and applications."
                ],
                learning_objectives: "Formulate differential state models for mechanical/electrical dynamics and simplify SFG graphs."
              },
              {
                unit: 2,
                title: "Time Response Analysis",
                topics: [
                  "Standard test signals: Step, ramp, parabolic, impulse.",
                  "Time response of first-order systems, transient response of second-order systems.",
                  "Time domain specifications: Delay time, rise time, peak time, settling time, peak overshoot.",
                  "Steady-state errors, error constants (Kp, Kv, Ka) for Type 0, 1, 2 systems.",
                  "Effects of proportional, integral, and derivative (PID) control actions."
                ],
                learning_objectives: "Calculate time-domain specification metrics and determine steady-state tracking error bounds."
              },
              {
                unit: 3,
                title: "Stability in Time Domain",
                topics: [
                  "Concept of stability, absolute, relative, and conditional stability.",
                  "Routh-Hurwitz stability criterion: Necessary and sufficient conditions, special cases.",
                  "Root Locus technique: Rules for construction of root loci, determination of stability from root locus."
                ],
                learning_objectives: "Verify absolute system stability using Routh criteria and plot root locus paths."
              },
              {
                unit: 4,
                title: "Frequency Response Analysis",
                topics: [
                  "Frequency domain specifications: Resonant peak, resonant frequency, bandwidth.",
                  "Bode plots: Determination of gain margin, phase margin, and stability.",
                  "Polar plots, Nyquist stability criterion, relative stability using Nyquist plot."
                ],
                learning_objectives: "Construct asymptotic Bode diagrams and determine closed-loop stability margins."
              },
              {
                unit: 5,
                title: "State Variable Analysis",
                topics: [
                  "State space representation of continuous-time systems: State equations, state transition matrix.",
                  "Computation of state transition matrix, transfer function from state model.",
                  "Concepts of controllability and observability: Kalman's and Gilbert's tests.",
                  "State feedback controller design, pole placement techniques."
                ],
                learning_objectives: "Assess systems controllability/observability matrices and compute state feedback gains."
              }
            ],
            textbooks: [
              "I.J. Nagrath and M. Gopal, 'Control Systems Engineering'.",
              "Benjamin C. Kuo, 'Automatic Control Systems', John Wiley & Sons."
            ]
          }
        ]
      }
    ]
  },
  CIVIL: {
    semesters: [
      {
        semester: 6,
        courses: [
          {
            code: "CE601",
            title: "Design of Steel Structures",
            units: [
              {
                unit: 1,
                title: "Structural Fasteners",
                topics: [
                  "Properties of structural steel, rolled steel sections, limit state design philosophy.",
                  "Bolted connections: Types of bolts, behavior of bolted joints, design of strength of joint, efficiency.",
                  "Welded connections: Types and behavior of welds, design of fillet and butt welds, eccentric connections."
                ],
                learning_objectives: "Design high-strength bolted and fillet welded connections under eccentric loads."
              },
              {
                unit: 2,
                title: "Tension Members",
                topics: [
                  "Behavior of tension members, modes of failure: yielding of gross section, rupture of critical section, block shear.",
                  "Design of plate and angle tension members, lug angles application."
                ],
                learning_objectives: "Calculate tension member load capacities accounting for block shear failures."
              },
              {
                unit: 3,
                title: "Compression Members",
                topics: [
                  "Elastic buckling of columns, Euler's formula, effective length configurations.",
                  "Design of compression members, built-up columns, design of lacings and battens.",
                  "Design of column bases: Slab base, gusseted base design."
                ],
                learning_objectives: "Design column shafts, lacing matrices, and slab/gusseted base plates."
              },
              {
                unit: 4,
                title: "Flexural Members & Beams",
                topics: [
                  "Behavior of beams in bending, plastic moment capacity, lateral torsional buckling.",
                  "Design of laterally supported and laterally unsupported beams, built-up beams.",
                  "Web buckling, web crippling, design of bearing plates."
                ],
                learning_objectives: "Design laterally supported steel beams and check web crippling criteria."
              },
              {
                unit: 5,
                title: "Plate Girders & Roof Trusses",
                topics: [
                  "Plate girder components: Web, flange, stiffeners (bearing, intermediate, longitudinal).",
                  "Design of plate girders under bending and shear limit states.",
                  "Roof trusses: Loads, design of purlins, design of truss members."
                ],
                learning_objectives: "Design plate girders with transverse stiffeners and estimate roof truss purlin loads."
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

export default comprehensiveSyllabusOutlines_v7;
