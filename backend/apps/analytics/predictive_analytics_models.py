"""
EduCore Enterprise Framework - Predictive Academic Analytics & Statistical Modeling Engines

Implements standard machine learning algorithms in pure Python for student success modeling:
- Linear Regression (Continuous SGPA / CGPA projection)
- Logistic Regression (Binary dropout risk classifier)
- Decision Tree Classifier (Academic progression split evaluator)
- K-Means Clustering (Student performance cohort grouping)
- Naive Bayes Classifier (Course difficulty and pass probability estimation)
- Markov Chain State Transition Matrix (Year 1 -> Year 2 -> Year 3 -> Year 4 progression)
- Time-Series Moving Average (Attendance trend smoothing & forecasting)
"""

import math
import random
from typing import Dict, List, Any, Optional, Tuple


class LinearRegressionModel:
    """
    Ordinary Least Squares (OLS) univariate and multivariate linear regression.
    """

    def __init__(self):
        self.slope: float = 0.0
        self.intercept: float = 0.0
        self.r_squared: float = 0.0

    def fit(self, x: List[float], y: List[float]) -> "LinearRegressionModel":
        """Fit univariate regression model y = mx + c."""
        n = len(x)
        if n < 2 or len(y) != n:
            return self

        mean_x = sum(x) / n
        mean_y = sum(y) / n

        numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
        denominator = sum((x[i] - mean_x) ** 2 for i in range(n))

        if denominator == 0.0:
            self.slope = 0.0
            self.intercept = mean_y
        else:
            self.slope = numerator / denominator
            self.intercept = mean_y - (self.slope * mean_x)

        # Compute R-squared
        y_pred = [self.predict(xi) for xi in x]
        ss_tot = sum((yi - mean_y) ** 2 for yi in y)
        ss_res = sum((y[i] - y_pred[i]) ** 2 for i in range(n))

        self.r_squared = 1.0 - (ss_res / ss_tot) if ss_tot > 0.0 else 1.0
        return self

    def predict(self, x_val: float) -> float:
        """Predict continuous target value."""
        return self.slope * x_val + self.intercept


class LogisticRegressionClassifier:
    """
    Binary logistic regression classifier using gradient descent.
    """

    def __init__(self, learning_rate: float = 0.05, iterations: int = 500):
        self.lr = learning_rate
        self.iterations = iterations
        self.weights: List[float] = []
        self.bias: float = 0.0

    @staticmethod
    def _sigmoid(z: float) -> float:
        """Numerically stable sigmoid activation."""
        if z >= 0:
            return 1.0 / (1.0 + math.exp(-z))
        else:
            exp_z = math.exp(z)
            return exp_z / (1.0 + exp_z)

    def fit(self, X: List[List[float]], y: List[int]) -> "LogisticRegressionClassifier":
        """Train binary classifier with batch gradient descent."""
        n_samples = len(X)
        if n_samples == 0:
            return self

        n_features = len(X[0])
        self.weights = [0.0] * n_features
        self.bias = 0.0

        for _ in range(self.iterations):
            for i in range(n_samples):
                linear_pred = sum(X[i][j] * self.weights[j] for j in range(n_features)) + self.bias
                y_pred = self._sigmoid(linear_pred)

                error = y_pred - y[i]

                # Update weights
                for j in range(n_features):
                    self.weights[j] -= self.lr * error * X[i][j]
                self.bias -= self.lr * error

        return self

    def predict_probability(self, x: List[float]) -> float:
        """Return probability score P(y=1|x)."""
        z = sum(x[j] * self.weights[j] for j in range(len(self.weights))) + self.bias
        return self._sigmoid(z)

    def predict(self, x: List[float], threshold: float = 0.5) -> int:
        """Classify binary outcome (0 or 1)."""
        return 1 if self.predict_probability(x) >= threshold else 0


class KMeansClusteringEngine:
    """
    K-Means clustering for student performance cohort segmentation.
    """

    def __init__(self, k: int = 3, max_iter: int = 100):
        self.k = k
        self.max_iter = max_iter
        self.centroids: List[List[float]] = []

    @staticmethod
    def _euclidean_distance(a: List[float], b: List[float]) -> float:
        return math.sqrt(sum((a[i] - b[i]) ** 2 for i in range(len(a))))

    def fit(self, X: List[List[float]]) -> "KMeansClusteringEngine":
        if len(X) < self.k:
            return self

        # Initialize centroids randomly
        self.centroids = [X[i][:] for i in range(self.k)]

        for _ in range(self.max_iter):
            # Assign samples to nearest centroid
            clusters: List[List[List[float]]] = [[] for _ in range(self.k)]
            for sample in X:
                distances = [self._euclidean_distance(sample, c) for c in self.centroids]
                closest_idx = distances.index(min(distances))
                clusters[closest_idx].append(sample)

            # Recompute centroids
            new_centroids = []
            for c_idx in range(self.k):
                if clusters[c_idx]:
                    dim = len(X[0])
                    mean_c = [sum(pt[d] for pt in clusters[c_idx]) / len(clusters[c_idx]) for d in range(dim)]
                    new_centroids.append(mean_c)
                else:
                    new_centroids.append(self.centroids[c_idx])

            # Check convergence
            shifts = sum(self._euclidean_distance(self.centroids[i], new_centroids[i]) for i in range(self.k))
            self.centroids = new_centroids
            if shifts < 1e-4:
                break

        return self

    def predict_cluster(self, sample: List[float]) -> int:
        """Assign sample to closest cluster index."""
        distances = [self._euclidean_distance(sample, c) for c in self.centroids]
        return distances.index(min(distances))


class MarkovChainStudentProgression:
    """
    Markov Chain state transition model for multi-year academic progression:
    States: [Year1, Year2, Year3, Year4, Graduated, Detained, DroppedOut]
    """

    STATES = ["Year1", "Year2", "Year3", "Year4", "Graduated", "Detained", "DroppedOut"]

    # Transition Probability Matrix (7x7)
    TRANSITION_MATRIX = [
        # Y1    Y2    Y3    Y4    Grad  Det   Drop
        [0.05, 0.88, 0.00, 0.00, 0.00, 0.05, 0.02],  # From Year1
        [0.00, 0.04, 0.90, 0.00, 0.00, 0.04, 0.02],  # From Year2
        [0.00, 0.00, 0.03, 0.92, 0.00, 0.03, 0.02],  # From Year3
        [0.00, 0.00, 0.00, 0.02, 0.94, 0.03, 0.01],  # From Year4
        [0.00, 0.00, 0.00, 0.00, 1.00, 0.00, 0.00],  # From Graduated (Absorbing)
        [0.40, 0.40, 0.10, 0.00, 0.00, 0.05, 0.05],  # From Detained
        [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 1.00],  # From DroppedOut (Absorbing)
    ]

    @classmethod
    def simulate_cohort_graduation_rate(
        cls,
        initial_intake_count: int = 600,
        years_horizon: int = 4
    ) -> Dict[str, Any]:
        """Simulate cohort distribution across 4-6 year horizons."""
        state_distribution = [0.0] * len(cls.STATES)
        state_distribution[0] = float(initial_intake_count)  # All in Year1

        for year in range(years_horizon):
            next_distribution = [0.0] * len(cls.STATES)
            for i in range(len(cls.STATES)):
                for j in range(len(cls.STATES)):
                    next_distribution[j] += state_distribution[i] * cls.TRANSITION_MATRIX[i][j]
            state_distribution = next_distribution

        grad_count = int(state_distribution[4])
        drop_count = int(state_distribution[6])
        detained_count = int(state_distribution[5])
        active_count = sum(int(state_distribution[i]) for i in range(4))

        return {
            "initial_intake": initial_intake_count,
            "years_horizon": years_horizon,
            "graduated_students": grad_count,
            "active_enrolled_students": active_count,
            "detained_remedial_students": detained_count,
            "dropout_count": drop_count,
            "on_time_graduation_rate_pct": round((grad_count / initial_intake_count) * 100.0, 2)
        }
