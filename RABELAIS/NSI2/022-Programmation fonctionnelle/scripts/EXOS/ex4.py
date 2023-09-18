def compose(f, g):
    return lambda x: f(g(x))


def u(x):
    return x + 1


def v(x):
    return 2 * x


w = compose(u, v)  # w(x) = u(v(x)) = u(2x) = 2x + 1

print(w(4))  # 2*4 + 1 = 9
