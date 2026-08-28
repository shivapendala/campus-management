/**
 * Department Syllabi Store for All 5 Engineering Branches
 */

export const allDepartmentSyllabi = {
  ECE: {
    dept_code: 'ECE',
    name: 'Electronics & Communication Engineering',
    courses: [
      {
        code: 'EC301',
        title: 'Electronic Circuits & Semiconductor Devices',
        credits: 4,
        regulation: 'R23',
        units: [
          { unit: 1, title: 'Semiconductor Physics & PN Diodes', hours: 9, blooms: 'L1/L2', co: 'CO1' },
          { unit: 2, title: 'Bipolar Junction Transistors (BJT)', hours: 9, blooms: 'L2/L3', co: 'CO2' },
          { unit: 3, title: 'Field Effect Transistors (JFET/MOSFET)', hours: 9, blooms: 'L3/L4', co: 'CO3' },
          { unit: 4, title: 'Small Signal Low-Frequency Amplifiers', hours: 9, blooms: 'L3/L4', co: 'CO4' },
          { unit: 5, title: 'Power Amplifiers & Tuned Amplifiers', hours: 9, blooms: 'L4/L5', co: 'CO5' },
        ],
      },
      {
        code: 'EC501',
        title: 'Digital Signal Processing (DSP) Architecture',
        credits: 4,
        regulation: 'R23',
        units: [
          { unit: 1, title: 'Discrete-Time Signals & Z-Transforms', hours: 9, blooms: 'L1/L2', co: 'CO1' },
          { unit: 2, title: 'DFT and Radix-2 FFT Butterfly Algorithms', hours: 9, blooms: 'L2/L3', co: 'CO2' },
          { unit: 3, title: 'IIR Digital Filter Approximations (Butterworth/Chebyshev)', hours: 9, blooms: 'L3/L4', co: 'CO3' },
          { unit: 4, title: 'FIR Digital Filter Design (Windowing/Sampling)', hours: 9, blooms: 'L3/L4', co: 'CO4' },
          { unit: 5, title: 'Finite Word Length Effects & TMS320C6748 Processor', hours: 9, blooms: 'L4/L5', co: 'CO5' },
        ],
      },
    ],
  },
  MECH: {
    dept_code: 'MECH',
    name: 'Mechanical Engineering',
    courses: [
      {
        code: 'ME301',
        title: 'Engineering Thermodynamics & Applied Heat Transfer',
        credits: 4,
        regulation: 'R23',
        units: [
          { unit: 1, title: 'First Law & Steady Flow Energy Equation (SFEE)', hours: 9, blooms: 'L1/L2', co: 'CO1' },
          { unit: 2, title: 'Second Law, Clausius Inequality & Entropy', hours: 9, blooms: 'L2/L3', co: 'CO2' },
          { unit: 3, title: 'Pure Substances & Rankine Vapor Power Cycle', hours: 9, blooms: 'L3/L4', co: 'CO3' },
          { unit: 4, title: 'Otto, Diesel, Dual & Brayton Gas Turbine Cycles', hours: 9, blooms: 'L3/L4', co: 'CO4' },
          { unit: 5, title: 'Psychrometric Processes & Vapor Compression (VCRS)', hours: 9, blooms: 'L4/L5', co: 'CO5' },
        ],
      },
    ],
  },
  CIVIL: {
    dept_code: 'CIVIL',
    name: 'Civil Engineering',
    courses: [
      {
        code: 'CE301',
        title: 'Strength of Materials & Structural Mechanics',
        credits: 4,
        regulation: 'R23',
        units: [
          { unit: 1, title: 'Stress, Strain & Hookes Law Elastic Constants', hours: 9, blooms: 'L1/L2', co: 'CO1' },
          { unit: 2, title: 'Shear Force & Bending Moment Diagrams (SFD/BMD)', hours: 9, blooms: 'L2/L3', co: 'CO2' },
          { unit: 3, title: 'Flexural & Horizontal Shear Stresses in Beams', hours: 9, blooms: 'L3/L4', co: 'CO3' },
          { unit: 4, title: 'Torsion of Circular Shafts & Helical Springs', hours: 9, blooms: 'L3/L4', co: 'CO4' },
          { unit: 5, title: 'Mohrs Circle of Stress & Thin Cylindrical Shells', hours: 9, blooms: 'L4/L5', co: 'CO5' },
        ],
      },
    ],
  },
  EEE: {
    dept_code: 'EEE',
    name: 'Electrical & Electronics Engineering',
    courses: [
      {
        code: 'EE301',
        title: 'Electric Circuit Analysis & Network Synthesis',
        credits: 4,
        regulation: 'R23',
        units: [
          { unit: 1, title: 'Mesh, Nodal & Network Graph Topology', hours: 9, blooms: 'L1/L2', co: 'CO1' },
          { unit: 2, title: 'Thevenin, Norton & Maximum Power Theorems', hours: 9, blooms: 'L2/L3', co: 'CO2' },
          { unit: 3, title: 'Transient Response in Time & Laplace Domains', hours: 9, blooms: 'L3/L4', co: 'CO3' },
          { unit: 4, title: 'Series/Parallel Resonance & Magnetically Coupled Coils', hours: 9, blooms: 'L3/L4', co: 'CO4' },
          { unit: 5, title: 'Two-Port Network Parameters (Z, Y, ABCD, h)', hours: 9, blooms: 'L4/L5', co: 'CO5' },
        ],
      },
    ],
  },
  AIML: {
    dept_code: 'AIML',
    name: 'Artificial Intelligence & Data Science',
    courses: [
      {
        code: 'AI301',
        title: 'Mathematical Foundations of Machine Learning',
        credits: 4,
        regulation: 'R23',
        units: [
          { unit: 1, title: 'Linear Algebra, Eigenvalues, SVD & PCA', hours: 9, blooms: 'L1/L2', co: 'CO1' },
          { unit: 2, title: 'Vector Calculus, Gradient Descent & KKT Conditions', hours: 9, blooms: 'L2/L3', co: 'CO2' },
          { unit: 3, title: 'Multivariate Gaussian Distributions & Bayes Theorem', hours: 9, blooms: 'L3/L4', co: 'CO3' },
          { unit: 4, title: 'Maximum Likelihood (MLE) & Bayesian Inference', hours: 9, blooms: 'L3/L4', co: 'CO4' },
          { unit: 5, title: 'Information Entropy, KL Divergence & Cross-Entropy Loss', hours: 9, blooms: 'L4/L5', co: 'CO5' },
        ],
      },
    ],
  },
};

export default allDepartmentSyllabi;
