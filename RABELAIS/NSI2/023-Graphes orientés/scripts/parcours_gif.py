import matplotlib.pyplot as plt
import networkx as nx
from random import randint, sample
from Stack import *
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
                tmp[i]=WAITING
            i+=1
        result.append(tmp)

    return result


def colorize(g: nx.Graph) -> list:
    color_dict = dict()
    nb_colors_used = 0
    result = [[0 for n in g.nodes]]
    for n in g.nodes:
        available_colors = [True] * nb_colors_used
        for u in g.neighbors(n):
            if u in color_dict:
                available_colors[color_dict[u]] = False
        i = 0
        while i < nb_colors_used and available_colors[i] == False:
            i += 1
        if i == nb_colors_used:
            nb_colors_used += 1
        color_dict[n] = i
        tmp = list(result[-1])
        tmp[list(g.nodes).index(n)] = i
        result.append(tmp)
    for i in range(len(result)):
        for j in range(len(g.nodes)):
            print(result[i][j])
            result[i][j] = COLOR_LIST[result[i][j]]
    return result


def random_graph(min_node=5, max_node=10, min_deg=1, max_deg=3):
    node_name = "AZERTYUIOPQSDFGHJKLMWXCVBN"
    g = nx.Graph()
    n = randint(min_node, max_node)
    nodes = sample(node_name, n)
    edges = []
    for node in nodes:
        remaining_nodes = list(nodes)
        remaining_nodes.remove(node)
        extremities = sample(remaining_nodes, randint(min_deg, max_deg))
        edges.extend([(node, e) for e in extremities])
    g.add_edges_from(edges)
    return g


def path_to_gif(g: nx.Graph, color_steps: list):
    i = 0
    images = []
    for c in color_steps:
        plt.clf()
        nx.draw(g, pos=nx.shell_layout(g), with_labels=True, node_color=c)

        plt.savefig('tmp/' + str(i).zfill(2) + '.png')
        images.append(Image.open('tmp/' + str(i).zfill(2) + '.png'))
        i += 1
    plt.clf()
    plt.savefig('tmp/' + str(i).zfill(2) + '.png')
    images.append(Image.open('tmp/' + str(i).zfill(2) + '.png'))
    images[0].save('result.' + str(datetime.now().strftime('%Y.%m.%d--%H.%M.%S')) + '.gif',
                   save_all=True, append_images=images[1:], optimize=True, duration=1000, loop=0)


G = random_graph()
print(G.nodes)
colors = bfs(G, list(G.nodes)[0])

path_to_gif(G, colors)
