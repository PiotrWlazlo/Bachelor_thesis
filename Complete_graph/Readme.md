#Algorytm kolorowania krawędzi grafu 
Kolorowanie krawędzi grafu to przyporządkowanie kolorów (które mogą być np. liczbami) do krawędzi w sposób taki by żadna 
z krawędzi wychodzących bądź wchodzących z tego samego wierzchołka grafu nie była pokolorowana na ten sam kolor.
Problem kolorowania krawędzi grafu polega na znalezieniu sposobu aby możliwe było pokolorowanie krawędzi
używając co najwyżej k kolorów lub jak najmniejszą ilością kolorów. Minimalną liczbą kolorów potrzebną do pokolorowania
wszystkich krawędzi grafu nazywamy liczbą chromatyczną grafu.

#Twierdzenie Vizinga
Twierdzenie które mówi że dla każdego grafu nieskierwanego liczba kolorów potrzebna do pokolorowania krawędzi tego grafu
jest równa co najmniej na Δ kolorów (maksymalny stopień wejściowy grafu) i co najwyżej Δ+1. Dzięki czemu możemy 
takie grafy podzielić na dwie klasy czyli takie które do pokolorowania swoich krawędzi potrzebuje Δ kolorów oraz takie które 
potrzebują Δ+1 kolorów.

#Algorytm kolorowania krawędzi grafu pełnego
Kolorowanie krawędzi grafu pełnego należy podzielić na dwa podproblemy w zależności czy jest to graf o nieparzystej liczbie 
wierzchołków czy też parzystej liczbie wierzchołków. 

#Kolorowanie krawędzi grafu pełnego z nieparzystą liczbą wierzchołków
Na początku w mojej klasie EdgeColoring wywołuje konstruktor __init__ który sprawdza czy graf któy został dostarczony jako input
nie jest skierowany, czy nie posiada pętli oraz czy wszystkie krawędzie są unikalne. Tworzę również słownik w którym będę przechowywał
wszystkie krawędzie wraz z jej kolorem oraz oznaczam kolor każdej krawędzi jako None.
W pierwszej fazie algorytmu musimy założyć że nasz graf jest ułożony w formie wielościanu gdzie jego wierzchołkami są wierzchołki
tego grafu, a jego skrajne krawędzie stanowią boki tego wielościanu.
Następnie koloruje n krawędzi stanowiące boki wieloboku na n różnych kolorów stanowiących Δ+1 kolorów. Dodaje wtedy do 
tablicy te krawędzie sąsiadujące z nimi.
Następnie koloruje wewnętrzne niepokolorowane jeszcze krawędzie tego grafu w sposób taki każda krawędź wewnętrzna była pokolorowana
na ten sam kolor co krawędź zewnętrzna do niej równoległa gdyż każda krawędź w tym grafie jest równoległa do dokładnie jednej krawędzi
zewnętrznej. 
Liczba kolorów użyta do pokolorowania tego grafu wynosi Δ+1.

#Kolorowanie krawędzi grafu pełnego z parzystą liczbą wierzchołków.
Algorytm ten wykorzystuje algorytm przedstawiony powyżej. Otóż musimy założyć że ignorujemy, ostatni node wraz z krawędziami wychodzącymi
z niego w takim celu aby nasz graf był z nieparzystą ilością wierzchołków. Następnie wykonujemy na nim algorytm opisany powyżej
dla grafu z nieparzystą ilością wierzchołków. Następnie należy "ujawnić" nasz ostatni skrywany node i pokolorować jego wszystkie krawezie
na kolor taki któremu brakuje z dostępnej listy kolorów node'owi łączącego naszego ostatniego node'a przez tą krawędź.

Liczba kolorów potrzebna do pokolorowania tego grafu wynosi Δ.


werwa





