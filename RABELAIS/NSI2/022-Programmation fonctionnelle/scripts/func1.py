def make_table(f, a: int, b: int) -> list:
    return [f(x) for x in range(a, b + 1)]


def g(x: float) -> float:
    return x ** 2 + x + 1


print(make_table(g, 0, 5))

# result : [1, 3, 7, 13, 21, 31]