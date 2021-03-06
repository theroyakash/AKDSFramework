# Implementation of moving average with classic queue structure.

from AKDSFramework.structure import ArrayQueue

class MovingAverage:
    """
    Implementation of moving average using classic queue data structure
    """

    def __init__(self, size):
        """
        Initializes the Queue
        Args:
            size: Specify the size of the queue before hand as AKDSFramework implements a static array for Queues
        """
        self.queue = ArrayQueue(capacity=size)
        self.current_average = 0

    def next(self, value):
        """
        Add the next value for the moving average to continue
        Args:
            value: Value for the next element in the moving average calculation.
        """
        self.queue.enqueue(value)

        sum_queue = 0
        for data in self.queue:
            if data != None:
                sum_queue += data

        self.current_average = sum_queue / len(self.queue)

    def current_average(self):
        return self.current_average
