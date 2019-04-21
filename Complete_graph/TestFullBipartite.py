import unittest
from Complete_graph.BipartiteGraphEdgeColoring import *
#from Factory import *
from Complete_graph.Graphs import *

class TestCompleteBipartiteGraph(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()
        self.g1 = graph.load("graf.txt")

    def test_full_bipartite_edge_color(self):
        algorithm = EdgeColorBipartite(self.g1)
        algorithm.bipartite_edge_color()
        pass