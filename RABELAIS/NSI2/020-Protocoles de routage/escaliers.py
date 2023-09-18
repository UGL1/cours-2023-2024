from math import sqrt
import sys
from numba import njit,jit, int32

sys.setrecursionlimit(100000)  # voire plus

n_max = 10000  # parce qu'il faut bien une limite
k_max = 100
escaliers_pp_n_max = [i * (i + 1) // 2 for i in range(1, int(sqrt(2 * n_max - .25) + .5))]  # les nombres escaliers plus

sol = [[None for k in range(1, k_max + 1)] for n in range(1, n_max + 1)]


@njit
def p(n, k):
    if sol[n][k] is not None:
        return sol[n][k]
    else:
        esc_pp_n = [x for x in escaliers_pp_n_max if x <= n]
        if k == 1:
            res = n in esc_pp_n
            sol[n][k] = res
            return res
        else:
            for x in esc_pp_n:
                if p(n - x, k - 1):
                    sol[n][k] = True
                    return True
            sol[n][k] = False
            return False


for i in range(n_max):
    for j in range(1, 101):
        p(i, j)

print(sol)
