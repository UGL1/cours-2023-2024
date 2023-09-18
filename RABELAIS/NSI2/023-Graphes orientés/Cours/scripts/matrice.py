G = [[0, 1, 1, 0],
     [0, 0, 1, 1],
     [1, 1, 0, 0],
     [1, 0, 1, 0]]


def arc(graphe: list, sommet1, sommet2) -> bool:
    return graphe[sommet1][sommet2] == 1


def successeurs(graphe: list, sommet: int) -> list:
    resultat = []
    for i in range(len(graphe)):
        if graphe[sommet][i] == 1:
            resultat.append(i)
    return resultat
