from AKDSFramework.applications.complexity_analysis import Constant, Linear, Logarithmic, Linearithmetic, Quadratic, Cubic, Polynomial, Exponential
import time
from timeit import Timer
from tqdm import tqdm
import numpy as np

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

    for _, pumping_data_size in tqdm(enumerate(pumping_data_sizes), total=len(pumping_data_sizes), desc='Processing'):
        
        timer = Timer(Wrapper(pumping_data_size))
        exec_times = timer.repeat(1, 5)
        runtime_dictionary[pumping_data_size] = np.min(np.array(exec_times))

        # Alternate way to measure the execution time but it has huge error factor.
        # exec_times = np.zeros(10)

        # for i in range(10):
        #     start = time.time()
        #     Wrapper(pumping_data_size)
        #     end = time.time()
        #     exec_times[i] = (end - start) * 1000

        # # Execution time in milliseconds
        # runtime_dictionary[pumping_data_size] = np.min(exec_times)

    return runtime_dictionary


def run_inference_on_complexity(rtdc):
    """
    Fit to a complexity from the runtime dictionary.
        Args:
            - rtdc: the runtime dictionary

        Returns:
            - Fitted class. If not possible raises NotFittedError.
    """

    complexities = [Constant, Linear, Logarithmic, Linearithmetic, Quadratic, Cubic, Exponential]

    x = np.array([data for data in rtdc.keys()])       # Size of N
    y = np.array([data for data in rtdc.values()])     # Execution time with respect to size of N
    
    fit_dict = dict()

    for complexity in tqdm(complexities, total=7, desc="Calculating complexity: "):
        complexity_objc = complexity()
        residuals = complexity_objc.fit(x, y)
        fit_dict[residuals] = f"{complexity_objc}"
    
    minimum_residual = min(np.array([data for data in fit_dict.keys()]))

    return fit_dict[minimum_residual]
