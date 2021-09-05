from AKDSFramework.structure.linkedlist import SinglyLinkedList
from AKDSFramework.error import EmptyStackError
from typing import Any


class Stack:

    stack: SinglyLinkedList

    def __init__(self):
        """
        Stack Implementation with Linked List
        """
        self.stack = SinglyLinkedList()

    def push(self, value: Any) -> None:
        """
        Push some value on to the stack
        Args:
            value (Any): Any value you want to push to the stack.
        """
        self.stack.add(value)

    def pop(self) -> Any:
        """
        pops out the last value from the stack.
        Returns:
            - Element that just popped off the stack
        """
        if self.stack.count() != 0:
            return self.stack.removeAt(self.stack.count() - 1)
        else:
            raise LookupError('Stack Underflow')

    def __reversed__(self) -> SinglyLinkedList:
        return reversed(self.stack)

    def __iter__(self):
        raise NotImplementedError(
            'Iteration over the stack is not implemented yet')

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
        return self.stack.count() == 0

    def __str__(self):
        """
        This is the string representation of the stack element's values
        Returns:
            - String representation of the stack element's values
        """
        return str(self.stack)


class ListBasedStack:

    array: list[Any]

    def __init__(self, array=None):
        """
        Create a Stack based on array.
        Args:
            - array (list): Pass in an array to initialize the stack. If nothing is passed a blank stack is intialized.
        """
        self.stack = [] if array is None else array

    def push(self, value: Any) -> None:
        """
        Push data onto the stack.
        Args:
            - value (Any): Pass in the value you want to push
        """
        self.stack.append(value)

    def pop(self) -> Any:
        if len(self.stack) == 0:
            raise EmptyStackError('Stack may be empty')
        else:
            self.stack.pop(-1)

    def clear(self) -> None:
        """
        Clears the entire stack
        """
        self.stack = []

    def __len__(self) -> int:
        return len(self.stack)

    def clone(self):
        return self.stack.copy()

    def peek(self) -> Any:
        if len(self.stack) == 0:
            raise EmptyStackError('Stack may be empty')
        else:
            return self.stack[-1]

    def search(self, element: Any) -> Any:
        index = -1
        for i in range(len(self.stack)):
            if self.stack[i] == element:
                index = i

        return index

    def __str__(self) -> str:
        return str(self.stack)
