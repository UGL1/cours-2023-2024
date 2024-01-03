def compresse(ligne: list) -> list:
    resultat = []
    valeur = 0
    compteur = 0
    i = 0
    while i < len(ligne):
        if ligne[i] == valeur:
            compteur += 1
        else:
            valeur = 1 - valeur
            resultat.append(compteur)
            compteur = 1
        i += 1
    resultat.append(compteur)
    return resultat


def taux_compression(ligne: list) -> float:
    return (1 - len(compresse(ligne)) / len(ligne)) * 100


def decompresse(liste: list) -> list:
    resultat = []
    valeur = 0
    for e in liste:
        resultat.extend([valeur] * e)
        valeur = 1 - valeur
    return resultat


l = [1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0]
l2 = compresse(l)
print(taux_compression(l))
print(decompresse(l2))
