def differentiate(f):
    h = 1e-7
    return lambda x: (f(x + h) - f(x)) / h


def g(x: float) -> float:
    return x ** 2 + x * 4 + 2


g_prime = differentiate(g)

print(g_prime(2))

# g'(x) = 2x + 4 so g'(2) = 8
# numerical result given : 8.00000009348878
