from graph import *
from stack import *
from queue import Queue


def dfs_recursif(g: Graph, start, marque=None) -> list:
    marque = marque or []
    marque.append(start)
    for n in g.neighbors(start):
        if n not in marque:
            dfs_recursif(g, n, marque)
    return marque


def dfs_rec_chemin(g: Graph, start, end, marque=None, pred=None) -> list:
    marque = marque or []
    pred = pred or {start: None}
    marque.append(start)
    for n in g.neighbors(start):
        if n not in marque:
            if n not in pred:
                pred[n] = start
            if n != end:
                dfs_rec_chemin(g, n, end, marque, pred)
    result = [end]
    while pred[result[0]]:
        result = [pred[result[0]]] + result
    return result


def dfs_iterative_path(g: Graph, start, end) -> list:
    result = []
    stack = Stack()  # on crée une pile
    remaining_nodes = list(g.nodes)  # une copie de la liste des sommets
    predecessors = {start: None}
    stack.push(start)  # on empile le sommet de départ
    remaining_nodes.remove(start)  # et on l'enlève des sommets restants
    current = None
    while not stack.is_empty() and current != end:  # tant que la pile n'est pas vide
        current = stack.pop()  # on dépile
        for n in g.neighbors(current):  # pour chacun de ses voisins
            if n in remaining_nodes:  # s'il n'a pas déjà été empilé
                stack.push(n)  # on l'empile
                if n not in predecessors:
                    predecessors[n] = current
                remaining_nodes.remove(n)  # et on le retire de la liste des
                # sommets disponibles
    if current == end:
        while current:
            result = [current] + result
            current = predecessors[current]
    return result


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


def bfs_iterative(g: Graph, start) -> list:
    queue = Queue()  # on crée une file
    remaining_nodes = list(g.nodes)  # une copie de la liste des sommets
    visited = []  # et la liste des sommets visités
    queue.enqueue(start)  # on enfile le sommet de départ
    remaining_nodes.remove(start)  # et on l'enlève des sommets restants
    while not queue.is_empty():  # tant que la file n'est pas vide
        current = queue.dequeue()  # on défile
        visited.append(current)  # on ajoute à la liste des sommets visités
        for n in g.neighbors(current):  # pour chacun de ses voisins
            if n in remaining_nodes:  # s'il n'a pas déjà été enfilé
                queue.enqueue(n)  # on l'enfile
                remaining_nodes.remove(n)  # et on le retire de la liste des
                # sommets disponibles
    return visited


def bfs_iterative_path(g: Graph, start, end) -> list:
    result = []
    queue = Queue()  # on crée une pile
    remaining_nodes = list(g.nodes)  # une copie de la liste des sommets
    predecessors = {start: None}
    queue.enqueue(start)  # on empile le sommet de départ
    remaining_nodes.remove(start)  # et on l'enlève des sommets restants
    current = None
    while not queue.is_empty() and current != end:  # tant que la pile n'est pas vide
        current = queue.dequeue()  # on dépile
        for n in g.neighbors(current):  # pour chacun de ses voisins
            if n in remaining_nodes:  # s'il n'a pas déjà été empilé
                queue.enqueue(n)  # on l'empile
                if n not in predecessors:
                    predecessors[n] = current
                remaining_nodes.remove(n)  # et on le retire de la liste des
                # sommets disponibles
    if current == end:
        while current:
            result = [current] + result
            current = predecessors[current]
    return result


G = Graph()
G.add_edges_from(
    [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'F'), ('F', 'G'), ('G', 'O'), ('C', 'H'), ('D', 'I'),
     ('D', 'J'),
     ('D', 'K'), ('K', 'L'), ('E', 'M'), ('H', 'O')])
# G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'A')])

print(dfs_iterative(G,'A'))
print(bfs_iterative(G,'A'))

print(dfs_iterative_path(G, 'A', 'L'))
print(bfs_iterative_path(G, 'A', 'L'))
