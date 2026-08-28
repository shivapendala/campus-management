"""
EduCore Enterprise Framework - Department of Artificial Intelligence & Machine Learning (AIML) Detailed Course Syllabi

Complete 5-unit syllabus specifications, learning outcomes, and textbooks for advanced AIML courses:
- AI401: Statistical Machine Learning (SML)
- AI501: Deep Neural Networks (DNN)
- AI502: Natural Language Processing (NLP)
- AI601: Computer Vision & Generative AI (CV)
"""

from typing import Dict, Any

AIML_DETAILED_COURSES_CATALOG: Dict[str, Dict[str, Any]] = {
    "AI401": {
        "code": "AI401",
        "title": "Statistical Machine Learning",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Supervised Learning Fundamentals",
                "topics": [
                    "Introduction to ML paradigms, linear models for regression, Ordinary Least Squares (OLS)",
                    "Ridge and Lasso regularization methods, bias-variance trade-off, model selection criteria",
                    "Linear classification models: Logistic regression, Fisher's linear discriminant, Naive Bayes classifier",
                    "Support Vector Machines (SVM): Max-margin classifiers, dual formulation, kernel trick (RBF, Polynomial kernels)"
                ]
            },
            {
                "unit": 2,
                "title": "Decision Trees and Ensemble Methods",
                "topics": [
                    "Decision tree induction algorithms (ID3, C4.5, CART), split criteria (Entropy, Gini impurity, Variance reduction)",
                    "Pruning strategies, bagging, random forests, feature importance calculations",
                    "Boosting frameworks: AdaBoost algorithm derivation, Gradient Boosting Decision Trees (GBDT), XGBoost, LightGBM"
                ]
            },
            {
                "unit": 3,
                "title": "Unsupervised Learning & Clustering",
                "topics": [
                    "K-Means clustering convergence properties, K-Means++ initialization strategy",
                    "Hierarchical clustering: Agglomerative and Divisive methods, linkage criteria (Single, Complete, Average)",
                    "Density-based clustering: DBSCAN algorithm, parameter tuning (epsilon, minPoints)",
                    "Gaussian Mixture Models (GMM), Expectation-Maximization (EM) algorithm derivation"
                ]
            },
            {
                "unit": 4,
                "title": "Dimensionality Reduction & Matrix Factorization",
                "topics": [
                    "Principal Component Analysis (PCA) spectral formulation, kernel PCA",
                    "Linear Discriminant Analysis (LDA) supervised dimensionality reduction",
                    "t-Distributed Stochastic Neighbor Embedding (t-SNE) non-linear visualization",
                    "Matrix factorization: Singular Value Decomposition (SVD), Non-Negative Matrix Factorization (NMF)"
                ]
            },
            {
                "unit": 5,
                "title": "Bayesian Learning & Graphical Models",
                "topics": [
                    "Bayesian networks structure, conditional independence assumptions, d-separation rules",
                    "Hidden Markov Models (HMM): Filtering, smoothing, Viterbi decoding algorithm",
                    "Sampling methods: Monte Carlo, Markov Chain Monte Carlo (MCMC), Gibbs sampling overview",
                    "Symmetric Dirchlet priors, latent Dirichlet allocation (LDA) topic modeling"
                ]
            }
        ],
        "textbooks": [
            "Christopher M. Bishop, 'Pattern Recognition and Machine Learning', Springer.",
            "Kevin P. Murphy, 'Machine Learning: A Probabilistic Perspective', MIT Press."
        ]
    },
    "AI501": {
        "code": "AI501",
        "title": "Deep Neural Networks",
        "credits": 4,
        "regulation": "R23",
        "units": [
            {
                "unit": 1,
                "title": "Feedforward Architectures",
                "topics": [
                    "Biological neurons vs artificial neurons, Perceptron training convergence theorem",
                    "Multi-Layer Perceptrons (MLP), feedforward propagation calculations",
                    "Activation functions: Sigmoid, Hyperbolic Tangent (Tanh), Rectified Linear Unit (ReLU), Leaky ReLU, ELU, GELU",
                    "Backpropagation algorithm: Chain rule derivation, computation graphs, gradient flow analysis",
                    "Loss functions: Mean Squared Error, Binary Cross-Entropy, Categorical Cross-Entropy, Softmax output layer"
                ]
            },
            {
                "unit": 2,
                "title": "Optimization & Regularization",
                "topics": [
                    "Gradient descent variants: Batch, Mini-batch, Stochastic gradient descent (SGD)",
                    "Momentum-based SGD, Nesterov accelerated gradient",
                    "Adaptive learning rates: AdaGrad, RMSprop, Adam, AdamW, Learning rate schedule decays",
                    "Overfitting prevention: L2/L1 weight decay, Dropout mechanics, Batch Normalization, Layer Normalization",
                    "Weight initialization techniques: Xavier/Glorot initialization, He/Kaiming initialization"
                ]
            },
            {
                "unit": 3,
                "title": "Convolutional Neural Networks (CNNs)",
                "topics": [
                    "Spatial structure representation, Convolutional layer operations, stride, padding, pooling layers (Max, Average pooling)",
                    "Translation invariance, parameter sharing, receptive field calculations",
                    "Classic architectures: LeNet-5, AlexNet, VGG-16, ResNet (Residual skip connections), DenseNet",
                    "1x1 convolutions, depthwise separable convolutions (MobileNet)"
                ]
            },
            {
                "unit": 4,
                "title": "Recurrent Neural Networks (RNNs) & LSTMs",
                "topics": [
                    "Sequential processing, Recurrent cell structure, backpropagation through time (BPTT)",
                    "Vanishing and exploding gradient problems in sequence modeling",
                    "Long Short-Term Memory (LSTM) cells: Forget gate, input gate, cell state, output gate equations",
                    "Gated Recurrent Units (GRU), Bidirectional RNNs, Sequence-to-Sequence (Seq2Seq) models, Attention mechanism"
                ]
            },
            {
                "unit": 5,
                "title": "Transformers & Self-Attention",
                "topics": [
                    "Vaswani Transformer architecture, Scaled Dot-Product Self-Attention derivation",
                    "Multi-Head Attention mechanism, Positional encodings, Encoder-Decoder stacks",
                    "Pre-training paradigms: Masked Language Modeling (BERT), Autoregressive causal modeling (GPT)",
                    "Vision Transformers (ViT) spatial patches representation"
                ]
            }
        ],
        "textbooks": [
            "Ian Goodfellow, Yoshua Bengio, and Aaron Courville, 'Deep Learning', MIT Press.",
            "Charu C. Aggarwal, 'Neural Networks and Deep Learning', Springer."
        ]
    }
}
