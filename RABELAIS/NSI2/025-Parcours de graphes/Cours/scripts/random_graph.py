from graph import *
from random import randint, sample

ALPHABET = "AZERTYUIOPQSDFGHJKLMWXCVBN"  # pour piocher dans les lettres de l'alphabet


def random_graph() -> Graph:
    """
    Crée un graphe ni trop gros ni trop compliqué
    """
    n = randint(5, 10)  # nombre de sommets aléatoires

    nodes = sample(ALPHABET, n)  # on en choisit n distincts

    G = Graph()
    G.add_nodes_from(nodes)

    for node in nodes:
        remaining_nodes = [n for n in nodes if n != node]  # On ne veut pas de boucle
        extremities = sample(remaining_nodes, randint(1, 3))  # On choisit les sommets au hasard

        for extremity in extremities:
            if G.degree(extremity) < 3 and G.degree(node) < 3:  # On veille à respecter la contrainte
                G.add_edge(node, extremity)

    return G
