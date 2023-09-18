from stack import Stack


def reverse_with_stack(string: str) -> str:
    s = Stack()
    for letter in string:
        s.push(letter)
    result = ''
    print(s)
    while not s.is_empty():
        result += s.pop()
    return result


print(reverse_with_stack('Salut.'))
