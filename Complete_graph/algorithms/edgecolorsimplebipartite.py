#!/usr/bin/python

try:
    integer_types = (int)
except NameError:   # Python 3
    integer_types = (int,)
    xrange = range

from Complete_graph.algorithms.bipartite import BipartiteGraphBFS as Bipartite
#from bipartite import BipartiteGraphDFS as Bipartite
from Complete_graph.algorithms.edgecolorcs import ConnectedSequentialEdgeColoring
from Complete_graph.structures.Graphs import *
from Complete_graph.structures.Factory import *


class BipartiteGraphEdgeColoring:
    """Find an edge coloring for a bipartite graph."""
    # Szacowanie zlozonosci obliczeniowej.
    # Na poczatku O(V+E) na rozpoznanie grafu dwudzielnego.
    # E krawedzi do kolorowania.
    # O(V) na ustalenie Delta.
    # Tworzenie slownika missing to O(V*Delta).
    # O(Delta) na znalezienie wspolnego koloru brakujacego.
    # Jezeli nie ma wspolnego koloru brakujacego, to:
    # O(V) na znalezienie sciezki,
    # O(V) na przekolorowanie sciezki.
    # Overall, O(V*E) complexity.

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
        # Tast czy graf jest dwudzielny.
        # Wlasciwie potem nie jest jawnie potrzebny podzial wierzcholkow.
        algorithm = Bipartite(self.graph)   # O(V+E) time
        algorithm.run()
        # dict with missing colors for nodes.
        self.missing = None

    def run(self):
        """Executable pseudocode."""
        # Ustal liczbe wykorzystywanych kolorow.
        Delta = max(self.graph.degree(node) for node in self.graph.iternodes())
        if Delta <= 2:
            # Greedy coloring suffies.
            algorithm = ConnectedSequentialEdgeColoring(self.graph)
            algorithm.run()
            self.color = algorithm.color
        else:
            self.missing = dict((node, set(range(Delta)))
                for node in self.graph.iternodes())
            for edge in self.graph.iteredges():
                # Sprawdz wspolny kolor brakujacy.
                # To mozna chyba zrobic bardziej wydajnie.
                both = self.missing[edge.source] & self.missing[edge.target]
                if len(both) == 0:
                    self._recolor(edge)
                else:
                    c = min(both)   # choose min color available [moze dowolny?]
                    self._add_color(edge, c)

    def _add_color(self, edge, c):
        """Add color."""
        if edge.source > edge.target:
            edge = ~edge
        self.color[edge] = c
        self.missing[edge.source].remove(c)
        self.missing[edge.target].remove(c)

    def _del_color(self, edge, c):
        """Delete color."""
        if edge.source > edge.target:
            edge = ~edge
        self.color[edge] = None
        self.missing[edge.source].add(c)
        self.missing[edge.target].add(c)

    def _recolor(self, edge):
        """Swap edge colors and add color."""
        # edge.source i edge.target maja rozne kolory brakujace.
        alpha = min(self.missing[edge.source])
        beta = min(self.missing[edge.target])
        # Tworze sciezke o poczatku w edge.source i kolorach
        # na przemian beta i alpha.
        # Sciezka sie urwie, jak nie znajdziemy danego koloru.
        # Na sciezce na pewno nie spotkamy edge.target, bo tam
        # nie ma koloru beta.
        path = []
        node = edge.source   # chodzi po wierzcholkach sciezki
        finished = False
        # Zmienna parity pozwala kontrolowac jaki kolor szukamy.
        parity = 0
        while not finished:
            finished = True
            if parity % 2 == 0:   # szukamy kolor beta
                for edge1 in self.graph.iteroutedges(node):
                    # Kolor krawedzi ma byc beta.
                    if edge1.source > edge1.target:
                        pass
                        c = self.color[~edge1]
                    else:
                        c = self.color[edge1]
                    if c == beta:   # c moze byc None!
                        node = edge1.target
                        path.append(edge1)
                        finished = False   # bedziemy szukac drugiego koloru
                        break
            else:   # parity % 2 == 1, szukamy kolor alpha
                for edge1 in self.graph.iteroutedges(node):
                    # Kolor krawedzi ma byc alpha.
                    if edge1.source > edge1.target:
                        edge1 = ~edge1
                        c = self.color.get(edge1)
                    else:
                        c = self.color[edge1]
                    if c == alpha:   # c moze byc None!
                        node = edge1.target
                        path.append(edge1)
                        finished = False   # bedziemy szukac drugiego koloru
                        break
            parity += 1
        #print "path", path
        # Sciezka zostala znaleziona i na pewno istnieje.
        # Zamieniamy kolory alpha i beta na sciezce.
        # Najpierw usuwam kolory, pierwszy to beta.
        for i, edge1 in enumerate(path):
            c = beta if (i % 2 == 0) else alpha
            self._del_color(edge1, c)
        # Teraz dodaje kolory, pierwszy to alpha.
        for i, edge1 in enumerate(path):
            c = alpha if (i % 2 == 0) else beta
            self._add_color(edge1, c)
        # Teraz mamy wolny kolor beta dla krawedzi edge.
        self._add_color(edge, beta)


if __name__ == '__main__':
    graph = GraphFactory(Graph)
    g1 = graph.make_bipartite(20, 30, directed=False, edge_probability=0.99)
    g1.save("bipartite_graf.txt")
    algorithm = BipartiteGraphEdgeColoring(g1)
    algorithm.run()
    #print("Set U")
    #print(algorithm.U)
    #print("Set V")
    #print(algorithm.V)
    print(algorithm.color)


#EOF
