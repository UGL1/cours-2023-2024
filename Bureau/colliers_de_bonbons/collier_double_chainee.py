class LDC:
    def __init__(self, element, pred, succ):
        self.elt = element
        self.succ = succ
        self.pred = pred




def produire_collier(n: int) -> LDC:
    depart = LDC(0, None, None)
    courant = depart
    for i in range(1, n):
        suivant = LDC(i, None, None)
        suivant.pred = courant
        courant.succ = suivant
    depart.pred = courant
    courant.succ = depart
    return depart


def obtenir_ordre(n: int) -> list[int]:
    courant = produire_collier(n)
    ordre = []
    for i in range(n):
        ordre.append(courant.elt)
        avant = courant.pred
        apres = courant.succ
        avant.succ = apres
        apres.pred = avant
        courant = apres.succ.succ
    return ordre


def parcours(b: LDC):
    courant = b
    print(b.elt, end=" ")
    courant = courant.succ
    while courant.elt != b.elt:
        print(courant.elt, end=" ")
        courant = courant.succ


dep = produire_collier(7)
parcours(dep)
