import matplotlib.pyplot as plt
import networkx as nx
from random import randint, sample
from Stack import *
from queue import *
from PIL import Image
from datetime import datetime

NOT_VISITED = (.5, .5, .5)
CURRENT = (1, 0, 0)
VISITED = (.5, .5, 1)

COLOR_LIST = ['#808080', '#FF0000', '#00FF00', '#0000FF', '#FFFF00', '#FF00FF', '#00FFFF', '#FF4040', '#40FF40',
              '#4040FF']


def dfs(g: nx.Graph, starting_node) -> list:
    result = [[NOT_VISITED for n in g.nodes]]
    stack = Stack()
    stack.push(starting_node)
    remaining_nodes = list(g.nodes)
    remaining_nodes.remove(starting_node)
    while stack:
        current_node = stack.pop()
        tmp = list(result[-1])
        for i in range(len(tmp)):
            if tmp[i] == CURRENT:
                tmp[i] = VISITED
            elif i == list(g.nodes).index(current_node):
                tmp[i] = CURRENT
        result.append(tmp)
        for node in g.neighbors(current_node):
            if node in remaining_nodes:
                stack.push(node)
                remaining_nodes.remove(node)
    return result


def bfs(g: nx.Graph, starting_node) -> list:
    result = [[NOT_VISITED for n in g.nodes]]
    queue = Queue()
    queue.enqueue(starting_node)
    remaining_nodes = list(g.nodes)
    remaining_nodes.remove(starting_node)
    while queue:
        current_node = queue.dequeue()
        tmp = list(result[-1])
        for i in range(len(tmp)):
            if tmp[i] == CURRENT:
                tmp[i] = VISITED
            elif i == list(g.nodes).index(current_node):
                tmp[i] = CURRENT
        result.append(tmp)
        for node in g.neighbors(current_node):
            if node in remaining_nodes:
                queue.enqueue(node)
                remaining_nodes.remove(node)
    return result


def path_to_gif(g: nx.Graph, color_steps: list, positions_list=None):
    positions_list = positions_list or nx.shell_layout(g)
    i = 0
    images = []
    for c in color_steps:
        plt.clf()
        nx.draw(g, pos=positions_list, with_labels=True, node_color=c)

        plt.savefig('tmp/' + str(i).zfill(2) + '.png')
        images.append(Image.open('tmp/' + str(i).zfill(2) + '.png'))
        i += 1
    plt.clf()
    plt.savefig('tmp/' + str(i).zfill(2) + '.png')
    images.append(Image.open('tmp/' + str(i).zfill(2) + '.png'))
    images[0].save('result.' + str(datetime.now().strftime('%Y.%m.%d--%H.%M.%S')) + '.gif',
                   save_all=True, append_images=images[1:], optimize=True, duration=1000, loop=0)


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
colors = dfs(G, list(G.nodes)[0])
path_to_gif(G, colors,positions_list=positions)

colors = bfs(G, list(G.nodes)[0])
path_to_gif(G, colors,positions_list=positions)
