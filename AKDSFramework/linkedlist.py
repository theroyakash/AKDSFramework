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
            value (Any): For each node this attribute will carry the value
        """
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        """
        Initialization of Singly linked list.
        """
        # Sentinel Means a soldier or guard whose job is to stand and keep watch.
        self.sentinel = Node(None)
        self.head = self.sentinel
        self.size = 0

    def add(self, value):
        """
        Adds any element to the linked list
        Args:
            value (Any): Put in the value you want to add.
        """
        new = Node(value)

        if self.size == 0:
            # If there exists no element in the LinkedList
            self.head.next = new
            self.head = new
            self.size += 1
        else:
            # If there exists at least one/few element in the LinkedList
            self.sentinel.next = new
            new.next = self.head
            self.head = new
            self.size += 1

    def remove(self):
        """
        Remove any node from linked list
        Returns:
            value (Any): returns the value at the node
        """
        if self.size == 0:
            return None
        elif self.size == 1:
            removed_node = self.head
            self.sentinel.next = None
            self.head = self.sentinel
            self.size -= 1
            return removed_node
        else:
            removed_node = self.head
            self.sentinel.next = self.head.next
            self.head = self.sentinel.next
            self.size -= 1
            return removed_node

    def get_head(self):
        """
        Get the head node value of the linked list
        Returns:
            - The node value for the head
        """
        return self.head.value

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

    def __len__(self):
        """
        Alternate way of getting the size of the linked list
        Returns:
            Size of the linked list
        """
        return self.size

    def __str__(self):
        """
        This is the string representation of the linked list values
        Returns:
            - String representation of the linked list values
        """
        array = []
        current = self.head

        while current:
            array.append(current.value)
            current = current.next

        return str(array)
