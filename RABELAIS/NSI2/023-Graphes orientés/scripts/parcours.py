import matplotlib.pyplot as plt
import networkx as nx
from random import randint, sample
from Stack import *
from queue import *

G = nx.Graph()

G.add_edges_from(
    [('C', 'O'), ('C', 'J'), ('C', 'G'), ('C', 'R'), ('O', 'J'), ('O', 'X'), ('J', 'G'), ('J', 'R'), ('J', 'X'),
     ('G', 'Q'), ('R', 'X'), ('R', 'Q')])
positions = {'C': [-0.31934877, -0.15269138], 'O': [-0.62606592, 0.81546769], 'J': [-0.26602134, 0.25992198], 'G':
    [-0.1577814, -0.82012323], 'R': [0.49072014, -0.0064218], 'X': [0.18605347, 0.90384673], 'Q': [0.69244381, -1.]}

color_dict = {'C': '#FF0000', 'O': '#00FF00', 'J': '#0000FF', 'G': '#00FF00', 'R': '#00FF00', 'X': '#FF0000',
              'Q': '#FF0000'}
# Profondeur
stack = Stack()
starting_node = 1
stack.push(starting_node)
remaining_nodes = list(G.nodes)
remaining_nodes.remove(starting_node)
while stack:
    current_node = stack.pop()
    print(' ' * len(stack) + str(current_node))
    for node in G.neighbors(current_node):
        if node in remaining_nodes:
            stack.push(node)
            remaining_nodes.remove(node)

# Largeur
queue = Queue()
starting_node = 1
queue.enqueue(starting_node)
remaining_nodes = list(G.nodes)
remaining_nodes.remove(starting_node)
while queue:
    current_node = queue.dequeue()
    print(' ' * len(queue) + str(current_node))
    for node in G.neighbors(current_node):
        if node in remaining_nodes:
            queue.enqueue(node)
            remaining_nodes.remove(node)

color_list = []
for u in G.nodes:
    color_list.append(color_dict[u])



plt.clf()
nx.draw(G, pos = nx.shell_layout(G),with_labels=True)

plt.show()
