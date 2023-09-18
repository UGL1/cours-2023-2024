def f(lst):
    s = []
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            s.append(lst[i] + lst[j])
    for e in lst:
        if e in s:
            return True
    return False


print(f([]))
print(f([1]))
print(f([1, 2]))
print(f([1, 2, 4]))
print(f([1, 2, 3]))
