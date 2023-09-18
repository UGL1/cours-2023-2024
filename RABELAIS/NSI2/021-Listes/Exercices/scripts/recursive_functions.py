from LinkedList import LinkedList


def recursive_length(ll: LinkedList):
    def rl(c: LinkedList.Cell):
        if not c:
            return 0
        else:
            return 1 + rl(c.succ)

    return rl(ll.head)


def recursive_find(ll: LinkedList, value):
    def rf(c: LinkedList.Cell, v, n=0):
        if not c:
            return -1
        elif c.value == v:
            return n
        else:
            return rf(c.succ, v, n + 1)

    return rf(ll.head, value)


L = LinkedList()
L.find(2)
L.insert(23)
L.insert(42)
L.insert(30)
L.insert(12)
L2 = LinkedList()
L2.insert(99)
L2.insert(98)
L.extend(L2)
print(L)
print(len(L))
print(recursive_length(L))
print(recursive_find(L, ))