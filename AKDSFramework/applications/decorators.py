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
