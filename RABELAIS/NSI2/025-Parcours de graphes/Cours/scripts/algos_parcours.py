from random_graph import *
from stack import *
from queue import Queue


def dfs(g: Graph, start) -> list:
    """
    Parcours en profondeur itératif du graphe g en partant du sommet start
    """
    visited = []  # et la liste des sommets visités

    return visited


def bfs(g: Graph, start) -> list:
    """
        Parcours en largeur itératif du graphe g en partant du sommet start
    """
    visited = []  # et la liste des sommets visités

    return visited


G = random_graph()
print(G)

print(dfs(G, G.nodes[0]))
print(bfs(G, G.nodes[0]))
