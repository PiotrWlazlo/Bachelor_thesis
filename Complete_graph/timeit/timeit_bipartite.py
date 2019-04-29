#!/usr/bin/python
#
# Sprawdzam szybkosc kolorowania grafu dwudzielnego.

import timeit
import random
from Complete_graph.edgecolorsimplebipartite import *
from Complete_graph.BipartiteGraphEdgeColoring import *

V = 5000
gf = GraphFactory(Graph)
G = gf.make_bipartite(V/2, V-(V/2), False, 1)   # complete bipartite
#G = gf.make_bipartite(V/2, V-(V/2))
#G = gf.make_grid(size=10)
# s =    7,  10,  20,  30,   70,   100,   200,   300,    700, 1e3
# s*s = 49, 100, 400, 900, 4900, 10000, 40000, 90000, 490000, 1e6
V = G.v()
E = G.e()
#G.show()

print("Testing BipartiteGraphEdgeColoring ...")
t1 = timeit.Timer(lambda: BipartiteGraphEdgeColoring(G).run())
print(V, E, t1.timeit(1))            # pojedyncze wykonanie

print("Testing CompleteBipartiteGraphEdgeColoring ...")
t1 = timeit.Timer(lambda: CompleteBipartiteGraphEdgeColoring(G).run())
print(V, E, t1.timeit(1))            # pojedyncze wykonanie

# EOF
