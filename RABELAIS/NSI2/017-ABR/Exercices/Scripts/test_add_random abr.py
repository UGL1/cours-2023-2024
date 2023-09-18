from node_bst import *
from random import shuffle

size = 200

values = list(range(0, size))
shuffle(values)
root = NodeBST(values[0])
for i in range(1, len(values)):
    root.add_value(values[i])
print(root.height())
root.draw()