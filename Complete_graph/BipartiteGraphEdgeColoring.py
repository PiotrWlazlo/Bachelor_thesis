# -*- coding: utf-8 -*-

from Complete_graph.Factory import *
from Complete_graph.Graphs import *
import queue
import random


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
                #self.edges.append(edge)
        if len(self.color) < self.m:
            raise ValueError("edges are not unique")

    def bipartite_edge_color(self):
        self.isBipartite(list([x for x in self.graph.iternodes()])[0])
        #pokoloruj krawędzie kolorami w losowej kolejnosci
        #Ustalenie ilości kolorów - porównanie dwóch długości dwóch list
        p = self.color.keys() #Edges to colored
        #self.U = dict(self.U)
        #self.V = dict(self.V)
        x = len(self.U) #delta - liczbba kolorów
        if len(self.V)>x:
            x = len(self.V) #delta
        colors = list(range(x))
        for node in self.U.keys():
            for count,edge in enumerate(self.graph.iteroutedges(node)):
                self.color[edge] = colors[count]
            colors.append(colors.pop(0))
            '''
                    for i in self.U.keys():
                        for x in range(1, x+1):
                            self.U[i].add(x)   #missing colors for nodes from U set
                    for i in self.V.keys():
                        for x in range(1, x+1):
                            self.V[i].add(x)   #missing colors for node from V set
                    i = 1
                    '''
        #for i in range(x):
        #    self.color[Edge(random.choice(self.U), random.choice(self.V))] = i
        #for edge in p:
        #    x = random.choice(range(1, x+1))
        #    self.color[edge] = x
        #    self.U[edge.source].pop()


    def recolor(self):
        pass

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
    algorithm.bipartite_edge_color()
    print("Set U")
    print(algorithm.U)
    print("Set V")
    print(algorithm.V)
    print(algorithm.color)
