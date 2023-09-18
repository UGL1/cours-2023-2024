def compute(operator, l: list) -> float:
    result = l[0]
    for i in range(1, len(l)):
        result = operator(result, l[i])
    return result


L = [1, 2, 3, 4, 5]

print(compute(lambda x, y: x * y, L))
