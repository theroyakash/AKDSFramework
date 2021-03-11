import unittest
from AKDSFramework.structure import GraphDictionaryRepresented, Vertex

class Test(unittest.TestCase):
    def setUp(self):
        self.g = GraphDictionaryRepresented()
        for i in range(1, 8):
            self.g.register_vertex(Vertex(f'{i}'))

        edges = ['15', '14', '12', '27', '26', '23']

        for edge in edges:
            self.g.register_edge(edge[:1], edge[1:], directed=False)

    def test_bfs(self):
        self.assertEqual("['1', '2', '4', '5', '3', '6', '7']", str(self.g.BFS("1")))

    def test_dfs(self):
        self.assertEqual("['1', '2', '3', '6', '7', '4', '5']", str(self.g.DFS("1")))

    def test_other(self):
        self.assertEqual(7, self.g.number_of_vertices)

if __name__ == '__main__':
    print('graph tests running')
    unittest.main()
