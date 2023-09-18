import networkx as nx
import matplotlib.pyplot as plt
from Stack import *
from queue import *

h = 4

edges = sorted(
    [(i, 2 * i) for i in range(1, 2 ** (h + 1) - 2 ** h)] + [(i, 2 * i + 1) for i in range(1, 2 ** (h + 1) - 2 ** h)],
    key=lambda x: x[0])

i = 0
j = 0
k = 0
positions = []
while j < 2 ** (h + 1):
    k = 2 ** (i + 1)
    while j < k:
        j += 1
        positions.append((j - 3 * k // 4, -i))
    i += 1



G = nx.Graph()
G.add_edges_from(edges)
nx.draw(G, with_labels=True, pos=positions)
plt.show()
# Profondeur
stack = Stack()
starting_node = 1
stack.push(starting_node)
remaining_nodes = list(G.nodes)
remaining_nodes.remove(starting_node)
while stack:
    current_node = stack.pop()
    print(str(current_node), end='-')
    for node in G.neighbors(current_node):
        if node in remaining_nodes:
            stack.push(node)
            remaining_nodes.remove(node)
print()
# Largeur
queue = Queue()
starting_node = 1
queue.enqueue(starting_node)
remaining_nodes = list(G.nodes)
remaining_nodes.remove(starting_node)
while queue:
    current_node = queue.dequeue()
    print(str(current_node), end='-')
    for node in G.neighbors(current_node):
        if node in remaining_nodes:
            queue.enqueue(node)
            remaining_nodes.remove(node)
