from AKDSFramework.structure.linkedlist import SinglyLinkedList


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
