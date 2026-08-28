"""
EduCore Framework - Master Curriculum Course Catalog Database Seeder - Part 2

Contains comprehensive static syllabus definitions, credit structures, L-T-P parameters,
textbooks, and reference lists for EEE, CIVIL, and AIML courses.
Used by the course attainment engines and lesson planners.
"""

from typing import Dict, List, Any

CURRICULUM_COURSE_CATALOG_DB_EXPANDED: Dict[str, Dict[str, Any]] = {
    "EE301": {
        "code": "EE301",
        "title": "Electric Circuit Analysis",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Electrical & Electronics Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Basic Circuit Concepts & Topology",
                "topics": [
                    "Voltage and current sources, independent and dependent sources, Ohm's law, Kirchhoff's laws.",
                    "Mesh analysis and nodal analysis with dependent and independent sources, supermesh and supernode concepts.",
                    "Network graph theory: Graph, tree, co-tree, incidence matrix, basic loop and cut-set matrices.",
                    "Duality and dual networks, source transformations, star-delta transformations."
                ]
            },
            {
                "unit": 2,
                "title": "Network Theorems",
                "topics": [
                    "Superposition theorem, Thevenin's and Norton's theorems, maximum power transfer theorem.",
                    "Reciprocity theorem, Millman's theorem, Tellegen's theorem, substitution theorem.",
                    "Application of theorems to DC and AC steady-state circuits, operational amplifier circuits analysis."
                ]
            },
            {
                "unit": 3,
                "title": "Transient Analysis",
                "topics": [
                    "Transient response of RL, RC, and RLC circuits under DC and AC excitations, initial and final conditions.",
                    "Differential equation approach, Laplace transform method, step, ramp, and impulse response analysis.",
                    "S-plane representation, transfer functions, poles and zeros, stability definitions."
                ]
            },
            {
                "unit": 4,
                "title": "AC Resonance & Coupled Circuits",
                "topics": [
                    "Series resonance: Bandwidth, quality factor, selectivty, half-power frequencies.",
                    "Parallel resonance: Tank circuit characteristics, dynamic impedance.",
                    "Coupled circuits: Self and mutual inductance, coefficient of coupling, dot convention.",
                    "Analysis of conductively coupled and magnetically coupled circuits, linear transformers."
                ]
            },
            {
                "unit": 5,
                "title": "Two-Port Network Parameters & Synthesis",
                "topics": [
                    "Z, Y, ABCD, inverse ABCD, hybrid, and inverse hybrid parameters, parameter conversions.",
                    "Interconnection of two-port networks (series, parallel, cascade).",
                    "Positive Real (PR) functions, synthesis of driving point impedance functions using Foster and Cauer forms."
                ]
            }
        ],
        "textbooks": [
            "William H. Hayt, Jack E. Kemmerly, and Steven M. Durbin, 'Engineering Circuit Analysis', McGraw-Hill.",
            "Charles K. Alexander and Matthew N.O. Sadiku, 'Fundamentals of Electric Circuits', McGraw-Hill."
        ]
    },
    "CE301": {
        "code": "CE301",
        "title": "Strength of Materials",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Civil Engineering",
        "units": [
            {
                "unit": 1,
                "title": "Simple Stresses & Strains",
                "topics": [
                    "Concept of stress, strain, Hooke's law, elastic constants (E, G, K, Poisson's ratio) and their relations.",
                    "Stress-strain curve for mild steel, working stress, factor of safety.",
                    "Thermal stresses and strains in simple and composite bars, elastic deformation under axial loads.",
                    "Strain energy under gradual, sudden, and impact loads, resilience, proof resilience."
                ]
            },
            {
                "unit": 2,
                "title": "Shear Force & Bending Moment in Beams",
                "topics": [
                    "Types of beams, loads, supports, shear force and bending moment definitions.",
                    "Relationship between load, shear force, and bending moment (dF/dx = -w, dM/dx = F).",
                    "SFD and BMD for cantilevers, simply supported, and overhanging beams under point loads, UDL, and UVL.",
                    "Point of contraflexure, maximum bending moment coordinates."
                ]
            },
            {
                "unit": 3,
                "title": "Flexural & Shear Stresses in Beams",
                "topics": [
                    "Theory of simple bending, assumptions, derivation of bending formula (M/I = f/y = E/R).",
                    "Section modulus of rectangular, circular, I, T, and channel sections.",
                    "Shear stress distribution in beams: Derivation of shear stress formula, shear stress profile across standard sections."
                ]
            },
            {
                "unit": 4,
                "title": "Torsion of Circular Shafts & Helical Springs",
                "topics": [
                    "Theory of pure torsion, assumptions, derivation of torsion equation (T/J = fs/r = C*theta/L).",
                    "Power transmission in solid and hollow circular shafts, design of shafts for strength and rigidity.",
                    "Helical springs: Close-coiled and open-coiled helical springs, deflection and stiffness equations."
                ]
            },
            {
                "unit": 5,
                "title": "Principal Stresses & Thin Cylinders",
                "topics": [
                    "Principal planes and principal stresses, analytical and graphical (Mohr's circle) methods.",
                    "Theories of elastic failure: Maximum principal stress, maximum shear stress, maximum distortion energy theories.",
                    "Thin cylinders and spheres: Hoop stress, longitudinal stress, volumetric strain under internal fluid pressure."
                ]
            }
        ],
        "textbooks": [
            "R.K. Rajput, 'Strength of Materials (Mechanics of Solids)', S. Chand & Company.",
            "Ferdinand P. Beer, E. Russell Johnston Jr., and David F. Mazurek, 'Mechanics of Materials', McGraw-Hill."
        ]
    },
    "AI301": {
        "code": "AI301",
        "title": "Mathematical Foundations of Machine Learning",
        "credits": 4,
        "ltp": "3-1-0",
        "department": "Artificial Intelligence & Data Science",
        "units": [
            {
                "unit": 1,
                "title": "Vector Spaces & Decompositions",
                "topics": [
                    "Vector spaces, basis, dimension, linear transformations, range and null space, norms (L1, L2, L-infinity).",
                    "Inner product spaces, orthogonality, projections, Gram-Schmidt process.",
                    "Eigenvalues, eigenvectors, spectral theorem, Singular Value Decomposition (SVD), Low-rank matrix approximations."
                ]
            },
            {
                "unit": 2,
                "title": "Vector Calculus & Optimization",
                "topics": [
                    "Gradients, Jacobian, Hessian matrix, Taylor series approximations.",
                    "Convex sets, convex functions, local and global minima criteria.",
                    "Unconstrained optimization: Gradient descent, SGD, momentum, Adam, RMSprop.",
                    "Constrained optimization: Lagrange multipliers, KKT conditions, duality."
                ]
            },
            {
                "unit": 3,
                "title": "Probability & Density Distributions",
                "topics": [
                    "Probability spaces, conditional probability, Bayes theorem.",
                    "Discrete and continuous random variables, multivariate Gaussian distributions.",
                    "Covariance matrix, marginal and conditional distributions, Central Limit Theorem."
                ]
            },
            {
                "unit": 4,
                "title": "Statistical Parameter Estimation",
                "topics": [
                    "Maximum Likelihood Estimation (MLE), Maximum A Posteriori (MAP) estimation.",
                    "Bayesian parameter estimation, conjugate priors, bias-variance tradeoff.",
                    "Hypothesis testing, Type I and II errors, p-values, confidence intervals."
                ]
            },
            {
                "unit": 5,
                "title": "Information Theory & Distance Metrics",
                "topics": [
                    "Entropy, joint entropy, conditional entropy, mutual information.",
                    "Kullback-Leibler (KL) divergence, Jensen-Shannon divergence, cross-entropy loss function.",
                    "Distance metrics: Euclidean, Manhattan, Cosine similarity, Mahalanobis distance, curse of dimensionality."
                ]
            }
        ],
        "textbooks": [
            "Marc Peter Deisenroth, A. Aldo Faisal, and Cheng Soon Ong, 'Mathematics for Machine Learning', Cambridge University Press.",
            "Gilbert Strang, 'Linear Algebra and Learning from Data', Wellesley-Cambridge Press."
        ]
    }
}
