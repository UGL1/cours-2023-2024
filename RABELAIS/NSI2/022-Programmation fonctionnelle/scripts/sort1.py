def f(t: tuple) -> int:
    return t[1]


l1 = [(1, 2), (2, 0), (10, 1)]
l2 = sorted(l1, key=f)
print(l2)
# result : [1, 3, 7, 13, 21, 31]