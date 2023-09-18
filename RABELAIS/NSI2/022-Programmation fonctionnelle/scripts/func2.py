def compute(operator, l: list) -> float:
    result = l[0]
    for i in range(1, len(l)):
        result = operator(result, l[i])
    return result


def product(x: float, y: float) -> float:
    return x * y


print(compute(product, [1, 2, 3, 4, 5]))
# result : 120
