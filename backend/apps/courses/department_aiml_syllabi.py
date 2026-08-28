"""
EduCore Enterprise Framework - Department of Artificial Intelligence & Machine Learning (AI & ML) Course Syllabi

Complete 5-unit syllabus specifications, learning outcomes, and laboratory manuals for AI/ML core courses:
- AI301: Mathematical Foundations of Machine Learning (Linear Algebra & Probability)
- AI302: Foundations of Artificial Intelligence & Heuristic Search
- AI401: Statistical Machine Learning Algorithms & Ensembles
- AI402: Knowledge Representation, Ontologies & Reasoning
- AI501: Deep Neural Networks & Backpropagation Architectures
- AI502: Natural Language Processing (NLP) & Large Language Models (LLMs)
- AI601: Computer Vision, CNNs & Generative Adversarial Networks (GANs)
- AI602: Reinforcement Learning & Autonomous Decision Making
- AI701: Generative AI, Diffusion Models & Prompt Engineering
- AI702: AI Ethics, Explainable AI (XAI) & Governance
"""

from typing import Dict, List, Any

AIML_DEPARTMENT_COURSES_SPECIFICATION: Dict[str, Dict[str, Any]] = {
    "AI301": {
        "code": "AI301",
        "title": "Mathematical Foundations of Machine Learning",
        "credits": 4,
        "regulation": "R23",
        "department": "Artificial Intelligence & Data Science",
        "units": [
            {
                "unit": 1,
                "title": "Linear Algebra, Vector Spaces & Matrix Decompositions",
                "hours": 9,
                "blooms": "L1_REMEMBER/L2_UNDERSTAND",
                "co": "CO1",
                "topics": "Vector spaces, Subspaces, Linear independence, Basis and dimension, Linear transformations and matrix representations, Range and Null space, Inner product spaces, Norms (L1, L2, L-infinity norms), Orthogonality, Gram-Schmidt orthogonalization process, Orthogonal projections, Eigenvalues and Eigenvectors, Characteristic polynomial, Diagonalization, Spectral Theorem for symmetric matrices, Singular Value Decomposition (SVD), Geometric interpretation of SVD, Low-rank matrix approximations and Principal Component Analysis (PCA) derivation."
            },
            {
                "unit": 2,
                "title": "Multivariate Vector Calculus & Optimization",
                "hours": 9,
                "blooms": "L2_UNDERSTAND/L3_APPLY",
                "co": "CO2",
                "topics": "Functions of several variables, Directional derivatives, Gradient vector, Direction of steepest descent, Hessian matrix, Second-order Taylor series approximation, Convex sets and convex functions, First and second-order conditions for convexity, Unconstrained optimization, Gradient Descent, Learning rate schedules, Stochastic Gradient Descent (SGD), Mini-batch SGD, Momentum-based gradient descent, Nesterov accelerated gradient, Adaptive gradient algorithms (AdaGrad, RMSprop, Adam, AdamW), Constrained optimization, Lagrange multipliers, Karush-Kuhn-Tucker (KKT) conditions, Duality theory (Primal and Dual problems, Slater's condition)."
            },
            {
                "unit": 3,
                "title": "Probability Distributions, Random Variables & Estimation",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO3",
                "topics": "Probability spaces, Axioms of probability, Conditional probability, Bayes' Theorem and its applications, Random variables, Discrete distributions (Bernoulli, Binomial, Poisson, Geometric), Continuous distributions (Uniform, Exponential, Gaussian / Normal, Beta, Gamma, Dirichlet), Multivariate Gaussian distribution, Covariance matrix and correlation, Marginal and conditional distributions of multivariate Gaussians, Expectation, Variance, Covariance, Joint moments, Moment generating functions, Law of Large Numbers, Central Limit Theorem."
            },
            {
                "unit": 4,
                "title": "Statistical Inference & Parameter Estimation",
                "hours": 9,
                "blooms": "L3_APPLY/L4_ANALYZE",
                "co": "CO4",
                "topics": "Point estimation versus Interval estimation, Maximum Likelihood Estimation (MLE), Properties of MLE (Consistency, Asymptotic normality, Efficiency), Maximum A Posteriori (MAP) estimation, Conjugate priors (Beta-Binomial, Dirichlet-Multinomial, Gaussian-Gaussian conjugate pairs), Bayesian inference framework, Bias-Variance decomposition, Cramér-Rao lower bound, Fisher Information matrix, Hypothesis testing, Null and alternative hypotheses, Type I and Type II errors, p-values, Likelihood Ratio Tests, Confidence intervals."
            },
            {
                "unit": 5,
                "title": "Information Theory & Distance Metrics in High Dimensions",
                "hours": 9,
                "blooms": "L4_ANALYZE/L5_EVALUATE",
                "co": "CO5",
                "topics": "Entropy of discrete and continuous random variables, Differential entropy, Joint entropy and Conditional entropy, Mutual Information, Kullback-Leibler (KL) Divergence, Properties of KL divergence (Non-negativity, Asymmetry), Jensen-Shannon (JS) Divergence, Cross-Entropy loss function derivation for classification, Distance metrics in vector spaces (Euclidean distance, Manhattan distance, Minkowski distance, Mahalanobis distance, Cosine similarity), Curse of dimensionality in high-dimensional feature spaces, Concentration of distances, Random projections and Johnson-Lindenstrauss lemma."
            }
        ],
        "textbooks": [
            "Marc Peter Deisenroth, A. Aldo Faisal, and Cheng Soon Ong, 'Mathematics for Machine Learning', Cambridge University Press, 2020.",
            "Gilbert Strang, 'Linear Algebra and Learning from Data', Wellesley-Cambridge Press, 2019."
        ]
    }
}
