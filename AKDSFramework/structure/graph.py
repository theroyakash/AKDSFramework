import numpy as np


class Graph:

    def __init__(self, vertices, is_directed=False):
        """
        Initialize the graph
            Args:
                - vertices (int): Number of total vertices in the graph
                - is_directed (Bool): Expects directed or not directed graph. Defaults to not directed graph.

            Examples:
                >>> from AKDSFramework.structure.graph import Graph
                >>> import numpy as np
                >>> graph1 = Graph(vertices=20, is_directed=True)
                >>> # Now add few edges with random weights
                >>> while graph1.number_of_edges < 100:
                >>>     random_start = np.random.randint(low=0, high=graph1.vertices)
                >>>     random_end = np.random.randint(low=0, high=graph1.vertices)
                >>>     random_weight = np.random.randint(-7, 20)
                >>>     if random_weight != 0 and graph1.show_graph()[random_start][random_end] == 0:
                >>>         graph1.add_edge_between(start=random_start, end=random_end, weight=random_weight)
                >>>         graph1.add_edge_between(start=random_start, end=random_end, weight=random_weight)
                >>>     else:
                >>>         pass
                >>> print(graph1.number_of_edges)  # or print(graph1.count_edges())
                >>> print(graph1.vertices)
                >>> print(graph1.show_graph())
        """

        self.vertices = vertices
        self.graph = np.zeros((vertices, vertices), dtype=int)
        self.is_directed = is_directed
        self.number_of_edges = 0

    def add_edge_between(self, start, end, weight):
        """
        Adds edge between two points in a graph. If the graph is not directed then one edge b/w start and end and one b/w end and start will be added which has the same weight.
            Args:
                - start (int): Starting Index where the edge starts
                - end (int): Ending index where the edge ends
                - weight (float or int): Weight of the edge
        """

        if not self.is_directed and self.graph[start][end] == 0 and self.graph[end][start] == 0:
            self.graph[start][end] = weight
            self.graph[end][start] = weight
            self.number_of_edges += 1

        elif self.is_directed and self.graph[start][end] == 0:
            self.graph[start][end] = weight
            self.number_of_edges += 1

        else:
            pass

    def show_graph(self):
        """
        Shows the graph as a 2D Numpy matrix.
            Returns:
                - Numpy 2D array showing the graph.
        """
        return self.graph

    def count_edges(self):
        """
        Returns:
            - Total edge count
        """
        return self.number_of_edges
