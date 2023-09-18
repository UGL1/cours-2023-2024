def inverse(x: float) -> float:
    try:
        return 1 / x
    except:
        print('Erreur avec 1 /', x)
        return 0
