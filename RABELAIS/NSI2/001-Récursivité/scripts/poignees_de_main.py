def f(n: int) -> int:
    return 0 if n == 0 else (n - 1) + f(n - 1)



for i in range(10):
    print(f(i))