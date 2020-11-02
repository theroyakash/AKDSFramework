"""
Heap Implementation
@author: theroyakash

Heaps are advanced data structures and are mostly implemented using priority queues.
They can be thought of as a tree-based structure, in which the tree is a complete binary tree.

The 2 main characteristics of Heaps are the followings
    - It should be a completely binary tree
    - Nodes must be according to the min-max order property
"""

from terminaltables import AsciiTable
from AKDSFramework.error.error import InvalidOperationError


class Heap:
    """
    Base Heap class
    """

    def __init__(self):
        pass

    def build(self):
        raise NotImplementedError

    def add(self, value):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

    def __len__(self):
        raise NotImplementedError


class MaxHeap(Heap):
    def __init__(self, array):
        """
        Heap Initialization with unsorted or sorted array whatever.
            Args:
                - array (list): Unsorted array to initialize the heap
        """
        super(MaxHeap, self).__init__()
        self.heap = array
        self.size = 0
        self.built = False

    def get_right_child(self, i):
        """
        Get right child for index i
            Args:
                - i (int): Index whose right child you want
            Returns:
                - Returns the right child of any node, if not possible returns None
        """
        right_index = i * 2 + 2
        if right_index < self.size:
            return right_index

        return None

    def get_left_child(self, i):
        """
        Get right child's index for parent i
            Args:
                - i (int): Index whose left child's index you want
            Returns:
                - Returns the right child of any node, if not possible returns None
        """
        left_index = i * 2 + 1
        if left_index < self.size:
            return left_index

        return None

    def heapify(self, index):
        if index < self.size:
            largest = index
            left_child = self.get_left_child(index)
            right_child = self.get_right_child(index)

            if left_child is not None and self.heap[left_child] > self.heap[largest]:
                largest = left_child
            if right_child is not None and self.heap[right_child] > self.heap[largest]:
                largest = right_child

            if largest != index:
                self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
                self.heapify(largest)

    def add(self, value):
        self.heap.append(value)
        self.__built = False
        self.size += 1

    def __getitem__(self, index):
        return self.heap[index]

    def __len__(self):
        return self.size

    def __reversed__(self):
        raise InvalidOperationError('Invalid operation specified.')

    def build(self):
        self.size = len(self.heap)
        self.heap = list(self.heap)
        if self.size <= 1:
            return

        for i in range(self.size // 2 - 1, -1, -1):
            self.heapify(i)

        self.__built = True

    def __str__(self):
        if not self.__built:
            print('The MaxHeap is not built yet, consider using the .build() method to build the heap first.')
        return str(self.heap)

    def prettyprint(self):
        table = [
            ['Head Node Value', 'left child', 'right child']
        ]

        for i in range(len(self.heap) // 2):
            entry = []
            head = self.heap[i]
            entry.append(head)
            try:
                lc = self.heap[i * 2 + 1]
            except IndexError:
                lc = 'None'
            try:
                rc = self.heap[i * 2 + 2]
            except IndexError:
                rc = 'None'

            entry.append(str(lc))
            entry.append(str(rc))
            table.append(entry)

        termtable = AsciiTable(table)
        print(termtable.table)
