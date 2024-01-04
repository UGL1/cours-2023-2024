from stack import *


def faro(s: Stack) -> None:
    left, right = Stack(), Stack()
    for _ in range(s.size() // 2):
        left.push(s.pop())
    for _ in range(s.size()):
        right.push(s.pop())
    print(left)
    print(right)
    for _ in range(left.size()):
        s.push(left.pop())
        s.push(right.pop())




deck = Stack()
lst = list("BACNSI")
lst.reverse()
for i in lst:
    deck.push(i)
print(deck)
faro(deck)
print(deck)