from node_bst import NodeBST


from random import shuffle


values = [10,20,5,3,8,4,2,7,9,11,22]
root = NodeBST(values[0])
for i in range(1, len(values)):
    root.add_value(values[i])


print(root.father(root.find_node_by_value(4)))
root.draw()