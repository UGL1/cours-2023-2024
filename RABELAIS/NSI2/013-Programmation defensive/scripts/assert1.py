def inverse(x: float) -> float:
    try:
        assert x != 0
    except AssertionError:
        print('x ne doit pas être nul !')
        return 0
    return 1 / x
