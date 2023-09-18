import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

cols = ['#FF0000', '#0000FF', '#00FF00', '#FFFF00', '#FF00FF', '#00FFFF']
G = nx.Graph()
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('A', 'D'), ('C', 'F'), ('C', 'E'), ('F', 'E'), ('F', 'D')])
print(G.nodes)

positions = {'A': np.array([0, 0]), 'B': np.array([-1, -1]),
             'C': np.array([0, -2]), 'D': np.array([1, 1]),
             'E': np.array([2, -2]), 'F': np.array([2, 0])}

color_dict = dict()
nb_colors_used = 0
for n in G.nodes:
    available_colors = [True] * nb_colors_used
    for u in G.neighbors(n):
        if u in color_dict:
            available_colors[color_dict[u]] = False
    i = 0
    while i < nb_colors_used and not available_colors[i]:
        i += 1
    if i == nb_colors_used:
        nb_colors_used += 1
    color_dict[n] = i
print(color_dict)
color_list = []

for u in G.nodes:
    color_list.append(cols[color_dict[u]])
for i in range(len(color_list) + 1):
    plt.clf()
    color_list_tmp = color_list[:i] + ['#808080'] * (len(color_list) - i)
    print(color_list_tmp)
    nx.draw(G, with_labels=True, pos=positions, node_color=color_list_tmp)
    plt.savefig(str(i).zfill(2) + '-.png')

