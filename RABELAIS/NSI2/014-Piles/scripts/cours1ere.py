def fact(n: int) -> int:
    """
    On va calculer
    1 x 2 x 3 x ... x n
    ca se fait avec une boucle
    for, et i doit aller de 1
    à n
    le produit progressif,
    on l'appelle result
    et on le renvoie à la fin
    """
    result = 1  # valeur de base
    for i in range(1, n + 1):
        result = result * i
    return result


print(fact(10))


def password(n: int) -> str:
    symboles = "poiuytrezamlkjhgfdsqnbvcxwPOIUYTREZAMLKJHGFDSQNBVCXW0987654321"
    result = ""

    ...  # quelques lignes
    # avec choice(symboles)

    return result
