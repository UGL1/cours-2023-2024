from random import randint, choice

n = 4
m = 5

identifiants = []
compteur = 0
for i in range(n):
    ligne = []
    for j in range(m):
        ligne.append(compteur)
        compteur += 1
    identifiants.append(ligne)
print(identifiants)

murs_verticaux = []
for i in range(n):
    ligne = []
    for j in range(m - 1):
        ligne.append(True)
    murs_verticaux.append(ligne)

murs_horizontaux = []
for i in range(n - 1):
    ligne = []
    for j in range(m):
        ligne.append(True)
    murs_horizontaux.append(ligne)

murs_verticaux_r = [(i, j, 0) for i in range(n) for j in range(m - 1)]
murs_horizontaux_r = [(i, j, 1) for i in range(n - 1) for j in range(n - 1)]
murs_r = murs_horizontaux_r + murs_verticaux_r

regions = [[(i,j)] for i in range(n) for j in range(m)]


def choisis_mur() -> tuple:
    return choice(murs_r)

def possible_enlever(mur: tuple) -> bool:
    if mur[2] == 0:
        return identifiants[mur[0]][mur[1]] != identifiants[mur[0]][mur[1] + 1]
    else:
        return identifiants[mur[0]][mur[1]] != identifiants[mur[0] + 1][mur[1]]


def fusionne_regions(v1,v2):
    region1 = regions[v1[0]][v1[1]]
    region2 = regions[v2[0]][v2[1]]



def enleve_mur(mur:tuple)->None:
    pass