def apply(f, lst: list) -> list:
    return [f(x) for x in lst]


def f(x):
    return 2 * x + 1


print(apply(f, [1, 2, 3]))  # [3, 5, 7]
