from LinkedList import *


def recursive_length(ll: LinkedList):
    def rl(c: Cell):
        if not c:
            return 0
        else:
            return 1 + rl(c.succ)

    return rl(ll.head)


def recursive_find(ll: LinkedList, value):
    def rf(c, v, n=0):
        if not c:
            return -1
        elif c.value == v:
            return n
        else:
            return rf(c.succ, v, n + 1)
    return rf(ll.head, value)


L = LinkedList([21, 54, 87, 98, 65, 32, 21, 584, 3, 1])

print(recursive_length(L))
print(recursive_find(L, 3))
