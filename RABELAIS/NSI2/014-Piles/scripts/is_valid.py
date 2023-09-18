from stack import Stack


def is_valid(string: str) -> bool:
    s = Stack()
    for letter in string:
        if letter == '(':
            s.push('*')
        elif letter == ')':
            if s.is_empty():
                return False
            else:
                s.pop()
    if s.is_empty():
        return True
    return False


print(is_valid(''))
print(is_valid('()'))
print(is_valid('())'))
print(is_valid('(()'))


