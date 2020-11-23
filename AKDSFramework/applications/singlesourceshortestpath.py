from AKDSFramework.structure.graph import GraphDictionaryRepresented, Vertex
from AKDSFramework.structure.heap import MinHeap

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
    prQueue.build()   # O(V)

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
