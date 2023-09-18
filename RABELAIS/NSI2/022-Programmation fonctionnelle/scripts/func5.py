def double_function(f):
    return lambda x: 2 * f(x)


def g(x: float) -> float:
    return x * x


df = double_function(g)
print(df(10)) # result 200
