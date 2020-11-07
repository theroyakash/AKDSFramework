class QueueADT:
    def __init__(self):
        self.size = 0
    
    def __len__(self):
        return self.size
    
    def isEmpty(self):
        return False if self.size > 0 else True
    
    def enqueue(self):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

    def peek(self):
        raise NotImplementedError

    def __iter__(self):
        raise NotImplementedError


class ArrayQueue(QueueADT):
    """
    Intialize an Queue using Array
            Args:
                - capacity (int): Creates a None value static array with specified capacity.
    """
    def __init__(self, capacity):
        super(ArrayQueue, self).__init__()
        self.array = [None] * capacity

        self.front, self.rear = 0, 0

    def enqueue(self, value):
        """
        Enqueue an element into the Queue Object
            Args:
                - value (Any): Pass in the object you want to enqueue
        """
        if self.rear == len(self.array):
            self.expand()
        self.array[self.rear] = value
        self.size += 1
        self.rear += 1
    
    def dequeue(self):
        """
        Dequeue from the beginning of the Queue following the FIFO policy
        """
        if self.isEmpty():
            raise IndexError('Queue Empty')
        val = self.array[self.front]
        self.array[self.front] = None
        self.front += 1
        self.size -= 1
        return val

    def __iter__(self):
        """
        Iterable in a for and while loop
        """
        pointer = self.front
        while True:
            if pointer == self.rear:
                return
            yield self.array[pointer]
            pointer += 1

    def expand(self):
        """
        Expands the size of the array with linear time complexity, Meant for usage in internal state. Don't use this operation outside.
        """
        self.array += [None] * len(self.array)

    def __str__(self):
        return str(self.array)
