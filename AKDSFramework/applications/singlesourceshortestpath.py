from AKDSFramework.structure.graph import GraphDictionaryRepresented, Vertex
from AKDSFramework.structure.heap import MinHeap
from AKDSFramework.error import NegativeEdgeCycleWarning

# We'll use minheap for maintaining min priority queue and getting the next smallest edge.
def compute_dijkstra(graph: GraphDictionaryRepresented, starting_vertex: str) -> dict:
    r"""
    Computes dijkstra single source shortest path algorithm. Requires GraphDictionaryRepresented dictionary build with Vertex class.
        Args:
            - ``graph`` (GraphDictionaryRepresented): Graph on which you want to operate
            -  ``starting_vertex``: Starting vertex name in a string.
        Time complexity:
            Building distances dictionary takes :math:`O(V)` time. The while loop is executed once for every entry that gets added to the priority queue (Min Heap). 
            An entry can only be added when we explore an edge, so there are at most :math:`O(E)` iterations of the while loop.
            The for loop is executed at most once for every vertex, since the ``current_distance > distances[current_vertex]`` check ensures that we only process a vertex once.
            The for loop iterates over outgoing edges, so among all iterations of the while loop, the body of the for loop executes at most :math:`O(E)` times.
            Finally, if we consider that each priority queue operation (adding or removing an entry) is :math:`O(\log E)`, we can say the total running time is :math:`O(V + E \log E)`.
    """
    # Set distance from current vertex to all vertex as inf
    distances = {vertex: float('infinity') for vertex in graph.vertices}
    # Set distances from the starting vertex to starting vertex as 0
    distances[starting_vertex] = 0

    # Now make and maintain a min priority queue
    prQueue = [(0, starting_vertex)]
    prQueue = MinHeap(prQueue)
    prQueue.build()   # O(1) because pushing only one element in a empty heap is constant time

    # This while loop is running O(V) times.
    while len(prQueue) > 0:
        current_distance, current_vertex = prQueue.delete_root()
        prQueue.build()
        
        if current_distance > distances[current_vertex]:
            continue

        for adjacent_vertex in graph.vertices[current_vertex].neighbors:
            distance = current_distance + adjacent_vertex[1]  # adjacent_vertex[1] is the weight

            if distance < distances[adjacent_vertex[0]]:
                distances[adjacent_vertex[0]] = distance
                prQueue.add((distance, adjacent_vertex[0]))
                prQueue.build()

    return distances

def compute_bellmanford(graph: GraphDictionaryRepresented, starting_vertex: str):
    r"""
    Computes single source shortest path algorithms using bellman ford algorithm
        Args:
            - ``graph`` (GraphDictionaryRepresented): Graph you want to work on
            - ``starting_vertex`` (str): Starting Vertex of the graph to compute bellman ford

        Algorithm:
            - Prepare distance and predecessor for each node
            - Relax all the edges :math:`|V|-1` times
            - Run the loop one more time to check for if there is any negative edge cycle.

        Time complexity:
            Time complexity is :math:`O(V * E)` where V is the number of vertices and E is the number of edges
    """
    distances = {vertex : float('infinity') for vertex in graph.vertices}
    distances[starting_vertex] = 0

    # Run relaxation of edges for |V| - 1 times
    for _ in range(0, graph.number_of_vertices):
        # Go through each edge and relax them
        for vertex in graph.vertices.keys():
            for adjacent_vertex in graph.vertices[vertex].neighbors:
                if distances[adjacent_vertex[0]] > distances[vertex] + adjacent_vertex[1]:
                    distances[adjacent_vertex[0]] = distances[vertex] + adjacent_vertex[1]

    # Run this one more time to check if there is more relaxation then raise Negative edge Warning
    for vertex in graph.vertices.keys():
        for adjacent_vertex in graph.vertices[vertex].neighbors:
            if distances[adjacent_vertex[0]] > distances[vertex] + adjacent_vertex[1]:
                raise NegativeEdgeCycleWarning("Negative Edge cycle detected")

    return distances

