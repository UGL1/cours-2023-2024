from node_bst import *
from random import shuffle

h = 3
n = 2 ** (h + 1) - 1
values = list(range(n))
shuffle(values)
root = NodeBST(values[0])
for i in range(1, n):
    root.add_value(values[i])

print(n, n ** 2)
print(NodeBST.opel)
print(root.infix())
print(NodeBST.opel)
root.draw()
