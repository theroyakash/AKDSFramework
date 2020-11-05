from AKDSFramework.structure.linkedlist import SinglyLinkedList
from AKDSFramework.error import EmptyStackError

class Stack:
    def __init__(self):
        """
        Stack Implementation with Linked List
        """
        self.stack = SinglyLinkedList()

    def push(self, value):
        """
        Push some value on to the stack
            Args:
                value (Any): Any value you want to push to the stack.
        """
        self.stack.add(value)

    def pop(self):
        """
        pops out the last value from the stack.
            Returns:
                - Element that just popped off the stack
        """
        if self.stack.count() != 0:
            return self.stack.removeAt(self.stack.count() - 1)
        else:
            raise LookupError('Not enough element to pop')

    def __reversed__(self):
        return reversed(self.stack)

    def __iter__(self):
        raise NotImplementedError('Iteration over the stack is not implemented yet')

    def peak_top(self):
        """
        Quickly peak at the very top of the stack
            Returns:
                - The top most element of the stack
        """
        return self.stack.get_head()

    def __len__(self):
        return len(self.stack)

    def isEmpty(self):
        """
        Says whether the stack is empty or not
            Returns:
                - Bool: True if no elements in the stack else False.
        """
        return True if self.stack.count() == 0 else False

    def __str__(self):
        """
        This is the string representation of the stack element's values
            Returns:
                - String representation of the stack element's values
        """

        array = []
        current = self.stack.get_head()

        while current:
            array.append(current.value)
            current = current.next

        return str(array)


class ListBasedStack:
    def __init__(self, array=None):
        """
        Create a Stack based on array.
            Args:
                - array (list): Pass in an array to initialize the stack. If nothing is passed a blank stack is intialized.
        """
        if array is None:
            self.stack = []
        else:
            self.stack = array
    
    def push(self, value):
        """
        Push data onto the stack.
            Args:
                - value (Any): Pass in the value you want to push
        """
        self.stack.append(value)
        
    def pop(self):
        if len(self.stack)==0:
            raise EmptyStackError('Stack may be empty')
        else:
            self.stack.pop(-1)

    def clear(self):
        self.stack = []
    
    def __len__(self):
        return len(self.stack)
    
    def clone(self):
        return self.stack.copy()
    
    def peek(self):
        if len(self.stack)==0:
            raise EmptyStackError('Stack may be empty')
        else:
            return self.stack[-1]
    
    def searchFor(self, element):
        index = -1
        for i in range(len(self.stack)):
            if self.stack[i] == element:
                index = i
        
        return index

    def __str__(self):
        return str(self.stack)
