class Edge:
    """The class defining a directed edge.
    
    Attributes
    ----------
    source : starting node
    target : ending node
    weight : number (edge weight)
    
    Examples
    --------
    '''
    >>> from graphtheory.structures.edges import Edge
    >>> edge = Edge(1, 2, 5)
    >>> ~edge
    '''
    Edge(2, 1, 5)
    
    Notes
    -----
    Hashable edges - the idea for __hash__ from
    
    http://stackoverflow.com/questions/793761/built-in-python-hash-function
    """

    def __init__(self, source, target, weight=1):
        """Load up a directed edge instance.
        
        Parameters
        ----------
        source : starting node
        target : ending node
        weight : number, optional (default=1)
        """
        self.source = source
        self.target = target
        self.weight = weight

    def __repr__(self):
        """Compute the string representation of the edge."""
        if self.weight == 1:
            return "{}({}, {})".format(
                self.__class__.__name__,
                repr(self.source),
                repr(self.target))
        else:
            return "{}({}, {}, {})".format(
                self.__class__.__name__,
                repr(self.source),
                repr(self.target),
                repr(self.weight))

    def __cmp__(self, other):
        """Comparing of edges (the weight first)."""
        # Check weights.
        if self.weight > other.weight:
            return 1
        if self.weight < other.weight:
            return -1
        # Check the first node.
        if self.source > other.source:
            return 1
        if self.source < other.source:
            return -1
        # Check the second node.
        if self.target > other.target:
            return 1
        if self.target < other.target:
            return -1
        return 0

    def __hash__(self):
        """Hashable edges."""
        #return hash(repr(self))
        return hash((self.source, self.target, self.weight))

    def __invert__(self):
        """Return the edge with the opposite direction."""
        return self.__class__(self.target, self.source, self.weight)

    inverted = __invert__


class UndirectedEdge(Edge):
    """The class defining an undirected edge."""

    def __init__(self, source, target, weight=1):
        """Load up an edge instance."""
        if source > target:
            self.source = target
            self.target = source
        else:
            self.source = source
            self.target = target
        self.weight = weight

    def __invert__(self):
        """The edge direction is not defined."""
        return self

# EOF

'''
Byłyby to Węgry a konkretnie do Budapesztu. Podróż do tego miasta ciągnie się za mną już bardzo długą ilość czasu gdyż moim marzeniem było pojechanie tam na program Erasmus+. Niestety moja uczelnia zmieniła bez mojej wiedzy terminy przesyłania zgłoszeń. Rok temu były do połowy Lutego, a w tym roku było do połowy Stycznia. Dowiedziałem się o tym dwa dni po terminie zgłoszeń. Poprawiałem moją srednią przez cały semestr by dobić do średniej wymaganej, żeby na końcu nie nawet nie wysłać zgłoszenia :P Ciężko to przeżyłem i podbicie tego miasta stało się moim celem numer jeden jeśli chodzi o podróże :D

Najważniejszą rzeczą powinno być wybranie odpowiedniego terminu do sprzedawania gorącej herbaty. Ważne jest żeby to był najlepiej jakiś duży spęd osób, np. targi wielbładów. Na targach wielbładów przewija się bardzo dużo ludzi i też w ten deseń chciałbym uderzyć. Kolejną ważną rzeczą jest wtopienie się w tłum, myślę że dziwnym pomysłem było by zakładanie zwykłych szortów i banerów jak na festynie, najlepszym rozwiązaniem będzie pomalowanie się czarną pastą do butów i nauczenie się kilku zwrotów po marokańsku. Oczywiście muszę nauczyć się afrykańskiego sposobu parzenia herbaty, nie mogę przecież robić tej herbaty w czajniku tylko miętowa na ognisku jak u Makłowicza, jak to mówił McKłowicz"Mocna jak diabli". Mog też nawoływać że jeśli nie będą kupować to wysadzę się w powietrze, myślę że to dobry sposób na przekoanie ich że jestem od nich.

Przyczyną końca świata w moim odczuciu będzie w jednym momencie szczery i przyjazny pocałunek między Kaczyńskim, a Tuskiem poprzedzoną konferencją światową na której Donald Trump na kolanach złoży przed tronem naczelnika Morawieckiego hołd oddający stany Texas oraz Alaskę Polsce w ramach dozgonnej przyjaźni Polsko-Amerykańskiej. Wtedy to na ziemię stąpi z niebios Michael Jackson który oświadczy że to prawda że molestował dzieci i zaśpiewa Smooth Criminal. Wtedy Bóg stwierdzi że już za dużo i zakończy nasz świat włączając przycisk stop w matrixie :)

'''