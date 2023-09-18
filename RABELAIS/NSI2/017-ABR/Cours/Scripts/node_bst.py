class NodeBST:
    opel = 0

    @classmethod
    def reset(cls):
        cls.opel = 0

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
        NodeBST.opel +=1
        if self.left:
            NodeBST.opel += 1
            result.extend(self.left.infix())
        NodeBST.opel += 1
        result.append(self.value)
        NodeBST.opel += 1
        if self.right:
            NodeBST.opel += 1
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
        NodeBST.opel += 1
        if item < self.value:
            NodeBST.opel += 1
            if self.left:
                self.left.add_value(item)
            else:
                NodeBST.opel += 1
                self.left = NodeBST(item)
        elif self.right:
            NodeBST.opel += 1
            self.right.add_value(item)
        else:
            NodeBST.opel += 1
            self.right = NodeBST(item)

    def min(self):
        if self.left:
            return self.left.min()
        return self.value

    def max(self):
        if self.right:
            return self.right.max()
        return self.value
