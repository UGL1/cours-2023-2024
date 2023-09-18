from stack import Stack


def npi_compute(expression: str):
    stack = Stack()
    expression_list = expression.split()
    for element in expression_list:
        if element == '+':
            stack.push(stack.pop() + stack.pop())
        elif element == '*':
            stack.push(stack.pop() * stack.pop())
        elif element == '-':
            b, a = stack.pop(), stack.pop()
            stack.push(a - b)
        elif element == '/':
            b, a = stack.pop(), stack.pop()
            stack.push(a / b)
        else:
            stack.push(float(element))
    return stack.pop()


print(npi_compute('5 3 * 4 -'))
print(npi_compute('4 3 5 * +'))
print(npi_compute('1 3 + 5 /'))

