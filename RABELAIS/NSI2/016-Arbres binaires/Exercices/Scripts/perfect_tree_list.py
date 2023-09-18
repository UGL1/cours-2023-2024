import networkx as nx


def create_perfect_tree(height: int) -> list:
    return [_ for _ in range(2 ** (height + 1))]


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1


def prefix(pt, i=1):
    print(pt[i], end=" ")
    if left(i) < len(pt):
        prefix(pt, left(i))
    if right(i) < len(pt):
        prefix(pt, right(i))


def infix(pt, i=1):
    if left(i) < len(pt):
        infix(pt, left(i))
    print(pt[i])
    if right(i) < len(pt):
        infix(pt, right(i))


def postfix(pt, i=1):
    if left(i) < len(pt):
        postfix(pt, left(i))
    if right(i) < len(pt):
        postfix(pt, right(i))
    print(pt[i])


def list_edge(pt, i=1):
    result = []
    if left(2 * i) < len(pt):
        result.append((i, 2 * i))
        result.extend(list_edge(pt, 2 * i))
    if left(2 * i + 1) < len(pt):
        result.append((i, 2 * i + 1))
        result.extend(list_edge(pt, 2 * i + 1))
    return result


def draw(pt):
    g = nx.DiGraph()
    g.add_edges_from(list_edge(pt))
    p = nx.drawing.nx_pydot.to_pydot(g)
    p.write_png('example.png')


draw(create_perfect_tree(5))
