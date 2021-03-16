class Node(object):
    """
    A Binary Search Tree Node.
    """
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


    def __str__(self):
        if self.left is None and self.right is None:
            return f'<Node> object {self.data} with no children'
        elif self.left is not None and self.right is None:
            return f'<Node> object {self.data} with left child {self.left.data} and no right children'
        elif self.left is None and self.right is not None:
            return f'<Node> object {self.data} with not left child and right child {self.right.data}'
        else:
            return f'<Node> object {self.data} with left child {self.left.data} and right child {self.right.data}'


class BinarySearchTree(object):
    """
    BinarySearchTree representation.
        Args:
            - root: Optional Root of the search tree. If not provided, returns an empty tree
    """

    def __init__(self, root=None):
        self.root = root

    def isEmpty(self):
        """
        Returns whether the search tree is empty
        """
        return self.root is None

    def __insert(self, value):
        """
        Insert Method for internal usage only.
        """
        new = Node(value, None, None)

        # Set the root as the value if the search tree is empty
        if self.isEmpty():
            self.root = new
        else:
            parent_node = self.root
            while True:  # While we don't reach a leaf node
                if value < parent_node.data:
                    if parent_node.left is None:
                        parent_node.left = new
                        break
                    else:
                        parent_node = parent_node.left

                else:
                    if parent_node.right is None:
                        parent_node.right = new
                        break
                    else:
                        parent_node = parent_node.right

    def insert(self, *values):
        """
        Insert a series of values into the binary search tree
        """
        for value in values:
            self.__insert(value)

    def search(self, value):
        if self.isEmpty():
            raise IndexError("Empty binary search tree")
        
        else:
            root_node = self.root
            while root_node is not None and root_node.data is not None:
                root_node = root_node.left if value<root_node.data else root_node.right

                return root_node


    def __str__(self):
        binary_search_tree_repr = ''
        return binary_search_tree_repr
