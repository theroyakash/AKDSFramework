from AKDSFramework.applications.complexity_analysis import Constant, Linear, Linearithmetic, Logarithmic, Quadratic
import time, types
from timeit import Timer
from AKDSFramework.applications.complexity_analysis import generatorIntegers
import numpy as np

complexities = [Constant, Linear, Linearithmetic, Logarithmic, Quadratic]

def runtimedict(func, pumping_lower_bound, pumping_upper_bound, total_measurements, pumping, **kwargs):
    """
    Measure exec time for increasing size of n
	    Args:
            - ``pumping``: Variable name which will be used for growth of the function
            - ``total_measurements``: Number of measurements, defaults set to 20
            - and put all the arguments for the main function
	    Returns:
            - A dictionary of executing time with respect to the size of some data of size N.
    """

    runtime_dictionary = {}
    pumping = kwargs.pop(f'{pumping}')

    class Wrapper(object):
        def __init__(self, n):
            self.pumping_data = pumping(n)

        def __call__(self):
            return func(self.pumping_data, **kwargs)

    
    pumping_data_sizes = np.linspace(pumping_lower_bound, pumping_upper_bound, total_measurements).astype('int64')
    for _, pumping_data_size in enumerate(pumping_data_sizes):
        
        exec_times = np.zeros(10)

        for i in range(10):
            start = time.perf_counter()
            Wrapper(pumping_data_size)
            end = time.perf_counter()
            exec_times[i] = end - start

        runtime_dictionary[pumping_data_size] = np.min(exec_times)

    return runtime_dictionary


# Example code for testing
# def find(array, target):
#     for i in array:
#         if i == target:
#             return i

# integer_generator = lambda x: generatorIntegers(lb=0, ub=1000, size=x)
# print(runtimedict(find, 100, 100000, 30, pumping='array', array=integer_generator, target=100))