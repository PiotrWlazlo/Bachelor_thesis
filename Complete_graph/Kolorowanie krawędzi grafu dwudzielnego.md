#Kolorowanie krawędzi grafu dwudzielnego pełnego

#Dane Wejściowe
Graf pełny dwudzielny
#Problem
Kolorowanie krawędzi grafu dwudzielnego pełnego
#Opis algorytmu
Algorytm przyporządkowuje krawędziom grafu dwudzielnego pełnego
kolor w taki sposób aby spełniona była zależność że z każdego wierzchołka
może wychodzić tylko jedna krawędź pokolorowana na określony kolor.
Podczas inicjalizacji algorytmu jesteśmy zmuszeni sprawdzić
jego dwudzielnośc. Robimy to przyporządkowując określonego node'a do jednego z dwóch grup
tak aby żadne dwa dowolne wierzchołki z tej samej grupy nie były ze sobą połączone krawędzią.
Następnie wykonujemy kolorowanie grafu. Wyznaczamy najpierw zmienną Delta (Δ)

