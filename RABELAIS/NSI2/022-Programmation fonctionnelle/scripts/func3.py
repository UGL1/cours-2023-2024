def affine_function(m: float, p: float):
    return lambda x: m * x + p


f = affine_function(2, 3)
print(f(1))  # result : 2*1+3 = 5
