#!/usr/bin/python

import unittest
from Complete_graph.structures.Edges import *
from Complete_graph.structures.Graphs import *
from Complete_graph.structures.Factory import *
from Complete_graph.algorithms.edgecolorsimplebipartite import *


class TestEdgeColoring(unittest.TestCase):

    def setUp(self): pass

    def test_cyclic_graph(self):
        N = 8
        assert N % 2 == 0
        gf = GraphFactory(Graph)
        G = gf.make_cyclic(N)
        algorithm = BipartiteGraphEdgeColoring(G)
        algorithm.run()
        for edge in G.iteredges():
            self.assertNotEqual(algorithm.color[edge], None)
        for node in G.iternodes():
            color_set = set()
            for edge in G.iteroutedges(node):
                if edge.source > edge.target:
                    color_set.add(algorithm.color[~edge])
                else:
                    color_set.add(algorithm.color[edge])
            self.assertEqual(len(color_set), G.degree(node))
        #print algorithm.color
        all_colors = set(algorithm.color[edge] for edge in G.iteredges())
        self.assertEqual(len(all_colors), 2)

    def test_Kpq(self):
        N1 = 5
        N2 = 3
        gf = GraphFactory(Graph)
        G = gf.make_bipartite(N1, N2, False, 1)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), N1 + N2)
        self.assertEqual(G.e(), N1 * N2)
        algorithm = BipartiteGraphEdgeColoring(G)
        algorithm.run()
        for edge in G.iteredges():
            self.assertNotEqual(algorithm.color[edge], None)
        for node in G.iternodes():
            color_set = set()
            for edge in G.iteroutedges(node):
                if edge.source > edge.target:
                    color_set.add(algorithm.color[~edge])
                else:
                    color_set.add(algorithm.color[edge])
            self.assertEqual(len(color_set), G.degree(node))
        #print algorithm.color
        all_colors = set(algorithm.color[edge] for edge in G.iteredges())
        self.assertEqual(len(all_colors), max(N1, N2))

    def test_bipartite(self):
        N1 = 5
        N2 = 8
        gf = GraphFactory(Graph)
        G = gf.make_bipartite(N1, N2)
        algorithm = BipartiteGraphEdgeColoring(G)
        algorithm.run()
        for edge in G.iteredges():
            self.assertNotEqual(algorithm.color[edge], None)
        for node in G.iternodes():
            color_set = set()
            for edge in G.iteroutedges(node):
                if edge.source > edge.target:
                    color_set.add(algorithm.color[~edge])
                else:
                    color_set.add(algorithm.color[edge])
            self.assertEqual(len(color_set), G.degree(node))
        #print algorithm.color
        all_colors = set(algorithm.color[edge] for edge in G.iteredges())
        Delta = max(G.degree(node) for node in G.iternodes())
        self.assertEqual(len(all_colors), Delta)

    def test_exceptions(self):
        self.assertRaises(ValueError, BipartiteGraphEdgeColoring,
            Graph(5, directed=True))
        gf = GraphFactory(Graph)
        G = gf.make_cyclic(4)
        #G.show()
        G.add_edge(Edge(0, 2))   # nie bedzie dwudzielny
        self.assertRaises(ValueError, BipartiteGraphEdgeColoring, G)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
