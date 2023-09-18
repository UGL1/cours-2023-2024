from stack import *


def hanoi_stack_recursive(n, start: Stack, end: Stack, inter: Stack):
    print(s1)
    print(s2)
    print(s3)
    print('-'*40)
    if n != 0:
        hanoi_stack_recursive(n - 1, start, inter, end)
        end.push(start.pop())
        hanoi_stack_recursive(n - 1, inter, end, start)


def hanoi_stack(a: Stack, b: Stack, c: Stack):
    n = 0
    while not a.is_empty():
        b.push(a.pop())
        n += 1
    for _ in range(n):
        a.push(b.pop())
    hanoi_stack_recursive(n, a, b, c)


s1, s2, s3 = Stack(), Stack(), Stack()

for i in range(3, -1, -1):
    s1.push(i)
hanoi_stack(s1, s3, s2)
