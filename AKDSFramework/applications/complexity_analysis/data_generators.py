import random

def integer_sequence(lb, ub, size):
    """
    Sequence of Integer generator
        Args:
            - lb: Lower bound of the generated array
            - ub: Upper bound of the generated array
            - size: Size of the generated array

        Returns:
            - Array of Integers
    """
    return [random.randint(lb, ub) for _ in range(size)]

def one_integer(n):
    """
    Generate only one integer
    """
    return n

def large_integer_sequence(lb, ub, size):
    """
    Sequence of Large Integer generator
        Args:
            - lb: Lower bound of the generated array
            - ub: Upper bound of the generated array
            - size: Size of the generated array

        Returns:
            - Array of Integers
    """

    return [random.randint(lb, ub) * 200000 for _ in range(size)]

def float_sequence(lb, ub, size):
    """
    Sequnce of floating point numbers
        Args:
            - lb: Lower bound of the generated array
            - ub: Upper bound of the generated array
            - size: Size of the generated array

        Returns:
            - Array of floating points
    """

    return [random.uniform(lb, ub) for _ in range(size)]
