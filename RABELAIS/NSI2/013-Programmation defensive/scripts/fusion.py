def fusion_imp1_plus(l1, l2):
    if not l1 or not l2:
        return l1 or l2
    n = len(l1)
    p = len(l2)
    i = 0
    j = 0
    result = []
    while len(result) < n + p:
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
        if i == n or j == p:
            result += l2[j:] or l1[i:]
    return result


def fusion_imp1(l1, l2):
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    n = len(l1)
    p = len(l2)
    i = 0
    j = 0
    result = []
    while len(result) < n + p:
        if l1[i] < l2[j]:
            result.append(l1[i])
            i += 1
        else:
            result.append(l2[j])
            j += 1
        if i == n:
            result += l2[j:]
        elif j == p:
            result += l1[i:]
    return result


def fusion_imp2(l1: list, l2: list) -> list:
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    result = []

    done = False
    l_one, l_two = l1, l2
    i, j = 0, 0
    while not done:
        while i < len(l_one) and l_one[i] < l_two[j]:
            result.append(l_one[i])
            i += 1
        if i == len(l_one):
            result.extend(l_two[j:])
            done = True
        else:
            l_one, l_two = l_two, l_one
            i, j = j, i
    return result


def fusion_rec(l1: list, l2: list) -> list:
    if l1 == []:
        return l2
    elif l2 == []:
        return l1
    else:
        if l1[0] <= l2[0]:
            return [l1[0]] + fusion_rec(l1[1:], l2)
        else:
            return [l2[0]] + fusion_rec(l1, l2[1:])


print(fusion_imp1_plus([1, 2, 7, 12333, 99999], [4, 5, 6, 8, 100]))
