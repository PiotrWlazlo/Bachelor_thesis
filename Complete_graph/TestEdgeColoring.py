import unittest
from EdgeColoring import *
from Factory import *
from Graphs import *


class TestCompleteGraphEdgeColoring(unittest.TestCase):

    def setUp(self):
        self.N = 11
        self.N2 = 12
        self.graph = GraphFactory(Graph)
        self.g1 = self.graph.make_complete(self.N, directed=False)
        self.g1.save("graf.txt")
        self.g2 = self.graph.make_complete(self.N2, directed=False)

    def test_complete_odd_edge_coloring(self):
        algorithm = EdgeColor(self.g1)
        algorithm.run_complete()
        for edge in algorithm.color.keys():
            self.assertNotEqual(algorithm.color[edge], None)
        for i in range(self.g1.v()-1):
            color_set = set()
            for j in range(self.g1.v()-1):
                if i == j:
                    continue
                elif i > j:
                    color_set.add(algorithm.color[(j, i)])
                else:
                    color_set.add(algorithm.color[(i, j)])
            self.assertEqual(len(color_set), self.g1.degree(i)-1)
        all_colors = set(algorithm.color[edge] for edge in algorithm.color.keys())
        self.assertEqual(len(all_colors),self.g1.v())

    def test_complete_even_edge_coloring(self):
        algorithm = EdgeColor(self.g2)
        algorithm.run_complete()
        for edge in algorithm.color.keys():
            self.assertNotEqual(algorithm.color[edge], None)
        for i in range(self.g1.v()-1):
            color_set = set()
            for j in range(self.g1.v()-1):
                if i == j:
                    continue
                elif i > j:
                    color_set.add(algorithm.color[(j, i)])
                else:
                    color_set.add(algorithm.color[(i, j)])
            self.assertEqual(len(color_set), self.g1.degree(i)-1)
        all_colors = set(algorithm.color[edge] for edge in algorithm.color.keys())
        self.assertEqual(len(all_colors),self.g1.v())


if __name__ == '__main__':
    unittest.main()
