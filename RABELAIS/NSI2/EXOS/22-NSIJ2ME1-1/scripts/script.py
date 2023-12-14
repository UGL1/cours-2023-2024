class Noeud:
    def __init__(self, g=None, v=None, d=None):
        self.gauche = g
        self.valeur = v
        self.droit = d


def nb_sup(v, abr):
    global opel
    opel += 1
    if abr is None:
        print("NONE")
        return 0
    else:
        print(abr.valeur)
        if abr.valeur >= v:
            return 1 + nb_sup(v, abr.gauche) + nb_sup(v, abr.droit)
        else:
            return nb_sup(v, abr.gauche) + nb_sup(v, abr.droit)


opel = 0
n15 = Noeud(v=15)
n13 = Noeud(v=13)
n21 = Noeud(v=21)
n11 = Noeud(v=11)
n14 = Noeud(v=14)
n18 = Noeud(v=18)
n27 = Noeud(v=27)
n20 = Noeud(v=20)

n18.droit = n20
n21.gauche = n18
n21.droit = n27
n13.gauche = n11
n13.droit = n14
n15.gauche = n13
n15.droit = n21

abr = n15
print(nb_sup(16, abr))

print(opel)
