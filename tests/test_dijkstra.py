import unittest
from AKDSFramework.applications.singlesourceshortestpath import compute_dijkstra
from AKDSFramework.structure.graph import GraphDictionaryRepresented, Vertex
from AKDSFramework.structure.heap import MinHeap

class Test(unittest.TestCase):
    def setUp(self):
        self.g = GraphDictionaryRepresented()
        for i in range(1, 7):
            self.g.register_vertex(Vertex(f'{i}'))

        edges = [('12', 2), ('13', 4), ('23', 1), ('24', 7), ('35', 3), ('54', 2), ('46', 1), ('56', 5)]

        for edge in edges:
            self.g.register_edge(edge[0][:1], edge[0][1:], directed=True, weight=edge[1])

    def test_case_1(self):
        self.assertEqual({'1': 0, '2': 2, '3': 3, '4': 8, '5': 6, '6': 9}, compute_dijkstra(self.g, starting_vertex='1'))

if __name__ == '__main__':
    unittest.main()