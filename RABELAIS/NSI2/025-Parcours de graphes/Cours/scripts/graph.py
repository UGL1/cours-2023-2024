class Graph:
    """
    Encore une classe pour représenter des graphes non orientés.
    Créée par votre serviteur...
    """

    def __init__(self, vertices=None):
        """
        Soit on crée un graphe vide soit on donne la liste des sommets
        """
        self.neighb = dict()  # les sommets sont stockés dans un dict
        if vertices:
            for v in vertices:
                self.neighb[v] = set()  # et les voisins dans un ensemble
                # le type set est nouveau, plus puissant que les listes quand... on doit manipuler des ensembles !

    def add_node(self, v):
        """
        On peut ajouter des sommets à la volée
        """
        self.neighb[v] = set()

    def add_nodes_from(self, node_list: list):
        """
         On peut ajouter une liste de noeuds à la volée
        """
        for n in node_list:
            self.add_node(n)

    @property  # ne pas se soucier de ce décorateur
    def nodes(self) -> list:
        """
        Renvoie la liste des sommets
        """
        return list(self.neighb)  # en fait list(self.neighb) revient à list(self.neighb.keys())

    def add_edge(self, v1, v2):
        """
        Ajouter une arête
        """
        if v1 not in self.neighb:
            self.neighb[v1] = set()
        if v2 not in self.neighb:
            self.neighb[v2] = set()
        if v2 not in self.neighb[v1]:
            self.neighb[v1].add(v2)
        if v1 not in self.neighb[v2]:
            self.neighb[v2].add(v1)

    def add_edges_from(self, e_list):
        """
        On peut ajouter une liste d'arêtes
        """
        for e in e_list:
            if not isinstance(e, tuple) or len(e) != 2:
                raise TypeError(f'Graph.add_edges_from : {e} is not a 2-tuple.')
            self.add_edge(e[0], e[1])

    @property  # ne pas se soucier de ce décorateur
    def edges(self) -> list:
        """
        renvoie la liste des arêtes
        """
        result = []
        for v1 in self.neighb:
            for v2 in self.neighb[v1]:
                if (v2, v1) not in result:
                    result.append((v1, v2))
        return result

    def neighbors(self, v) -> list:
        """renvoie la liste des voisins d'un sommet"""
        return list(self.neighb[v])

    def degree(self, v) -> int:
        """renvoie le nombre d'arêtes partant d'un sommet"""
        return len(self.neighb[v])

    def __str__(self):
        result = "Sommets \tVoisins\n"
        result +="-------------------\n\n"
        for n in self.nodes:
            result += str(n) + '\t\t\t' + str(self.neighb[n]) + '\n'
        return result