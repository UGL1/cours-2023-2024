from stack import *

operation = {"+": lambda x, y: x + y,
             "-": lambda x, y: x - y,
             "*": lambda x, y: x * y,
             "/": lambda x, y: x / y}


def npi_compute_functional(expr : str) -> float:
    operation_symbols = operation.keys()
    c = expr.split()
    s = Stack()
    for x in c:
        if x not in operation_symbols:
            s.push(float(x))
        else:
            b = s.pop()
            a = s.pop()
            s.push(operation[x](a, b))
    return s.pop()

print(npi_compute_functional("1 2 3 4 + * -"))