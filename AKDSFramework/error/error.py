class InvalidOperationError(Exception):
    pass

class NotFoundError(Exception):
    pass

class HeapNotBuildError(Exception):
    pass

class EmptyStackError(Exception):
    pass

class BadVertexTypeError(Exception):
    pass

class NegativeEdgeCycleWarning(UserWarning):
	pass