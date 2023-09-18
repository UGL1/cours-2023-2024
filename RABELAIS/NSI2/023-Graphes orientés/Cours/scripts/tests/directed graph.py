import networkx as nx
import pylab

G = nx.DiGraph()
G.add_edges_from([('A', 'B'), ('C', 'D'), ('G', 'D')], weight=1)
G.add_edges_from([('D', 'A'), ('D', 'E'), ('B', 'D'), ('D', 'E')], weight=2)
G.add_edges_from([('B', 'C'), ('E', 'F')], weight=3)
G.add_edges_from([('C', 'F')], weight=4)

edge_labels = dict([((u, v,), d['weight'])
                    for u, v, d in G.edges(data=True)])
pos=nx.spring_layout(G)
pos = nx.circular_layout(G)
nx.draw_networkx_edge_labels(G,pos,edge_labels=edge_labels)
nx.draw(G,pos)
pylab.show()
