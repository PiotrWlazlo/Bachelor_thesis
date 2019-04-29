# -*- coding: utf-8 -*-

from Complete_graph.Factory import *
from Complete_graph.Graphs import *
import queue
import random
'''

class EdgeColorBipartite:

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict()
        self.m = 0   # graph.e() is slow
        self.U = dict()  # color RED
        self.V = dict()  # color BLUE
        self.visited = []
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
            else:
                self.color[edge] = None   # edge.source < edge.target
                self.m += 1
        if len(self.color) < self.m:
            raise ValueError("edges are not unique")

    def run(self):
        self.isBipartite(list([x for x in self.graph.iternodes()])[0])
        #pokoloruj krawędzie kolorami w losowej kolejnosci
        #Ustalenie ilości kolorów - porównanie dwóch długości dwóch list
        delta = max(self.graph.degree(node) for node in self.graph.iternodes()) #to można szbciej, porównanie dwóch node'ów z dwóch zbiorów
        colors = list(range(delta))
        for node in self.U.keys():
            for count, edge in enumerate(self.graph.iteroutedges(node)):
                self.color[edge] = colors[count]
            colors.append(colors.pop(0))

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
                        self.V[n] = set()
                        Q.put(n)
                    elif source in self.V:
                        self.U[n] = set()
                        Q.put(n)


if __name__ == '__main__':
    graph = Graph(8)
    g1 = graph.load("graf.txt")
    algorithm = EdgeColorBipartite(g1)
    algorithm.run()
    print("Set U")
    print(algorithm.U)
    print("Set V")
    print(algorithm.V)
    print(algorithm.color)
'''

#!/usr/bin/python

from Complete_graph.bipartite import BipartiteGraphBFS as Bipartite
#from bipartite import BipartiteGraphDFS as Bipartite


class CompleteBipartiteGraphEdgeColoring:
    """Find an edge coloring for a complete bipartite graph."""

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict()
        self.m = 0   # graph.e() is slow
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
            else:
                self.color[edge] = None   # edge.source < edge.target
                self.m += 1
        if len(self.color) < self.m:
            raise ValueError("edges are not unique")
        algorithm = Bipartite(self.graph)   # O(V+E) time
        algorithm.run()
        # Slowniki na indeksy wierzcholkow.
        self.D1 = dict()
        self.D2 = dict()
        idx1 = 0
        idx2 = 0
        for node in self.graph.iternodes():   # O(V) time
            if algorithm.color[node] == 1:
                self.D1[node] = idx1
                idx1 += 1
            else:
                self.D2[node] = idx2
                idx2 += 1
        if self.m != len(self.D1) * len(self.D2):
            raise ValueError("the graph is not complete bipartite")

    def run(self):
        """Executable pseudocode."""
        # Liczba dostepnych kolorow krawedzi.
        Delta = max(len(self.D1), len(self.D2))
        for node in self.D1:   # lacznie czas O(E)
            for edge in self.graph.iteroutedges(node):
                # Konce krawedzi sa w D2.
                c = (self.D1[edge.source] + self.D2[edge.target]) % Delta
                if edge.source > edge.target:   # moga byc odwrocone krawedzie
                    edge = ~edge
                self.color[edge] = c

# EOF
