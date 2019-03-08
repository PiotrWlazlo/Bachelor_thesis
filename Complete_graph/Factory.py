import random
import math
from Edges import *


class GraphFactory:
    """The class for graph generators."""

    def __init__(self, graph_class):
        """Get a graph class."""
        self.cls = graph_class

    def make_complete(self, n=1, directed=False):
        """Create a weighted complete graph."""
        graph = self.cls(n, directed)
        weights = list(range(1, math.floor(1 + n * (n-1)/2)))   # different weights
        random.shuffle(weights)
        for node in range(n):
            graph.add_node(node)
        for source in range(n):
            for target in range(source + 1, n):   # no loops
                if random.random() > 0.5:   # random direction
                    graph.add_edge(Edge(source, target, weights.pop()))
                else:
                    graph.add_edge(Edge(target, source, weights.pop()))
        return graph
