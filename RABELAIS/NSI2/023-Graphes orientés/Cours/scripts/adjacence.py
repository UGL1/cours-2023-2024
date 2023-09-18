class Graphe:
    def __init__(self):
        self.sommets = dict()

    def sommets(self) -> list:
        return list(self.sommets.keys())

    def ajoute_sommet(self, sommet):
        self.sommets[sommet] = []

    def ajoute_arc(self, sommet1, sommet2):
        if sommet2 not in self.sommets[sommet1]:
            self.sommets[sommet1].append(sommet2)

    def voisins(self, sommet):
        if sommet in sommet.keys():
            return self.sommets[sommet]

G = Graphe()
G.ajoute_sommet('A')
G.ajoute_sommet('B')
G.ajoute_sommet('C')
G.ajoute_sommet('D')
G.ajoute_arc('')
