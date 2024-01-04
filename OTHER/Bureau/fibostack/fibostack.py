from stack import *


def fibostack(n: int) -> int:
    s = Stack()
    f = 0
    s.push(n)
    while not s.is_empty():
        print(f)
        print(s)
        print("-"*10)
        v = s.pop()
        if v <2:
            f += v
        else:
            s.push(v - 1)
            s.push(v - 2)
    return f


print(fibostack(4))
