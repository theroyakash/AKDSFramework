from AKDSFramework.applications.singlesourceshortestpath import compute_bellmanford
from AKDSFramework.structure.graph import GraphDictionaryRepresented, Vertex
from AKDSFramework.error import NegativeEdgeCycleWarning

import unittest

class Test(unittest.TestCase):
	def setUp(self):
		self.g = GraphDictionaryRepresented()

		for i in range(1, 5):
		    self.g.register_vertex(Vertex(f'{i}'))

		edges = [('12', 4), ('14', 5), ('24', 5), ('43', 3), ('32', -10)]

		for edge in edges:
		    self.g.register_edge(edge[0][:1], edge[0][1:], directed=True, weight=edge[1])

	def test_case_NegativeEdgeCycleWarning(self):
		self.assertRaises(NegativeEdgeCycleWarning, compute_bellmanford, graph=self.g, starting_vertex ='1')

	def test_case_pass(self):
		self.g1 = GraphDictionaryRepresented()
		for i in range(1, 7):
		    self.g1.register_vertex(Vertex(f'{i}'))

		edges = [('12', 2), ('13', 4), ('23', 1), ('24', 7), ('35', 3), ('54', 2), ('46', 1), ('56', 5)]

		for edge in edges:
		    self.g1.register_edge(edge[0][:1], edge[0][1:], directed=True, weight=edge[1])

		self.assertEqual({'1': 0, '2': 2, '3': 3, '4': 8, '5': 6, '6': 9}, compute_bellmanford(self.g1, starting_vertex='1'))

if __name__ == '__main__':
    unittest.main()