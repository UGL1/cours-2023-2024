def create():
    return None


def is_empty(s):
    return s is None


def push(s, value):
    return (value, s)


def top(s):
    if not s:
        raise IndexError('Stack is empty.')
    return s[0]


def pop(s):
    if not s:
        raise IndexError('Stack is empty.')
    return s[1], s[0]


def display(s):
    result = ""
    while s:
        result += str(s[0]).center(8) + '\n'
        s = s[1]
    result += '-' * 8
    print(result)


st = create()
st = push(st, 20)
st = push(st, 20203)
display(st)
