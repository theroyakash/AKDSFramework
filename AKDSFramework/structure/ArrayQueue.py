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
        if (self.rear + 1) == len(self.array):
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
        for index in range(len(self.array)):
            if index != len(self.array) - 1:
                self.array[index] = self.array[index + 1]
            else:
                self.array[index] = None
        return val

    def __iter__(self):
        """
        Iterable in a for and while loop
        """
        for index in range(len(self.array)):
            if index == self.rear:
                return
            yield self.array[index]

    def __getitem__(self, index):
        return self.array[index]

    def expand(self):
        """
        Expands the size of the array with linear time complexity, Meant for usage in internal state. Don't use this operation outside.
        """
        self.array += [None] * len(self.array)

    def __str__(self):
        returnable_array = []
        for index in range(len(self.array)):
            if self.array[index]==None:
                break
            else:
                returnable_array.append(self.array[index])
        return str(returnable_array)
