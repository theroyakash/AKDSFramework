import cProfile
import pstats
import io

def benchmark(func):
    """
    AKDSFramework default benchmark profiler. Implemented with cProfile and pstats.
    """
    def profiler(*args, **kwargs):
        profiler = cProfile.Profile()
        profiler.enable()
        returnvalue = func(*args, **kwargs)
        profiler.disable()

        stringIO = io.StringIO()

        ps = pstats.Stats(profiler, stream=stringIO).sort_stats("cumulative")
        ps.print_stats()
        print(stringIO.getvalue())

        return returnvalue
    
    return profiler

# def hashkey(args, kwargs, validate_type, type=type):

#     pass
# def cached(func, maxsize=64, validate_type=False):
#     """
#     AKDSFramework default caching profiler.
#         Args:
#             - ``maxsize`` (int): maxsize of the cached size.
#             - ``validate_type``: If ``validate_type`` is set True, arguments of different types will be cached separately.
#             For example, f(4.0) and f(4) will be treated as distinct calls with distinct results.
#         Caution:
#             Arguments to the cached function must be hashable as we are storing the args into a hash table or python dictionary.
#     """
#     if isinstance(maxsize, int):
#         if maxsize < 0:
#             raise TypeError("Max size of the cache storage should be positive")
    
#     def cache_decorating(*args, **kwargs):
#         cache = {}
#         returnval = func(*args, **kwargs)
#         pass

#     return cache_decorating