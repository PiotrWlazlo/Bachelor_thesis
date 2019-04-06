#!/usr/bin/python

class CompleteGraphEdgeColoring:
    """Find an edge coloring for a complete graph."""

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

    def run(self):
        """Executable pseudocode."""
        if self.graph.v() % 2 == 1:
            self.run_odd()
        else:
            self.run_even()

    def run_odd(self):
        """Edge coloring for n odd."""
        n = self.graph.v()
        # Numerowanie wierzcholkow.
        D = dict((node, i) for (i, node) in enumerate(self.graph.iternodes()))   # O(n)
        # Kolorowanie krawedzi.
        for edge in self.graph.iteredges():   # O(E)=O(n^2) time
            c = (D[edge.source] + D[edge.target]) % n
            self.color[edge] = c

    def run_even(self):
        """Edge coloring for n even."""
        n = self.graph.v()
        removed_node = self.graph.iternodes().next()
        removed_edges = list(self.graph.iteroutedges(removed_node)) # O(n) time
        self.graph.del_node(removed_node) # O(n) time, removed with edges
        #self.graph.show()
        self.run_odd()
        # Teraz trzeba znalezc brakujace kolory przy wierzcholkach.
        free = dict((node, set(range(n-1))) for node in self.graph.iternodes())
        for edge in self.graph.iteredges():   # O(E)=O(n^2) time
            c = self.color[edge]
            free[edge.source].remove(c)
            free[edge.target].remove(c)
        # Przywracanie wierzcholka z krawedziami.
        self.graph.add_node(removed_node)
        for edge in removed_edges:   # O(n) time
            assert edge.source == removed_node
            c = free[edge.target].pop()
            assert len(free[edge.target]) == 0   # byl jeden kolor wolny
            self.graph.add_edge(edge)
            if edge.source > edge.target:
                edge = ~edge
            self.color[edge] = c

# EOF
