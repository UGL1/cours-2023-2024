import matplotlib.pyplot as plt
import networkx as nx
from random import randint, sample
from stack import *
from queue import *
from PIL import Image
from datetime import datetime

NOT_VISITED = (.5, .5, .5)
CURRENT = (1, 0, 0)
WAITING = (.5, 0, .5)

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
        for node in g.neighbors(current_node):
            if node in remaining_nodes:
                stack.push(node)
                remaining_nodes.remove(node)
        i = 0
        for n in g.nodes:
            if n in stack.content:
                tmp[i] = WAITING
            i += 1
        result.append(tmp)

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
        for node in g.neighbors(current_node):
            if node in remaining_nodes:
                queue.enqueue(node)
                remaining_nodes.remove(node)
        i = 0
        for n in g.nodes:
            if n in queue.content:
                tmp[i] = WAITING
            i += 1
        result.append(tmp)

    return result





def path_to_gif(g: nx.Graph, color_steps: list, pos=None):
    pos = pos or nx.spring_layout(g)
    i = 0
    images = []
    for c in color_steps:
        plt.clf()
        nx.draw(g, pos=pos, with_labels=True, node_color=c)

        plt.savefig('tmp/' + str(i).zfill(2) + '.svg',transparent=True)
        images.append(Image.open('tmp/' + str(i).zfill(2) + '.png'))
        i += 1
    plt.clf()
    plt.savefig('tmp/' + str(i).zfill(2) + '.png')
    images.append(Image.open('tmp/' + str(i).zfill(2) + '.png'))
    images[0].save('result.' + str(datetime.now().strftime('%Y.%m.%d--%H.%M.%S')) + '.gif',
                   save_all=True, append_images=images[1:], optimize=True, duration=1000, loop=0)




G = nx.Graph()

G.add_edges_from(
    [('A', 'B'), ('A', 'C'), ('A', 'D'), ('A', 'E'), ('B', 'C'), ('C', 'E'), ('E','D'),('D','B'), ('B', 'F'),
     ('C', 'G'),
     ('D', 'H'), ('E', 'I'),('F','G')])

colors = bfs(G,'H')

positions = {'A': (0, 0), 'B': (0, 1), 'C': (1, 0), 'D': (-1, 0), 'E': (0, -1), 'F': (0, 2), 'G': (2, 0), 'H': (-2, 0),
             'I': (0, -2)}

path_to_gif(G, colors,pos=positions)
