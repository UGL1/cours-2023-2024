from stack import Stack


def are_equal(s: Stack, t: Stack) -> bool:
    s1 = Stack()
    t1 = Stack()
    result = True
    while result and not s.is_empty() and not t.is_empty():
        v = s.pop()
        w = t.pop()
        s1.push(v)
        t1.push(w)
        if v != w:
            result = False

    if s.is_empty() != t.is_empty():
        result = False

    while not s1.is_empty():
        s.push(s1.pop())
        t.push(t1.pop())
    return result


st1 = Stack()
st1.push(1)
st1.push(2)
st1.push(3)

st2 = Stack()
st2.push(1)
st2.push(2)
st2.push(3)

st3 = Stack()
st3.push(2)
st3.push(3)

st4 = Stack()
st4.push(5)
st4.push(2)
st4.push(3)

st5 = Stack()

print(are_equal(st1, st2))
print(are_equal(st1, st3))
print(are_equal(st1, st4))
print(are_equal(st1, st5))
print(st1)
print(st2)
print(st3)
print(st4)
print(st5)