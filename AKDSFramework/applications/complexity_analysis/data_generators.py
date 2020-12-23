import random

def generatorIntegers(lb, ub, size):
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