def fabrique_fonction_affine(m, p):
    """
    Renvoie la fonction qui à tout float x associe m*x+p
    """

    def f(x):
        return m * x + p

    return f


ma_fonction_affine = fabrique_fonction_affine(3, 2)
print(type(ma_fonction_affine))