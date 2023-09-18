import networkx as nx
import matplotlib.pyplot as plt
from random import randint, sample

alphabet = 'AZERTYUIOPQSDFGHJKLMWXCVBN'
nb_sommets = randint(5, 10)
sommets = sample(alphabet, nb_sommets)

G = nx.Graph()

G.add_nodes_from(sommets)
plt.clf()

for i in range(10):
    extremites = sample(alphabet, 2)
    G.add_edge(extremites[0], extremites[1])

nx.draw(G, with_labels=True)
plt.show()
