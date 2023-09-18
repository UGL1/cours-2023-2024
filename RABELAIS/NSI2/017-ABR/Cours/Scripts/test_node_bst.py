from node_bst import NodeBST

n2 = NodeBST(2)
n8 = NodeBST(8)
n12 = NodeBST(12)
n15 = NodeBST(15)
n3 = NodeBST(3, n2)
n9 = NodeBST(9, n8)
n13 = NodeBST(13, n12, n15)
n6 = NodeBST(6, n3, n9)
n10 = NodeBST(10, None, n13)
root = NodeBST(10, n6, n10)

print(14 in root)
root.add_value(11)
print(11 in root)
print(root.infix())
print(root.min(), root.max())
print(root.height())
