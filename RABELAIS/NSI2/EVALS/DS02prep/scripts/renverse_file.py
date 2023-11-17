def enfiler(file, valeur):
    file.append(valeur)


def defiler(file):
    return file.pop(0)


def empiler(pile, valeur):
    pile.append(valeur)


def depiler(pile):
    return pile.pop()


def est_vide(file):
    return not file


def pile_vide():
    return []


def renverse_file(file):
    p = pile_vide()
    while not est_vide(file):
        empiler(p, defiler(file))
    while not est_vide(p):
        enfiler(file, depiler(p))


r = []
enfiler(r, 2)
enfiler(r, 5)
enfiler(r, 1)
print(r)
renverse_file(r)
print(r)
