import numpy as np
from AKDSFramework.structure.queue import ArrayQueue
from AKDSFramework.error import BadVertexTypeError

class GraphMatrixRepresented:
    """
    Matrix representation of Graph
        Args:
            - ``vertices`` (int): Number of total vertices in the graph
            - ``is_directed`` (Bool): Expects directed or not directed graph. Defaults to not directed graph.

        Space Complexity:
            Space complexity for graphs represented with adjacenecy matrix is :math:`O(V^2)` where :math:`V` is number
            of vertices. Use this method of representation only when your graph is dense. Number of edges `:math:|E| ≥ V^2`
            Else a lot of zeros will be placed inside the matrix which won't be that efficient space wise. For sparse matrix
            use ``GraphDictionaryRepresented`` instead of ``GraphMatrixRepresented``.

        .. Examples::
            >>> from AKDSFramework.structure.graph import GraphMatrixRepresented
            >>> import numpy as np
            >>> graph1 = GraphMatrixRepresented(vertices=20, is_directed=True)
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
    def __init__(self, vertices, is_directed=False):
        self.vertices = vertices
        self.graph = np.zeros((vertices, vertices), dtype=int)
        self.is_directed = is_directed
        self.number_of_edges = 0

    def add_edge_between(self, start, end, weight):
        """
        Adds edge between two points in a graph. If the graph is not directed then one edge b/w start and end and one b/w end and start will be added which has the same weight.
            Args:
                - ``start`` (int): Starting Index where the edge starts
                - ``end`` (int): Ending index where the edge ends
                - ``weight`` (float or int): Weight of the edge
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
        Shows the graph as a 2D Numpy matrix. Alternatively you can use the ``print()`` method to show the graph.
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

    def __str__(self):
        """
        2D matrix representation of declared graph
        """
        return str(self.graph)


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbors = list()

    def __iter__(self):
        for vertex in self.neighbors:
            yield vertex[0]

    def add_neighbor(self, v, weight):
        if v not in self.neighbors:
            self.neighbors.append((v, weight))
            self.neighbors.sort()

    def __repr__(self):
        return f"<AKDSFramework.structure.graph.Vertex object {self.name} with neighbors: {self.neighbors}>"

    
class GraphDictionaryRepresented:
    """
    Dictionary representation of Graph
        Args:
            - vertices (int): Number of total vertices in the graph
            - is_directed (Bool): Expects directed or not directed graph. Defaults to not directed graph.
    """
    def __init__(self):
        self.vertices = {}
        self.number_of_vertices = 0
    
    def register_vertex(self, vertex):
        """
        Register a vertex in the graph
        """
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            self.number_of_vertices += 1
            return True
        else:
            raise BadVertexTypeError

    def register_edge(self, init, stop, weight=1, directed=True):
        if directed:
            if init in self.vertices and stop in self.vertices:
                self.vertices[init].add_neighbor(stop, weight)
                self.vertices[stop].add_neighbor(init, weight)
                return True
            else:
                return False
        else:
            if init in self.vertices and stop in self.vertices:
                self.vertices[init].add_neighbor(stop, weight)
                return True
            else:
                return False
        
    def prettyprint(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + ':' + str(self.vertices[key].neighbors))

    def raw_dict(self):
        return self.vertices

    def BFS(self, startFromVertex):
        visited_set = set()
        # create a first in first out queue to store all the vertices for BFS
        queue = ArrayQueue(capacity=20)
        # mark the source node as visited and enqueue it
        visited_set.add(startFromVertex)
        queue.enqueue(startFromVertex)

        while queue:
            vertex = queue.dequeue()
            # loop through all adjacent vertex and enqueue it if not yet visited
            for adjacent_vertex in self.vertices[vertex]:
                if adjacent_vertex not in visited_set:
                    queue.enqueue(adjacent_vertex)
                    visited_set.add(adjacent_vertex)

        return visited_set
