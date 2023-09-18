L = [1, 2]


def f(x: int) -> int:
    L[0] += 1
    return x + L[0]


print(f(10))  # result : 12
print(f(10))  # result : 13
