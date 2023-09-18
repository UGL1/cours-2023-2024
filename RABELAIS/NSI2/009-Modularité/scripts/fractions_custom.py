def create(a: int, b: int):
    """
    creates a/b
    :param a: int
    :param b: int
    """
    return [a, b]


def _pgcd(a: int, b: int) -> list:
    a, b = max(a, b), min(a, b)
    while b != 0:
        a, b = b, a % b
    return a


def _simplify(f: list) -> list:
    p = _pgcd(f[0], f[1])
    return [f[0] // p, f[1] // p]


def add(f1, f2):
    """
    adds f1 and f2
    """
    f = [f1[0] * f2[1] + f2[0] * f1[1], f1[1] * f2[1]]
    if f[0] != 0:
        return _simplify(f)
    else:
        return [0, 1]


def sub(f1, f2):
    """
    subtracts f2 from f1
    """
    f = [f1[0] * f2[1] - f2[0] * f1[1], f1[1] * f2[1]]
    if f[0] != 0:
        return _simplify(f)
    else:
        return [0, 1]


def mul(f1, f2):
    """
    multiplies f1 and f2
    """
    f = [f1[0] * f2[0], f1[1] * f2[1]]
    if f[0] != 0:
        return _simplify(f)
    else:
        return [0, 1]


def div(f1, f2):
    """
    divides f1 by f2
    """
    f = [f1[0] * f2[1], f1[1] * f2[0]]
    if f[0] != 0:
        return _simplify(f)
    else:
        return [0, 1]


def display(f):
    """
    prints f on screen
    """
    print(f[0], '/', f[1])
