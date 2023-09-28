def A(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif n == 0:
        return A(m - 1, n)
    else:
        return A(m - 1, A(m, n - 1))
