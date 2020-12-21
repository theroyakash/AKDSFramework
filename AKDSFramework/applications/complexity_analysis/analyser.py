from AKDSFramework.applications.complexity_analysis import Constant, Linear, Linearithmetic, Logarithmic, Quadratic
import time, types
from AKDSFramework.applications.complexity_analysis import generatorIntegers

complexities = [Constant, Linear, Linearithmetic, Logarithmic, Quadratic]

def runtimedict(func, total_measurements = 20, **kwargs):
    """
    Measure exec time for increasing size of n
	    Args:
            - ``total_measurements``: Number of measurements, defaults set to 20
            - and put all the arguments for the main function
	    Returns:
            - A dictionary of executing time with respect to the size of some data of size N.
    """

    dictionary = {}

    for expt_number in range(1, total_measurements+1):
        # Run function each time and register the time in the dictionary
        start = time.time()
        _ = func(**kwargs)
        end = time.time()
        dictionary[expt_number] = (end - start) * 1000

    return dictionary
