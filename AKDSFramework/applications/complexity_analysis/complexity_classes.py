class ComplexityAbstractClass(object):
    """
    Abstract Complexity class
    """

    def __init__(self):
        super(ComplexityAbstractClass, self).__init__()

    def __str__(self):
        raise NotImplementedError()


class Constant(ComplexityAbstractClass):
    pass


class Linear(ComplexityAbstractClass):
    pass


class Logarithmic(ComplexityAbstractClass):
    pass


class Linearithmetic(ComplexityAbstractClass):
    pass
