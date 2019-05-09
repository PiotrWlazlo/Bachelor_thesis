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
Następnie wykonujemy kolorowanie grafu. Wyznaczamy najpierw zmienną Delta (Δ), a następnie 
kolorujemy krawędzie poczynając od pojedynczego wierzchoka z jednego ze zbiorów wyznaczonych
w teście dwudzielności i iterujemy po jego sąsiadach zmieniając kolory.
#Złożoność
Wykonanie testu dwudzielności zajmuje dokładnie O(V) czasu gdzie V to iość wierzchołków,
z racji tego że każdy musimy przyporządkować to konkretnej grupy. Następnie samo kolorowanie
krawędzi zajmuje O(E) czasu z racji pokolorowania wszystkich krawędzi. Sumarycznie więc 
złożoność czasowa zajmuje O(V+E)
Złożoność pamięciowa zajmuje O(V+E) gdyż słownik color zajmuje dokładnie O(E) pamięci,
zaś dwa słowniki D1 i D2 zajmują łącznie O(V) pamięci.

#Kolorowanie krawędzi grafu dwudzielnego zwykłego

#Dane wejściowe
Graf dwudzielny zwykły
#Problem
Kolorowanie krawędzi grafu dwudzielnego prostego




