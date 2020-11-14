class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return f'<Node: ({self.key}, {self.value}, Next: {self.next})>'

    def __repr__(self):
        return str(self)


class Hash:
    """
    Hash object class.
    """

    def __init__(self):
        self.buckets_capacity = 60
        self.size = 0
        self.buckets = [None] * self.buckets_capacity

    def hash(self, key):
        hash_sum = 0
        # For each character in the key do this
        # Add (index + length of key) ^ (current char code)
        # Cap the hash_sum in range [0, self.buckets_capacity - 1]
        for index, y in enumerate(key):
            hash_sum += (index + len(key)) ** ord(y)
            hash_sum = hash_sum % self.buckets_capacity
        return hash_sum

    def include(self, key, value):
        """
        Include a new key-value pair in your already existing hash table.
            Args:
                - key (str): Any thing can be your key
                - value (Any): Mention the value associated with your particular key
        """
        index = self.hash(key)
        node = self.buckets[index]

        # If the bucket is empty then add the key, value pair
        if node is None:
            self.buckets[index] = Node(key, value)
            return

        prev = node
        while node is not None:
            prev = node
            node = node.next

        self.size += 1

        prev.next = Node(key, value)

    def searchFor(self, key):
        """
        Search for a given key.
            Args:
                - key (str): Any thing can be your key. Mention the key you want to search for the value associated with it.
        """

        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key:
            node = node.next

        if node is None:
            return None
        else:
            return node.value

    def removeFor(self, key):
        """
        Remove value associated with some key.
            Args:
                - key (str): Mention the key for which you want to delete the value.
        """
        index = self.hash(key)
        node = self.buckets[index]

        prev = None

        # Go to the node for key in the args
        while node is not None and node.key != key:
            prev = node
            node = node.next

        if node is None:
            return None
        else:
            # we found a key and now deleting the data
            self.size -= 1
            result = node.value
            if prev is None:
                self.buckets[index] = node.next
            else:
                prev.next = prev.next.next

        return result
