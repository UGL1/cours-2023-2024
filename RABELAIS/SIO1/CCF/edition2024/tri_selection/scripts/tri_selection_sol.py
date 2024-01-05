def indice_min(lst: list, i: int) -> int:
    j_min = i
    for j in range(i, len(lst)):
        if lst[j] < lst[j_min]:
            j_min = j
    return j_min


def tri_selection(lst: list) -> None:
    for i in range(len(lst) - 1):
        i_min = indice_min(lst, i)
        lst[i], lst[i_min] = lst[i_min], lst[i]


lst_exemple = [0, 2, 4, 1, 8, 7]
print(indice_min([0, 2, 4, 1, 8, 7], 2))
tri_selection(lst_exemple)
print(lst_exemple)
