def inverse(x: float) -> float:
    try:
        return 1 / x
    except ZeroDivisionError:
        print('Erreur - 1 /', x, ': division par zéro.')
    except TypeError:
        print('Erreur - 1 /', x, ': type incorrect.')
    return 0
