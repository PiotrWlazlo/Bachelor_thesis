# -*- coding: utf-8 -*-

from Complete_graph.Graphs import *
import queue
from Complete_graph.edgecolorcs import *


class SimpleBipartiteEdgeColoring:

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict()
        self.m = 0  # graph.e() is slow
        self.U = dict()  # color RED
        self.V = dict()  # color BLUE
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
            else:
                self.color[edge] = None  # edge.source < edge.target
                self.m += 1
        if len(self.color) < self.m:
            raise ValueError("edges are not unique")
        # dict with missing colors for nodes.
        self.missing = None

    def run(self):
        Delta = max(self.graph.degree(node) for node in self.graph.iternodes())
        if Delta <= 2:
            # Greedy coloring suffies.
            algorithm = ConnectedSequentialEdgeColoring(self.graph)  # co to?
            algorithm.run()
            self.color = algorithm.color
        else:
            # Ustal liczbe wykorzystywanych kolorow.
            k = Delta + 1  # almost optimal (simple graphs!)
            self.missing = dict((node, set(range(k)))
                                for node in self.graph.iternodes())  # missing colors
            for edge in self.graph.iteredges():
                # Sprawdz wspolny kolor brakujacy.
                # To mozna chyba zrobic bardziej wydajnie.
                both = self.missing[edge.source] & self.missing[edge.target]
            #    if len(both) == 0:
            #        self._recolor(edge)
            #    else:
            #        c = min(both)  # choose min color available
            #        self._add_color(edge, c)

    def isBipartite(self, source=None):
        print(source)
        if source is None:
            pass
        else:
            self.U[source] = set()
            for node in self.graph.iternodes():
                if node not in self.U or node not in self.V:
                    self.visit(node)

    def visit(self, node):
        Q = queue.Queue()
        Q.put(node)
        while not Q.empty():
            source = Q.get()
            for n in self.graph.iteradjacent(source):
                if (source in self.U and n in self.U) or (n in self.V and source in self.V):
                    raise Exception("Graph is not Bipartite")
                if n not in self.U and n not in self.V:
                    if source in self.U:
                        #self.V[n] = set()
                        Q.put(n)
                    elif source in self.V:
                        #self.U[n] = set()
                        Q.put(n)