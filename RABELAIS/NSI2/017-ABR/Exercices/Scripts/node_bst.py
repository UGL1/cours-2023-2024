import networkx as nx


class NodeBST:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left  # left child
        self.right = right  # right child

    def height(self):
        n, m = 0, 0
        if not self.right and not self.left:
            return 0
        elif self.left:
            m = self.left.height()
        if self.right:
            n = self.right.height()
        return 1 + max(m, n)

    def __str__(self):
        def _str(x):
            if not x:
                return ''
            return '(' + _str(x.left) + str(x.value) + _str(x.right) + ')'

        return _str(self)

    def prefix(self) -> list:
        result = [self.value]
        if self.left:
            result.extend(self.left.prefix())
        if self.right:
            result.extend(self.right.prefix())
        return result

    def infix(self) -> list:
        result = []
        if self.left:
            result.extend(self.left.infix())
        result.append(self.value)
        if self.right:
            result.extend(self.right.infix())
        return result

    def postfix(self) -> list:
        result = []
        if self.left:
            result.extend(self.left.postfix())
        if self.right:
            result.extend(self.right.postfix())
        result.append(self.value)
        return result

    def __eq__(self, other):
        return other is not None and self.value == other.value and self.left == other.left and self.right == other.right

    def __contains__(self, item):
        if self.value == item:
            return True
        elif self.left and item < self.value:
            return item in self.left
        elif self.right and item > self.value:
            return item in self.right
        else:
            return False

    def add_value(self, item):
        if item < self.value:
            if self.left:
                self.left.add_value(item)
            else:
                self.left = NodeBST(item)
        elif self.right:
            self.right.add_value(item)
        else:
            self.right = NodeBST(item)

    def min(self):
        if self.left:
            return self.left.min()
        return self.value

    def max(self):
        if self.right:
            return self.right.max()
        return self.value

    # ---------------------------------------------------
    def find_node_by_value(self, value):
        if self.value == value:
            return self
        elif self.left and value < self.value:
            return self.left.find_node_by_value(value)
        elif self.right and value > self.value:
            return self.right.find_node_by_value(value)
        else:
            return None

    def max_and_father(self, father=None):
        if self.right:
            return self.right.max_and_father(self)
        return father, self

    def min_and_father(self, father=None):
        if self.left:
            return self.left.min_and_father(self)
        return father, self

    def father(self, other, father=None):
        if self == other or self == other:
            return father
        elif other.value < self.value:
            return self.left.father(other, self)
        return self.right.father(other, self)

    def delete(self, value):
        return

    def list_edges(self):
        result = []
        if self.left:
            result.append([self.value, self.left.value])
            result.extend(self.left.list_edges())
        if self.right:
            result.append([self.value, self.right.value])
            result.extend(self.right.list_edges())
        return result

    def draw(self, name='result.png'):
        g = nx.DiGraph()
        g.add_edges_from(self.list_edges())
        p = nx.drawing.nx_pydot.to_pydot(g)
        p.write_png(name)
