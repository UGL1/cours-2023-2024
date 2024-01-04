class Pile:
    def __init__(self):
        """ Creates an empty stack"""
        self.content = []

    def est_vide(self) -> bool:
        """ Indicates whether the stack's empty or not """
        return self.content == []

    def empile(self, value):
        """ Pushes the value on the top of the stack """
        self.content.append(value)

    def depile(self):
        """ Retrieves the value from the top of the stack"""
        if self.est_vide():
            raise IndexError('Stack Empty')
        return self.content.pop()

    def __repr__(self):
        if self.est_vide():
            return "<empty>"
        result = '-' * 20 + '\n'
        t = Pile()
        while not self.est_vide():
            v = self.depile()
            t.empile(v)
            result += '|' + str(v).center(18) + '|\n'
            result += '-' * 20 + '\n'
        while not t.est_vide():
            self.empile(t.depile())
        return result + '\n'


def produire_jeu(n: int) -> Pile:
    resultat = Pile()
    for i in range(n, 0, -1):
        resultat.empile(i)
    return resultat

def scinder_jeu(p: Pile, n: int) -> tuple[Pile, Pile]:
    m1 = Pile()
    m2 = Pile()
    for i in range(n // 2):
        m1.empile(p.depile())
    for i in range(n // 2):
        m2.empile(p.depile())
    return m1, m2

def recombiner(m1: Pile, m2:Pile) -> Pile:
    p = Pile()
    while not m1.est_vide():
        p.empile(m1.depile())
        p.empile(m2.depile())
    return p


def faro(p: Pile,n:int)->Pile:
    return recombiner(*scinder_jeu(p,n))



jeu = produire_jeu(6)

print(faro(jeu,6))
