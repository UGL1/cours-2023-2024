piece = [100, 50, 20, 10, 5, 2, 1]


def trouve_piece(somme):
    i = 0
    n = len(piece)
    trouve = False
    resultat = 0
    while i < n and trouve == False:
        if piece[i] <= somme:
            resultat = piece[i]
            trouve = True
        i = i + 1
    return resultat


def nb_pieces_rendues(somme):
    resultat = 0
    while somme > 0:
        somme = somme - trouve_piece(somme)
        resultat += 1
    return resultat


def liste_pieces_rendues(somme):
    resultat = []
    while somme > 0:
        enleve = trouve_piece(somme)
        resultat.append(enleve)
        somme = somme - enleve
    return resultat


print(trouve_piece(49))
print(nb_pieces_rendues(13))
print(liste_pieces_rendues(43))
