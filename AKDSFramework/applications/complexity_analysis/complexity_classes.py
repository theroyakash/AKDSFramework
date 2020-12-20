class ComplexityAbstractClass(object):
    """
    Abstract Complexity class
    """
    priority_rank = 0

    def __init__(self):
        super(ComplexityAbstractClass, self).__init__()

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
    def __str__(self):
        return "O(1)"


class Linear(ComplexityAbstractClass):
    priority_rank = 1
    def __str__(self):
        return "O(N)"


class Logarithmic(ComplexityAbstractClass):
    priority_rank = 2
    def __str__(self):
        return "O(log N)"


class Linearithmetic(ComplexityAbstractClass):
    priority_rank = 3
    def __str__(self):
        return "O(N log N)"

class Quadratic(ComplexityAbstractClass):
    priority_rank = 4
    def __str__(self):
        return "O(N^2)"