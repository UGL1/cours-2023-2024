def enfiler(file, valeur):
    file.append(valeur)


def defiler(file):
    return file.pop(0)

def empiler(pile,valeur):
    pile.append(valeur)

def depiler(pile):
    return pile.pop()

def max_queue(file):
    resultat = -1
    enfiler(file, -1)
    valeur = defiler(file)
    while valeur != -1:
        print(file)
        input()
        enfiler(file, valeur)
        if valeur > resultat:
            resultat = valeur
        valeur = defiler(file)
    return resultat


r = []
enfiler(r, 2)
enfiler(r, 5)
enfiler(r, 1)
print(r)
print(max_queue(r))
print(r)
