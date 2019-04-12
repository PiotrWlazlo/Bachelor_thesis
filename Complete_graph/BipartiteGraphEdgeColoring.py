# -*- coding: utf-8 -*-

from Factory import *
from Graphs import *
import Queue
import random


class EdgeColorBipartite:

    def __init__(self, graph):
        """The algorithm initialization."""
        if graph.is_directed():
            raise ValueError("the graph is directed")
        self.graph = graph
        self.color = dict()
        self.m = 0   # graph.e() is slow
        self.U = list()  # color RED
        self.V = list()  # color BLUE
        self.visited = []
        for edge in self.graph.iteredges():
            if edge.source == edge.target:
                raise ValueError("a loop detected")
            else:
                print("Dodałem krawedz")
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
        x = len(self.U)
        if len(self.V)>x:
            x = len(self.V)
        #for i in range(x):
        #    self.color[Edge(random.choice(self.U), random.choice(self.V))] = i
        for edge in p:
            self.color[edge] = random.choice(range(1, x+1))


    def recolored(self):
        pass


    def isBipartite(self, source=None, pre_action=None, post_action=None):
        print(source)
        #if source is None:
        #    print('dupa')
        if source is None:
            pass
        else:
            self.U.append(source)
            for node in self.graph.iternodes():
                if node not in self.U or node not in self.V:
                    self.visit(node)

    def visit(self, node, pre_action=None, post_action=None):
        Q = Queue.Queue()
        Q.put(node)
        while not Q.empty():
            source = Q.get()
            for n in self.graph.iteradjacent(source):
                if (source in self.U and n in self.U) or (n in self.V and source in self.V):
                    raise Exception("Graph is not Bipartite")
                if n not in self.U and n not in self.V:
                    if source in self.U:
                        self.V.append(n)
                        Q.put(n)
                    elif source in self.V:
                        self.U.append(n)
                        Q.put(n)
'''         
        for node in self.graph.iternodes():
            if node in U or node in V:
                continue
            else:
                U.add(node) #coloring first node as RED
'''

if __name__ == '__main__':
    graph = Graph(6)
    g1 = graph.load("graf.txt")
    print(g1.v())
    #print(g1.m)
    #g1.save("graf.txt")
    algorithm = EdgeColorBipartite(g1)
    print(g1)
    #print(algorithm.m)
    #print(algorithm.color)
    #print(list([x for x in g1.iternodes()])[0])
    algorithm.bipartite_edge_color()
    print("Set U")
    print(algorithm.U)
    print("Set V")
    print(algorithm.V)
    print(algorithm.color)
'''
if __name__ == '__main__':
    graph = Factory(Graph)
    g1 = graph.make_complete(5)
    #print(g1.v())
    algorithm = EdgeColor(g1)
    #print(algorithm.color)
    algorithm.run_odd()
    print("Kolory")
    print(algorithm.color)
'''