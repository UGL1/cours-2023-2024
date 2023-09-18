def mystery1(n: int) -> int:
    """n est un entier positif"""
    if n == 0:
        return 1
    else:
        return 2 * mystery1(n - 1)
