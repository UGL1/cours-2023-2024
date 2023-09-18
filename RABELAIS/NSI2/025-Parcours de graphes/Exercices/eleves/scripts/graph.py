from stack import *


class Graph:
    def __init__(self, vertices=None):
        self.neighb = dict()
        if vertices:
            for v in vertices:
                self.neighb[v] = []

    def add_node(self, v):
        self.neighb[v] = []

    def add_nodes_from(self, n_list):
        for n in n_list:
            self.add_node(n)

    @property
    def nodes(self):
        return list(self.neighb)

    def add_edge(self, v1, v2):
        if v1 not in self.neighb:
            self.neighb[v1] = []
        if v2 not in self.neighb:
            self.neighb[v2] = []
        if v2 not in self.neighb[v1]:
            self.neighb[v1].append(v2)
        if v1 not in self.neighb[v2]:
            self.neighb[v2].append(v1)

    def add_edges_from(self, e_list):
        for e in e_list:
            if not isinstance(e, tuple) or len(e) != 2:
                raise TypeError(f'Graph.add_edges_from : {e} is not a 2-tuple.')
            self.add_edge(e[0], e[1])

    @property
    def edges(self):
        result = []
        for v1 in self.neighb:
            for v2 in self.neighb[v1]:
                if (v2, v1) not in result:
                    result.append((v1, v2))
        return result

    def neighbors(self, v):
        return self.neighb[v]

    def path_dfs(self, start, end):
        visited = [start]
        predecessor = {start: None}
        s = Stack()
        s.push(start)
        current = start
        while current != end and not s.is_empty():
            current = s.pop()
            for n in self.neighb[current]:
                if n not in visited:
                    visited.append(n)
                    predecessor[n] = current
                    s.push(n)
        if current != end:
            return None
        else:
            result = [end]
            while predecessor[current]!=None:
                result = [predecessor[current]] + result
                current = predecessor[current]
            return result
