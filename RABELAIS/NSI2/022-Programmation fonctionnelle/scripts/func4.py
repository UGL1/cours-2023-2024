def affine_function(m: float, p: float):
    def f(x: float) -> float:
        return m * x + p

    return f
