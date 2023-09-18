from Marienbad import *

m = Marienbad("yves", "patrick")
while not m.termine():
    print(m)
    tas = -1
    allumettes = 2
    while not (0 <= tas <= 5 and m.verifie(allumettes, tas)):
        print("Dans quel tas ", m.joueurs[m.tour], "pioche-t-il ? ", end="")
        tas = int(input()) - 1
        if 0 <= tas <= 5:
            print("Combien d'allumettes pioche-t-il sur les", m.tas[tas], end=" ? ")
            allumettes = int(input())
        else:
            tas = -1
    m.enlever(allumettes, tas)
    m.tour = (m.tour + 1) % 2
print("Le gagnant est", m.joueurs[m.tour])