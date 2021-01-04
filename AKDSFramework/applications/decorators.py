import cProfile
import pstats
import io
import functools, time

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
    Default dictionary based caching decorator for AKDSFramework. 
    Maintains a dictionary with hashable arguments to cache data.
    Ensures constant look-up time when a cache hit occurs.
    """
    cache = dict()

    def caching(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result

    return caching


def exectime(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        returnValue = func(*args, **kwargs)
        end = time.time()

        if int(end - start) > 0:
            print(f"Run time for {func.__name__}: {(end - start):0.2f}s")
        else:
            print(f"Run time for {func.__name__}: {(end - start)*1000:0.2f}ms")
        
        return returnValue

    return wrapper