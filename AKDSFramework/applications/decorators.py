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

def cached(func):
    """
    Default caching decorator for AKDSFramework. Maintains a dictionary with hashable arguments to cache data.
    Ensures constant look-up time when cache hit occurs.
    """
    cache = dict()

    def caching(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return caching
