def affine_function2(xa, ya, xb, yb):
    if xa != xb:
        m = (yb - ya) / (xb - xa)
        p = ya - m * xa
        return lambda x: m * x + p


f = affine_function2(0, 2, 1, 5)  # points sur y = 3 * x + 2
print(f(4))  # 14
