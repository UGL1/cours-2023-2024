def scinder_jeu(p, n):
    m1 = Pile()
    m2 = Pile()
    for i in range(n):
        m1.empile(p.depile())
    for i in range(n):
        m2.empile(p.depile())
    return m1, m2
