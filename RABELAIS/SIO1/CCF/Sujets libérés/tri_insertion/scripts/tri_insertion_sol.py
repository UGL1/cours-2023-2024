def insere(lst, i) -> None:
    while i > 0 and lst[i] < lst[i - 1]:
        lst[i], lst[i - 1] = lst[i - 1], lst[i]
        i -= 1


def tri_insertion(lst) -> None:
    for i in range(1, len(lst)):
        insere(lst, i)


exemple_lst = [1, 2, 4, 5, 0, 2]
insere(exemple_lst, 4)
print(exemple_lst)

exemple_lst = [2, 4, 1, 5, 0, 3]
tri_insertion(exemple_lst)
print(exemple_lst)
