from graph import *
from stack import *


def dfs_iterative(g: Graph, start) -> list:
    stack = Stack()  # on crée une pile
    remaining_nodes = list(g.nodes)  # une copie de la liste des sommets
    visited = []  # et la liste des sommets visités
    stack.push(start)  # on empile le sommet de départ
    remaining_nodes.remove(start)  # et on l'enlève des sommets restants
    while not stack.is_empty():  # tant que la pile n'est pas vide
        current = stack.pop()  # on dépile
        visited.append(current)  # on ajoute à la liste des sommets visités
        for n in g.neighbors(current):  # pour chacun de ses voisins
            if n in remaining_nodes:  # s'il n'a pas déjà été empilé
                stack.push(n)  # on l'empile
                remaining_nodes.remove(n)  # et on le retire de la liste des
                # sommets disponibles
    return visited


def dfs_recursive(g: Graph, start, marque=None) -> list:
    if marque is None:  # lors du premier appel, par l'utilisateur, marque n'est pas précisé
        marque = []  # donc on crée une liste vide
    pass  # TODO : terminer d'écrire la fonction, ne pas oublier de passer marque d'appels en appels et de renvoyer marque dans les cas d'arrêts.


def dfs_path(g: Graph, start, end) -> list:
    pass  # TODO : ex 3


def bfs_path(g: Graph, start, end) -> list:
    pass  # TODO : ex 4


G = Graph()
G.add_edges_from(
    [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'F'), ('F', 'G'), ('G', 'O'), ('C', 'H'), ('D', 'I'),
     ('D', 'J'),
     ('D', 'K'), ('K', 'L'), ('E', 'M'), ('H', 'O')])

print(dfs_iterative(G, 'A'))

print(dfs_recursive(G, 'A'))
