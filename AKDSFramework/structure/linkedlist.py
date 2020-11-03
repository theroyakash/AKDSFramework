"""
This is the beginning of Linked list data structure module.
We currently support singly linked list and doubly linked list.

@author: theroyakash
"""


# Linked list helper class Node


class Node:
    def __init__(self, value):
        """
        Node class for linked list. Each element of a linked list is called a node.
            Args:
                - value (Any): For each node this attribute will carry the value
        """
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        """
        Initialization of Singly linked list.
        """
        self.head = Node(None)
        self.size = 0

    def add(self, value, at_end=True, position=0):
        """
        Adds any element to the linked list
            Args:
                - value (Any): Put in the value you want to add.
                - at_end (bool): If you want to add to the end of the list leave this blank. Defaults to adding at the end.
                - position (int): If you choose ``at_end`` = False then add the position where you want to add new value.
        """
        new = Node(value)

        if at_end:
            position = self.size
        else:
            position = position

        if not 0 <= position <= self.size:
            raise IndexError('Directed position out of bounds')
        elif position == 0:
            new.next = self.head
            self.head = new
            self.size += 1
        else:
            temp = self.head
            for _ in range(position - 1):
                temp = temp.next
            new.next = temp.next
            temp.next = new
            self.size += 1

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.next

    def removeAt(self, index=0):
        """
        Remove any node from linked list
            Returns:
                - value (Any): returns the value at the node
        """
        if not 0 <= index <= self.size:
            raise IndexError(f"Directed position {index} out of bounds")

        delete_node = self.head
        if index == 0:
            self.head = self.head.next
            self.size -= 1
        else:
            temp = self.head
            for _ in range(index - 1):
                temp = temp.next
            delete_node = temp.next
            temp.next = temp.next.next
            self.size -= 1
            return delete_node.value

    def get_head(self):
        """
        Get the head node value of the linked list
            Returns:
                - The node value for the head
        """
        return self.head

    def count(self):
        """
        Get the size of the linked list. How many Nodes are there in the linked list.
            Returns:
                - The number of nodes in the linked list.
        """
        return self.size

    def isEmpty(self):
        """
        Checks if linked list is empty or not.
            Returns:
                - Bool: Return True if linkedlist is empty else False.
        """
        return True if self.size == 0 else False

    def __reversed__(self):
        """
        Returns:
            - Reverses the defined linked list
        """

        previous = None
        current = self.head

        while current:
            # Store the current node's next node in temporary variable
            next_node = current.next
            # Make the current node's next pointer pointing back
            current.next = previous
            # Make the previous node be the current node
            previous = current
            # progress the iteration
            current = next_node

        # return previous in order to put the head at the end
        self.head = previous

        self.removeAt(0)
        noneNode = Node(None)
        pointer = self.head

        while pointer.next is not None:
            pointer = pointer.next
        pointer.next = noneNode
        self.size += 1

        return self

    def __len__(self):
        """
        Alternate way of getting the size of the linked list
            Returns:
                Size of the linked list
        """
        return self.size

    def __getitem__(self, index):
        if not 0 <= index <= self.size:
            raise IndexError(f"You messed up boy. Index {index} is not available because it's out of bounds")
        for y, node in enumerate(self):
            if y == index:
                return node

    def __str__(self):
        """
        This is the string representation of the linked list values
            Returns:
                - String representation of the linked list values
        """
        array = []
        current = self.head

        while current:
            array.append(str(current.value))
            array.append(' --> ')
            current = current.next

        return ''.join(array[:-1])

    def prettyprint(self):
        # graph = pydot.Dot(graph_type='digraph')
        # parent_node = pydot.Node(f'{self.get_head().value}')
        # graph.add_node(parent_node)
        #
        # IMAGE = graph.create_png()
        # return IMAGE

        raise NotImplementedError
