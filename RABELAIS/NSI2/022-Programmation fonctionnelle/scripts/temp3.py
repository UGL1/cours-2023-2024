def double_fonction(f):
    return lambda x: f(x) * 2


def bateau(x):
    return x ** 2


double_bateau = double_fonction(bateau)

print(double_bateau(10))
