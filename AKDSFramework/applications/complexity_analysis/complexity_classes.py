import numpy as np


class ComplexityAbstractClass(object):
    """
    Abstract Complexity class
    """
    priority_rank = 0

    def __init__(self):
        super(ComplexityAbstractClass, self).__init__()

    def adjust_for_complexity(self, n):
        raise NotImplementedError()

    def adjust_time(self, time):
        return time

    def fit(self, n, time):
        """
        Retrun the squared Euclidean 2-norm for each column in ||b - a*x||. If the rank of a is < N or M <= N, this is an empty array. 
        If b is 1-dimensional, this is a (1,) shape array. 
        Otherwise the shape is (K,)
        """
        x = self.adjust_for_complexity(n)
        y = self.adjust_time(time)

        # See here: https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html
        _, residuals, _, _ = np.linalg.lstsq(x, y, rcond=None)

        return residuals[0]

    def __str__(self):
        raise NotImplementedError()

    def __gt__(self, other):
        """
        Grater than comparison
        """
        return self.priority_rank > other.priority_rank

    def __lt__(self, other):
        """
        Lesser than comparison
        """
        return self.priority_rank < other.priority_rank

    def __eq__(self, other):
        """
        Equality comparison
        """
        return self.priority_rank == other.priority_rank

    def __hash__(self):
        return id(self)


class Constant(ComplexityAbstractClass):
    priority_rank = 0

    def adjust_for_complexity(self, n):
        return np.ones((len(n), 1))

    def __str__(self):
        return "O(1)"


class Linear(ComplexityAbstractClass):
    priority_rank = 1

    def adjust_for_complexity(self, n):
        """
        See Documentation here https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html
        """
        return np.vstack([np.ones(len(n)), n]).T

    def __str__(self):
        return "O(N)"


class Logarithmic(ComplexityAbstractClass):
    priority_rank = 2

    def adjust_for_complexity(self, n):
        """
        See Documentation here https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html
        """
        return np.vstack([np.ones(len(n)), np.log(n)]).T

    def __str__(self):
        return "O(log N)"


class Linearithmetic(ComplexityAbstractClass):
    priority_rank = 3

    def adjust_for_complexity(self, n):
        """
        See Documentation here https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html
        """
        return np.vstack([np.ones(len(n)), n * np.log(n)]).T

    def __str__(self):
        return "O(N log N)"


class Quadratic(ComplexityAbstractClass):
    priority_rank = 4

    def adjust_for_complexity(self, n):
        """
        See Documentation here https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html
        """
        return np.vstack([np.ones(len(n)), n ** 2]).T

    def __str__(self):
        return "O(N^2)"


class Cubic(ComplexityAbstractClass):
    priority_rank = 5

    def adjust_for_complexity(self, n):
        """
        See Documentation here https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html
        """
        return np.vstack([np.ones(len(n)), n ** 3]).T

    def __str__(self):
        return "O(N^3)"


class Polynomial(ComplexityAbstractClass):
    priority_rank = 6

    def __str__(self):
        return "Polynomial time"


class Exponential(ComplexityAbstractClass):
    priority_rank = 7

    def adjust_for_complexity(self, n):
        """
        See Documentation here https://numpy.org/doc/stable/reference/generated/numpy.linalg.lstsq.html
        """
        return np.vstack([np.ones(len(n)), n]).T      # Linear if the time is brought down to Linear.

    def adjust_time(self, time):
        return np.log(time)

    def __str__(self):
        return "Exponential time"
