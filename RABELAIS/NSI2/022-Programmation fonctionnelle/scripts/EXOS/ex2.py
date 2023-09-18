def verify(property, lst: list):
    for x in lst:
        if property(x):
            return x


def p(x: int) -> bool:
    return x % 10 == 2


print(verify(p, [1, 3, 293, 202, 14]))
