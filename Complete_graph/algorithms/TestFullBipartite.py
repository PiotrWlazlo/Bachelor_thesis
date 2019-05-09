#!/usr/bin/python

import unittest
from Complete_graph.algorithms.BipartiteGraphEdgeColoring import *

class TestFullEdgeColoring(unittest.TestCase):

    def setUp(self): pass

    def test_Kpq(self):
        N1 = 5
        N2 = 3
        gf = GraphFactory(Graph)
        G = gf.make_bipartite(N1, N2, False, 1)
        self.assertFalse(G.is_directed())
        self.assertEqual(G.v(), N1 + N2)
        self.assertEqual(G.e(), N1 * N2)
        algorithm = CompleteBipartiteGraphEdgeColoring(G)
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

    def test_exceptions(self):
        self.assertRaises(ValueError, CompleteBipartiteGraphEdgeColoring,
            Graph(5, directed=True))
        gf = GraphFactory(Graph)
        G = gf.make_bipartite(2, 2, False, 1)
        #G.show()
        G.del_edge(Edge(0, 2))   # nie bedzie pelny dwudzielny
        self.assertRaises(ValueError, CompleteBipartiteGraphEdgeColoring, G)

    def tearDown(self): pass

if __name__ == "__main__":

    unittest.main()

# EOF
