def multiples(n: int) -> list:
    resultat = []
    i = 2
    while i * n <= Nmax:
        resultat.append(n*i)
        i += 1
    return resultat

def diviseurs(n: int) -> list:
    resultat = [1]
    for i in range(2,n):
        if n % i == 0:
            resultat.append(i)
    return resultat


def diviseurs_ou_multiples(n: int) -> list:
    return diviseurs(n) + multiples(n)


def prochains_nombres_possibles(n: int) -> list:
    resultat = []
    for nombre in diviseurs_ou_multiples(n):
        if nombre in liste_nombres_restants:
            resultat.append(nombre)
    return resultat



Nmax = 100
liste_nombres_restants = [i for i in range(1, Nmax + 1)]
