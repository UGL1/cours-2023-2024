lst = [1, 2, 3]


def somme(l):
    if l == []:
        return 0
    else:
        return l[0] + somme(l[1:])


print(somme(lst))
